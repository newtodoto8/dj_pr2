# class Solution:
#     def makesquare(self, matchsticks) -> bool:
#         n=len(matchsticks)
#         x=sum(matchsticks)//4
#         if (x*4)!=sum(matchsticks):
#             return False
#         sums=[0]*4
#         def fn(ind):
#             if ind==n:
#                 if sums[0]==sums[1]==sums[2]==x:
#                     return True
#             for i in range(4):
#                 if sums[i]+matchsticks[ind]<=x:
#                     sums[i]+=matchsticks[ind]
#                     if fn(ind+1):
#                         return True
#                     sums[i]-=matchsticks[ind]
#             return False

def pivot(arr,ind):
    pivot=arr[ind]
    start,end=0,len(arr)-1
    i=0
    while(i<end):
        if arr[i]<=pivot:
            i+=1
        else:
            arr[i],arr[end]=arr[end],arr[i]
            end-=1
    return arr
print(pivot([12,1,5,6,4,4,1,3,4,7,91,16,8,1],4))



