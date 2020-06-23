"""
Completed: 22.06.20
Converting a decimal number to binary through long divison.

"""

def to_binary(num):
    small_result = num
    result = ""
    while small_result != 0:
        num = small_result
        remainder = small_result%2
        small_result = small_result//2
        print(num, "/2 = ", small_result, " remainder ", remainder)
        result = str(remainder) + result
    return result
    


num = int(input("Please enter a number to be converted into binary: "))
result = to_binary(num)
print("The result is: ", result)