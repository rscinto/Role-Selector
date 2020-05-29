
#Roles 1-5 are required
#1 Project Manager
#2 Deputy PM
#3 Lead Engi
#4 Lead Sci
#5 Lead Admin
#6 Engi
#7 Engi
#8 *Engi
#9 Sci
#10 Sci
#11 *Sci
#12 Admin
#13 Admin
#14 *Admin
#* one of these will have 3

#manning array of a team of 12
# [1,1,1,1,1,2,3,2]

#Ask user for name and top 5 picks
    #looped routine with a switch
#Create a scientist object and confgure(name Choices)
#Shuffle Scientists

#Fill positions one at a time
    #sift through scientists for top pick,
    # then second pick or third... until a person 
    # is found to fill. If no one found at all,
    # random scientist assigned role
 
 #Roles assigned top down, random scientist
 #array keeps things fair.

#randomizes the roster
import random

NUM_CHOICES = 6
NUM_POSITIONS = 12
BUFFER = NUM_POSITIONS * 2
NUM_Scientists = 12
 
class Scientist:

    role = 0

    def getRole(self):
        if self.role == 1:
            return "Project Manager"
        elif self.role == 2:
            return "Deputy Project Manager"
        elif self.role == 3:
            return "Lead Engi"
        elif self.role == 4:
            return "Lead Sci"
        elif self.role == 5:
            return "Lead Admin"
        elif self.role == 6:
            return "Engineer"
        elif self.role == 7:
            return "Scientist"
        else:
            return "Admin"
    #End getRole

    def __init__(self, name, topSix):

        self.name = name

        self.topSix = [None] * BUFFER

        #need iteration
        for i in range(0, NUM_CHOICES):
            self.topSix[i] = topSix[i] 

#END SCIENTIST CLASS

#main                        main                        main 

#priming read for name
userName = str(input('What is your name? (0 to quit): '))

#declare Roster of sccientists
roster = []

#Scientist Entry Routine
while userName != "0":

    userChoices = [None] * BUFFER
    
    print("Enter your top 6 positions in order starting from your faorite.")
    print("#1 Project Manager")
    print("#2 Deputy PM")
    print("#3 Lead Engi")
    print("#4 Lead Sci")
    print("#5 Lead Admin")
    print("#6 Engi")
    print("#7 Sci")
    print("#8 Admin")

    for index in range(0, NUM_CHOICES):
        print('Choice :', index + 1)
        userChoices[index] = int(input("Position #: "))
        #userChoices.append(int(input("Position #: ")))

    newScientist = Scientist(userName, userChoices)
    roster.append(newScientist)
    userName = str(input('What is your name? (0 to quit): '))
#END WHILE

#randomization routine is done 10 times because CPU time is cheap
#for i in range(0, 10):
    #random.shuffle(roster)

#create role roster
#list of user choices
   # print("#1 Project Manager")
   # print("#2 Deputy PM")
   # print("#3 Lead Engi")
   # print("#4 Lead Sci")
   # print("#5 Lead Admin")
   # print("#6 Engi")
   # print("#7 Sci")
   # print("#8 Admin")

#OVERALL ROSTER
#1 Project Manager
#2 Deputy PM
#3 Lead Engi
#4 Lead Sci
#5 Lead Admin
#6 Engi
#7 Engi
#8 *Engi
#9 Sci
#10 Sci
#11 *Sci
#12 Admin
#13 Admin
#14 *Admin
#puts string names into positions 1-14
rosterNumber = 0
roleRoster = []

#routine fills the first  positions
#later routine will go past whos left and 
#fill in the team roles

#going through the first 8 roles
#prime internal temp
temp = roster.pop()
for x in range(1,8):

    positionFilled = False
    
    while not positionFilled:

        #goes through user selected roles
        for z in range(0,6):
            #checks all in roster for 1st pick, 2nd and so on
            if temp.topSix[z] == x:
                temp.role = x
                roleRoster.append(temp)
                positionFilled = True
                break
            #last resort fullfillment
            elif z == 5 and not positionFilled:
                temp.role = x
                roleRoster.append(temp)
                positionFilled = True
                break
            else:
                roster.append(temp)
                temp = roster.pop()
        #END for loop
    #End While
#END OVERALL ROSTER FORLOOP


#fills in positions with 2 or more
#goes until empty

#going through the first filling last 4
#if it can't then it will assign randomly
numPasses = 0

while roster.count > 0:

    for x in range(6,9):

        positionFilled = False
        
        while not positionFilled:

            #goes through user selected roles
            for z in range(0,6):
                #checks all in roster for 1st pick, 2nd and so on
                if temp.topSix[z] == x:
                    temp.role = x
                    roleRoster.append(temp)
                    positionFilled = True
                    break
                #last resort fullfillment 
                elif numPasses > 5:
                    temp.role = x
                    roleRoster.append(temp)
                    positionFilled = True
                    break

                else:
                    roster.append(temp)
                    temp = roster.pop()
                    numPasses = numPasses + 1
            #END for loop
        #End While     while not filled
    #END FORLOOP     Engi, Sci and Admin
#End While         Not empty roster
    

for Scientist in roleRoster:
    print('Name: ' + Scientist.name + ' Role: ' + Scientist.role)

#team roles assigning who's left 
#going through roster 6,7,8 until no more people left. 

    

    

#main                        main                        main 


"""

This is a random role selecting machine. The program creates Scientist objects and stores them in an array. ("roster") Each Scientist object has (<int>role, <str>name, <int>[] ). The roster is shuffled several times before it is referenced again. Once it is shuffled there are 2 routines that assign the role <int> to each Scientists. It's basically two different filters. 

Routine #1 assigns the first 9 slots of the #OVERALL ROSTER, Line 27. The first role sought out by the machine is Project Manager and down from there. A random Scientist is selected to see if this job was there top pick. If that person is found they are assigned the role. If not, the search continues for 2nd place picks, and on. If none are found then the program will force a decision. 

This allows for greater than %50 of Scientists to get their number one pick. 
(math help)

Routine #2
Once Management and first pick of engi, sci and admin have been set. The rest of the team roles will be assigned in descending order with higher picks getting the roles at random and forced decisions if there are no selections made. 

Print
Line 221 is the goal to aim for. 


State of machine: 
The logic of the machine is %90 there with some implementation challenges.
Last fail:

"""

"""
This is Line 257: Important information
"""
