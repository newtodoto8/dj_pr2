import re
# class Solution(object):
# def simplifyPath(s):
#     s=s+'/'
#     pat=r'/\./'
#     pat2=r'/+'
#     pat3=r'/[a-z,A-Z,\.,\_]+/\.\./'
#     # pat3=r'/w+/\.\./'

#     print(s)
#     # s='////.//////////hero//'
#     s=re.sub(pat2,'/',s)
#     print(s)
#     while(re.search(pat,s)):
#         s=re.sub(pat,'/',s)
#     print(s)
#     while(re.search(pat3,s)):
#         s=re.sub(pat3,'/',s,count=1)
#         print(s,'adasd')
#         s=re.sub(pat2,'/',s)
#         print('steps:',s)
#     # s=re.sub(pat2,'/',s)
#     while(re.search(pat3,s)):
#         s=re.sub(pat3,'/',s,count=1)
#         print('steps:',s)
#     print('after double dot',s)
#     # s=re.sub()
#     while(re.search(r'/\.\./',s)):
#         s=re.sub(r'/\.\./','/',s)
#     print(s)
#     s=re.sub(pat2,'/',s)
#     print(s)
#     news=''
#     if s=='/':
#         return s
#     if s[-1]=='/':
#         s=s[:-1]

#     # for i in range(len(s)-1,1,-1):

#     print(s)
        
# simplifyPath("/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///")
# simplifyPath("/../")
# def minRemoveToMakeValid(s: str) -> str:
#         inds=[]
#         arr=[]
#         l=len(s)
#         c=0
#         for i in range(l):
#             if s[i]==')':
#                 if c==0:
#                     inds.append(i)
#                 else:
#                     c-=1
#                     inds.pop()
#             elif s[i]=='(':
#                 inds.append(i)
#                 c+=1
#             else:
#                 pass
#         j=0
#         if not inds:
#             return s
#         print (inds)
#         for i in range(l):
#             if j<len(inds) and i==inds[j]:
#                 j+=1
#             else:
#                 arr.append(s[i])

#         return ''.join(arr)
def validateStackSequences( pushed, popped) -> bool:
    cur=0
    last_i=0
    j=0
    pus=[]
    # pus.append(pushed[0])
    while(True):
        if pus and pus[-1]==popped[j]:
            pus.pop()
            j+=1
            # last_i+=1(las)
        else:
            if (last_i==len(pushed)):
                break
            pus.append(pushed[last_i])
            last_i+=1
        print(pus)
    if pus:
        return False
    else:
        return True

# print(minRemoveToMakeValid("a)b(c)d"))
print(validateStackSequences([1,2,3,4,5],[4,1,3,2,5]))