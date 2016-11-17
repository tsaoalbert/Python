def isPalindrome():
    string1 = input('Enter a string: ');
    string2 = string1[::-1]
    if string1 == string2:
        print 'It is a palindrome'
    else:
        print 'It is not a palindrome'

isPalindrome()
