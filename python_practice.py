# def add_num(a, b):
#     print(a + b)

# i = add_num(1, 3)
# print(i)      # none이 출력된다. i에 값이 없음

# def add_num(a, b):
#     return a + b # return을 쓰면 식을 반환해준다. return을 쓰면 함수 끝남
# i = add_num(1, 3)
# print(i) 

# def input_a(*args): #(*변수명)튜플로 원하는 값 지정가능
#     return args

# print(input_a(13,12,11,"김치"))

# def input_b(**args): #(**변수명)딕셔너리로 원하는 값 지정가능
#     return args

# print(input_b(박명수 = 11, 유재석 = "감자", 정형돈 = 14))

def quiz(): 
    a = input("1 + 3 = ")
    return 1 + 3 == int(a)
print(quiz())




