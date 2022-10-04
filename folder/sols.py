from collections import defaultdict
# class Solution:
#     def merge(self,a,b):
#         return (a[0],max(b[1],a[1]))
#     def partitionLabels(self, s: str):
#         l=len(s)
#         d=defaultdict(lambda:[])
#         for i,j in enumerate(s):
#             if not d[j]:
#                 d[j].append(i)
#             elif len(d[j])==1:
#                 d[j].append(i)
#             else:
#                 d[j][1]=i
#         arr=list(d.values())
#         for i,j  in enumerate(arr):
#             if len(j)==1:
#                 arr[i]=[j[0],j[0]]
#         cur=0
#         i=0
#         j=1
#         while (j<len(arr)):
#             if arr[j][0]<arr[i][1]:
#                 arr[i]=self.merge(arr[i],arr[j])
#                 arr[j]=None
#                 j+=1
#             else:
#                 i=j
#                 j+=1


#         ans=[i[1]-i[0]+1 for i in arr if i]

#         return ans
import math
# class Solution:
#     def bc(self, x: int, y: int) -> int:
#         # ans=0
#         ans=0
#         while(y!=x):
#             if x>y:
#                 return ans+(x-y)
#             if y%2:
#                 y+=1
#                 ans+=1
#             else:
#                 y=y//2
#                 ans+=1
#         return ans
#         # log=int(math.log(y/x,2))
#         # ans=ans+1+log
#         # val=x*2**log
#         # ki2=(2*val)%y
#         # ki3=x%(y//2)
#         # ans+=min(ki2,ki3)
#         # print(ki2,ki3,ans)
#         #if startValue==target:

# class Solution:
#     def twoCitySchedCost(self, costs) -> int:
#         diff=[]
#         l=len(costs)//2
#         for j,i in enumerate(costs):
#             temp=None
#             if i[1]-i[0]>0:
#                 temp=('a',i[1]-i[0],j)
#             else:
#                 temp=('b',i[0]-i[1],j)
#             diff.append(temp)
#         diff.sort(key=lambda x:x[1],reverse=True)
#         ans=0
#         c_a=0
#         c_b=0
#         for i in diff:
            
#             if (i[0]=='a' and c_a<l):
#                 ans+=costs[i[2]][0]
#                 c_a+=1
#             elif(i[0]=='b' and c_b<l):
#                 ans+=costs[i[2]][1]
#                 c_b+=1
#             elif (c_a==l):
#                 ans+=costs[i[2]][1]
#             else:
#                 ans+=costs[i[2]][0]
#         print(diff)
            
#         return ans 

# class Solution:
#     def search(self, nums, target: int) -> bool:
#         s=0
#         end=len(nums)-1
#         while(s<=end):
#             pivot=s+(end-s)//2
#             if nums[s]>nums[pivot]:
#                 end=pivot-1
#             else:
#                 s=pivot+1
#         s=s
#         end=len(nums)-1+end
#         print(s,end)
#         pivot=0
#         k=len(nums)
#         while(s<=end):
#             pivot=s+(end-s)//2
#             if nums[pivot%k]>target:
#                 end=pivot-1
#             else:
#                 s=pivot+1
#         print(nums[pivot%k])
#         return nums[pivot%k]==target

# class Solution:
#     def searchMatrix(self, matrix, target) -> bool:
#         if not matrix or not matrix[0]: return False
#         rows=len(matrix)
#         cols=len(matrix[0])
#         s=0
#         end=rows*cols-1
#         print(s,end)
#         m, n = len(matrix[0]), len(matrix)
#         beg, end = 0, m*n - 1
#         print(beg,end)
#         while beg < end:
#             mid = (beg + end)//2
#             if matrix[mid//m][mid%m]<target:
#                 beg = mid + 1
#             else:
#                 end = mid
#         return matrix[beg//m][beg%m] == target
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#     def __repr__(self):
#         temp=self
#         s=[]
#         while(temp!=None):
#             s.append(temp.val)
#             temp=temp.next
#         return ''.join([str(i) for i in s])
# class Solution:
#     def swapNodes(self, head, k: int):
#         prev_fir=None
#         fir=None
#         prev_last=None
#         last=None
#         c=0
#         cur=head
#         prev=None
#         while(c!=k-1):
#             prev=cur
#             cur=cur.next
#             c+=1
#         fir=cur
#         prev_fir=prev
#         print(fir.val,prev_fir.val)
#         cur=head
#         hare=head
#         turtle=head
#         mid=0
#         even=False
#         while(hare.next!=None):
#             hare=hare.next.next
#             turtle=turtle.next
#             mid+=1
#             if not hare:
#                 even=True
#                 break
        
#         print(turtle.val,mid)
#         c=mid
#         cur=turtle
#         if k-1>mid:
#             if even:
#                 k=2*mid-k
#             else:
#                 k=2*mid-k+1
#         while(c!=2*mid-k+1):
#             prev=cur
#             cur=cur.next
#             c+=1
#         prev_last=prev
#         last=cur
#         temp=fir.next
#         fir.next=last.next
#         prev_last.next=fir
#         prev_fir.next=last
#         last.next=temp
#         return head
# alice_arr=[11,12,0,13,0,0,22,11,0,11,21,0]
# k=0
# def maxBOB(arr_left,alice_arr):
#     def dp(index_arr,arr_left):
#         # print(index_arr,arr_left)
        
#         if index_arr==12 or arr_left<=0:
#             return 0
#         maxscore=dp(index_arr+1,arr_left)
#         if arr_left>alice_arr[index_arr]:
#             maxscore=max(maxscore,index_arr+dp(index_arr+1,arr_left-alice_arr[index_arr]-1))
#         return maxscore
#     ans=[0]*12
#     for i in range(12):
#         if dp(i+1,arr_left)!=dp(i,arr_left):
#             ans[i]=alice_arr[i]+1
#             arr_left-=ans[i]
#     return ans

# print(maxBOB(9,[0,0,0,0,0,0,0,1,0,1,0,0]))
import random
import time
from functools import cache
from math import comb


# arr1=[random.randint(2,79) for _ in range(30)]
# arr2=[random.randint(2,790) for _ in range(30)]
# val=random.randint(79*4,79*10)
# x=time.time()
# @cache
# def knapsack(W,weights,values,n):
#     if n<0:
#         return 0
#     if W-weights[n]>=0:
#         score=max(knapsack(W,weights,values,n-1),values[n]+knapsack(W-weights[n],weights,values,n-1))
#     else:
#         return knapsack(W,weights,values,n-1)
#     return score

# def knapsack(W,weights,values,n):
#     dp=[[0]*W for _ in range(n)]
#     for i in range(1,n):
#         for j in range(W):
#             if j>=weights[i]:
#                 dp[i][j]=max(dp[i-1][j],values[i]+dp[i-1][j-weights[i]])
#             else:
#                 dp[i][j]=dp[i-1][j]
    
#     return dp[n-1][W-1]
# print(knapsack(90,[30,50,10],[10,20,40],3))
# print(time.time()-x)
# print(k)
# a=Solution()
# l=ListNode(1)
# l2=l.next=ListNode(2)
# l3=l2.next=ListNode(3)
# l4=l3.next=ListNode(4)
# # l5=l4.next=ListNode(5)
# a.swapNodes(l,4)
# print(l)
# class Solution:
#     def threeSumMulti(self, arr, target: int) -> int:
#         all_tup=[]
#         # def comb2(x,y):
            
            
#         d=defaultdict(lambda:0)
#         ans=0
#         for i in arr:
#             d[i]+=1
#         for i in range(target+1):
#             for j in range(i,target+1-i):
#                 if target-i-j>=j:
#                     all_tup.append((i,j,target-i-j))
#         print(all_tup)
#         for i in all_tup:
#             temp=defaultdict(lambda :0)
#             for j in i:
#                 temp[j]+=1
#             temp_ans=1
#             print(temp)
#             for k in temp:
#                 print(d[k],temp[k])
#                 temp_ans*=(comb(d[k],temp[k]))
#             ans+=temp_ans
#         return ans
# class Solution:
#     def gameOfLife(self, board) -> None:
#         print(board)
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         r,c=len(board),len(board[0])
#         def all_valid(i,j):
#             ans=[]
#             for ind in [i-1,i,i+1]:
#                 for ind2 in [j-1,j,j+1]:
#                     if ind>=0 and ind<r and ind2>=0 and ind2<c and not(ind==i and ind2==j):
#                         ans.append((ind,ind2))
#             print(ans)
#             return ans
                        
                
#         def score(i,j):
#             inds=all_valid(i,j)
#             s=0
#             for ind in inds:
#                 s=s+board[ind[0]][ind[1]]%2
#             if s<2 and board[i][j]:
#                 board[i][j]=3
#             elif s<2 and not board[i][j]:
#                 pass
                
#             elif s<4 and board[i][j]:
#                 pass
#             elif s==3 and not board[i][j]:
#                 board[i][j]=2
#             elif s>3 and board[i][j]:
#                 board[i][j]=3
#             else:
#                 pass
#         for i in range(r):
#             for j in range(c):
#                 score(i,j)
#         for i in range(r):
#             for j in range(c):
#                 board[i][j]=board[i][j]%2
#         print(board)
# class Solution:
#     """docstring for Solution"""
#     def code(self, n):
#         ans=[[None]*n for _ in range(n)]
#         i=0
#         counter=1
#         print(ans)
#         while(counter<=n*n):
#             for x in range(i,n-i):
#                 ans[i][x]=counter
#                 counter+=1
#             for x in range(i+1,n-i):
#                 print(i,x)
#                 ans[x][n-i-1]=counter
#                 counter+=1
#             for x in range(n-i-2,i-1,-1):
#                 ans[n-i-1][x]=counter
#                 counter+=1
#             for x in range(n-i-2,i,-1):
#                 ans[x][i]=counter
#                 counter+=1
#             i+=1
            
#         return ans
# class Solution:
#     def maximumScore(self, scores, edges) -> int:
#         d=defaultdict(lambda :[])
#         for i in edges:
#             # if d[i[0]]:
#             d[i[0]].append(i[1])
#             # else:
#                 # d[i[0]]=i[1]

#             d[i[1]].append(i[0])
#         n=len(scores)
#         print(d)
#         # visited=[0]*n
#         ma=-1
#         for i,j in enumerate(scores):
#             visited=[i]
#             # visited[i]=1
#             for k in d[i]:
#                 # print(k)
#                 # visited[k]=1
#                 visited.append(k)
#                 for l in d[k]:
#                     if l in visited:
#                         pass
#                     else:
#                         visited.append(l)
#                         for m in d[l]:
#                             if m in visited:
#                                 pass
#                             else:
#                                 # visited.append(m)
#                                 # print(i,k,l,m)
#                                 ma=max(ma,scores[i]+scores[k]+scores[l]+scores[m])
#                                 # visited.pop()
#                                 # print(visited)
#                         visited.pop()
#                 visited.pop()
#         # print(d)
#         return ma
# import lru_cache
# class Solution:
    
#     def minimumEffortPath(self, heights) -> int:
#         r=len(heights)
#         c=len(heights[0])
#         visited=[[None for _ in range (r)] for _ in range(c)]
#         # @lru_cache
#         def travel(row,col):
#             if row==r-1 and col==c-1:
#                 return 0
#             if row>r-1 or col>c-1 or row<0 or col<0:
#                 return 0
#             else:
#                 print(heights[row][col])
                
#                 a,b,e,f=10**6,10**6,10**6,10**6
#                 if row+1<r and not visited[row+1][col]  :
#                     a=max(heights[row+1][col]-heights[row][col],travel(row+1,col))
#                 if row-1>-1 and not visited[row-1][col]  :
#                     b=max(heights[row-1][col]-heights[row][col],travel(row-1,col))
#                 if col+1<c and not visited[row][col+1]  :
#                     e=max(heights[row][col+1]-heights[row][col],travel(row,col+1))
#                 if col-1>-1 and not visited[row][col-1]  :
#                     f=max(heights[row][col-1]-heights[row][col],travel(row,col-1))
#                 visited[row][col]=True
#                 print((row,col),a,b,e,f)
#             return min(a,b,e,f)
                
                
                
                
#         return travel(0,0)
# class Solution:
#     def letterCombinations(self, digits: str):
#         dic={'2':['a','b','c'],'3':['d','e','f']}
#         ans=[]
#         def yielder(st,ans):
#             if not len(st):
#                 return ''
#             for i in range(len(st)):
#                 for j in dic[st[i]]:
#                     ans.append(j+yielder(st[i:],ans))
#         yielder(digits,ans)
#         return ans
# from functools import reduce
# class Solution:
#     # @return a list of strings, [s1, s2]
#     def letterCombinations(self, digits):
#         if '' == digits: return []
#         kvmaps = {
#             '2': 'abc',
#             '3': 'def',
#             '4': 'ghi',
#             '5': 'jkl',
#             '6': 'mno',
#             '7': 'pqrs',
#             '8': 'tuv',
#             '9': 'wxyz'
#         }
#         return reduce(lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]], digits,[''])
from heapq import *                 
# class Solution:
#     def minimumObstacles(self, grid) -> int:
#         m=len(grid)
#         n=len(grid[0])
#         dp=[[100]*n for _ in range(m)]
#         visited=[[False]*n for _ in range(m)]
#         dp[0][0]=0
#         q=[[0,0,0]]
#         def valid_cells(x,y):
#             ans=[]
#             # if x-1>=0 :
#             #     ans.append([x-1,y])
#             # if y-1>=0:
#             #     ans.append([x-1,y])
#             for i,j in [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]:
#                 if i>=0 and j>=0 and i<m and j<n:
#                     ans.append([i,j])
#             return ans
                
#         while q:
#             temp=heappop(q)
#             visited[temp[1]][temp[2]]=True
#             for i in valid_cells(temp[1],temp[2]):
#                 if not visited[i[0]][i[1]]:
#                     dp[i[0]][i[1]]=min(dp[i[0]][i[1]],temp[0]+grid[i[0]][i[1]])
#                     heappush(q,[dp[i[0]][i[1]],i[0],i[1]])
#         print(dp)
#         return dp[-1][-1]
from itertools import accumulate
class Mat:
    def __init__(self, matrix):
        self.matrix=matrix
    def pm(self):
        for i in self.matrix:
            print(i)

# class NumMatrix:

#     def __init__(self, matrix):
#         # cum_mat=matrix
#         a=Mat(matrix)
#         a.pm()
#         for i in range(len(matrix)):
#             matrix[i]=list(accumulate(matrix[i]))
#         for j in range(len(matrix[0])):
#             for i in range(len(matrix)-1):
#                 matrix[i+1][j]=matrix[i][j]+matrix[i+1][j]
#         self.matrix=matrix
#         print('\n')
#         a=Mat(matrix)
#         a.pm()
#         # print(matrix)
#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         row1=max(0,row1-1)
#         col1=max(0,col1-1)
#         if row1==0 and col1==0:
#             return self.matrix[row2][col2]
            
#         elif row1==0:
#             print('here')
            
#             return self.matrix[row2][col2]-self.matrix[row2][col1]
#         elif col1==0:
#             return self.matrix[row2][col2]-self.matrix[row1][col2]
#         else:
#             return self.matrix[row2][col2]+self.matrix[row1][col1]-self.matrix[row1][col2]-self.matrix[row2][col1]

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d=defaultdict(lambda:-1)
        offset=0
        ans=0
        cur=0
        i=0
        n=len(s)
        base=0
        while(i<n):
            if d[s[i]]<base or d[s[i]]==-1:
                cur+=1
                d[s[i]]=i
                i+=1
            else:
                ans=max(ans,cur+offset)
                cur=0
                offset=i-d[s[i]]-1
                base=d[s[i]]
                d[s[i]]=-1
        ans=max(ans,cur+offset)
        return ans
        # while(i<n):
        #     if d[s[i]]==-1:
        #         cur+=1
        #         d[s[i]]=i
        #         i+=1
        #     else:
        #         ans=max(ans,cur)
        #         cur=0
        #         temp=s[i]
        #         # print(d)
        #         i=d[s[i]]+1
        #         d=defaultdict(lambda:-1)
        # ans=max(ans,cur)
        # return ans
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n=len(s)
#         r=0
#         def xxx(mid1,mid2):
#             while(mid1>0 and mid2<n and s[mid1]==s[mid2]):
#                 mid1-=1
#                 mid2+=1
#             # print(mid1,mid2)
            
#             return (mid1+1,mid2-1)
#         x,y=0,0
#         for i in range(n):
#             mid1,mid2=xxx(i,i)
#             l1=mid2-mid1
#             mid11,mid22=xxx(i,i+1)
#             l2=mid22-mid11
            
#             if l1>r:
#                 x,y=mid1,mid2
#                 r=l1
#                 print(mid1,mid2)
#             if l2>r:
#                 x,y=mid11,mid22
#                 r=l2
#                 print(mid11,mid22)
#         return s[x:y+1]#
from typing import List
# class Solution:
#     def largestMagicSquare(self, grid: List[List[int]]) -> int:
#         m=len(grid)
#         n=len(grid[0])
#         row_cum=[[0]*(n+1) for _ in range(m)]
#         for i in range(m):
#             for j in range(n):
#                 row_cum[i][j+1]=row_cum[i][j]+grid[i][j]
#         col_cum=[[0]*(n) for _ in range(m+1)]
#         for i in range(m):
#             for j in range(n):
#                 col_cum[i+1][j]=col_cum[i][j]+grid[i][j]
#         up_diag_cum=[[0]*(n+1) for _ in range(m+1)]
#         for i in range(m):
#             for j in range(n):
#                 up_diag_cum[i+1][j+1]=up_diag_cum[i][j]+grid[i][j]
#         l_diag_cum=[[0]*(n+1) for _ in range(m+1)]
#         for i in range(m):
#             for j in range(n,-1,-1):
#                 l_diag_cum[i][j]=l_diag_cum[i+1][j+1]+grid[i][j]
#         q=min(m,n)
#         print(row_cum)
#         # print(up_diag_cum)
#         # print(col_cum)
#         ans=0
#         for i in range(1,q):
#             for j in range(m-i):
#                 for k in range(n-i):
#                     for l in range(m-i):
#                     if (row_cum[j][k+i]-row_cum[j][k])==(col_cum[j+i][k]-col_cum[j][k])==(up_diag_cum[j+i][k+i]-up_diag_cum[j][k]):
#                         ans=max(ans,i)
#         return ans
# class Solution:
#     def longestStrChain(self, words: List[str]) -> int:
#         # def checker(s1,s2):
#         #     if len(s2)-len(s1)!=1:
#         #         return False
#         #     i,j=0,0
#         #     counter=0
#         #     while(i<len(s1) and j<len(s2)):
#         #         if s1[i]==s2[j] and counter<=1:
#         #             i+=1
#         #             j+=1
#         #         else:
#         #             j+=1
#         #             counter+=1
#         #         if counter>1:
#         #             return False
#         #     return True
#         n=len(words)
#         # for i in range(n):
#         #     for j in range(i,n):
#         #         # print(words[i],words[j],checker(words[i],words[j]))
#         #         pass
#         # word_tuples=[(len(word),word) for word in words]
#         # word_tuples.sort()
#         # ans=0
#         dp=defaultdict(lambda: 1)
#         # s=set(words)
#         words.sort(key=lambda x:len(x))
#         for word in words:
#             for i in range(len(word)):
#                 pred=word[:i]+word[i+1:]
#                 if pred in dp:
#                     dp[word]=max(dp[pred]+1,dp[word])
#         if dp.values():
#             return max(dp.values())
#         else:
#             return 1

        # for i in range(n):
        #     for j in range(n):
        #         if checker(words[i],words[j]):
        #             dp[j]=max(dp[j],1+dp[i])
        # print(dp)
        # return max(dp)
        # for i in range(n):
        #     # cur_counter=dp[i]
        #     cur_word=word_tuples[i][1]
        #     # cur_ind=i
        #     for j in range(i+1,n):
        #         if checker(cur_word,word_tuples[j][1]):
        #             # cur_word=word_tuples[j][1]
        #             dp[j]=max(dp[j],dp[i]+1)
        #             # cur_ind=j
        #     # ans=max(ans,cur_counter)
        # # print(ans+1)
        # print(max(dp))



        # print(word_tuples)

# def is_prime(x):
#     temp=x//2+1
#     ans=True
#     for i in range(2,temp+1):
#         if not x%i:
#             x=x/i
#             ans=False
#     return ans
# # lis=[i for i in range(3,100000) if is_prime(i)]
# # print(lis)
# def K_primes(a,b,k):
#     dp=[1]*(b+1)
#     # dp[2]=1
#     for i in range(2,b):
#         temp=i
#         for j in range(1,i//2+1):
#             if temp%j==0:
#                 dp[i]=dp[temp]+dp[j]
#     print(dp)          

    # for i in range(a,b+1):
    #     temp=i
    #     for j in range(2,i//2+1):
    #         if not temp%j and :
    #             dp[i]=dp[temp//]


# K_primes(15,29,2)
# a=Solution()
# print(a.longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]))
# print(a.lengthOfLongestSubstring('aaadvdfefa'))
# print(a.longestPalindrome("abba"))
# print(a.largestMagicSquare([[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]))
# a=NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
# a=NumMatrix([[-1]])
# print(a.sumRegion(0,0,0,0))


# print(a.letterCombinations('23'))
# print(a.hasAllCodes("10010111100001110010",5))
# print(a.minimumObstacles([[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]))
# print(a.maximumScore([5,2,7,9,10],[[0,1],[1,2],[2,3],[0,2],[3,4]]))



# arr=[1,4,2,3,31,1,222,111,1111]
# n=len(arr)
# ans=0
# i=0
# while(i<n-1):
#     j=1
#     while(i <n-1 and arr[i+1]>=arr[i]):
#         i+=1
#         j+=1
#     ans+=j*(j+1)/2
#     i+=1
# print(ans)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val #parent
        self.left = left
        self.right = right
    def __repr__(self):
        if self.par:
            return ' val  :'+str(self.val)+'  parent '+str(self.par.val)+" visited "+str(self.visited)
        else:
            return ' val  :'+str(self.val)+' visited '+str(self.visited)

class Solution:
    def minCameraCover(self, root) -> int:
        root.par=None
        heap=[]
        def cardinality(temp):
            ans=0
            ans+=temp.visited==False
            if temp.par:
                ans+=temp.par.visited==False
            if temp.right:
                ans+=temp.right.visited==False
            if temp.left:
                ans+=temp.left.visited==False
            return ans
        def max_card(arr):
            ans=0
            ret=None
            for n,i in enumerate(arr):
                if i.visited:
                    continue
                if ans<(t:=cardinality(i)):
                    ans=t
                    ret=n
                # ans=max(ans,cardinality(i))
            if ret!=None:
                # print(ret)
                return arr[ret]
            else:
                # print('here')
                return ret 


        ans2=0

        def trav(node):
            if node:
                if node.left:
                    node.left.par=node
                trav(node.left)
                # node.par=node
                # node.card=node.val!=None+node.left!=None+node.right!=None+1
                node.visited=False
                heap.append(node)
                # print(node)
                if node.right:
                    node.right.par=node
                trav(node.right)
        trav(root)  
        k1=0  
        while(True):
            temp=max_card(heap)
            if temp==None:
                break
            # temp=heapq.heappop(heap)
            print(heap)
            if not temp.visited:
                ans2+=1
                # if temp.visited:
                temp.visited=True
                if temp.par:
                    temp.par.visited=True
                if temp.right:
                    temp.right.visited=True
                if temp.left:
                    temp.left.visited=True
            # if k1>8:
            #     break
            # k1+=1
        # print(heap)
        # temp=max_card(heap)
        # print(temp)
        # print(temp.visited)

        return ans2

a=TreeNode(3)
b=TreeNode(4)
c=TreeNode(5)
d=TreeNode(1)
e=TreeNode(2)
f=TreeNode(7)
g=TreeNode(6)
a.right=b
b.left=c
c.right=d
d.right=e
# a.right=c
# b.left=g
# g.left=e
# e.right=d
# b.right=f
# c.left=d
# d.left=e
abc=Solution()
print(abc.minCameraCover(a))




