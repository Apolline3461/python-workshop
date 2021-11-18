def dice_roll_res(dice_value1, dice_value2):
    if dice_value1 == dice_value2:
        return("Same value play again")
    if dice_value1 == 1 or dice_value2 == 1:
        return("too bad you lose")
    elif dice_value1 % 2 == 0 and dice_value2 % 2 != 0:
        return("you win")
    else:
        return("nothing happen...")

# print(dice_roll_res(7, 3))

def ask_me_about_string(string):
    if len(string) < 5:
        print("error, need longer string")
    if string[0] == string[-1]:
        print("they are the same O_O")
    if string[0] == 'a' or string[0] == 'A':
        print("that's an A")
    else:
        print("what a boring string...")

ask_me_about_string("alpapapa")