#팰린드롬수


while True:
  number = int(input())
  # print(number)
  if number == 0:
    break
  else:
    number = str(number)
    count = len(number)//2
    yesno = "yes"
    for i in range(count):
      if number[i] != number[-(i+1)]:
        yesno = "no"
    print(yesno)
    