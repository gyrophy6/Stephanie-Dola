b = -1
c = [-1]
d = []

with open("input.txt", "r", encoding='utf-8') as f:
	while True:
		a = list(f.readline().strip('\n').split())
		if not a:
			break
		if int(a[3]) == b:
			c.append(int(a[2]))
		if int(a[3]) > b:
			b = int(a[3])
			c.pop()
			c.append(int(a[2]))
	[d.append(i) for i in c if i not in d]

print(d)

