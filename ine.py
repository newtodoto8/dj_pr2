from random import randint as rd
import re
def chr1(a):
	return(chr(a+96))
def ord1(a):
	return(ord(a)-96)
def return_comp(a,b):
	s=ord1(a)+ord1(b)
	if s<=27:
		return chr1(28-s)
	else:
		return chr1(54-s)
# f=open('hre.txt','w') 
# for i in range(1,27):
# 	for j in range(1,27):
# 		if i>=j:
# 			f.write(f'{chr1(i)}{chr1(j)}{return_comp(chr1(i),chr1(j))}    ')
# 	f.write(f'\n')
# f.close()
def code_gen(c):
	g=open('key.txt','w')
	h=open('text.txt','w')
	k=open('answer.txt','w')
	for _ in range(c):
		g.write('\n')
		h.write('\n')
		k.write('\n')																																															
		for _ in range(5):
			wordk=''.join(chr1(rd(1,26)) for _ in range (5))
			wordt=''.join(chr1(rd(1,26)) for _ in range (5))
			worda=''
			for i in range(5):
				worda+=return_comp(wordk[i],wordt[i])
			h.write(wordk)
			g.write(wordt)
			k.write(worda)
			g.write(' ')
			h.write(' ')
			k.write(' ')
	g.close()
	h.close()
	k.close()
#code_gen(15)
with open('sample.txt','r+') as f:
	for line in f.readlines():
		formatted=line.strip()
		pattern=r'[\s]'
		formatted=re.sub(pattern,'',formatted)
		f.write(formatted)
# sample=' hehrada dasdas dasfaf \n faasfsafasfaas'
# pattern=r'[\s]'
# sample=re.sub(pattern,'',sample)
# print(sample)
# print(''.join(chr1(rd(1,26)) for _ in range (5)))