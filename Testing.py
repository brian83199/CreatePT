import webbrowser
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
        print("stress                         1 ")
        print("anxiety                        2 ")
        print("feeling_sick                   3 ")
        print("naturally_cold_hands           4 ")
        print("cold_day_outside               5 ")
        print("workout                        6 ")
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
	elif option == 2:
		anxiety()
        elif option == 3:
		feeling_sick()
        elif option == 4:
		naturally_cold_hands()
        elif option == 5:
		cold_day_outside()
        elif option == 6:
		workout()
        else:
            done = True
	    break
def stress():
    print("Is the stress caused by work, school, or family? ")
    print("[Work / School / Family]: ")
    ans = eval(input())
    if ans.lower() == 'work':
        done = True
    elif print("Stress Relief in the Workplace: "):
        print(webbrowser.open('https://www.helpguide.org/articles/stress/stress-in-the-workplace.htm'))
    elif print("Stress Relief at School: "):
        print(webbrowser.open('https://www.verywellmind.com/reduce-student-stress-and-excel-in-school-3145175'))
    elif print("Stress Relief with the Family: "):
        print(webbrowser.open('https://psychcentral.com/lib/tips-to-reduce-family-stress/'))
    else:
        done = False

def anxiety():
    print("Is the temperature caused anxiety? ")
    print("[Yes / No]: ")
    ans = eval(input())
    if ans.lower() == 'yes':
        print("Here's how to lower your temperature from anxiety ")
        print(webbrowser.open('https://www.calmclinic.com/anxiety/symptoms/hotness'))
    else:
        done = False

def feeling_sick():
    print("Are you feeling sick? ")
    print("[Yes / No]: ")
    ans = eval(input())
    if ans.lower() == 'yes':
        print("You might want to see a doctor or get some rest")
    else:
        done = True

def naturally_cold_hands():
    print("Do you have naturally cold hands? ")
    print("[Yes / No]: ")
    ans = eval(input())
    if ans.lower() == 'yes':
        print("Here's how to raise the temperature of your handas: ")
        print(webbrowser.open('http://www.naturalfertilityandwellness.com/raise-basal-body-temperature/'))
    else:
        done = True

def cold_day_outside():
    print("If you were just outside, was it cold out? ")
    print("[Yes / No]: ")
    ans = eval(input())
    if ans.lower == 'no':
        done = True
    else:
        print("Here's how to raise yuor temperature on a cold day: ")
        print(webbrowser.open("https://www.wikihow.com/Increase-Body-Temperature"))

def workout():
    print("Did you just workout? ")
    print("[Yes / No]: ")
    ans = eval(input())
    if ans.lower() == 'no':
        done = True
    else:
        print("Here's how to lower your temperature after working out: ")
        print(webbrowser.open("https://healthyliving.azcentral.com/lower-body-temperature-quickly-after-exercise-17366.html"))





if __name__ == '__main__': main()

           
