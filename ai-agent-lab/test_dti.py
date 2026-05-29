#!/usr/bin/env python3
"""DTI 계산 테스트 스크립트"""

import sys
import json
sys.path.insert(0, '.')

from m02_tool_use.lab_tools_chatgpt import calculate_dti

# 테스트 입력값
annual_income = 80000000  # 8000만원
existing_monthly_debt = 0  # 0원
new_monthly_payment = 2500000  # 250만원

result = calculate_dti(
    existing_monthly_debt=existing_monthly_debt,
    new_monthly_payment=new_monthly_payment,
    annual_income=annual_income
)

print("=" * 60)
print("DTI 계산 테스트")
print("=" * 60)
print("\n[입력값]")
print(f"  연소득: {annual_income:,}원 (8000만원)")
print(f"  기존 월 부채: {existing_monthly_debt:,}원")
print(f"  신규 월 상환액: {new_monthly_payment:,}원")
print("\n[계산 과정]")
print(f"  총 월 부채 = {existing_monthly_debt:,} + {new_monthly_payment:,} = {existing_monthly_debt + new_monthly_payment:,}원")
print(f"  DTI = ({existing_monthly_debt + new_monthly_payment:,} × 12 / {annual_income:,}) × 100")
print(f"  DTI = ({(existing_monthly_debt + new_monthly_payment) * 12:,} / {annual_income:,}) × 100")
print(f"  DTI = {((existing_monthly_debt + new_monthly_payment) * 12 / annual_income) * 100:.1f}%")
print("\n[결과]")
print(json.dumps(result, ensure_ascii=False, indent=2))
print("\n" + "=" * 60)
