"""DTI 계산 테스트 - 직접 구현"""

# 테스트 입력값
annual_income = 80000000  # 8000만원
existing_monthly_debt = 0  # 0원
new_monthly_payment = 2500000  # 250만원

# DTI 공식: (기존 월 부채 + 신규 월 상환액) × 12 / 연소득 × 100
total_monthly_debt = existing_monthly_debt + new_monthly_payment
dti_percentage = (total_monthly_debt * 12 / annual_income) * 100
dti_threshold = 40.0
is_passed = dti_percentage <= dti_threshold

print("=" * 70)
print("DTI 계산 테스트")
print("=" * 70)
print("\n[입력값]")
print(f"  연소득: {annual_income:,}원 (8000만원)")
print(f"  기존 월 부채: {existing_monthly_debt:,}원")
print(f"  신규 월 상환액: {new_monthly_payment:,}원")

print("\n[계산 과정]")
print(f"  총 월 부채 = {existing_monthly_debt:,} + {new_monthly_payment:,}")
print(f"            = {total_monthly_debt:,}원")
print(f"\n  DTI = (총 월 부채 × 12 / 연소득) × 100")
print(f"      = ({total_monthly_debt:,} × 12 / {annual_income:,}) × 100")
print(f"      = ({total_monthly_debt * 12:,} / {annual_income:,}) × 100")
print(f"      = {(total_monthly_debt * 12) / annual_income:.3f} × 100")
print(f"      = {dti_percentage:.1f}%")

print("\n[결과]")
result = {
    "DTI": f"{round(dti_percentage, 1)}%",
    "통과_여부": is_passed,
    "기준": "40% 이하",
    "기존_월_부채": f"{round(existing_monthly_debt):,}원",
    "신규_월_상환액": f"{round(new_monthly_payment):,}원",
    "총_월_부채": f"{round(total_monthly_debt):,}원",
    "연소득": f"{round(annual_income):,}원",
    "판정_결과": "적격" if is_passed else "부적격",
    "설명": (
        "부채비율이 40% 이하이면 대출 심사에 유리합니다."
        if is_passed
        else "부채비율이 40%를 초과하여 대출 심사 기준에 부적합할 수 있습니다."
    ),
}

for key, value in result.items():
    print(f"  {key}: {value}")

print("\n" + "=" * 70)
