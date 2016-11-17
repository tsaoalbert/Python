cnt=0
N=input ("Please input a number: ")

def display(queens):
    print
    for i in queens:
        for j in range(N):
            if j==i:
                print "Q",
            else:
                print "*",
        print
    print
          
def Fine(queens, row):
    c = 0
    ans = True
    curr = queens[row]
    for i in range(row):
        c=c+1
        other = queens[row-c]
        if (curr == other) or (curr-c == other) or (curr+c == other):
            ans = False
            break
    return ans

def Permute(queens, row):
    global cnt
    for i in range(N):
        queens[row] = i
        if Fine(queens, row):
            if row == N-1:
                cnt = cnt + 1
                print str(cnt) + str(": "),
                
                print(queens)
                display(queens)
                
            else:
                Permute(queens, row+1)
                




queens = [0]*N

Permute(queens, 0)

