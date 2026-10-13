"""
Project 1
Project notes:
    Forces acting in the problem (5):
    Down: The load weight on the forklift (Wl) and the combined forklift (Wf) and operator (Wp) weight (Wf + Wp)
    Up: The ground pushes the two front wheels up with a force of 2F and the ground pushes on the two rear wheels with a force of 2R

    Equilibrium - forkilft isnt accceleration nor rotating so forces must add to zero and moments must add to zero

    Equations:
        Part a)
            Verticle force balance: Everything pushing up should equal everything pushing down to equal zero
                2F + 2R - Wl - Wf - Wp = 0
            Moment balance: The sum of the moments about any point should equal zero. Pivot point will be front wheel. Generic formula: Moment = Force * Distance from pivot point
                The Wl Force is in front of the L1 and is pulling the nose down. Wl only acts on L1.
                The Wf + Wp Force is behind the L1 and is pulling the nose up. Wf + Wp only acts on L2.
                The 2R Force is behind L2 and L3 and is pushing the back up. 2R acts on L2 and L3.
                The 2F Force is exactly at the pivot point and does not create a moment. 2F is nothing.

                Moment equation: Wl * L1 + 2R * (L2 + L3) - (Wf + Wp) * L2 = 0

                If we are taking tipping as positive, then (Wl * L1) and (2R * (L2 + L3)) are positive because they are trying to tip the forkilft.
                The ((Wf +Wp) * L2) is negative because it is trying to keep the forklift from tipping.
        
        Part b)
            We are asked to find the load the forklift is carrying. To do this we can rearrange the equation to determine the load.
            Through this our load will essentially be Y, and we can graph this with respect to another variable.
            By rearranging the moment equation we get:
            
            Wl = ((Wf + Wp) * L2 - 2R * (L2 + L3)) / L1

            The maximum stable load is the maxmimum load where the forklift wont tip. We can solve for Wl in terms of L1, L2, L3, Wf, and Wp.
            In this equation for maxmimum load, we can set R to zero because we are looking for the exact weight load where the forklift will just not tip.
            As the load increases, the reaction force from the ground to the rear wheels decreases. The maximum load tells us what load makes the rear wheels have no reaction force.
            Because of this, we can set R to zero and solve for Wl which will give us the maximum load the forklift can carry without tipping.

            Wl = ((Wf + Wp) * L2 - 2R * (L2 + L3)) / L1
                2R * (L2 + L3) = 0 because R is zero
            
            Due to this we get this equation for maximum load:

    Wl_max = ((Wf + Wp) * L2) / L1

            In this equation our Y is Wl. If we were to graph this, one of our variables, either L1 or L2, will become our X and we will graph with respect to those.

            Equations for R and F:
                To solve for R we can take this equation and rearrange it for R: Wl * L1 + 2R * (L2 + L3) - (Wf + Wp) * L2 = 0
                After this we get:

    R = (((Wf + Wp) * L2) - (Wl * L1)) / (2 * (L2 + L3))

                To solve for F we can take this equation and rearrange it for F: 2F + 2R - Wl - Wf - Wp = 0
                After this we get:

    F = ((Wl + Wf + Wp) / 2) - R

                For this equation we will need to solve for R before this one to use the value of R in this one.
           
"""

import matplotlib.pyplot as plt
import numpy as np

# This is the function we are using for deriving outputs which allows the user to quit the program at any time by entering q.
# This function also allows us to make sure the user is inputing a positive number.
# By using a simple function like this we dont have to repeat the same code over and over again for each input we need from the user.
def ask(prompt):
    answer = input(prompt)
    try:
        if answer.lower() == 'q': # Determines if the answer variable is q, if not then it moves on.
            print("Exitting Program.")
            exit() # If answer is q then it quits the entire code.
        answer = float(answer) #Since it was not q, it trys to turn answer into a float variable.
    except ValueError: # If the try fails, then it is probably a string or boolean value, so we tell the user to input again.
        print("Invalid input. Please enter a number.")
        return ask(prompt) # This line makes the user input again.

    if answer <= 0: # All our inputs should be positive so this ensures that every input from the user is positive.
        print("Invalid input. Please enter a positive number that is not zero.")
        return ask(prompt) # This line makes the user input again.
    else:
        return answer # If everything is good it returns the answer variable as a float.

#Functions that do all of the questions

def questionOne():
    print ("You have selected option 1: Find maximum stable load")
    
    #Questions that give the variables for the next equations
    Wf = ask("Please enter the weight of the forklift (Wf) in pounds: ")
    Wp = ask("Please enter the weight of the operator (Wp) in pounds: ")
    Wl = ask("Please enter the weight of the load (Wl) in pounds: ")
    L1 = ask("Please enter the distance from the front wheel to the load (L1) in feet: ")
    L2 = ask("Please enter the distance from the front wheel to the center of mass of the forklift and operator (L2) in feet: ")
    L3 = ask("Please enter the distance from the rear wheel to the center of mass of the forklift and operator (L3) in feet: ")

    #Equations for maximum stable load, reaction force on the rear wheels, and reaction force on the front wheels.
    Wl_max = ((Wf + Wp) * L2) / L1 #Equation for maximum stable Load
    R = (((Wf + Wp) * L2) - (Wl * L1)) / (2 * (L2 + L3)) #Equation for reaction force on the rear wheels
    F = ((Wl + Wf + Wp) / 2) - R #Equation for reaction force on the front wheels

    #Prints the results of the calculations
    print(f"The reaction force on the rear wheels (R) is: {R:.4f} pounds")
    print(f"The reaction force on the front wheels (F) is: {F:.4f} pounds")
    print(f"The maximum stable load (Wl_max) is: {Wl_max:.4f} pounds")

def questionTwo():
    print ("You have selected option 2: Graph maximum stable load as a function of L1")

    #Questions that give the variables for the next equations
    Wf = ask("Please enter the weight of the forklift (Wf) in pounds: ")
    Wp = ask("Please enter the weight of the operator (Wp) in pounds: ")
    L2 = ask("Please enter the distance from the front wheel to the center of mass of the forklift and operator (L2): ")
    L1_max = ask("Please enter the maximum distance from the front wheel to the load (L1): ")
    pointNumber = ask("Please enter the number of points you want to graph: ")

    L1_x = np.linspace(0.1, L1_max, int(pointNumber))  # Avoid division by zero by starting from 0.1
    Wl_y = ((Wf + Wp) * L2) / L1_x #Give the equation for maximum stable load as a function of L1

    plt.plot(L1_x, Wl_y) #Plots the graph
    plt.ylim(top=140000) #Sets the y-axis maximum to 140000
    plt.xlim(left=0) #Sets the x-axis limit to start at 0
    plt.ylim(bottom=0) #Sets the y-axis limit to start at 0
    plt.yticks(np.arange(0, 140001, 20000)) #Includes 140000 as the top y-axis tick
    plt.ticklabel_format(axis='y', style='plain') #Displays y-axis values without scientific notation
    plt.title("Maximum Stable Load as a Function of L1") #Sets the title of the graph
    plt.xlabel("Distance from Front Wheel to Load (L1) [ft]") #Sets the x-axis label of the graph
    plt.ylabel("Maximum Stable Load (Wl_max) [lbs]") #Sets the y-axis label of the graph
    plt.show()

def questionThree():
    print ("You have selected option 3: Graph maximum stable load as a function of L2")

    #Questions that give the variables for the next equations
    Wf = ask("Please enter the weight of the forklift (Wf) in pounds: ")
    Wp = ask("Please enter the weight of the operator (Wp) in pounds: ")
    L1 = ask("Please enter the distance from the front wheel to the load (L1): ")
    L2_max = ask("Please enter the maximum distance from the front wheel to the center of mass of the forklift and operator (L2): ")
    pointNumber = ask("Please enter the number of points you want to graph: ")

    L2_x = np.linspace(0, L2_max, int(pointNumber))
    Wl_y = ((Wf + Wp) * L2_x) / L1 #gives the equation for maximum stable load as a function of L2

    plt.plot(L2_x, Wl_y) #Plots the graph
    plt.xlim(left=0) #Sets the x-axis limit to start at 0
    plt.ylim(bottom=0) #Sets the y-axis limit to start at 0
    plt.title("Maximum Stable Load as a Function of L2") #Sets the title of the graph
    plt.xlabel("Distance from Front Wheel to Center of Mass (L2) [ft]") #Sets the x-axis label of the graph
    plt.ylabel("Maximum Stable Load (Wl_max) [lbs]") #Sets the y-axis label of the graph
    plt.show()

def questionFour():
    print ("You have selected option 4: Graph maximum stable load as a function of Wf")

    #Questions that give the variables for the next equations
    Wf_max = ask("Please enter the weight of the forklift (Wf) in pounds: ")
    Wp = ask("Please enter the weight of the operator (Wp) in pounds: ")
    L1 = ask("Please enter the maximum distance from the front wheel to the load (L1): ")
    L2 = ask("Please enter the distance from the front wheel to the center of mass of the forklift and operator (L2): ")
    pointNumber = ask("Please enter the number of points you want to graph: ")

    Wf_x = np.linspace(0, Wf_max, int(pointNumber))
    Wl_y = ((Wf_x + Wp) * L2) / L1 #gives the equation for maximum stable load as a function of Wf

    plt.plot(Wf_x, Wl_y) #Plots the graph
    plt.xlim(left=0) #Sets the x-axis limit to start at 0
    plt.ylim(bottom=0) #Sets the y-axis limit to start at 0
    plt.title("Maximum Stable Load as a Function of Wf") #Sets the title of the graph
    plt.xlabel("Weight of Forklift (Wf) [lbs]") #Sets the x-axis label of the graph
    plt.ylabel("Maximum Stable Load (Wl_max) [lbs]") #Sets the y-axis label of the graph
    plt.show()


while True:

    print("Please select an option:")

    # Beginning questions for the user
    # Asks the user to select what they want to do
    # Tells the user that they can quit the code anytime by entering 'q'

    print("Stability of a Forklift")
    print("Quit any time by entering 'q'")
    print("-----------------------")
    print("1. Find maximum stable load")
    print("2. Graph maximum stable load as a function of L1")
    print("3. Graph maximum stable load as a function of L2")
    print("4. Graph maximum stable load as a function of the forklift weight")
    print("5. Quit")


    # This below part ensures the user inputs a whole number between 1 and 5.
    # We only need to do this here because this is the only part that requires an a whole number and a number between 1 and 5.
    # Every other part only requires a positive float number which is handled by the ask function.

    while True:

        playerSelectionInput = ask("Please select an option (1-5): ") # This line asks the user to input a whole number between 1-5
        if not playerSelectionInput.is_integer(): # This line is to ensure the user didnt put in a decimal number. If they did, it will tell them to input again.
            print("Invalid selection. Please select a whole number between 1 and 5.")
        else: # This runs if the user inputted a whole number.
            if playerSelectionInput < 1 or playerSelectionInput > 5: # If the input is not between 1 and 5, it will ask for another input.
                print("Invalid selection. Please select a integer number between 1 and 5.")
            else: # If everything is good it should skip the try and if statements and break out of the code.
                break

    if playerSelectionInput == 1: #Does question 1, which is to find the maximum stable load.
        questionOne()

    if playerSelectionInput == 2: #Does question 2, which is to graph maximum stable load as a function of L1.
        questionTwo()

    if playerSelectionInput == 3: #Does question 3, which is to graph maximum stable load as a function of L2.
        questionThree()
        
    if playerSelectionInput == 4: #Does question 4, which is to graph maximum stable load as a function of Wf.
        questionFour()
        

    if playerSelectionInput == 5: #Does question 5, which is to quit the program.
        print ("You have selected option 5: Quit")
        print("Exitting Program.")
        exit() #exits the program
