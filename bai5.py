def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            for k in range(100000):
                print(str(arrayA[i]) + "," + str(arrayB[j]))

array_A = [1,3,5]
array_B = [2,4,6]
printUnorderedPairs(array_A,array_B)            