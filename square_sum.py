n = 10000000

en = 0
enl = []

def which_count(x,o):
	global en,enl

	if x==1:
		return False
	if x==89:
		en += 1
		enl.append(o)
		return True
	if x in enl:
		if o not in enl:
			enl.append(o)
		return True
	#else
	s = 0
	for i in str(x):
		s += int(i)*int(i)
	which_count(s,o)

for i in range(1,n+1):
	which_count(i,i)

print(en)


