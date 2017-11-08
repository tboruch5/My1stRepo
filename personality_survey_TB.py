print("What's your name?")
name = input().title()

if name == "Teo":
    print("No way that my name too!")
elif name == "Jack":
    print("I know a lot of people named Jack.")
else:
    print(name + " is a pretty cool name!")



print("What's your favorite sport?")
sport = input().title()


if sport == "Football":
    print("Same, what's your favorite team?")
    footballteam = input().title()

    if footballteam == "Giants":
        print("That's my favorite team!")
    else:
        print("I don't like the " + footballteam + "(s)")
        
elif sport == "Soccer":
    print("Did you know people in the UK call it football?")
elif sport == "Basketball":
    print("Same, I also like basketball!")
else:
    print("Nice, " + sport + " sounds like fun.")


print("What's you favorite TV Show?")
tvshow = input().title()

if tvshow == "Flash" or tvshow == "The Flash" or tvshow == "Arrow":
    print("I love " + tvshow + " too! Who's your favorite character?")
    character = input().title()

    if character == "Cisco" or character == "Barry" or character == "Oliver" or character == "Felicity" or character == "HR" or character == "Wally":
        print("Same! I love " + character + " Too!")
    elif character == "Iris":
        print("I don't really like " + character + " that much.")
    else:
        print(character + " isn't bad but they're not my favorite.")
    
elif tvshow == "Wizards Of Waverly Place" or tvshow == "Barney":
    print("I used to watch " + tvshow + " too!")
else:
    print("I don't know about " + tvshow + " but it sounds good!")


