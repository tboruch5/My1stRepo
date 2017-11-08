from MadLib_TB_Chapter1 import *

print("Chapter 2")
print("Are you ready to begin your adventure? Yes/No")
if ready == "Yes":
    print("OK")

    print("My name is " + name1 + " and I have been the protector of " + city1 + " for the past six months.")

    print("Type a noun")
    noun11 = input().lower()
    print("Type a verb in the past tense")
    verb11 = input().lower()
    print("Type a verb in the past tense")
    verb12 = input().lower()
    print("Type a adjective")
    adj11 = input().lower()
    

    print("Last week my friends, " + name2 + ", " + name3 + " and I came accross an evil " + noun11 + ".")
    print("When we enountered the evil " + noun11 + ", we " + verb11 + " it.")
    print("We quickly " + verb12 + " away in a " + adj11 + ".")
    print
    

elif ready == "No":
    print("Your loss.")
else:
    print("That is not a valid answer")

