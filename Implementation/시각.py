h = int(input())
count = 0

for i in range(h + 1): # 입력받은 시
    for j in range(60): # 0~59분
        for k in range(60): # 0~59초
            # 시각 안에 '3' 이 포함되어 있으면
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
