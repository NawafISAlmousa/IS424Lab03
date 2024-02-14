numList = []
largestValue = None
for x in range(10):
    num = int(input(f"Enter value  {x+1}: "))
    numList.append(num)
largestValue = numList[0]
for x in numList:
    if x > largestValue:
        largestValue = x
print(f"Largest Value is : {largestValue}")