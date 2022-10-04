from collections import defaultdict
from typing import List
from heapq import *
# trie=lambda:dd(trie)
# # class Solution:
# #     def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
# #         products.sort()
# #         # head=trie()
# #         d=dd(lambda :[])
# #         for n,i in enumerate(products):
# #             for j in range(1,len(i)+1):
# #                 d[i[:j]].append(n)
# #         ans=[]
# #         # 
# #         for i in range(1,len(searchWord)+1):
# #             ans.append(list(products[j] for j in d[searchWord[:i]])[:3])
# #         return ans
# class Solution:
#     def minimumLengthEncoding(self, words: List[str]) -> int:
#         words2=words.copy()
#         words2.sort(key=len,reverse=True)
#         print(words,words2)
#         d={}
#         ans=0
#         for i in words:
#             n=len(i)
#             if i in d:
#                 pass
#             else:
#                 ans+=(n+1)
#                 for j in range(n):
#                     d[i[j:n]]=1
                    
#         return ans
        # for 
# class Solution:
#     def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
#         n=len(heights)
#         diffs=[]
#         for i in range(n-1):
#             diffs.append(heights[i+1]-heights[i])
#         print(diffs)
#         # def noob(ind,x,y):
#         #     if x<0 or y<0:
#         #         return -1
#         #     if ind>n-2 :
#         #         return 0
            

#         #     if diffs[ind]<=0:
#         #         return 1+noob(ind+1,x,y)
#         #     else:
#         #         return max(1+noob(ind+1,x-diffs[ind],y),1+noob(ind+1,x,y-1))
#         # return noob(0,bricks,ladders)
#         brick_sum=0
#         ans=0
#         heap=[]
#         for i in diffs:
#             if i<=0:
#                 ans+=1
#                 continue
#             if ladders and len(heap)<ladders:
#                 heappush(heap,i)
#             else:
#                 if heap and i>heap[0]:
#                     if heap[0]+brick_sum<=bricks:
#                         brick_sum+=heap[0]
#                         heappop(heap)
#                         heappush(heap,i)
#                         ans+=1
#                     else:
#                         break
#                 else:
#                     if brick_sum+i<=bricks:
#                         brick_sum+=i
#                         ans+=1
#                     else:
#                         break
#         return ans+len(heap)
# def heap
import random
from itertools import accumulate
# class Solution:
#     def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
#         diff1_2=[nums1[i]-nums2[i] for i in range(len(nums1))]
#         diff2_1=[nums2[i]-nums1[i] for i in range(len(nums1))]
#         diff2_1=list(accumulate(diff2_1))
#         diff1_2=list(accumulate(diff1_2))
#         diff1_2.insert(0,0)
#         diff2_1.insert(0,0)
#         # diff1_2=[(j,i) for i,j in enumerate(diff1_2)]
#         # diff2_1=[(j,i) for i,j in enumerate(diff2_1)]
#         # diff1_2.sort()
#         # diff2_1.sort()
#         print(diff1_2)
#         print(diff2_1)
#         def fn(arr):
#             minel=arr[0]
#             diff=arr[1]-arr[0]
#             n=len(arr)
#             for i in range(1,n):
#                 if arr[i]-minel>diff:
#                     diff =arr[i]-minel
#                 if minel>arr[i]:
#                     minel=arr[i]
#             return diff
            
#         return max(sum(nums1)+fn(diff2_1),sum(nums2)+fn(diff1_2))
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda h: (-h[0],h[1]))
        print(people)
        # d=defaultdict(lambda:[])
        # for i in people:
        #     if i[1] in d:
        #         d[i[1]].append(i[0])
        #     else:
        #         d[i[1]]=[i[0]]
        # for i in d:
        #     d[i].sort(reverse=True)
        # cur=0
        # n=len(people)
        # ans=[]
        # print(d)
        # counter=0
        # while(cur<n) and counter<20:
        #     for i in range(cur,-1,-1):
        #         if d[i]:
        #             temp=d[i][-1]
        #             ct=0
        #             for j in range(len(ans)):
        #                 if ans[j][0]>=temp:
        #                     ct+=1
        #                 if ct==i:
        #                     break
                        

        #             print('dasdasd')    
        #             if ct==i:
        #                 d[i].pop()
        #                 ans.append([temp,i])
        #                 cur+=1
        #                 break
        #         counter+=1
        #         print(ans,cur)
        #     # break
        return ans 
        

# arr1=[random.randint(5,30) for _ in range(10)]
# arr1=[19, 13, 26, 10, 9, 11, 16, 22, 12, 14]
# arr2=[17, 21, 13, 7, 27, 26, 11, 16, 27, 24]
# print(arr1)
# print(arr2)       
a=Solution()
# print(a.isPossible([1,100000]))
# print(a.maximumsSplicedArray(arr1,arr2))
print(a.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))
# print(a.suggestedProducts(products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"))
# print(a.minimumLengthEncoding(["time", "me", "bell"]))
# print(a.furthestBuilding(heights = [14,3,19,3], bricks = 17, ladders = 0))
# print(a.furthestBuilding(heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2))
# print(a.furthestBuilding(heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1))

        