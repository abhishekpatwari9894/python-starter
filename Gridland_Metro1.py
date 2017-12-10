import sys
def countLampposts(track,n):
    if track==None:
        return n[0]*n[1]
    else:
        for train in track:
            for i in range(0,len(train)):
                train[i]=train[i]-1
        #print(track)
        c=0
        flag=0
        for i in range(0,n[0]):
            for j in range(0,n[1]):
                flag=0
                for train in track:
                    if i==train[0]:
                        if j>=train[1] and j<=train[2]:
                        flag=1
                        #print(i,j,"abc")
                if flag!=1:
                    c=c+1
                    
    return c    
        
        
        
n=list(map(int,input().strip().split()))
track=[]
for i in range(n[2]):
    track_1=list(map(int,input().strip().split()))
    track.append(track_1)

result=countLampposts(track,n)
print(result)
