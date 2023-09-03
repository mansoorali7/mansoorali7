 Write a Python function to sum all the numbers in a list.
 Sample List : (8, 2, 3, 0, 7)

Expected Output : 20

Explanation:

Summation should like 8+2+3+0+7 = 20

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

OUTPUT:
def sample_list_numbers(i):
    summation = 0
    for num in i:
        sum = summation+num
sample_list = (8,2,3,0,7)
result = sum_list_numbers(sample_list)
print("Expected Output:", result)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Write a Python program to reverse a string.

Sample String : "1234abcd"

Expected Output : "dcba4321"

OUTPUT:

def reverse_string(sample_string):
    for i in sample_string:
         i =sample_string[::-1]
sample_string = "1234abcd"
Expected_Output = reverse_string(sample_string)
print("Expected output :", i)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

﻿Sample String : 'The quick Brow Fox'

Expected Output :

No. of Upper case characters : 3

No. of Lower case Characters : 12

OUTPUT:

def count_uppercase_lowercase(input_string):
    uppercase_count=0
    lowercase_count=0
    for i in input_string:
        if i.isupper():
            uppercase_count+=1
        elif i.islower():
            lowercase_count+=1
    return uppercase_count, lowercase_count
input_string = 'The quick Brow Fox'    
uppercase, lowercase = count_uppercase_lowercase(input_string)
print("No of upper case characters :", uppercase)
print("No of lower case characters :", lowercase)
