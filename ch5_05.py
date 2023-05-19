#리스트 자료형 실습문제 
#팔굽혀 펴기 개수
result = [33, 40, 12, 63, 52]
#6번의 팔굽혀 펴기 개수는 9개 
result.append(9)
print(result)
#3번부터 6번까지 슬라이싱 
print(result[2:])
print(result[2:6])
#2번은 재측정해서 50개 
result[1] = 50
print(result)
#모든 데이터를 오름차순 
result.sort()
print(result)

#턱걸이 측정프로그램 1) 빈리스트, 일주일간의 턱걸이 횟수 기록 
#턱걸이 측정 프로그램 

pullup = []
for i in range(7):
    print(i+1,"일차",end="")
    n = int(input("턱걸이 횟수>>>>>"))
    pullup.append(n)
    print(pullup)
    if pullup[i] >= 30:
        print("오늘은 컨디션이 좋으시네요")
    else:
        print("오늘은 컨디션이 별로군요")


