def solve(n, l):
	c = 0;
	for i in range(l):
		if i < l - 1:
			if (n[i] == '0' and n[i + 1] == '1'):
				c = c + 1
	if (n[0] == '1'):
		c = c + 1
	print(c)


t = int(input())

for i in range(t):
	n = input()
	l = len(n)
	solve(n, l)
