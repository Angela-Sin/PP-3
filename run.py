# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def intro():
    print("You are Alice. You've fallen a rabbit hole into the strange and magical world of Wonderland")
    print("You must find your way home, but first, you must explore this curious place and face its many challenges.")
    print("GOOD LUCK!")


print(""" ____ _____  _    ____ _____    ____    _    __  __ _____ 
/ ___|_   _|/ \  |  _ \_   _|  / ___|  / \  |  \/  | ____|
\___ \ | | / _ \ | |_) || |   | |  _  / _ \ | |\/| |  _|  
 ___) || |/ ___ \|  _ < | |   | |_| |/ ___ \| |  | | |___ 
|____/ |_/_/   \_\_| \_\|_|    \____/_/   \_\_|  |_|_____|""")

startGame = input('Would You like to play? (Y/N): ')
if startGame == 'N':
    print("Next time")
elif startGame == 'Y':
    intro()