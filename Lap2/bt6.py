lst = []
n = int(input())
for i in rage(n):
	lst.append(int(input()))

answer= []
for v in lst:
	if v %5 ==0:
		answer.append(v)
	if len(answer) ==0:
		answer=[o]
print(answer)