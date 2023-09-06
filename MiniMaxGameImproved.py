'''
Here more factors are added to static estimation function\
    to improve the selection of child nodes
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
    
'''
Counts number of double closed morrises
Input: board position
output: number of closed double morrises of White
'''
def DoubleMorris(b):
    cnt=0
    #9,10,11,6,5
    if (b[11]==b[10]==b[6]==b[9]==b[5]=='W'):
        cnt+=1
    #12,13,14,7,3
    if (b[12]==b[13]==b[14]==b[7]==b[3]=='W'):
        cnt+=1
    #15,16,17,8,1
    if (b[15]==b[16]==b[17]==b[8]==b[1]=='W'):
        cnt+=1
    #12,14,13,10,16
    if (b[12]==b[14]==b[13]==b[10]==b[16]=='W'):
        cnt+=1
    #6,8,7,3,14
    if (b[6]==b[8]==b[7]==b[3]==b[14]=='W'):
        cnt+=1
    #15,17,16,13,10
    if (b[15]==b[17]==b[16]==b[13]==b[10]=='W'):
        cnt+=1
    #9,11,10,13,16
    if (b[9]==b[11]==b[10]==b[13]==b[16]=='W'):
        cnt+=1
    #5,11,6,7,8
    if (b[5]==b[11]==b[6]==b[7]==b[8]=='W'):
        cnt+=1
    #1,17,8,7,6
    if (b[1]==b[17]==b[6]==b[7]==b[8]=='W'):
        cnt+=1
    #5,3,1,8,17
    if (b[1]==b[3]==b[5]==b[8]==b[17]=='W'):
        cnt+=1
    #11,14,17,8,1
    if (b[11]==b[14]==b[17]==b[8]==b[1]=='W'):
        cnt+=1
    #11,6,5,3,1
    if (b[11]==b[1]==b[6]==b[3]==b[5]=='W'):
        cnt+=1
    #5,6,11,14,17
    if (b[11]==b[14]==b[6]==b[17]==b[5]=='W'):
        cnt+=1
    #11,14,17,16,15
    if (b[11]==b[14]==b[17]==b[16]==b[15]=='W'):
        cnt+=1
    #9,12,15,16,17
    if (b[12]==b[15]==b[16]==b[9]==b[17]=='W'):
        cnt+=1
    #11,10,9,12,15
    if (b[11]==b[10]==b[12]==b[9]==b[15]=='W'):
        cnt+=1
    #9,10,11,14,17
    if (b[11]==b[10]==b[14]==b[9]==b[17]=='W'):
        cnt+=1
    #11,17,14,7,3
    if (b[11]==b[17]==b[14]==b[7]==b[3]=='W'):
        cnt+=1
    #1,5,3,7,14
    if (b[1]==b[3]==b[5]==b[7]==b[14]=='W'):
        cnt+=1
    #9,15,12,13,14
    if (b[9]==b[15]==b[12]==b[13]==b[14]=='W'):
        cnt+=1
    #11,17,14,13,12
    if (b[11]==b[17]==b[14]==b[13]==b[12]=='W'):
        cnt+=1
    
    return cnt

'''
A “3 pieces configuration” offers the opportunity to close a morris in two places. This function checks the same.
Input: board position
Output: number of 3 piece configurations possible for White
''' 
def threepiece(b):
    cnt=0
    #9,10,11,6,5
    if ((b[11]==b[10]==b[6]=='W' and b[9]==b[5]=='x') or (b[11]==b[10]==b[5]=='W' and b[9]==b[6]=='x') or (b[11]==b[9]==b[6]=='W' and b[10]==b[5]=='x') or (b[11]==b[5]==b[9]=='W' and b[6]==b[10]=='x')):
        cnt+=1
    #12,13,14,7,3
    if ((b[13]==b[14]==b[7]=='W' and b[3]==b[12]=='x') or (b[13]==b[14]==b[3]=='W' and b[7]==b[12]=='x') or (b[12]==b[14]==b[7]=='W' and b[3]==b[13]=='x') or (b[12]==b[14]==b[3]=='W' and b[7]==b[13]=='x')):
        cnt+=1
    #15,16,17,8,1
    if ((b[16]==b[17]==b[8]=='W' and b[1]==b[15]=='x') or (b[16]==b[17]==b[1]=='W' and b[8]==b[15]=='x') or (b[15]==b[17]==b[8]=='W' and b[1]==b[16]=='x') or (b[15]==b[17]==b[1]=='W' and b[8]==b[16]=='x')):
        cnt+=1
    #12,14,13,10,16
    if ((b[14]==b[13]==b[10]=='W' and b[12]==b[16]=='x') or (b[14]==b[13]==b[16]=='W' and b[12]==b[10]=='x') or (b[12]==b[13]==b[10]=='W' and b[14]==b[16]=='x') or (b[12]==b[13]==b[16]=='W' and b[14]==b[10]=='x')):
        cnt+=1
    #6,8,7,3,14
    if((b[8]==b[7]==b[3]=='W' and b[6]==b[14]=='x') or (b[8]==b[7]==b[14]=='W' and b[3]==b[6]=='x') or (b[6]==b[7]==b[3]=='W' and b[8]==b[14]=='x') or (b[6]==b[7]==b[14]=='W' and b[3]==b[8]=='x')):
        cnt+=1
    #15,17,16,13,10
    if((b[17]==b[16]==b[13]=='W' and b[10]==b[15]=='x') or (b[17]==b[16]==b[10]=='W' and b[15]==b[13]=='x') or (b[15]==b[16]==b[13]=='W' and b[17]==b[10]=='x') or (b[15]==b[16]==b[10]=='W' and b[13]==b[17]=='x')):
        cnt+=1
    #9,11,10,13,16
    if((b[11]==b[10]==b[13]=='W' and b[9]==b[16]=='x') or (b[11]==b[10]==b[16]=='W' and b[9]==b[13]=='x') or (b[10]==b[9]==b[13]=='W' and b[11]==b[16]=='x') or (b[9]==b[10]==b[16]=='W' and b[11]==b[13]=='x')):
        cnt+=1
    #5,11,6,7,8
    if((b[11]==b[7]==b[6]=='W' and b[8]==b[5]=='x') or (b[11]==b[6]==b[8]=='W' and b[5]==b[7]=='x') or (b[5]==b[7]==b[6]=='W' and b[11]==b[8]=='x') or (b[6]==b[5]==b[8]=='W' and b[7]==b[11]=='x')):
        cnt+=1
    #1,17,8,7,6
    if((b[17]==b[8]==b[7]=='W' and b[1]==b[6]=='x') or (b[17]==b[8]==b[6]=='W' and b[1]==b[7]=='x') or (b[1]==b[8]==b[7]=='W' and b[6]==b[17]=='x') or (b[1]==b[8]==b[6]=='W' and b[7]==b[17]=='x')):
        cnt+=1
    #5,3,1,8,17
    if((b[3]==b[1]==b[8]=='W' and b[17]==b[5]=='x') or (b[3]==b[1]==b[17]=='W' and b[5]==b[8]=='x') or (b[5]==b[1]==b[8]=='W' and b[3]==b[17]=='x') or (b[5]==b[1]==b[17]=='W' and b[3]==b[8]=='x')):
        cnt+=1
    #11,14,17,8,1
    if((b[14]==b[17]==b[8]=='W' and b[1]==b[11]=='x') or (b[14]==b[17]==b[1]=='W' and b[11]==b[8]=='x') or (b[11]==b[17]==b[8]=='W' and b[14]==b[1]=='x') or (b[11]==b[17]==b[1]=='W' and b[14]==b[8]=='x')):
        cnt+=1
    #11,6,5,3,1
    if((b[3]==b[5]==b[6]=='W' and b[11]==b[1]=='x') or (b[6]==b[1]==b[5]=='W' and b[11]==b[3]=='x') or (b[11]==b[5]==b[3]=='W' and b[1]==b[6]=='x') or (b[11]==b[5]==b[1]=='W' and b[6]==b[3]=='x')):
        cnt+=1
    #5,6,11,14,17
    if((b[11]==b[14]==b[6]=='W' and b[17]==b[5]=='x') or (b[11]==b[17]==b[6]=='W' and b[5]==b[14]=='x') or (b[11]==b[5]==b[14]=='W' and b[6]==b[17]=='x') or (b[11]==b[5]==b[17]=='W' and b[6]==b[14]=='x')):
        cnt+=1
    #11,14,17,16,15
    if((b[14]==b[17]==b[16]=='W' and b[11]==b[15]=='x') or (b[14]==b[17]==b[15]=='W' and b[11]==b[16]=='x') or (b[11]==b[17]==b[16]=='W' and b[14]==b[15]=='x') or (b[11]==b[17]==b[15]=='W' and b[14]==b[16]=='x')):
        cnt+=1
    #9,12,15,16,17
    if((b[12]==b[15]==b[16]=='W' and b[9]==b[17]=='x') or (b[12]==b[15]==b[17]=='W' and b[9]==b[16]=='x') or (b[15]==b[9]==b[16]=='W' and b[12]==b[17]=='x') or (b[17]==b[15]==b[9]=='W' and b[12]==b[16]=='x')):
        cnt+=1
    #11,10,9,12,15
    if((b[12]==b[10]==b[9]=='W' and b[11]==b[15]=='x') or (b[9]==b[10]==b[15]=='W' and b[11]==b[12]=='x') or (b[11]==b[9]==b[12]=='W' and b[10]==b[15]=='x') or (b[11]==b[15]==b[9]=='W' and b[12]==b[10]=='x')):
        cnt+=1
    #9,10,11,14,17
    if((b[11]==b[10]==b[14]=='W' and b[9]==b[17]=='x') or (b[11]==b[10]==b[17]=='W' and b[9]==b[14]=='x') or (b[11]==b[9]==b[14]=='W' and b[10]==b[17]=='x') or (b[11]==b[17]==b[9]=='W' and b[14]==b[10]=='x')):
        cnt+=1
    #11,17,14,7,3
    if((b[17]==b[14]==b[7]=='W' and b[11]==b[3]=='x') or (b[17]==b[14]==b[3]=='W' and b[7]==b[11]=='x') or (b[11]==b[14]==b[7]=='W' and b[17]==b[3]=='x') or (b[11]==b[14]==b[3]=='W' and b[7]==b[17]=='x')):
        cnt+=1
    #1,5,3,7,14
    if((b[5]==b[3]==b[7]=='W' and b[1]==b[14]=='x') or (b[3]==b[14]==b[5]=='W' and b[1]==b[7]=='x') or (b[1]==b[3]==b[7]=='W' and b[14]==b[5]=='x') or (b[1]==b[3]==b[14]=='W' and b[5]==b[7]=='x')):
        cnt+=1
    #9,15,12,13,14
    if((b[15]==b[12]==b[13]=='W' and b[9]==b[14]=='x') or (b[15]==b[12]==b[14]=='W' and b[9]==b[13]=='x') or (b[12]==b[9]==b[13]=='W' and b[14]==b[15]=='x') or (b[12]==b[14]==b[9]=='W' and b[13]==b[15]=='x')):
        cnt+=1
    #11,17,14,13,12
    if((b[17]==b[14]==b[13]=='W' and b[11]==b[12]=='x') or (b[17]==b[14]==b[12]=='W' and b[11]==b[13]=='x') or (b[11]==b[14]==b[13]=='W' and b[12]==b[17]=='x') or (b[11]==b[14]==b[12]=='W' and b[17]==b[13]=='x')):
        cnt+=1
    
    return cnt


#to check if it is a leaf
def ter(b):
    if (b.count('W')<3 or b.count('B')<3):
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
        return staticEstimationImproved(b)
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
        return staticEstimationImproved(b)
    
    if(h<depth):
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
Output: number of closed mills possible for white
'''
def PossibleMillsW(b):
    mills=0
    for i in range(0,len(b)):
        if (b[i]=='W'):
            if(closeMill(i, b)):
                mills+=1
    return -(-mills//3)

'''
Input: board position
Output: number of closed mills possible for black
'''
def PossibleMillsB(b):
    mills=0
    for i in range(0,len(b)):
        if (b[i]=='B'):
            if(closeMill(i, b)):
                mills+=1
    return -(-mills//3)

'''
Counts number of 2 piece configurations so that the next move is a mill
Input: board position
Output: number of 2 piece configurations for white
'''
def n2pcW(b):
    cnt=0
    for i in range(0,len(b)):
        if (b[i]=='x'):
            b1=b
            #b1[i]='W'
            temp=list(b1)
            temp[i]='W'
            b1="".join(temp)
            if closeMill(i, b1):
                cnt+=1
    return cnt

'''
Counts number of 2 piece configurations so that the next move is a mill
Input: board position
Output: number of 2 piece configurations for white
'''
def n2pcB(b):
    cnt=0
    for i in range(0,len(b)):
        if (b[i]=='x'):
            b1=b
            #b1[i]='W'
            temp=list(b1)
            temp[i]='B'
            b1="".join(temp)
            if closeMill(i, b1):
                cnt+=1
    return cnt

'''
Counts number of blocked pieces 
Input: board position
Output: number of blocked white pieces
'''
def nbloW(b):
    cnt=0
    s=0
    nwp=b.count('W')
    if (nwp>3):
        for i in range(0,len(b)):
            if (b[i]=='W'):
                n=neighbours(i)
                for j in n:
                    if (b[j]=='x'):
                        s+=1
                if(s==0):
                    cnt+=1
                s=0
    return cnt

'''
Counts number of blocked pieces 
Input: board position
Output: number of blocked white pieces
'''
def nbloB(b):
    cnt=0
    s=0
    nbp=b.count('B')
    if (nbp>3):
        for i in range(0,len(b)):
            if (b[i]=='B'):
                n=neighbours(i)
                for j in n:
                    if (b[j]=='x'):
                        s+=1
                if(s==0):
                    cnt+=1
                s=0
    return cnt

'''
Winning configuration for white
Input: board position
Output: 1 if white wins or 0
'''
def WCW(b):
    if (b.count('B')<3):
        return 1
    if (nbloB(b)==b.count('B')):
        return 1
    else:
        return 0
    
'''
Winning configuration for black
Input: board position
Output: 1 if black wins or 0
'''
def WCB(b):
    if (b.count('W')<3):
        return 1
    if (nbloW(b)==b.count('W')):
        return 1
    else:
        return 0

'''
Input: board position
Output: number of closed double morrises of White
'''
def DoubleMorrisW(b):
    return DoubleMorris(b)

'''
Input: board position
Output: number of closed double morrises of Black
'''
def DoubleMorrisB(b):
    b1=swap(b)
    return DoubleMorris(b1)

'''
Input: board position
Output: number of 3 piece configurations for white
'''
def n3pcW(b):
    return threepiece(b)

'''
Input: board position
Output: number of 3 piece configurations for white
'''
def n3pcB(b):
    b1=swap(b)
    return threepiece(b1)

'''
Input: board position
Output: Static estimation value
'''
def staticEstimationImproved(b):
    numwhitepieces=0
    numblackpieces=0
    #blackmoveslist=[]
    #blackmoveslist=generateBlackMoves(b)
    #numblackmoves=len(blackmoveslist)
    for i in b:
        if (i=='W'):
            numwhitepieces+=1
        elif (i=='B'):
            numblackpieces+=1
    
    if (numwhitepieces<=3):
        E1=n2pcW(b)-n2pcB(b)
        E2=n3pcW(b)-n3pcB(b)
        E3=PossibleMillsW(b)-PossibleMillsB(b)
        E4=WCW(b)-WCW(b)
        return (8*E1 + E2 + 13*E3 + 1500*E4)
    else: 
        H1=PossibleMillsW(b)-PossibleMillsB(b)
        H3=nbloB(b)-nbloW(b)
        H4=numwhitepieces-numblackpieces
        H6=DoubleMorrisW(b)-DoubleMorrisB(b)
        H7=WCW(b)-WCW(b)
        return (12*H1 + 8*H3 + 6*H4 + 34*H6 + 1500*H7)


if __name__=="__main__":
    position=getinputposition()
    print ("Given input position:"+position)
    depth=int(input("Enter depth:"))
    h=0
    #to play as black uncomment lines 659-661 and comment 663
    '''
    s=swap(position)
    (m,minimax_estimate)=MaxMin(s, h)
    m=swap(m)
    '''
    (m,minimax_estimate)=MaxMin(position, h)
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
    