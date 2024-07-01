# 입력값
number = int(input("정수를 입력해주세요: "))

# 조건문 입력
if number % 2 == 0:
    print(f"{number}은 2로 나누어 떨어지는 숫자입니다.")
    print(f"{number}은 3으로 나누어 떨어지는 숫자가 아닙니다.")
    print(f"{number}은 4로 나누어 떨어지는 숫자가 아닙니다.")
    print(f"{number}은 5로 나누어 떨어지는 숫자가 아닙니다.")
elif number % 3 == 0:
    print(f"{number}은 2로 나누어 떨어지는 숫자가 아닙니다.")
    print(f"{number}은 3으로 나누어 떨어지는 숫자입니다.")
    print(f"{number}은 4로 나누어 떨어지는 숫자가 아닙니다.")
    print(f"{number}은 5로 나누어 떨어지는 숫자가 아닙니다.")
elif number % 4 == 0:
    print(f"{number}은 2로 나누어 떨어지는 숫자가 아닙니다.")
    print(f"{number}은 3으로 나누어 떨어지는 숫자가 아닙니다.")
    print(f"{number}은 4로 나누어 떨어지는 숫자입니다.")
    print(f"{number}은 5로 나누어 떨어지는 숫자가 아닙니다.")
elif number % 5 == 0:
    print(f"{number}은 2로 나누어 떨어지는 숫자가 아닙니다.")
    print(f"{number}은 3으로 나누어 떨어지는 숫자가 아닙니다.")
    print(f"{number}은 4로 나누어 떨어지는 숫자가 아닙니다.")
    print(f"{number}은 5로 나누어 떨어지는 숫자입니다.")
else: 
    print(f"{number}은 2로 나누어 떨어지는 숫자가 아닙니다.")
    print(f"{number}은 3으로 나누어 떨어지는 숫자가 아닙니다.")
    print(f"{number}은 4로 나누어 떨어지는 숫자가 아닙니다.")
    print(f"{number}은 5로 나누어 떨어지는 숫자가 아닙니다.")
