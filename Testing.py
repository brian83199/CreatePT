import webbrowser


def menu():
    print("Hello")
    print("Your temperature:      1")
    print("Exit:                  0")
    print("Enter option:", end=" ")
    option1 = eval(input())
    return option1

#Parker Witt has helped me with ordering the functions to allow the program to work properly. Also helped by removing a return option4 that didnt need to be there.
def stress():
    # done = true
    print("Is the stress caused by work, school, or family? ")
    print("[1 = work / 2 = school / 3 = family]: ")
    ans = eval(input())
    if (ans < 1) or (ans > 3):
        print("invalid entry. Please try again")
        stress()
    elif ans == 1:
        print("Stress Relief in the Workplace: ")
        print(webbrowser.open('https://www.helpguide.org/articles/stress/stress-in-the-workplace.htm'))
        exit(Main())
    elif ans == 2:
        print("Stress Relief at School: ")
        print(webbrowser.open('https://www.verywellmind.com/reduce-student-stress-and-excel-in-school-3145175'))
        exit (main())
    else:
        print("Stress Relief with the Family: ")
        print(webbrowser.open('https://psychcentral.com/lib/tips-to-reduce-family-stress/'))
        exit(main())


def anxiety():
    print("Is the temperature caused anxiety? ")
    print("[1 = Yes / 2 = No]: ")
    ans = eval(input())
    if (ans < 1) or (ans > 2):
        print("invalid entry. Please try again")
        anxiety()
    elif ans == 1:
        print("Here's how to lower your temperature from anxiety ")
        print(webbrowser.open('https://www.calmclinic.com/anxiety/symptoms/hotness'))
    else:
        exit(main())


def feeling_sick():
    print("Are you feeling sick? ")
    print("[1 = Yes /2 =  No]: ")
    ans = eval(input())
    if (ans < 1) or (ans > 2):
        print("invalid entry. Please try again")
        feeling_sick()
    elif ans == 1:
        print("You might want to see a doctor or get some rest")
    else:
        exit(main())


def naturally_cold_hands():
    print("Do you have naturally cold hands? ")
    print("[1 = Yes / 2 = No]: ")
    ans = eval(input())
    if (ans < 1) or (ans > 2):
        print("invalid entry. Please try again")
        naturally_cold_hands()
    elif ans == 2:
        print("Here's how to raise the temperature of your hands: ")
        print(webbrowser.open('http://www.naturalfertilityandwellness.com/raise-basal-body-temperature/'))
    else:
        exit(main())


def cold_day_outside():
    print("If you were just outside, was it cold out? ")
    print("[1 = Yes / 2 = No]: ")
    ans = eval(input())
    if (ans < 1) or (ans > 2):
        print("invalid entry. Please try again")
        cold_day_outside()
    elif ans == 1:
        print("Here's how to raise your temperature on a cold day: ")
        print(webbrowser.open("https://www.wikihow.com/Increase-Body-Temperature"))
    else:
        exit(main())

def workout():
    done = False
    print("Did you just workout? ")
    print("[1 = Yes / 2 = No]: ")
    ans = eval(input())
    if (ans<1) or (ans>2):
        print("invalid entry. Please try again")
        workout()
    elif ans == 1:
        print("Here's how to lower your temperature after working out: ")
        print(webbrowser.open("https://healthyliving.azcentral.com/lower-body-temperature-quickly-after-exercise-17366.html"))
    else:
        exit(main())




def questions():
    done = False
    print("Please press the reason if known: ")
    print("stress                         1 ")
    print("anxiety                        2 ")
    print("feeling_sick                   3 ")
    print("naturally_cold_hands           4 ")
    print("cold_day_outside               5 ")
    print("workout                        6 ")
    print("Exit                           0 ")
    print("Enter option:", end=" ")
    option4 = eval(input())


    while not done:
        if ((option4 < 0) or (option4 > 7)):
            print("Invalid Option")
        elif option4 == 1:
            stress()
        elif option4 == 2:
            anxiety()
        elif option4 == 3:
            feeling_sick()
        elif option4 == 4:
            naturally_cold_hands()
        elif option4 == 5:
            cold_day_outside()
        elif option4 == 6:
            workout()
        else:
            done = True
            break





##################################################################


def temp():

#From here to print(temperature) was taken from this link, at the bottom of the page where it says "Step 3B: How to read the temperature in Python" http://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/temperature/
 
    tfile = open("/sys/bus/w1/devices/10-000802824e58/w1_slave")
    text = tfile.read()
    tfile.close()
    temperature_data = text.split()[-1]
    temperature = float(temperature_data[2:])
    temperature = temperature / 1000
    temperature = temperature*(9/5)+32
    print(temperature)


    temperature = float(input())
    if ((temperature < 72.5) or (temperature > 80)):
        print("Are you feeling well today?")

    else:
        print("I am glad you are feeling well")
        exit(main())
    print('[Yes or No]: ')
    ans = (input())

    if ans.lower() == 'yes':
        done = True
    else:
        questions()



def main():
    done = False
    while not done:
        option2 = menu()
        if ((option2 < 0) or (option2 > 2)):
            print("    Invalid selection")
        elif option2 == 1:
            temp()
        elif option2 == 0:
            done = True
            break


###################################################################







if __name__ == '__main__': main()
