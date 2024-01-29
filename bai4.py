def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            if arrayA[i] < arrayB[j]:
                print(str(arrayA[i]) + "," + str(arrayB[j]))
array_A = [1,3,5]
array_B = [2,4,6]
printUnorderedPairs(array_A,array_B)             
