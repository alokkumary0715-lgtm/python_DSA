"""here we learn abt extraction of digits from a number"""
"""to get the last digit of a number we can use modulus operator with 10"""
n = 12345
last_digit = n % 10 # this will give us the last digit of the number  #"%" THIS GIVE US THE REMAINDER OF THE DIVISION OF N BY 10, WHICH IS THE LAST DIGIT OF N
# # '//' THIS GIVE US THE QUOTIENT OF THE DIVISION OF N BY 10, WHICH IS THE NUMBER WITHOUT THE LAST DIGIT
print("Last digit:", last_digit)

#start code
nums = 12345
n = nums # this will give us the number of digits in the number
while n > 0:
    last_digit = n % 10 # this will give us the last digit of the number
    print(last_digit)
    n = n // 10 # this will give us the number without the last digit


#count the number of digits in a number
nums = 12345
n = nums # this will give us the number of digits in the number
count = 0
while n > 0:
    last_digit = n % 10 # this will give us the last digit of the number
    count += 1 # this will count the number of digits in the number
    n = n // 10 # this will give us the number without the last digit
print("Number of digits:", count) 

"""JAB BHI ITERATION EK PARTICULAR DIGIT KE DIVIDE SE HO RAHA HO TO USKA TIME COMPLEXITY O(LOG AND NICHE THAT NUMBER (N))"""


# CHECK PALINDROME NUMBER



NUM = 12345
n = NUM
reversed_num = 0
while n > 0:
    last_digit = n % 10
    reversed_num = (reversed_num * 10) + last_digit
    n = n // 10
if NUM == reversed_num:
    print("Palindrome number")
else:    
    print("Not a palindrome number:",reversed_num)


#amstrong number
num = 153
n = num
total = 0
nod =len(str(num)) # this will give us the number of digits in the number
while n > 0:
    ld = n % 10
    total += ld ** nod # this will give us the sum of the digits raised to the power of the number of digits
    n = n // 10 
if num == total:
    print("Amstrong number")
else:    print("Not an Amstrong number")

