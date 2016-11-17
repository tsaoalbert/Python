cnt=1

def hanoi(ndisks, startPeg=1, endPeg=3):
    if ndisks:
        global cnt
        names =["","A","B","C"]
        n1=hanoi( ndisks-1, startPeg, 6-startPeg-endPeg)
       
        print "%5d: Move disk %d from %s to %s" % (cnt, ndisks, names[startPeg], names[endPeg])
 
        cnt = cnt + 1;
        hanoi( ndisks-1, 6-startPeg-endPeg, endPeg)
    else:
        # do nothing
        pass
        


hanoi(4,1,3)


