from sys import exit

def gold_room():
    print "This room is full of gold. How much do you take?"

    choice = raw_input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        print("Man, learn to type a number.")
    
    if how_much < 50:
        print "Nice, you are not greedy, you win!"
        exit(0)
    else:
        print("You greedy bastard!")


def bear_room():
    print "There is a bear here."
    print "the bear has a bunch of money."
    print "the fat bear is in front of another door."
    print "how are you going to move the bear?"
   
    bear_moved = False
    

    while True:
       choice = raw_input("> ")

       if choice == "take honey":
           dead("the bear looks at you then slaps your face off.")
       elif choice == "taunt bear" and not bear_moved:
          print "the bear has moved from the door. you can go through it now."
          bear_moved == True
       elif choice == "taunt bear" and bear_moved:
            dead("The bear get pissed off and chews your legs off.")
       elif choice == "open door":
            gold_room()

       else:
          print "i got no idea what that means."


def cthulhu_room():
    print "Here you see the great evil cthulhu."
    print "he, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    choice = raw_input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print why, "good job!"
    exit(0)

def start():
    print "you are in dark room."
    print "there is a door to your right and left."
    print "which one do you take?"

    choice = raw_input("> ")

    if choice == "left":
       bear_room()
    elif choice == "right":
       cthulhu_room()
    else:
        dead("you stumble around the room untill you starve.")

start()  
