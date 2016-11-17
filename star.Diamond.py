def PrintOneLine(m,c):
    j=0
    while j < m:
        print c,
        j=j+1

def PrintOneLineReturn(m,c):
    PrintOneLine(m,c)
    print 


mark = "A"
mark2 = "."
n = input("Input dimond's size:")

if (n%2==0):
    n = n-1;

i = 1
m=n/2+1
PrintOneLineReturn(n+2,mark2)


while i < n:
    PrintOneLine(m,mark2)
    PrintOneLine(i,mark)
    PrintOneLineReturn(m,mark2)  
    i=i+2
    m= m-1

while i > 0 :
    PrintOneLine(m,".")
    PrintOneLine(i, mark)
    PrintOneLineReturn(m,mark2)  
    i=i-2
    m= m+1
    
PrintOneLineReturn(n+2,mark2)
    
