
import matplotlib.pyplot as plt
import functions_yehg as f

## Introduce Teacher ##

class Teacher:
    # define attributes of class
    def __init__(self, first_name, last_name, instrument):
        self.first_name = first_name
        self.last_name = last_name
        self.instrument = instrument
    
    # define method to greet student
    def greet_student(self):
        print(f"Hi! My name is {self.first_name} {self.last_name}\n")
        print(f"I will be your music teacher. You can call me teacher {self.first_name}\n")
        print(f"The instrument I play is the {self.instrument}\n")
        
# create instance to introduce teacher name
teacher1 = Teacher('Grace','Yeh', 'Violin')
teacher1.greet_student()

        
print("I am going to teach you how to read music notation\n\nLet's start by looking at some pictures", sep = ' ')


## Display pictures ##

#List of image names
imagelist = ['crotchetnote.png','stave.png','notesandstave.png']

# while loop for user to view pictures
check1 = True

while check1 == True:
    # Ask user which image they want to see
    userinput1 = int(input("What picture would you like to see?\n\nEnter 1 to see 'Notes'\nEnter 2 to see 'the Stave'\nEnter 3 to see 'Notes on the Stave\nEnter 0 once you have seen everything\n\nEnter[1/2/3/0]: "))

    if userinput1 == 1:
        check1 == True
        print("\nThis is a note, say it outloud: Note!\n")
        f.imagedisplay(imagelist[0])
        plt.show()  #Show image after the text, or else all images will be displayed together at the end
    
    elif userinput1 == 2:
        check1 == True
        print("\nNotes are drawn on the stave.\nThis is the stave. Say it outloud: Stave!\n")
        f.imagedisplay(imagelist[1])
        plt.show()
    
    elif userinput1 == 3:
        check1 == True
        print("\nThese are multiple notes on a stave\n")
        f.imagedisplay(imagelist[2])
        plt.show()  #Show image after the text, or else all images will be displayed together at the end
    
    elif userinput1 == 0:
        check1 == False
        break            

## Teaching note alphabet ##
print('__________________________________________________________')
print()
f.stave()
print("Now we are going to learn the letter names of notes\n")
print("There are 2 groups of notes:\n1) Notes 'in the space'\n2) Notes 'on the line'" )


check2 = True

while check2 == True:
    userinput2 = int(input("What would you like to learn?\nEnter 1 to learn the 'Notes in the space'\nEnter 2 to learn 'Notes on the line'\nEnter 0 when done\n\nEnter[1/2/0]: "))   
    f.teach(userinput2)
    
    if userinput2 == 0:
        check2 == False
        break 


## Test; bar graph display; check if user passed the test, redo if failed ##
        
check3 = False
while check3 == False:
    
    print("\nLet's test ourselves\nTEST 1: 'Notes in the space' -- FACE")
    totalscore1 = f.test1()
    
    print("\nTEST 2: 'Notes on the line' -- EGBDF")
    totalscore2 = f.test2()
    
    ## Bar graph of score ##
    totalscore = totalscore1 + totalscore2
    totalscorepossible = 9
    f.bargraph(totalscore, totalscorepossible)
    
    # Retake the test if total score < 5
    if totalscore < 5:
        print("\nPlease retake the test\n")
        check3 = False
    elif totalscore >= 5:
        print("Well done! You passed!")
        check3 = True


print("Congratulations. You are now competent in identifying the alphabet names of musical notes!")
    
