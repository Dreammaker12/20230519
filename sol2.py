import random

def getRandomNumber():
    number = random.randint(1,45)
    return number
n = list()
count = 0
while True:
    m = getRandomNumber()
    if m not in n:
        n.append(m)
        count+=1
    if count >6:
        break
n.sort()
answer = [27,34,25,21,30,42]
answer.sort()
correct = 0

for i in range(6):
    if n[i] == answer[i]:
        correct +=1

if correct ==6:
    print("로또에 당첨되었습니다.")
else: 
  print(correct,"개 맞힘")
  print("다음 기회에 ")
       