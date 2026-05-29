import functools
import logging
import os
import re
import time
from datetime import datetime, timezone, timedelta

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def get_logger(name: str):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    )
    return logging.getLogger(name)


def get_openai_client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY가 설정되어 있지 않습니다. .env 파일을 확인하세요.")
    return OpenAI(api_key=api_key)


def now_kst_str() -> str:
    kst = timezone(timedelta(hours=9))
    return datetime.now(kst).strftime("%Y-%m-%d %H:%M:%S KST")


PII_PATTERNS = {
    "ssn": (r"\d{6}-[1-4]\d{6}", "[주민번호_마스킹]"),
    "phone": (r"0[1789]\d-\d{3,4}-\d{4}", "[전화번호_마스킹]"),
    "account": (r"\d{3,4}-\d{2,6}-\d{4,6}", "[계좌번호_마스킹]"),
    "card": (r"\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}", "[카드번호_마스킹]"),
}


def mask_pii(text: str):
    masked = text
    found = {}
    for key, (pattern, replacement) in PII_PATTERNS.items():
        matches = re.findall(pattern, masked)
        if matches:
            found[key] = len(matches)
            masked = re.sub(pattern, replacement, masked)
    return masked, found


INJECTION_PATTERNS = [
    r"이전.{0,15}(지시|명령|규칙).{0,15}(무시|잊어|삭제)",
    r"모든.{0,5}(고객|계좌).{0,5}(출력|공개)",
    r"ignore.{0,20}(previous|all).{0,20}instruction",
    r"forget.{0,15}(everything|rules|training)",
    r"(jailbreak|dan mode|developer mode)",
]


def detect_prompt_injection(text: str):
    low = text.lower()
    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, low):
            return True, pattern
    return False, ""


def retry_on_api_error(max_attempts: int = 3, wait_seconds: float = 1.0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    last_error = exc
                    if attempt >= max_attempts:
                        raise
                    time.sleep(wait_seconds * attempt)
            raise last_error
        return wrapper
    return decorator


class Printer:
    def header(self, text: str, color: str = ""):
        print("\n" + "=" * 70)
        print(text)
        print("=" * 70)

    def section(self, text: str, color: str = ""):
        print("\n" + "-" * 50)
        print(text)
        print("-" * 50)

    def kv(self, key: str, value):
        print(f"{key}: {value}")

    def success(self, text: str):
        print(f"[SUCCESS] {text}")

    def error(self, text: str):
        print(f"[ERROR] {text}")