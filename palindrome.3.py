def palindrome3(s):
    if s == s[::-1]:
        print s + " is  a palindrome"
    else:
        print s +  " Is not a palindrome"



palindrome3 ("aabbaa")

s = input('input a string: ')
palindrome3(s)
