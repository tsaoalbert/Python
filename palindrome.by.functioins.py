# funtion 1
def removeSpace(s1):
    s2=""
    for letter in s1:
        if letter==" "or letter=="*" :
                pass
        else:
            s2 = s2 + letter
            #print letter,
    #print "check removeSace: " + s2
    return s2

#  funtion 2
def reverse(s1):
    return s1[::-1]

#  funtion 3
def isPalindrome(s1):
    s1 = removeSpace(s1)
    s2 = reverse(s1)
    if s1==s2:
        print  " is Palindrome"
        return True     
    else:
        print  " is not Palindrome"
        return False

# ----- test all the functions ------
s1 = "x   race  *****carx  " 
print s1, 
ans = isPalindrome(s1)


