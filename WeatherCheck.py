# change the give logic table into a python script that decides activity of a weather 
# and print the appropriate message for the activity depending on the 
# value of the Rule 1 and 2 give 
# Temperature rule 1 | Humiditiy rule2 | activity
# warm | dry | playing basketball
# warm | humid | playing tennis 
# cold | dry | playing cricket
# cold | humid | swim 


def decide_activity(temperature, humidity):
    if temperature == "warm" and humidity == "dry":
        print("Playing basketball")
    elif temperature == "warm" and humidity == "humid":
        print("Playing tennis")
    elif temperature == "cold" and humidity == "dry":
        print("Playing cricket")
    elif temperature == "cold" and humidity == "humid":
        print("Swim")
    else:
        print("Invalid input")

while True:
    temp = input("Enter temperature (warm/cold): ").strip().lower()
    humid = input("Enter humidity (dry/humid): ").strip().lower()
    decide_activity(temp, humid)
    
    cont = input("Do you want to continue? (yes/no): ").strip().lower()
    if cont != "yes":
        print("Exiting the program. Goodbye!")
        break
