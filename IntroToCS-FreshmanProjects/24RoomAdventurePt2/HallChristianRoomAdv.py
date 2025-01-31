#################################################################
# Name: Christian Hall
# Date: 4/14/2023
# Description: Room adventure game using tkinter and previous room adventure assignment
#################################################################
from tkinter import *

class Room:
    def __init__(self, name, image):
        self.name = name
        self.image = image
        self.exits = {}
        self.items = {}
        self.grabbables = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    def addExit(self, exit, room):
        self._exits[exit] = room

    # adds an item to the room
    # the item is a string (e.g., table)
    # the desc is a string that describes the item (e.g., it is
    # made of wood)
    def addItem(self, item, desc):
        # append the item and description to the appropriate
        # dictionary
        self._items[item] = desc

    # adds a grabbable item to the room
    # the item is a string (e.g., key)
    def addGrabbable(self, item):
        # append the item to the list
        self._grabbables.append(item)

    # removes a grabbable item from the room
    # the item is a string (e.g., key)
    def delGrabbable(self, item):
        # remove the item from the list
        self._grabbables.remove(item)

    # returns a string description of the room
    def __str__(self):
        # first, the room name
        s = "You are in {}.\n".format(self.name)
        # next, the items in the room

        s += "You see: "
        for item in self.items.keys():
            s += item + " "
        s += "\n"

        # next, the exits from the room
        s += "Exits: "
        for exit in self.exits.keys():
            s += exit + " "
        return s


# the game class
# inherits from the Frame class of Tkinter
class Game(Frame):
    # the constructor
    def __init__(self, parent):
        Frame.__init__(self, parent)

    # creates the rooms
    def createRooms(self):
        # r1 through r4 are the four rooms in the mansion
        # currentRoom is the room the player is currently in (which
        # can be one of r1 through r4)
        # create the rooms and give them meaningful names and an
        # image in the current directory
        r1 = Room("Room 1", "room1.gif")
        r2 = Room("Room 2", "room2.gif")
        r3 = Room("Room 3", "room3.gif")
        r4 = Room("Room 4", "room4.gif")
        r5 = Room("Room 5", "room5.gif")  # Bedroom (connected to bathroom and dining room)
        r6 = Room("Room 6", "room6.gif")  # Bathroom (connected to bedroom)
        r7 = Room("Room 7", "room7.gif")  # Bathroom (connected to room 1)
        r8 = Room("Room 8", "room8.gif")  # Kitchen (connected to room 3 and dining room)
        r9 = Room("Room 9", "room9.gif")  # Dining Room (connected to bedroom kitchen and Ballroom)
        r10 = Room("Room 10", "room10.gif")  # Gated Backyard (connected to room 2)
        r11 = Room("Room 11", "room11.gif")  # Ballroom (connected to room 3 foyer and dining room)
        r12 = Room("Room 12", "room12.gif")  # Foyer (connected to the ballroom)

        # add exits to room 1
        r1.addExit("east", r2)  # to the east of room 1 is room 2
        r1.addExit("south", r3)
        r1.addExit("west", r7)

        # add grabbables to room 1
        r1.addGrabbable("key")
        # add items to room 1
        r1.addItem("chair", "It is made of wicker and no one is sitting on it.")
        r1.addItem("table", "It is made of oak. A golden key rests on it.")

        # add exits to room 2
        r2.addExit("west", r1)
        r2.addExit("south", r4)
        r2.addExit("north", r10)
        # add items to room 2
        r2.addItem("rug", "It is nice and Indian. It also needs to be vacuumed.")
        r2.addItem("fireplace", "It is full of ashes.")

        # add exits to room 3
        r3.addExit("north", r1)
        r3.addExit("east", r4)
        r3.addExit("west", r8)
        r3.addExit("south", r11)

        # add grabbables to room 3
        r3.addGrabbable("book")
        # add items to room 3
        r3.addItem("bookshelves", "They are empty. Go figure.")
        r3.addItem("statue", "There is nothing special about it.")
        r3.addItem("desk", "The statue is resting on it. So is a book.")

        # add exits to room 4
        r4.addExit("north", r2)
        r4.addExit("west", r3)
        r4.addExit("south", None)  # DEATH!
        # add grabbables to room 4
        r4.addGrabbable("6-pack")
        # add items to room 4
        r4.addItem("brew_rig", "Gourd is brewing some sort of oatmeal stout on the brew rig. A 6-pack is resting beside it.")

        # add exits to room 5
        r5.addExit("south", r6)
        r5.addExit("east", r9)

        r5.addItem("nightstand", "It has a drawer with a metal handle."
                                 " There is a candle on top which as burned out. Inside is a lighter.")
        r5.addItem("chest", "It is small and locked a gold key might fit into it")
        r5.addGrabbable("lighter")

        # add exits to room 6
        r6.addExit("north", r5)
        r6.addItem("toilet", "There isn't any water in the bowl and it needs cleaning")
        r6.addItem("sink", "When you move the handles no water comes out")

        # add exits to room 7
        r7.addExit("east", r1)

        # add items to room 7
        r7.addItem("toilet", "Its a toilet... freshly cleaned")
        r7.addItem("sink", "When you move the handles water pours out. There is also a bar of soap")
        r7.addGrabbable("soap")

        # add exits to room 8
        r8.addExit("east", r3)
        r8.addExit("south", r9)

        # add items to room 8
        r8.addItem("pots", "This would make a loud sound... Better not")
        r8.addItem("cabinet", "You open them, inside is a lockpick. Why is that here?")
        r8.addGrabbable("lockpick")

        # add exits to room 9
        r9.addExit("north", r8)
        r9.addExit("east", r11)
        r9.addExit("west", r5)

        # add items to room 9
        r9.addItem("table", "It's not set. Clearly nobody is eating yet")

        # add exits to room 10
        r10.addExit("south", r2)

        # add items to room 10
        r10.addItem("Gate", "Its locked")

        # add exits to room 11
        r11.addExit("west", r9)
        r11.addExit("south", r12)
        r11.addExit("north", r3)

        # add items to room 12
        r11.addItem("painting", "You look behind it... Nothing, just another copy of starry night")
        r11.addItem("vase", "I wonder what it would cost if someone knocked this over?")
        r11.addGrabbable("reds_wings")

        # add exits to room 12
        r12.addExit("north", r11)

        # add items to room 12
        r12.addItem("armor", "It shines a metallic silver against the forces that would do the innocent harm")
        r12.addItem("door", "A way out! or it would be if it wasn't nailed shut")
        # set room 1 as the current room at the beginning of the
        # game
        Game.currentRoom = r1
        # initialize the player's inventory
        Game.inventory = []


    # sets up the GUI
    def setupGUI(self):
        # organize the GUI
        self.pack(fill=BOTH, expand=1)

        # setup the player input at the bottom of the GUI
        # the widget is a Tkinter Entry
        # set its background to white and bind the return key to the
        # function process in the class
        # push it to the bottom of the GUI and let it fill
        # horizontally
        # give it focus so the player doesn't have to click on it
        Game.player_input = Entry(self, bg="white")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.pack(side=BOTTOM, fill=X)
        Game.player_input.focus()

        # setup the image to the left of the GUI
        # the widget is a Tkinter Label
        # don't let the image control the widget's size
        img = None
        Game.image = Label(self, width=WIDTH // 2, image=img)
        Game.image.image = img
        Game.image.pack(side=LEFT, fill=Y)
        Game.image.pack_propagate(False)

        # setup the text to the right of the GUI
        # first, the frame in which the text will be placed
        text_frame = Frame(self, width=WIDTH // 2)
        # the widget is a Tkinter Text
        # disable it by default
        # don't let the widget control the frame's size
        Game.text = Text(text_frame, bg="lightgrey", state=DISABLED)
        Game.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=Y)
        text_frame.pack_propagate(False)


    # set the current room image
    def setRoomImage(self):
        if (Game.currentRoom == None):
            # if dead, set the skull image
            Game.img = PhotoImage(file="skull.gif")
        else:
            # otherwise grab the image for the current room
            Game.img = PhotoImage(file=Game.currentRoom.image)

        # display the image on the left of the GUI
        Game.image.config(image=Game.img)
        Game.image.image = Game.img


    # sets the status displayed on the right of the GUI
    def setStatus(self, status):
        # enable the text widget, clear it, set it, and disabled it
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)
        if (Game.currentRoom == None):
            # if dead, let the player know
            Game.text.insert(END, "You are dead. The only thing you can do now is quit.\n")
        else:
            # otherwise, display the appropriate status
            Game.text.insert(END, str(Game.currentRoom) + \
                             "\nYou are carrying: " + str(Game.inventory) + \
                             "\n\n" + status)
            Game.text.config(state=DISABLED)


    # play the game
    def play(self):
        # add the rooms to the game
        self.createRooms()
        # configure the GUI
        self.setupGUI()
        # set the current room
        self.setRoomImage()
        # set the current status
        self.setStatus("")
        # processes the player's input


    def process(self, event):
        # grab the player's input from the input at the bottom of
        # the GUI
        action = Game.player_input.get()
        # set the user's input to lowercase to make it easier to
        # compare the verb and noun to known values
        action = action.lower()
        # set a default response
        response = "I don't understand. Try verb noun. Valid verbs are go, look, take, and use"
        # exit the game if the player wants to leave (supports quit,
        # exit, and bye)
        if (action == "quit" or action == "exit" or action == "bye" \
                or action == "sionara!"):
            exit(0)
        # if the player is dead if goes/went south from room 4
        if (Game.currentRoom == None):
            # clear the player's input
            Game.player_input.delete(0, END)
            return
        # split the user input into words (words are separated by
        # spaces) and store the words in a list
        words = action.split()
        # the game only understands two word inputs
        if (len(words) == 2):
            # isolate the verb and noun
            verb = words[0]
            noun = words[1]
        # the verb is: go
        if (verb == "go"):
            # set a default response
            response = "Invalid exit."
            # check for valid exits in the current room
            if (noun in Game.currentRoom.exits):
                # if one is found, change the current room to
                # the one that is associated with the
                # specified exit
                Game.currentRoom = Game.currentRoom.exits[noun]
                # set the response (success)
                response = "Room changed."
        # the verb is: look
        elif (verb == "look"):
            # set a default response
            response = "I don't see that item."
            # check for valid items in the current room
            if (noun in Game.currentRoom.items):
                # if one is found, set the response to the
                # item's description
                response = Game.currentRoom.items[noun]
        # the verb is: take
        elif (verb == "take"):
            # set a default response
            response = "I don't see that item."
            # check for valid grabbable items in the current room
            for grabbable in Game.currentRoom.grabbables:
                # a valid grabbable item is found
                if (noun == grabbable):
                    # add the grabbable item to the player's inventory
                    self.inventory.append(grabbable)
                    # remove the grabbable item from the room
                    Game.currentRoom.delGrabbable(grabbable)
                    # set the response (success)
                    response = "Item grabbed."
                    # no need to check any more grabbable items
                    break
        # the verb is "use"
        elif(verb == "use"):
            # set as default response
            response = "You cannot use an item you do not have"
            # tests to see if object is in player inventory
            if noun in Game.inventory:
                response = "you cannot use this item in here"
                # unique interactions with different grabbables some require you to be in a specific room
                if (noun == "reds_wings"):
                    response = "YOU SHOULDN\'T HAVE THIS"
                    Game.currentRoom = None
                if (noun == "book"):
                    response = "oh the knowledge this must be hiding. Too bad you aren't in the mood to read right now"
                if (noun == "lockpick"):
                    response = "Picking locks? Do you know how to do that?"
                if (noun == "6_pack"):
                    response = "You drink one of the drinks. It tastes bad and you start to feel sick. You gather " \
                               "from this experience not to drink alcoholic drinks from strangers"
                if (noun == "lighter"):
                    response = "you light the lighter. Nothing happens. It must be out of juice"
                if(noun == "soap" and Game.currentRoom.name == "Room 6"):
                    response = "You washed your hands! Way to be a role model!"
                if (noun == "key" and Game.currentRoom.name == "Room 10"):
                    response = "You attempt to stick the gold key in the gate. It doesnt turn and the exit is still " \
                               "locked"
                if (noun == "key" and Game.currentRoom.name == "Room 5"):
                    response = "You insert the key into the chest and open it. You find... another key?"
                    self.inventory.append("new_key")
                if (noun == "new_key" and Game.currentRoom.name == "Room 10"):
                    response = "The lock clicks and the gate opens. you walk out in triumph as you exit the house... Or not... You can continue to explore if you so choose"

        # display the response on the right of the GUI
        # display the room's image on the left of the GUI
        # clear the player's input
        self.setStatus(response)
        self.setRoomImage()
        Game.player_input.delete(0, END)


##########################################################
# the default size of the GUI is 800x600
inventory = []
lose = True

WIDTH = 800
HEIGHT = 600
# create the window
window = Tk()
window.title("Room Adventure")
# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()
# wait for the window to close
window.mainloop()
