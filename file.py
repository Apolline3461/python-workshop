
is_oven_on = False

def prepMyFruit(quantity, fruit, pie_crust):
    print(f"You put {quantity} {fruit} on the crust")
    pie_crust = f"filled with delicious {fruit}"
    return pie_crust

def turn_on_oven(is_oven_on):
    is_oven_on = "True"
    return is_oven_on

pie_crust = prepMyFruit(3, "apples", "empty")
is_oven_on = turn_on_oven(is_oven_on)
print("my pie is", pie_crust)
print("Is the oven turned on ?", is_oven_on)

# print(f"You have {quantity} {fruit} and the pie crust is {pie_crust}, is the oven on ? {isOvenOn}")
