import sys

arguments = sys.argv[1:]
n = int(arguments[0])
m = int(arguments[1])
m1 = m - 1
nums = list(range(1, n+1))
newArr = []
way = [nums[0]]


s = ''.join(str(x) for x in nums[0:m:1])
newArr.append(s)
for j in range(m1):
    for i in range(m1):
        nums.append(nums.pop(0)) 
    way.append(nums[0])
    s = ''.join(str(x) for x in nums[0:m:1])
    newArr.append(s)
    

for i in range(m1):
    nums.append(nums.pop(0))
way.append(nums[0])    
s = ''.join(str(x) for x in nums[0:m:1])
newArr.append(s)



temp = [] 
for x in newArr: 
    if x not in temp: 
        temp.append(x) 
newArr = temp

temp1 = [] 
for x in way: 
    if x not in temp1: 
        temp1.append(x) 
way = temp1

c = ''.join(str(x) for x in way)

#print(temp)
print(c)
