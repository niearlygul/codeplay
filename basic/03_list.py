kor = ["사과", "포도", "딸기", "바나나", "토마토", "수박"]
eng = ["apple", "grape", "strawberry", "banana", "tomato", "watermelon"]
score = 0
answer = ""
# running = True
# count = 0



# while running:
#     answer = input(f"{kor[count]}을/를 영어로하면? : ")
#     if answer == eng[count]:
#             score += 1
#             print("정답.제법이군.")
#     else:
#         print("qttR")
#     count += 1
#     if count >= len(kor):
#          running = False
# print (f"당신의 점수는 {score}점 입니다")



for i in range(len(kor)):
    answer = input(f"{kor[i]}을/를 영어로하면? : ")
    if answer == eng[i]:
        score = score + 1
        print("정답.제법이군.")
    else:
         print("qttR")
print (f"당신의 점수는 {score}점 입니다")