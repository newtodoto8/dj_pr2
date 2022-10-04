import random
n=int(input())
#no.of hoops


class block:
	def __init__(self,value):
		self.value=value
	last_location=0 #instance variable

	def __repr__(self):
		return str(self.value)
start=[[block(i) for i in range(1,n)],[],[]]

def fun(arr):
	for i,j  in enumerate(arr):
		print(f'stack: {i} :{j} ')
	print('\n')

def is_empty(arr):
	return (len(arr)==0)
global step
def pops(a,arr):
	base=0
	bool_var=False
	for k,i in enumerate(arr,start=1):
		if (not is_empty(i)) and a==i[0].value:
			popped=i.pop(0)
			print(f'{popped.value} was popped')
			base=k
			print(f'from location: {base}')
			 # tracking location where it was popped
			bool_var=True
	bool_var2=False
	pref=0
	

	if bool_var:
			
		#var to check if value was popped
		#decide where to put the popped value

		for i in range(1,4):
			if base!=i and is_empty(arr[i-1]) and popped.last_location!=i:
				pref=i
			if base!=i and not is_empty(arr[i-1]) and arr[i-1][0].value>a and popped.last_location!=i:
				pref=i	
		

		
		
		# for k,i in enumerate(arr):
		# 	# if not is_empty(i) and i[0]>a and k!=base:
		if pref:
			arr[pref-1].insert(0,popped)
			bool_var2=True
		# print(f'{pref} : to where . {popped.value}\'s  last_location was {popped.last_location}')
		popped.last_location=base
		# print(f'{popped.value}\'s last_location is now {popped.last_location}\n')
	
	
	# print("step: {step}")
	fun(start)

		
	if bool_var and  not bool_var2:
		arr[base].insert(0,popped)

def build(a,arr):
	if a==1:
		pops(1,arr)
	else:
		build(a-1,arr)
		
		pops(a,arr)


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



