import random
n=int(input())
#no.of hoops

start=[[i for i in range(1,n)],[],[]]
def fun(arr):
	for i,j  in enumerate(arr):
		print(f'stack: {i} :{j} ')
	print('\n')

def is_empty(arr):
	return (len(arr)==0)
def pops(a,arr):
	base=0
	bool_var=False
	for k,i in enumerate(arr,start=1):
		if (not is_empty(i)) and a==i[0]:
			i.pop(0)
			base=k
			bool_var=True
	bool_var2=False
	pref1=0
	pref2=0

	if bool_var:
		print(base)				#var to check if value was popped
		for i in range(1,4):
			if base!=i and is_empty(arr[i-1]):
				pref2=i
			if base!=i and not is_empty(arr[i-1]) and arr[i-1][0]>a:
				pref1=i	
		print(pref1,pref2)
		if a>2 and a%2:
			pref1,pref2=pref2,pref1
		# for k,i in enumerate(arr):
		# 	# if not is_empty(i) and i[0]>a and k!=base:
		if pref1:
			arr[pref1-1].insert(0,a)
			bool_var2=True
		elif pref2:
			# if k!=base:
			arr[pref2-1].insert(0,a)
			bool_var2=True
	
			
	if bool_var and  not bool_var2:
		arr[base].insert(0,a)

def build(a,arr):
	if a==1:
		pops(1,arr)
	else:
		build(a-1,arr)
		
		pops(a,arr)
		fun(start)

		build(a-1,arr)
	



# fun(start)
# build(1,start)
# fun(start)
# pops(2,start)
# fun(start)
# build(1,start)
fun(start)

build(n-1,start)
print('\nafter changes\n')
fun(start)



