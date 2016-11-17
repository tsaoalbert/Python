
"""

Name: xxx
Date:  mm/dd/yyyy
Description: To print out a Christmas tree with decoration of differnt symbols
Feedback:  the lecture is interesting/confusing/boring, easy/difficult,, or whatever you feel about the lecture.
"""
"""
define a function "line: which prints a line of "n" symbol "c"
"""
def line(n,c):
    s = ""
    for i in range(n):
        #print c,
        s+=c
    return s
    

"""
 Your comments here
"""
def trunk(n,c,d, m):
    w = n/4
    list = []
    for i in range(n):
        s = line(m-w,d) + line(2*w+1,c) + line(m-w,d)
        list.append(s)
    return list

"""
define a function "triangle" chich prints an isoceles
of symbol "c". The length of the base is 2*n+1
and the height is "n"
"""

def triangle (n,c,d,m):
    list = []
    for i in range(n/3,n):
        #c = chr (ord('0')+i )
        j = m-i
        k = 2*i+1;
        s = line (j,d)+ line(k,c) + line (j,d) 
        list.append(s);
    return list
        

"""
define a function called "tree" which prints
"n" isoceles with symbol "c"
"m" is distance to the left edge of the screen
"""
def tree(n,c,d,m):
    list = []
    for i in range (n):
        list = list + triangle(i,c,d,m)
    return list

def decorate(list):
    dec = [[10,10, "#"]]
    for r,c,d in dec:
        s = list[r]
        list[r] = s[:c]+d+s[c:]

def markX (m):
    s = " "
    for i in range (2*m+1):
        s += chr ( ord('0')+i%10) 
    return s
        
n=10
c="*"
d=" " # d is the symbol of blank
m=n+3 # m is the distance to the lefe edge of the screen
list = tree(n,c,d,m) + trunk(n,c,d,m)
list.append(line (2*m+1, '^' )) # print the ground




snow1 = []
snow1.append( "          ,===.               ")
snow1.append( "         _|___|_              ")
snow1.append( "  __/     /. .\      /__      ")
snow1.append( "   /`.    \___/    ,'\        ")
snow1.append( "      `. .'=*=`. .'           ")
snow1.append( "        Y   *   Y             ")
snow1.append( "         \  *  /              ")
snow1.append( "         .`---'.              ")
snow1.append( "       .`   *   '.            ")
snow1.append( "       |    *    |            ")
snow1.append( "       \    *    /            ")
snow1.append( "    __.-`._____.'-.__         ") 
snow1.append( ".'`                `'..       ")
snow1.append( "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
snow2=[]
snow2.append("                  _________               ")
snow2.append("                 |         |              ")
snow2.append("                 | HELLO   |              ")
snow2.append("                 |         |              ")
snow2.append("                 |         |              ")
snow2.append("                 |_________|              ")
snow2.append("             ____|_________|_____         ")
snow2.append("                 /          \             ")
snow2.append("                J   *   *    L            ")
snow2.append("                |     *      |            ")
snow2.append("                J  *     *   F            ")
snow2.append("                 \   * *    /             ")
snow2.append("           _|     `.     .'               ")
snow2.append("             \   .-'      `-.     |__     ")
snow2.append("              |.'    *       `._.-'       ")
snow2.append("              /                \          ")
snow2.append("             J     *            L         ")
snow2.append("            F                  J          ")
snow2.append("             L     *            J         ")
snow2.append("             J                  F         ")
snow2.append("        -.    \     *          /          ")
snow2.append("   VK     `---.>              <_.----.__  ")
snow2.append("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")


decorate (list)
margin = "  ";

snow = [] + snow1
print margin + "   " + markX(m)
c = " ";
j = len(snow) -len(list)
for i in range(len(list)):
    print margin,
    print "%2d"%i,
    print list[i],
    if (j>=0):
        print snow[j]
    else:
        print 
    j= j+1


