n=int(input())
#no.of hoops

start=[[i for i in range(1,n)],[],[]]
def fun(arr):
	for i,j  in enumerate(arr):
		print(f'stack: {i} :{j} ')
fun(start)
