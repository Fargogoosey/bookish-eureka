import time

global secondsLeft
global end
global lastTime
global command
end = int(time.time()) + 3600
lastTime = None

global location
location = "start"

global paths
paths = {}
paths["start"] = ["route1"]
paths["route1"] = ["start", "route2", "onewaytest"]
paths["route2"] = ["route1"]
paths["onewaytest"] = ["route1", "route2"]

global locationName
locationName = {}
locationName["start"] = "Start"
locationName["route1"] = "Route 1"
locationName["route2"] = "Route 2" #was initially "Soute 1/2"
locationName["onewaytest"] = "One-Way test"

def parse(string):
    word = ""
    words = []
    for i in range(len(string)):
        if string[i] == " ":
            words.append(word)
            word = ""
        else:
            word += string[i]
    words.append(word)
    return words

def printTimeLeft(timeLeft=None):
    global lastTime
    if timeLeft == None:
        timeLeft = int(time.time())
    secondsLeft = end - timeLeft
    if lastTime == None:
        lastTime = secondsLeft
    #print(str(secondsLeft) + " S : L " + str(lastTime))
    if lastTime < secondsLeft:
        print('''You have cheated.
Preparing to toss salad...''')
        tossSalad()
    lastTime = secondsLeft
    #print(str(secondsLeft) + " S : L " + str(lastTime))
    if secondsLeft < 1:
        print("well... you lost")
        endGame()
    output = "You have "
    if secondsLeft < 60:
        if secondsLeft == 1:
            output += str(secondsLeft) + " second left."
        else:
            output += str(secondsLeft) + " seconds left."
    else:
        minutesLeft = int(secondsLeft / 60)
        if minutesLeft == 1:
            output += str(minutesLeft) + " minute"
        else:
            output += str(minutesLeft) + " minutes"
        if not secondsLeft%60 == 0:
            if secondsLeft - (minutesLeft * 60) == 1:
                output += " and " + str(secondsLeft - (minutesLeft * 60)) + " second left."
            else:
                output += " and " + str(secondsLeft - (minutesLeft * 60)) + " seconds left."
        else:
            output += " left."
    print(output)
    return

def changeTime(command):
    global end
    global lastTime
    if len(command) == 2:
        try:
            end += int(command[1])
            lastTime += int(command[1])
        except ValueError:
            print("invalid parameters")
    else:
        print("invalid parameters")
    return

def pause(command):
    while not str.lower(command[0]) == "start":
        print("The game is now paused. Time will pass again once you input 'start'.")
        print("Remember that planning your moves without the danger of time is not in spirit of the game,")
        print("but if you really want to I can't stop you.")
        command = parse(input("Pause> "))
    return

def move(command):
    global location
    try:
        if command[1] == "to":
            command.remove("to")
    except IndexError:
        print("invalid parameters")
    if len(command) > 1:
        try:
            if str.lower("".join(command[1:])) in paths[location]:
                print("Moved to " + locationName["".join(command[1:])])
                location = str.lower("".join(command[1:]))
            else:
                print("You can't move there.")
        except ValueError:
            print("invalid parameters")
    return

while True:
    print("Your location is: " + locationName[location])
    printTimeLeft()
    command = parse(input("Menu> "))
    print("")
    if str.lower(command[0]) == "changetime":
        changeTime(command)
    if str.lower(command[0]) == "pause":
        secondsLeft = end - int(time.time())
        pause(command)
        end = int(time.time()) + secondsLeft
    elif str.lower(command[0]) == "move" or str.lower(command[0]) == "go":
        move(command)
    elif str.lower(command[0]) == "paths":
        temp = paths[location]
        result = []
        for i in range(len(temp)):
            result.append(str(locationName[temp[i]]))
        print("List of paths: " + ", ".join(result[0:]))
    else:
        print("Unknown command")
    continue
