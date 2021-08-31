
#program to check whether the inputted string palindrome or not

str=input("Enter a String...:")
revstr=str[::-1]

if str==revstr:
    print("Its Palindrome String....")
else:
    print("Its Not Palindrome....")