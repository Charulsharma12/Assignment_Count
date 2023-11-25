#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

string = input("Enter the string:")

count_lower = 0 #Total count of lower characters
count_upper = 0 #Total count of upper characters

def upper_and_lower(string):
    
    global count_lower #global variable count_lower and count_upper
    global count_upper

    for char in string: #characters in the string
        if char.isupper(): #if and else function to count upper and lower characters
            count_upper = count_upper + 1 

        elif char.islower():
            count_lower = count_lower + 1

    return count_lower, count_upper
print(upper_and_lower(string)) #printing the values 