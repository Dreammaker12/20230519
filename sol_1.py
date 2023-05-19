print("[메뉴를 입력하세요.]")

while True:
    n = int(input("1.게임시작, 2.랭킹보기, 3.게임종료>>>"))
    if n ==3:
        print("게임을 종료합니다.")
        break
    elif n == 2:
        print("실기간 랭킹")
    elif n == 1:
        print("게임을 시작합니다.")
    else:
        print("다시 입력해 주세요")

#learning korean
korean = ["안녕하세요","감사합니다","사랑합니다"]
print("다음은 한국어 연습게임입니다. 그대로 입력하세요")
total = len(korean)
count = 0
for kor in korean:
    print(kor)
    m = input()
    if m != kor:
        break
    count += 1
print("전체 문제 개수:", total,"개")
print("맞힌 문제 개수:", count,"개")
print("틀린 문제 개수",total-count,"개")
