
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
            break
###################################################################

def temp():
    print("Enter your temperature: ")
    temp = float(input())
    if ((temp < 97) or (temp > 98.9)):
        print("Are you feeling well today?")

    else:
        done = True
    print('[Yes or No]: ')
    ans = (input())

    if ans.lower() == 'yes':
        done = True
    else:
        print("Please press the reason if available ")
        done = False

    if done == False:
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


def questions():
    done = False
    while not done:
        option = temp()
        if ((option < 0) or (option > 7)): print("Invalid Option")
        elif option == 1:
            Stress()
        else:
            done = True


import webbrowser
def Stress():
    print("Is the stress caused by work or school? ")
    print("[Work / School / Family]: ")
    ans = (input())

    if ans.lower() == 'work':
        done = True
    elif print("Stress Relief in the Workplace: "):
        webbrowser.open('https://www.helpguide.org/articles/stress/stress-in-the-workplace.htm')
    else:
        done = True




if __name__ == '__main__': main()

           
