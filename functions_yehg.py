"""
Created on Sat Nov  2 16:50:14 2019

@author: grace
"""

import matplotlib.pyplot as plt
import matplotlib.image as imgplt

########################################################################

## Image Display: Displays images stacked on top of each other ##

def imagedisplay(imagename):
    imgmatrix = imgplt.imread(imagename) # reads image pixels, converts to matrix
    plt.figure()  # print images stacked ontop of each other, not overlapped
    img = plt.imshow(imgmatrix) # displays picture
    return img

########################################################################

## Musical notes functions: Draws out the pattern of musical notes ##

# Draws basic pattern of 5 lines   
def stave():
    print('These 5 lines are called the Stave.\n')
    for row in range(10):
        for col in range(20):
            if (row == 0 or row == 2 or row == 4 or row == 6 or row == 8):
                print('-', end = '')
        print() 
    print('Musical notes are represented by small circles on the stave\n')


#  Pattern of first 4 notes F,A,C,E -- 'Notes in the Space'
      
def lowfnote():
    print()
    for row in range(10):
        for col in range(20):
            if (row == 0 or row == 2 or row == 4 or row == 6 or row == 8):
                print('-', end = '') #  prints '-' only for the above rows
        if (row == 0 or row == 2 or row == 4 or row == 6):
            print() # empty line for the above rows
        if (row == 7):
            print('         O         ' ) #print the note in the specified row
        
        
def anote():
    print()
    for row in range(10):
        for col in range(20):
            if (row == 0 or row == 2 or row == 4 or row == 6 or row == 8):
                print('-', end = '')
        if (row == 0 or row == 2 or row == 4 or row == 6):
            print()
        if (row == 5):
            print('         O         ' )
            

def cnote():
    print()
    for row in range(10):
        for col in range(20):
            if (row == 0 or row == 2 or row == 4 or row == 6 or row == 8):
                print('-', end = '')
        if (row == 0 or row == 2 or row == 4 or row == 6):
            print()
        if row == 3:
            print('         O         ' )
 
     
def highenote():
    print()
    for row in range(10):
        for col in range(20):
            if (row == 0 or row == 2 or row == 4 or row == 6 or row == 8):
                print('-', end = '')
        if (row == 0 or row == 2 or row == 4 or row == 6):
            print()
        if row == 1:
            print('         O         ' )


#  Pattern of next 5 notes E,G,B,D,F -- 'Notes on the line'
    
def lowenote():
    print()
    for row in range(11):
        for col in range(20):
            if (row == 0 or row == 2 or row == 4 or row == 6):
                print('-', end = '') #  prints '-' only for the above rows
        if (row == 0 or row == 2 or row == 4 or row == 6):
            print() # new line only after each row is printed
        if (row == 8 ):
            print('---------O----------' ) # #print the note and line in the specified row


def gnote():
    print()
    for row in range(11):
        for col in range(20):
            if (row == 0 or row == 2 or row == 4 or row == 8):
                print('-', end = '') 
        if (row == 0 or row == 2 or row == 4 or row == 8):
            print() 
        if (row == 6 ):
            print('---------O----------' )


def bnote():
    print()
    for row in range(11):
        for col in range(20):
            if (row == 0 or row == 2 or row == 6 or row == 8):
                print('-', end = '')
        if (row == 0 or row == 2 or row == 6 or row == 8):
            print()
        if (row == 4 ):
            print('---------O----------' )


def dnote():
    print()
    for row in range(11):
        for col in range(20):
            if (row == 0 or row == 4 or row == 6 or row == 8):
                print('-', end = '')
        if (row == 0 or row == 4 or row == 6 or row == 8):
            print()
        if (row == 2 ):
            print('---------O----------' )
 
           
def highfnote():
    print()
    for row in range(11):
        for col in range(20):
            if (row == 10 or row == 2 or row == 6 or row == 8):
                print('-', end = '')
        if (row == 10 or row == 2 or row == 6 or row == 8):
            print()
        if (row == 0 ):
            print('---------O----------' )
  
          
#########################################################################

## Teaching functions: Displays the note patterns in 2 groups
            ## User can choose which group to view first

def teach(userinput2):
    
    if userinput2 ==1:
        print("\nThis is F")
        lowfnote()
        print("\n\nThis is A")
        anote()
        print("\n\nThis is C")
        cnote()
        print("\n\nThis is E")
        highenote()
        print("\n\nHow do you remember the alphabet names?\nUse the mnemonic 'FACE'\nIt gives you the note names from bottom to top\n")
    
    elif userinput2 == 2:
        print("\n\nThis is E")
        lowenote()
        print("\n\nThis is G")
        gnote()
        print("\n\nThis is B")
        bnote()
        print("\n\nThis is D")
        dnote()
        print("\n\nThis is F")
        highfnote()
        print("\n\nHow do you remember the alphabet names?\nUse the mnemonic 'EVERY GOOD BOY DOES FINE'\nThe FIRST LETTER of EACH WORD corresponds to\nthe note name from bottom to top\n")
  
      
#####################################################################

## Testing function: Function displays notes one-by-one ##
        # User asked to enter their answer
        # Computer marks the answer as correct or incorrect

# Ask user functions
def askandreply1():
    ask1 = input('What note is this? Enter F, A, C, or E: ').upper()
    return ask1

def askandreply2():
    ask2 = input('What note is this? Enter E, G, B, D or F: ').upper()
    return ask2


# Test 1 - F,A,C,E
def test1():
    totalscore1 = 0  # score counter
    
    lowfnote()  # displays note pattern
    answerf = askandreply1()  # user asked to enter answer
    if answerf == 'F': # check if answer is correct
        print('Correct!') 
        totalscore1 += 1  # score counter increased if answer is correct
    else:
        print('Incorrect. Next question')
    
    anote()
    answera = askandreply1()
    if answera == 'A':
        print('Correct!')
        totalscore1 += 1
    else:
        print('Incorrect. Next question')
    
    cnote()
    answerc = askandreply1()
    if answerc == 'C':
        print('Correct!')
        totalscore1 += 1
    else:
        print('Incorrect. Next question')    
        
    highenote()
    answere = askandreply1()
    if answere == 'E':
        print('Correct!')
        totalscore1 += 1
    else:
        print('Incorrect. Next question')    
        
        
    print(f'\nYou got {totalscore1} out of 4 questions right\n')
    return totalscore1 # when  assign  function to variable, value is totalscore1


# Test 2 - E,G,B,D,F    
def test2():
    totalscore2 = 0
    
    lowenote()
    answere = askandreply2()
    if answere == 'E':
        print('Correct!')
        totalscore2 += 1
    else:
        print('Incorrect. Next question')
    
    gnote()
    answerg = askandreply2()
    if answerg == 'G':
        print('Correct!')
        totalscore2 += 1
    else:
        print('Incorrect. Next question')
    
    bnote()
    answerb = askandreply2()
    if answerb == 'B':
        print('Correct!')
        totalscore2 += 1
    else:
        print('Incorrect. Next question')    
        
    dnote()
    answerd = askandreply2()
    if answerd == 'D':
        print('Correct!')
        totalscore2 += 1
    else:
        print('Incorrect. Next question')    
    
    highfnote()  
    answerf = askandreply2()
    if answerf == 'F':
        print('Correct!')
        totalscore2 += 1
    else:
        print('Incorrect. Next question')    
        
    print(f'You got {totalscore2} out of 5 questions right')
    return totalscore2 
 

########################################################################
## Total Score Displayed with bar graph ##


def bargraph(totalscore,totalscorepossible):
    leftedges = [1,4] # list of x axis positions
    heights = [totalscore,totalscorepossible-totalscore] # totalcorrect and total incorrect
    color = ['g','r']  # list of bar colors
    
    #color each bar differently since the matplotlib default is to color all the same
    for i in range(len(leftedges)):
        plt.bar(leftedges[i],heights[i],color = color[i], align = 'center')
    
    plt.title('Total number of correct and incorrect answers from both tests') #title 
    plt.ylabel('No. of Questions') # Y axis label
    plt.xticks(leftedges,['Correct','Incorrect']) # label each bar
    plt.show() # display bar chart
    
    
########################################################################    
    
    
    

