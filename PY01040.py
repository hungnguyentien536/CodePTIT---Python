def testcase(s):
	d = 0
	x = ''
	for i in s:
		d += ord(i) - ord('A')
	for i in s:
		x += chr(((ord(i) - ord('A') + d) % 26 + ord('A')))
	return x

for _ in range(int(input())):
	s, x = input(), ''
	n = int(len(s) / 2)
	a = s[:n:] 
	b = s[n::]
	a = testcase(a)
	b = testcase(b)
	for i in range(n):
		x += chr(((ord(a[i]) - 2 * ord('A') + ord(b[i])) % 26 + ord('A')))
	print(x)