import sys


arguments = sys.argv[1:]

nums = str(arguments[0])
data = []
with open(nums) as f:
    for line in f:
        data.append([int(x) for x in line.split()])

newData = []
for i in data:
    for j in i:
        newData.append(j)

m = sorted(newData)[len(newData) // 2]
print(sum(abs(v - m) for v in newData))