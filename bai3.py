def printPairs(array):
    for i in array:
        for j in array:
            print(str(i) + "," + str(j))
        
my_array = [1,2,3,4]
printPairs(my_array)