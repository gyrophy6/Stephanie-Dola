with open("input.txt", "r", encoding='utf-8') as f:
	a = f.readlines()
	a = list(map(lambda x: x.rstrip().split(), a))
a = sorted(a, key = lambda x: x[0])
for i in range(len(a)):
	print(a[i][0], a[i][1], a[i][3], sep = ' ')