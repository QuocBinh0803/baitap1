def printUnorderedPairs(array):
    for i in range(0, len(array)):
        for j in range(i + i,len(array)):
            print(f'{array[i]},{array[j]}')

my_array = [4,5,6,7]      
printUnorderedPairs(my_array)      
