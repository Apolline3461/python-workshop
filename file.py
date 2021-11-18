# print("Success")

# fruit = "apple"
# quantity = 5
# pie_crust = "empty"
# isOvenOn = False

def prepMyFruit(quantity, fruit, pie_crust):
    print(f"You put {quantity} {fruit} on the crust")
    pie_crust = f"filled with delicious {fruit}"
    return pie_crust

pie_crust = prepMyFruit(3, "apple", "empty")
print("my pie is", pie_crust)
# print(f"You have {quantity} {fruit} and the pie crust is {pie_crust}, is the oven on ? {isOvenOn}")
