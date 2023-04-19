# ja = ""
# n1 = 0
# n2 = 0
# result = 0

# while True:
#     n1 = int(input("첫번째 숫자를 말해라"))
#     ja = input("무슨 계산할래? 기호로만 적어(+,-,*,/)")
#     n2 = int(input("두번째 숫자를 말해라"))
#     if ja == "+":
#         result = n1 + n2
#     elif ja == "-":
#         result = n1 - n2
#     elif ja == "*":
#         result = n1 * n2
#     elif ja == "/":
#         result = n1 / n2
#     else:
#         print("첨부터 다시")
#         continue
    
#     print(f"{n1} {ja} {n2} = {result}")

gyesan = ""
result = 0
running = True

while running:
    show = True
    gyesan = input("계산기입니다. 물어보세요 : ")
    if "+" in gyesan:
        result = int(gyesan.split("+")[0]) + int(gyesan.split("+")[1])
    elif "-" in gyesan:
        result = int(gyesan.split("-")[0]) - int(gyesan.split("-")[1])
    elif "*" in gyesan:
        result = int(gyesan.split("*")[0]) * int(gyesan.split("*")[1])
    elif "/" in gyesan:
        result = int(gyesan.split("/")[0]) / int(gyesan.split("/")[1])
    elif "q" in gyesan:
        print("주인 ㅃㅇ")
        running = False
        show = False
    else:
        print("연산식이 이상해.다시!")
        show = False
    if show:
        print(f"{gyesan} = {result}")