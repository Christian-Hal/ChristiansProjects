class Room:
    def __init__(self, name):
        self.name = name
        self.exits = []
        self.exitLocations = []
        self.items = []
        self.itemDescriptions = []
        self.grabbables = []

    # ==================== SETTERS AND GETTERS ====================
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def exitLocations(self):
        return self._exitLocations

    @exitLocations.setter
    def exitLocations(self, value):
        self._exitLocations = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def itemDescriptions(self):
        return self._itemDescriptions

    @itemDescriptions.setter
    def itemDescriptions(self, value):
        self._itemDescriptions = value

    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    # ================= User defined functions =====================

    def addExits(self, exit, room):
        self.exits.append(exit)
        self._exitLocations.append(room)

    def addItem(self, item, desc):
        self._items.append(item)
        self._itemDescriptions.append(desc)

    def addGrabbable(self, item):
        self.grabbables.append(item)

    def delGrabbable(self, item):
        self.grabbables.remove(item)

    def __str__(self):
        # first, the room name
        s = "You are in {}.\n".format(self.name)
        # next, the items in the room
        s += "You see: "
        for item in self.items:
            s += item + " "
        s += "\n"
        # next, the exits from the room
        s += "Exits: "
        for exit in self.exits:
            s += exit + " "
        return s

# ================ CREATE ROOM FUNCTION =====================
def createRooms():
    global currentRoom
    r1 = Room("The Study")     # initial room
    r2 = Room("The Living room")     # initial room
    r3 = Room("The Library")     # initial room
    r4 = Room("The Storage Closet")     # initial room
    r5 = Room("The Bedroom")     # Bedroom (connected to bathroom and dining room)
    r6 = Room("The Bathroom")     # Bathroom (connected to bedroom)
    r7 = Room("The Bathroom")     # Bathroom (connected to room 1)
    r8 = Room("The Kitchen")     # Kitchen (connected to room 3 and dining room)
    r9 = Room("The Dining Room")     # Dining Room (connected to bedroom kitchen and Ballroom)
    r10 = Room("The Gated Backyard")   # Gated Backyard (connected to room 2)
    r11 = Room("The Ballroom")   # Ballroom (connected to room 3 foyer and dining room)
    r12 = Room("The Foyer")   # Foyer (connected to the ballroom)
    # making the rooms
        # EXITS
    r1.exits = ["south", "east", "west"]
    r1.exitLocations = [r3, r2, r7]

    r2.exits = ["south", "west", "north"]
    r2.exitLocations = [r4, r1, r10]

    r3.exits = ["north", "east", "west", "south"]
    r3.exitLocations = [r1, r4, r8, r11]

    r4.exits = ["south", "north", "west"]
    r4.exitLocations = [None, r2, r3]

    r5.exits = ["south", "east"]
    r5.exitLocations = [r6, r9]

    r6.exits = ["north"]
    r6.exitLocations = [r5]

    r7.exits = ["east"]
    r7.exitLocations = [r1]

    r8.exits = ["east", "south"]
    r8.exitLocations = [r3, r9]

    r9.exits = ["north", "east", "west"]
    r9.exitLocations = [r8, r11, r5]

    r10.exits = ["south"]
    r10.exitLocations = [r2]

    r11.exits = ["west", "south", "north"]
    r11.exitLocations = [r9, r12, r3]

    r12.addExits("north", r11)
    # r12.exits = ["north", "south"]
    # r12.exitsLocations = [r11, r2]

        # ======= ITEMS ==========
    r1.items = ["chair", "table"]
    r1.itemDescriptions = ["It is made of wicker and no one is sitting on it.",
                           "It is made of oak. A golden key rests on it"]
    r1.grabbables = ["key"]

    r2.items = ["rug", "fireplace", "window"]
    r2.itemDescriptions = ["It is nice and Indian. It also needs to be vacuumed.", "It is full of ashes."]

    r3.items = ["bookshelves", "statue", "desk"]
    r3.itemDescriptions = ["They are empty. Go figure.", "There is nothing special about it.",
                           "The statue is resting on it. So is a book."]
    r3.grabbables = ["book"]

    r4.items = ["brew rig", "window"]
    r4.itemDescriptions =["Gourd is brewing some sort of oatmeal stout on the brew rig. A 6-pack is resting beside it.",
                          "A window looking south. That jump would hurt!"]
    r4.grabbables = ["6_pack"]

    r5.addItem("nightstand", "It has a drawer with a metal handle."
                             " There is a candle on top which as burned out. Inside is a lighter.")
    r5.addItem("chest", "It is small and locked a gold key might fit into it")
    r5.addGrabbable("lighter")

    r6.addItem("toilet", "There isn't any water in the bowl and it needs cleaning")
    r6.addItem("sink", "When you move the handles no water comes out")

    r7.addItem("toilet", "Its a toilet... freshly cleaned")
    r7.addItem("sink", "When you move the handles water pours out. There is also a bar of soap")
    r7.addGrabbable("soap")

    r8.addItem("pots", "This would make a loud sound... Better not")
    r8.addItem("cabinet", "You open them, inside is a lockpick. Why is that here?")
    r8.addGrabbable("lockpick")

    r9.addItem("table", "It's not set. Clearly nobody is eating yet")

    r10.addItem("Gate", "Its locked")

    r11.addItem("painting", "You look behind it... Nothing, just another copy of starry night")
    r11.addItem("vase", "I wonder what it would cost if someone knocked this over?")
    r11.addGrabbable("reds_wings")

    r12.addItem("armor", "It shines a metallic silver against the forces that would do the innocent harm")
    r12.addItem("door", "A way out! or it would be if it wasn't nailed shut")

    currentRoom = r1

# =========================== DEATH FUNCTION ===========================
# displays an appropriate "message" when the player dies
# yes, this is intentionally obfuscated!
# this code is not my own it is copy-pasted from the directions
def death():
    print(" " * 17 + "u" * 7)

    print(" " * 13 + "u" * 2 + "$" * 11 + "u" * 2)
    print(" " * 10 + "u" * 2 + "$" * 17 + "u" * 2)
    print(" " * 9 + "u" + "$" * 21 + "u")
    print(" " * 8 + "u" + "$" * 23 + "u")
    print(" " * 7 + "u" + "$" * 25 + "u")
    print(" " * 7 + "u" + "$" * 25 + "u")
    print(" " * 7 + "u" + "$" * 6 + "\"" + " " * 3 + "\"" + "$" * 3 +
          "\"" + " " * 3 + "\"" + "$" * 6 + "u")
    print(" " * 7 + "\"" + "$" * 4 + "\"" + " " * 6 + "u$u" + " " * 7
          + "$" * 4 + "\"")
    print(" " * 8 + "$" * 3 + "u" + " " * 7 + "u$u" + " " * 7 + "u" +
          "$" * 3)
    print(" " * 8 + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3)
    print(" " * 9 + "\"" + "$" * 4 + "u" * 2 + "$" * 3 + " " * 3 +
          "$" * 3 + "u" * 2 + "$" * 4 + "\"")
    print(" " * 10 + "\"" + "$" * 7 + "\"" + " " * 3 + "\"" + "$" * 7 + "\"")
    print(" " * 12 + "u" + "$" * 7 + "u" + "$" * 7 + "u")
    print(" " * 13 + "u$\"$\"$\"$\"$\"$\"$u")
    print(" " * 2 + "u" * 3 + " " * 8 + "$" * 2 + "u$ $ $ $ $u" + "$"
          * 2 + " " * 7 + "u" * 3)
    print(" u" + "$" * 4 + " " * 8 + "$" * 5 + "u$u$u" + "$" * 3 + " " * 7 + "u" + "$" * 4)
    print(" " * 2 + "$" * 5 + "u" * 2 + " " * 6 + "\"" + "$" * 9 +
          "\"" + " " * 5 + "u" * 2 + "$" * 6)
    print("u" + "$" * 11 + "u" * 2 + " " * 4 + "\"" * 5 + " " * 4 +
          "u" * 4 + "$" * 10)
    print("$" * 4 + "\"" * 3 + "$" * 10 + "u" * 3 + " " * 3 + "u" * 2
          + "$" * 9 + "\"" * 3 + "$" * 3 + "\"")
    print(" " + "\"" * 3 + " " * 6 + "\"" * 2 + "$" * 11 + "u" * 2 +
          " " + "\"" * 2 + "$" + "\"" * 3)
    print(" " * 11 + "u" * 4 + " \"\"" + "$" * 10 + "u" * 3)
    print(" " * 2 + "u" + "$" * 3 + "u" * 3 + "$" * 9 + "u" * 2 +
          " \"\"" + "$" * 11 + "u" * 3 + "$" * 3)
    print(" " * 2 + "$" * 10 + "\"" * 4 + " " * 11 + "\"\"" + "$" *
          11 + "\"")
    print(" " * 3 + "\"" + "$" * 5 + "\"" + " " * 22 + "\"\"" + "$" *
          4 + "\"\"")
    print(" " * 5 + "$" * 3 + "\"" + " " * 25 + "$" * 4 + "\"")


# ################################ MAIN ###########################################
inventory = []
createRooms()
lose = True

# game start
while(True):
    if currentRoom == None:
        break
    status = f"{currentRoom} \nYou are carrying: {inventory}"
    print("=" * 50)
    print(status)

    response = "I don't understand. Try a verb noun. Valid verbs are go, look, and take"

    action = input("What to do? ")
    action = action.lower()

    if(action in ["quit", "exit", "bye"]):
        lose = False
        break

    words = action.split(" ")

    if(len(words) == 2):
        verb = words[0]
        noun = words[1]

        if(verb == "go"):

            response = "invalid exit."

            for i in range(len(currentRoom.exits)):
                if(noun == currentRoom.exits[i]):
                    currentRoom = currentRoom.exitLocations[i]
                    response = "Room changed"
                    break

        elif (verb == "look"):
            response = "I dont see that item."

            for i in range(len(currentRoom.items)):
                if (noun == currentRoom.items[i]):
                    response = currentRoom.itemDescriptions[i]
                    break

        elif (verb == "take"):

            response = "I dont see that item."

            for grabbable in currentRoom.grabbables:
                if (noun == grabbable):
                    inventory.append(grabbable)
                    currentRoom.delGrabbable(grabbable)
                    response = "Item grabbed"
                    break

# USE KEYWORD ACTIONS
        elif (verb == "use"):
            response = "you cannot use an item you don't have"
            if noun in inventory:
                response = "you cannot use this item in here"
                if (noun == "reds_wings"):
                    for i in range(1000000):
                        print("you shouldn't have these")
                    break
                if (noun == "book"):
                    response = "oh the knowledge this must be hiding. Too bad you aren't in the mood to read right now"
                if (noun == "lockpick"):
                    response = "Picking locks? Do you know how to do that?"
                if (noun == "6_pack"):
                    response = "You drink one of the drinks. It tastes bad and you start to feel sick. You gather " \
                               "from this experience not to drink alcoholic drinks from strangers"
                if (noun == "lighter"):
                    response = "you light the lighter. Nothing happens. It must be out of juice"
                if(noun == "soap" and currentRoom.name == "Room 6"):
                    response = "You washed your hands! Way to be a role model!"
                if (noun == "key" and currentRoom.name == "The Gated Backyard"):
                    response = "You attempt to stick the gold key in the gate. It doesnt turn and the exit is still " \
                               "locked"
                if (noun == "key" and currentRoom.name == "The Bedroom"):
                    response = "You insert the key into the chest and open it. You find... another key?"
                    inventory.append("new_key")
                if (noun == "new_key" and currentRoom.name == "The Gated Backyard"):
                    print("The lock clicks and the gate opens. you walk out in triumph as you exit the house.")
                    lose = False
                    break

    print("=" * 50)
    print(response)
if(lose):
    death()
else:
    pass