def is_palindrome(s):
    n = len(s)
    m = n/2
    for i in range(m):
        if s[i] != s[n-i-1]:
            print s + ' is not a palindrome'
            return 
    print s+ ' is a palindrome'
 

print is_palindrome('malayayalam')
