s = input()
answer = ''
str_ = ''.join(sorted([i for i in s if i.isalpha()]))
num = str(sum([int(i) for i in s if i.isdigit()]))

print(str_ + num)



