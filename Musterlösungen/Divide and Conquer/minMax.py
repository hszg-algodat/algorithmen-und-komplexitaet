import random

def minMax(ls, count):
    if len(ls) == 1:
        min = ls[0]
        max = ls[0]
        return min, max, count
    else:
        if len(ls) == 2:
            count += 1
            if ls[0] < ls[1]:
                min = ls[0]
                max = ls[1]
            else:
                min = ls[1]
                max = ls[0]
            return min, max, count
        else:
            left = ls[:int(len(ls)/2)]
            right = ls[int(len(ls)/2):]
            return minMaxMerge(minMax(left, count), minMax(right, count))

def minMaxMerge(left, right):
    minLeft, maxLeft, countLeft = left
    minRight, maxRight, countRight = right
    count = countLeft + countRight

    count += 1
    if minLeft < minRight:
        min = minLeft
    else:
        min = minRight
    count += 1
    if maxLeft > maxRight:
        max = maxLeft
    else:
        max = maxRight
    return min, max, count

ls = []
for i in range(0,round(random.uniform(1, 200))):
    ls.append(round(random.uniform(-10000,10000)))

x, y, count = minMax(ls, 0)

print("Min: "+str(x)+", Max: "+str(y))
print("2(n - 1) = "+ str(2 * (len(ls) - 1)))
print("Count: "+str(count))

print("")
print(ls)
