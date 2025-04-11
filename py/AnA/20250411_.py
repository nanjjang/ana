# a = "noodle"
# b = True
# c = 10
# d = 10.2

# mix = ["noodle",True, 10, 10.2]

# print(mix)

# a = ['Math', 'Science', 'History']
# b = ['P.E', 'Music', 'Art']

# subject = a+b
# aa = a*2

# print(subject)
# print(aa)

# #index
# # ['Math', 'Science', 'History', 'Math', 'Science', 'History']

# print(subject[-1])
# print(subject[-6])

# #슬라이싱
# #배열[start:stop:step]
# #['Math', 'Science', 'History', 'P.E', 'Music', 'Art']
# print(subject[1:3])

# print(subject[5:1:-1])

# print(subject[::3])

# print(subject[::-1])


# k = [1,2,3,4,5,6,7,8,9,10]
# #[1,4,7,10]
# print(k[0:7:3])

# #리스트 메소드

# subway = ["프로도", "튜브", "어피치"]
# print(subway)

# print(subway.index("튜브"))

# subway.append("라이언")
# print(subway)

# subway.insert(3,"춘식이")
# print(subway)

# subway.append("춘식이")
# print(subway)

# print(subway.count("춘식이"))

# subway.clear()
# print(subway)

# li = [9,4,8,3,7]
# li.sort()
# print(li)

# li.reverse()
# print(li)

s1 = set([2,3,4,5,6,7,7,7])
# s1 = {2,3,4,5,6,7,7,7}

print(s1)

s2 = set("ana")
print(s2)

A = {1,2,3,4,5,6,7}
B = {4,5,6,7,8,9,10}

# 교집합 : intersection, &
C = A & B
# C = A.intersection(B)
print(C)

# 합집합 : union, |
C = A.union(B)
# C = A | B
print(C)

# 차집합 : difference, -
C = B-A
# C = B.difference(A)
print(C)

C = A-B
print(C)


A.add(100)
print(A)

A.update([100,101,102,103])
print(A)

A.remove(103) # 인덱스에 없는 값이 나오면 오류류
print(A)

A.discard(102) # 인덱스에 없는 값이 나와도 상관 X
print(A)

A.discard(1000)
print(A)

