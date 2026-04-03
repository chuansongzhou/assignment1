from greeter import Greeter
import sys

usage = 'Usage: ' + sys.argv[0] + ' <name> <place>\n\nFor names and places longer than one word, put them in quotes\n\n'
if len(sys.argv) != 3:
    print(usage)
    sys.exit()

name = sys.argv[1]
place = sys.argv[2]

bot = Greeter(name,place)
bot.greeting()
