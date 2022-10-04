import datetime

def fn(dt1,dt2):
	months = {	'01':'January',
		'02':'February',
		'03':'March',
		'04':'April',
		'05':'May',
		'06':'June',
		'07':'July',
		'08':'August',
		'09':'September',
		'10':'October',
		'11':'November',
		'12':'December'		}
	months=dict((x,y) for y,x in months.items())
	day,month,year=dt1.split()
	day2,month2,year2=dt2.split()
	month,month2=months[month],months[month2]
	print(day2,month2,year2)
	day,month,year=map(int,[day,month,year])
	day2,month2,year2=map(int,[day2,month2,year2])
	diff=datetime.date(year2,month2,day2)-datetime.date(year,month,day)
	print(diff.days)
	return diff.days
print(fn('1 January 2022','31 March 2022'))
# class Solution:
#     def makesquare(self, matchsticks) -> bool:
#     	ans=set()
#     	parts=[]

#         matchsticks.sort()
#     	n=len(matchsticks)
#     	x=sum(matchsticks)//4
#     	if (x*4)!=sum(matchsticks):
#     		return False

#     	def fn(ind,s,parts,ans):
    		
#     		if s==0:
#     			ans.add(tuple(parts))
#     		if ind>=n:
#     			return
#     		if s-matchsticks[ind]>=0:
#     			fn(ind+1,s,parts,ans)
#     			fn(ind+1,s- matchsticks[ind],parts+[ind],ans)
#     		else:
#     			fn(ind+1,s,parts,ans)
#     	fn(0,x,[],ans)
#     	# print(ans)
#     	def is_disjoint(s1,s2,s3):
#     		return not set.intersection(s1,s2) and not set.intersection(s1,s3) and  not set.intersection(s3,s2)
#     	for i in ans:
#     		for j in ans:
#     			for k in ans:
#     				if is_disjoint(set(i),set(j),set(k)):
#     					# print(i,j,k)
#     					return True
#     	return False
    	
# a=Solution()
# print(a.makesquare([2,3,2,1,6,2,5,3,4]))