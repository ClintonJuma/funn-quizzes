#Question
#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
#Trial one
word=input("Enter a string: ")
rvs=word[::-1]
print(rvs)
if word==rvs:
    print("The word is a palindrome")

else:
    print("The word is not a palindrome")



