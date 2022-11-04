n, t, e, ncnt, tcnt, ecnt = 0, 0, 0, 0, 0, 0

with open("input.txt", "r", encoding='utf-8') as f:
	while True:
		a = list(f.readline().strip('\n').split())
		if not a:
			break
		if int(a[2]) == 9:
			ncnt += 1
			n += int(a[3])
		if int(a[2]) == 10:
			tcnt += 1
			t += int(a[3])
		if int(a[2]) == 11:
			ecnt += 1
			e += int(a[3])
n = n / ncnt
t = t / tcnt
e = e / ecnt
print(n, t, e, sep = ' ')