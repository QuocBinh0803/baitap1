def foo(array):
    sum_result = 0
    product_result = 1

    for num in array:
        sum_result += num
    
    for num in array:
        product_result *= num

    print("sum =", sum_result,", Product =", product_result )

my_array = [2,3,4,5]
foo(my_array)