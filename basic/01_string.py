a =""
b = 0
c =""
a = input("이름을 입력하시오 : ")
b = input("나이를 입력하시오 : ")
c = input("직업은? : ")

if int(b) > 18:
    print(c + "시군요.")
else:
    print("어린이는 여기로 가")

print(f"{a[0]}{c}님 반갑습니다")

