# 입력값 받기
answer = input("입력: ")

# 조건문 설정
if "안녕" in answer:
    print("안녕하세요.")
elif "몇 시" in answer:
    import datetime
    now = datetime.datetime.now()
    print(f"지금은 {now.hour}시 입니다.")
else:
    print(answer)
