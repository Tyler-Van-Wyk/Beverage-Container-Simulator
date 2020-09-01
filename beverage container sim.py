import re

def print_flasks():
    for flask in flasks.values():
        #print('{0} has {1}/{2} ounces of {3}' .format(flask.name, flask.current_volume, flask.max_volume, flask.content))
        
        print("  {0}\n    ╔═╗\n  ╔═╝ ╚═╗\n  ║▒▒▒▒▒║\n  ║▒{1}/{2}▒║\n  ║▒▒▒▒▒║\n  ╚═════╝".format(flask.name, flask.current_volume, flask.max_volume))

class flask:
    def __init__(self, name, current_volume, max_volume, content, units):
        self.name = name
        self.current_volume = current_volume
        self.max_volume = max_volume
        self.content = content
        self.units = units
    def drink(self):
        self.current_volume -= 1
        print(self.name + ' now has ' + str(self.current_volume) + '/' + str(self.max_volume) + ' ounces of ' + self.content)
    def fill(self):
        self.current_volume = self.max_volume
        print(self.name + ' now has ' + str(self.current_volume) + '/' + str(self.max_volume) + ' ounces of ' + self.content)

# flask1 = flask("Flask 1", 8, 8, 'Wine', 'Ounces')
# flask2 = flask('Flask 2', 8, 8, 'Wine', 'Ounces')

# flasks = {flask1.name:flask1, flask2.name:flask2}
# flask_names = [flask1.name.lower(), flask2.name.lower()]
flasks = {}
flask_names = []
initial_start = 0
while True:
    if initial_start == 0:
        print("This program let's you track virtual beverage containers.\nType 'help' to see the list of commands.")
        initial_start = 1
    else:
        pass
    # if len(flasks) == 0:
    #     print('You have no containers created right now, type "create" to make one.')
    text = input()
    if 'help' == text.lower():
        print("create - create a new container\ndrink <container name> - drink from the container, decrement it by 1 unit\nfill <container name> - fill the container to it's maximum capacity\nfill all - fill all containers to their maximum capacity\nflasks - see a visual representation of your containers and their status")
        continue    
    if 'drink' in text.lower():
        flask = text[6:].lower() 
        if flask in flask_names:
            flasks[flask].drink()
            continue
        else:
            print("You don't seem to have a container with that name...")
            continue
    elif text.lower() == 'fill all':
        for flask in flask_names:
            flasks[flask].fill()
            continue
    elif 'fill' in text.lower():
        flask = text[5:].lower()
        if flask in flask_names:
            flasks[flask].fill()
            continue
        else:
            print("You don't seem to have a container with that name...")
            continue
    elif 'containers' in text.lower():
        if len(flasks) > 0:
            print_flasks()
            continue
        else:
            print("There are no containers to view. Type 'create' to make some!")
            continue
    elif ('create'.lower()) in text:
        while True:
            name = input('What is the name of the new container?\n')
            units = input('What unit of measurement would you like to use? (Ounces, Gallons, etc)\n')
            content = input('What kind of liquid does it contain?\n')
            while True:
                try:
                    max_volume = int(input('In a whole number, how many {0} of {1} can this hold?\n'.format(units, content)))
                except ValueError:
                    print("That didn't seem to work, please enter a whole number")
                    continue
                else:
                    break
            while True:
                try:
                    current_volume = int(input('In a whole number, how much {0} of {1} is in it right now?\n'.format(units, content)))
                except ValueError:
                    print("That didn't seem to work, please enter a whole number")
                    continue
                else:
                    break
            flasks[name.lower()] = flask(name, current_volume, max_volume, content, units)
            flask_names.append(name.lower())
            print('{0} has been created.'.format(name))
            break
    else:
        print("Invalid command. Type 'help' for list of valid commands.")
        continue