# ASk the user if they have played the game before.
show_instuctions =input("have you played this game "
                        "before? ") .lower()

# if they say yes, output 'program continues'
# if they say no, output 'display instructions'
# if the answer is invalid, print an error.

if show_instuctions == "yes":
    print ("program continues")

elif show_instuctions == "y":
    print ("program continues")

elif show_instuctions == "no":
    print("Display instuctions")

elif show_instuctions == "n":
    print("Display instuctions")

# if they say no, output 'display instuctions'
else:
    print("Please answer yes / no")

