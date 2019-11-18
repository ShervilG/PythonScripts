def generate_pattern(n):
	star = '* '
	p = int(1)
	if n%2!=0:
		q = int(n/2)+3
	else:
		q = int(n/2)+3
	for i in range(n):
		s1 = str(' ') * q;
		s2 = star * p;
		pat = s1 + s2
		print(pat)
		p += 1
		q -= 1

x = 7
generate_pattern(x)