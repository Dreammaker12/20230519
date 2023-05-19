#리스트 만들기 
#데이터가 있는 리스트 
animals = ["가물치","벼메뚜기","비단뱀","도룡뇽"]
#데이터가 없는 리스트 
empty = []
#리스트 조작하기 
#데이터 접근 
#인덱스는 0부터 시작한다. 
print(animals[2])
print(animals[-1])
animals.append("고라니")
print(animals)
#데이터 할당하기 
animals[1] = "청개구리"
print(animals)

del animals[0]
print(animals)

#리스트 슬라이싱
animals[1:3]
print(animals)
print(animals[:])#전체가져오기 
print(animals[:3])
print(animals[1:])

#리스트 길이 
print(len(animals))

animals.sort()
animals.sort(reverse= True)
print(animals)
