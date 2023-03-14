T = int(input()) # 학생의 수 입력 받기

# 학생 정보를 입력받아 리스트에 저장
array = []
for _ in range(T):
    input_data = input().split()
    # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
    array.append((input_data[0], int(input_data[1])))

# Key를 이용하여 점수를 기준으로 정렬
array.sort(key=lambda x:x[1])

# 정렬이 수행된 결과를 출력
for i in array:
    print(i[0], end=' ')
