# a =""
# b = 0
# c =""
# a = input("이름을 입력하시오 : ")
# b = input("나이를 입력하시오 : ")
# c = input("직업은? : ")

# print(f"{a[0]}{c}님 반갑습니다")

# if int(b) > 18:
#     print(c + "시군요.")
# else:
#     print("어린이는 여기로 가세요")

# eng = "abcdefg"
# kor = "가나다라마바사"

# print(eng[3])
# print(f"{kor[-1:-3:-1]}! 이자식아")

# print(eng[::-1])

# name = ""
# age = ""
# name = input("이름은? : ")
# age = input("나이는? : ")

# if int(age) <=16:
#     print(f"{name} 너 임마 까불지마.")
# elif int(age) >16:
#     print(f"{name[0]}사장님 안녕하세요")



import random


name = "못생긴코딩쌤"
call = ["바보", "천재", "추남", "또라이"]

print(f"역시! {name} {call[random.randint(0, 4)]}!")