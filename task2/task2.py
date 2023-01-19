import math
import sys

arguments = sys.argv[1:]

circle = str(arguments[0])
points = str(arguments[1])

data = []
with open(circle) as f:
    for line in f:
        data.append([float(x) for x in line.split()])
        
newData = []
for i in data:
    for j in i:
        newData.append(j)

x_start = newData[0]
y_start = newData[1]
radius = newData[2]



pointsArr = []
with open(points) as f:
    for line in f:
        pointsArr.append([float(x) for x in line.split()])

newPoints = []

for i in pointsArr:
    x_point = i[0]
    y_point = i[1]
    p = math.sqrt((x_start - x_point) ** 2 + (y_start - y_point) ** 2)
    if p < radius:
        print('1\n')
    else:
        if p == radius:
            print('0\n')
        else:
            print('2\n')
    
 