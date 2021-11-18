def print_hello_please(myName):
    print("Hello", myName)

print_hello_please("Jaqueline")

def calc_my_age_in_two_years(myCurrentAge):
    print(f"You are {myCurrentAge} years old")
    my_age_in_two_years = myCurrentAge + 2
    return my_age_in_two_years

my_age_in_two_years = calc_my_age_in_two_years(33)

print(f"In two years, i'll be {my_age_in_two_years} years old")
