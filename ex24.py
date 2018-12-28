# Time for some fake graphics! Let’s say we want to draw game boards that look like this:

#  --- --- --- 
# |   |   |   | 
#  --- --- ---  
# |   |   |   | 
#  --- --- ---  
# |   |   |   | 
#  --- --- --- 
# This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).

# Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.



if __name__ == "__main__":
    size = int(input('Size: '))

    block = []
    block.append(' ---')
    block.append('|   |')
    block.append(' ---')

    hsegment = []
    hsegment.append(' ---')
    hsegment.append('   |')
    hsegment.append(' ---')

    vsegment = []
    vsegment.append('|   |')
    vsegment.append(' ---')

    corner = []
    corner.append('   |')
    corner.append(' ---')
    
    print(block[0] + (hsegment[0]*(size-1)))
    print(block[1] + (hsegment[1]*(size-1)))
    print(block[2] + (hsegment[2]*(size-1)))
    for x in range (1,size):
            print(vsegment[0] + (corner[0]*(size-1)))
            print(vsegment[1] + (corner[1]*(size-1)))




