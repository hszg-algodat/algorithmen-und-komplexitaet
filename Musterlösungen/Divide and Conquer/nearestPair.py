import math
import random
import matplotlib.pyplot as plt

def nearestPair(points):
    points = sort(points)
    return nearestPairRec(points)

def nearestPairRec(points):
    if len(points) == 2:
        return points[0], points[1]
    if len(points) == 3:
        return nearestPairOutOfThreePairs((points[0],points[1]),(points[0],points[2]),(points[1],points[2]))
    leftPoints = points[:int(len(points)/2)]
    rightPoints = points[int(len(points)/2):]
    barrier = rightPoints[0][0] - ((rightPoints[0][0] - leftPoints[len(leftPoints)-1][0]) / 2)
    return mergePoints(leftPoints, rightPoints, nearestPairRec(leftPoints), nearestPairRec(rightPoints), barrier)

def mergePoints(leftPoints, rightPoints, leftPairNearest, rightPairNearest, barrier):
    points_ = []
    delta = minDistance(leftPairNearest, rightPairNearest)
    for i in range(0,len(leftPoints)):
        if calcDistance(leftPoints[i], (barrier, leftPoints[i][1])) < delta:
            points_.append(leftPoints[i])
    for i in range(0,len(rightPoints)):
        if calcDistance(rightPoints[i], (barrier, rightPoints[i][1])) < delta:
            points_.append(rightPoints[i])
    if len(points_) == 0:
        if calcDistance(leftPairNearest[0], leftPairNearest[1]) < calcDistance(rightPairNearest[0], rightPairNearest[1]):
            return leftPairNearest
        else:
            return rightPairNearest
    candidatePair = (points_[0], points_[len(points_)-1])
    for i in range(0,len(points_)):
        for j in range(0,len(points_)):
            if not i == j:
                if calcDistance(points_[i],points[j]) < calcDistance(candidatePair[0],candidatePair[1]):
                    candidatePair = (points_[i], points_[j])
    return nearestPairOutOfThreePairs(candidatePair, leftPairNearest, rightPairNearest)

def minDistance(p1, p2):
    if calcDistance(p1[0], p1[1]) < calcDistance(p2[0],p2[1]):
        return calcDistance(p1[0],p1[1])
    else:
        return calcDistance(p2[0],p2[1])

def calcDistance(point1, point2):
    a = abs(point1[0] - point2[0])
    b = abs(point1[1] - point2[1])
    c_2 = a * a + b * b
    return math.sqrt(c_2)

def nearestPairOutOfThreePairs(pair1, pair2, pair3):
    dist1 = calcDistance(pair1[0], pair1[1])
    dist2 = calcDistance(pair2[0], pair2[1])
    dist3 = calcDistance(pair3[0], pair3[1])
    if dist1 < dist2 and dist1 < dist3:
        return pair1
    else:
        if dist2 < dist1 and dist2 < dist3:
            return pair2
        else:
            return pair3

def sort(list): #Mergesort
    if len(list) < 2:
        return list
    else:
        lList = list[:int(len(list)/2)] # left List
        rList = list[int(len(list)/2):] # right list
        return merge(sort(lList), sort(rList))

def merge(lList, rList):
    if len(lList) == 0:
        return rList
    if len(rList) == 0:
        return lList
    if lList[0][0] < rList[0][0]:
        result = [lList[0]]
        return  result + merge(lList[1:],rList)
    else:
        result = [rList[0]]
        return result + merge(lList,rList[1:])

points = []
size = 100
numberOfPoints = 10
for i in range(0, numberOfPoints):
    points.append((random.uniform(-size,size), random.uniform(-size,size)))

# for i in range(0, len(points)):
#     j = i + 1
#     if j == len(points):
#         j = 0
#     print("Point1 "+str(points[i][0])+", "+str(points[i][1])+"; Point2 "+str(points[j][0])+", "+str(points[j][1])+": "+str(calcDistance(points[i], points[j])))

point1, point2 = nearestPair(points)

fig = plt.subplot()

pointsX = []
pointsY = []

for point in points:
    pointsX.append(point[0])
    pointsY.append(point[1])

fig.plot(pointsX, pointsY, 'bo')
fig.plot(point1[0], point1[1], 'ro')
fig.plot(point2[0], point2[1], 'go')

plt.show()

# print(str(point1[0]) + ", "+str(point1[1]))
# print(str(point2[0]) + ", "+str(point2[1]))
