
def menu():
    print("Hello")
    print("Your temperature:      1")
    print("Exit:                  0")
    print("Enter option:", end = " ")
    select = eval(input())
    return select

##################################################################


def main():
    done = False
    while not done:
        option = menu()
        if ((option < 0) or (option > 2)):
            print("    Invalid selection")
        elif option == 1:
            temp()
        elif option == 0:
            done = True
###################################################################

temp():
    print("Enter your temperature: ")
    temp = float(input())
    if ((temp < 97) or (temp > 98.9)):
        print("Are you feeling well today?")

    else:
        done = True
    print('[Yes or No]: ')
    ans = (input())

    if ans.lower() == 'yes':
        done = False
    else:
        print("Are any of these the reason? ")
        done = True



    print("Stress                         1 ")
    print("Hot inside                     2 ")
    print("Feeling sick                   3 ")
    print("Naturally have cold hands      4 ")
    print("Other                          5 ")
    print("Just came from a workout       6 ")
    print("Just came in from a cold day   7 ")
    print("Exit                           0 ")
    print("Enter option:", end = " ")
    select = eval(input())
    return select



###################################################################
# questions I want to ask, not code yet

# if the answer to the first question is no, say "Did you just work out or come from outside on a cold day"
# if yes, then exit code. If no, create a list of options for them to choose from
# if temperature is 102 or above, then ask if 911 is needed to be called

# List of possible reasons for your temperature to be high
#

if __name__ == '__main__': main()

