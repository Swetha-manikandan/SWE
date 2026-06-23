S = {101,102,101,103,104}
print(len(S))
S.update({104,105,106,107})
print(S)

set([101,102,103,104,105])
print()

num={1,1,3,5}
num.discard(4)
print(num)

s1={101,102,103,107}
s2={101,102,103,104,105}
print(s1-s2)
print(s1^s2)