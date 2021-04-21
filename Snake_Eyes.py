def roll_Dice():
    import random

    num_One = 0
    num_Two = 0
    num_Tries = 0

    while True:
        num_Tries += 1
        #Getting random numbers for both rolls
        num_One = random.randint(1, 6)
        num_Two = random.randint(1, 6)

        #Sleep for .3 seconds
        #time.sleep(.3)

        #Formatting it
        #print("(" + str(num_One) + ", " + str(num_Two) + ")")

        #Checking if both are ones
        if(num_One == 1 and num_Two == 1):
            break


    #Final result as snake eyes
    #print("Snake eyes! - (" + str(num_One) + ", " + str(num_Two) + ")")
    #print("It took " + str(num_Tries) + " tries to get snake eyes.")
    return num_Tries

def roll_Dice_Hundred(num_snake_eyes):

    #Init list
    dice_Mean_Value_List = []
    dice_Mean_Value = 0
    iteration = 0
    #Run instance 100 times and record values
    for i in range(num_snake_eyes):
        iteration += 1
        num_Tries_Instance = roll_Dice()
        #Adds every instance of it onto the list
        dice_Mean_Value_List.append(num_Tries_Instance)
        #Isolates each varable out of that list and passes it into a value
        for i in range(len(dice_Mean_Value_List)):
            dice_Mean_Value += dice_Mean_Value_List[i]
            #Calculates the mean/average of dice rolls until snake eyes
        dice_Mean_Value = dice_Mean_Value / len(dice_Mean_Value_List)
        print(str(iteration) + ".) " + str(dice_Mean_Value))
        #Resets to zero so it wont over lap onto the list
        dice_Mean_Value = 0