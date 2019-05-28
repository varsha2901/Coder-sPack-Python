#To multiply all the numbers in a list
def multiply(numbers):  
    product = 1
    for x in numbers:
        product *= x  
    return product 
print(multiply((8, 2, 3, -1, 7)))
