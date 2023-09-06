'''
To play black game given board position is swapped and given as\
    input and then the output is swapped and saved
'''
positions_evaluated=0
#minimax_estimate=0

#to read the input from board3.txt as mentioned in Project.pdf
def getinputposition():
    f=open('board3.txt','r')
    position=f.read()
    f.close()
    return position

'''
Input: a board position
Output: a list L of board positions
'''
def generateMovesMidgameEndgame(b):
    moves=[]
    whitepieces=0
    for i in range(0,len(b)):
        if (b[i]=='W'): 
            whitepieces+=1
    if (whitepieces==3):
        moves=generateHopping(b)
        return moves
    else:
        moves=generateMove(b)
        return moves

'''
If the game is in Endgame phase moves are generaed by hopping
Input: a board position
Output: a list L of possible child board positions 
'''
def generateHopping(b):
    hoplist=[]
    for i in range(0,len(b)):
        if (b[i]=='W'):
            for j in range(0,len(b)):
                if(b[j]=='x'):
                    bcopy=b
                    #bcopy[i]='x'
                    temp=list(bcopy)
                    temp[i]='x'
                    bcopy="".join(temp)
                    #bcopy[j]='W'
                    temp=list(bcopy)
                    temp[j]='W'
                    bcopy="".join(temp)
                    if (closeMill(j,bcopy)):
                        generateRemove(bcopy,hoplist)
                    else:
                        hoplist.append(bcopy)
    return hoplist

'''
If the game is in Midgame phase moves are generaed by moving pieces
Input: a board position
Output: a list L of possible child board positions 
'''
def generateMove(b):
    movelist=[]
    neighbourlist=[]
    for i in range(0,len(b)):
        if (b[i]=='W'):
            neighbourlist=neighbours(i)
            for j in neighbourlist:
                if (b[j]=='x'):
                    bcopy=b
                    #bcopy[i]='x'
                    temp=list(bcopy)
                    temp[i]='x'
                    bcopy="".join(temp)
                    #bcopy[j]='W'
                    temp=list(bcopy)
                    temp[j]='W'
                    bcopy="".join(temp)
                    if (closeMill(j,bcopy)):
                        generateRemove(bcopy,movelist)
                    else:
                        movelist.append(bcopy)
    return movelist

'''
Input: a board position and a list L
Output: positions are added to L by removing black pieces if there is a close mill of white pieces
'''
def generateRemove(b,movelist):
    l1=len(movelist)
    for i in range(0,len(b)):
        if (b[i]=='B'):
            if(not(closeMill(i,b))):
                bcopy=b
                #bcopy[i]='x'
                temp=list(bcopy)
                temp[i]='x'
                bcopy="".join(temp)
                movelist.append(bcopy)
    l2=len(movelist)
    if (l1==l2):
        movelist.append(b)

'''
Input: a location j in the array representing the board
Output: a list of locations in the array corresponding to j’s neighbors                        
'''
def neighbours(j):
    
    if (j==0): 
        arr=[1,2,15]
        return arr
    if (j==1): 
        arr=[0,3,8]
        return arr
    if (j==2): 
        arr=[0,4,3,12]
        return arr
    if (j==3): 
        arr=[1,5,2,7]
        return arr
    if (j==4): 
       arr=[2,9,5]
       return arr
    if (j==5): 
       arr=[3,4,6]
       return arr
    if (j==6): 
        arr=[11,7,5]
        return arr
    if (j==7): 
        arr=[6,8,3,14]
        return arr
    if (j==8): 
        arr=[1,7,17]
        return arr
    if (j==9): 
        arr=[4,10,12]
        return arr
    if (j==10): 
        arr=[9,13,11]
        return arr
    if (j==11): 
        arr=[6,10,14]
        return arr
    if (j==12): 
        arr=[9,13,15,2]
        return arr
    if (j==13): 
        arr=[12,14,10,16]
        return arr
    if (j==14): 
        arr=[11,17,7,13]
        return arr
    if (j==15): 
        arr=[0,12,16]
        return arr
    if (j==16): 
        arr=[13,15,17]
        return arr
    if (j==17): 
        arr=[8,14,16]
        return arr
    else:
        return None

'''
To check if there is a close mill at given position of either blacck or white
Input: a location j in the array representing the board and the board b
Output: true if the move to j closes a mill
'''
def closeMill(j, b):
    c=b[j]
    if(c=='W' or c=='B'):
        if (j==0):#a0
            if (b[2]==c and b[4]==c): return True#a0,b1,c2
            else: return False  
        if (j==1):#g0
            if ((b[3]==c and b[5]==c) or (b[8]==c and b[17]==c)):return True #g0,f1,e2 or g0,g3,g6
            else: return False
        if (j==2):#b1
            if (b[4]==c and b[0]==c): return True#a0,b1,c2
            else: return False 
        if (j==3):#f1
            if ((b[1]==c and b[5]==c) or (b[7]==c and b[14]==c)): return True#g0,f1,e2 or f1,f3,f5
            else: return False
        if (j==4):#c2
            if (b[2]==c and b[0]==c): return True#a0,b1,c2
            else: return False
        if (j==5):#e2
            if ((b[1]==c and b[3]==c) or (b[6]==c and b[11]==c)): return True#g0,f1,e2 or e2,e3,e4
            else: return False
        if (j==6):#e3
            if ((b[7]==c and b[8]==c) or (b[5]==c and b[11]==c)): return True#e3,f3,g3 or e2,e3,e4
            else: return False
        if (j==7):#f3
            if ((b[6]==c and b[8]==c) or (b[3]==c and b[14]==c)): return True#e3,f3,g3 or f1,f3,f5
            else: return False
        if (j==8):#g3
            if ((b[6]==c and b[7]==c) or (b[1]==c and b[17]==c)): return True#e3,f3,g3 or g0,g3,g6
            else: return False
        if (j==9):#c4
            if ((b[12]==c and b[15]==c) or (b[10]==c and b[11]==c)): return True#c4,b5,a6 or c4,d4,e4
            else: return False
        if (j==10):#d4
            if ((b[13]==c and b[16]==c) or (b[9]==c and b[11]==c)): return True#d4,d5,d6 or c4,d4,e4
            else: return False
        if (j==11):#e4
            if ((b[14]==c and b[17]==c) or (b[9]==c and b[10]==c) or (b[5]==c and b[6]==c)): return True#e4,f5,g6 or c4,d4,e4 or e2,e3,e4
            else: return False
        if (j==12):#b5
            if ((b[9]==c and b[15]==c) or (b[13]==c and b[14]==c)): return True#c4,b5,a6 or b5,d5,f5
            else: return False
        if (j==13):#d5
            if ((b[10]==c and b[16]==c) or (b[12]==c and b[14]==c)): return True#d4,d5,d6 or b5,d5,f5
            else: return False
        if (j==14):#f5
            if ((b[11]==c and b[17]==c) or (b[13]==c and b[12]==c) or (b[3]==c and b[7]==c)): return True#b5,d5,f5 or e4,f5,g6 or f1,f3,f5
            else: return False
        if (j==15):#a6
            if ((b[12]==c and b[9]==c) or (b[16]==c and b[17]==c)): return True#a6,b5,c4 or a6,d6,g6
            else: return False
        if (j==16):#d6
            if ((b[10]==c and b[13]==c) or (b[15]==c and b[17]==c)): return True#a6,d6,g6 or d4,d5,d6
            else: return False
        if (j==17):#g6
            if ((b[11]==c and b[14]==c) or (b[15]==c and b[16]==c) or (b[1]==c and b[8]==c)): return True#e4,f5,g6 or a6,d6,g6 or g0,g3,g6
            else: return False
    else:
        return False
    
def WCW(b):
    if (b.count('B')<3):
        return 1
    else:
        return 0
def WCB(b):
    if (b.count('W')<3):
        return 1
    else:
        return 0
    
'''
To select the successive node for Max position for certain depth
Input: board position and depth
Output: next move for white with minimax estimation
'''
def MaxMin(b,h):
    global positions_evaluated
    global depth
    if (h==depth or ter(b)):
        positions_evaluated+=1
        return staticEstimation(b)
    elif(h<depth):
        h=h+1
        v=-1000000
        children=generateMovesMidgameEndgame(b)
        maxChoice=[]
        for i in children:
            m=MinMax(i,h)
            if (v<m):
                v=m
                maxChoice=i
        if (h==1):
            #losing condition
            if (maxChoice==[]):
                maxChoice=children[0]
            return maxChoice,v
        return v

#to check if it is a leaf
def ter(b):
    if (WCW(b) or WCB(b)):
        return 1
    else:
        return 0

'''
To select the successive node for Min position for certain depth
Input: board position and depth
Output: next move for black with minimax estimation
'''   
def MinMax(b,h):
    global depth
    global positions_evaluated
    
    if (depth==h or ter(b)):
        positions_evaluated+=1
        return staticEstimation(b)
    elif(h<depth):
        h=h+1
        v=1000000
        bchildren=generateBlackMoves(b)
        for i in bchildren:
            v=min(v,MaxMin(i, h))
        return v
		
'''
To swap board positions i.e White to black and black to white
Input: board position
Output: swapped board position
'''   
def swap(b):
    for i in range(0,len(b)):
        if (b[i]=='W'):
            temp=list(b)
            temp[i]='B'
            b="".join(temp)
            continue
        
        if (b[i]=='B'):
            temp=list(b)
            temp[i]='W'
            b="".join(temp)
    return b

'''
Input: board position
Output: generates black moves
'''
def generateBlackMoves(b):
    x=swap(b)
    gbm=[]
    gbmswap=[]
    gbm=generateMovesMidgameEndgame(x)
    for i in gbm:
        gbmswap.append(swap(i))
    return gbmswap

'''
Input: board position
Output: returns static estimation value
'''
def staticEstimation(b):
    numwhitepieces=0
    numblackpieces=0
    blackmoveslist=[]
    blackmoveslist=generateBlackMoves(b)
    numblackmoves=len(blackmoveslist)
    for i in b:
        if (i=='W'):
            numwhitepieces+=1
        elif (i=='B'):
            numblackpieces+=1
    if (numblackpieces<=2):
        return 10000
    elif (numwhitepieces<=2):
        return -10000
    elif (numblackmoves==0):
        return 10000
    else:
        return ((1000*(numwhitepieces-numblackpieces))-numblackmoves)
    



if __name__=="__main__":
    position=getinputposition()
    print ("Given input position:"+position)
    depth=int(input("Enter depth:"))
    h=0
    s=swap(position)
    (m,minimax_estimate)=MaxMin(s, h)
    m=swap(m)
    print("Board position: "+m)
    print("Positions evaluated by static estimation:"+str(positions_evaluated))
    print("Minimax estimate:"+str(minimax_estimate))
    f=open("board4.txt",'w+')
    line1="Board Position: "+m
    line2="Positions evaluated by static estimation: "+str(positions_evaluated)
    line3="MINIMAX estimate: "+str(minimax_estimate)
    with open('board4.txt','w') as out:
        out.write('{}\n{}\n{}\n'.format(line1,line2,line3))
    f.close()
    