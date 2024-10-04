
def play():
    print("You are Alice. You've fallen down a rabbit hole into the strange and magical world of Wonderland!")
    print("Your goal is to find your way home, but first, you must explore this curious place and face its many challenges.")
    print("Wish you Good Luck Alice!")
    print()
    print("Where would you like to go?")
    print()
    print("1. Follow the White Rabbit")
    print("2. Visit the Mad Hatter's Tea Party")
    print("3. Enter the Queen of Hearts' Castle")
    


print("""     _    _ _            _                            
   / \  | (_) ___ ___  (_)_ __                       
  / _ \ | | |/ __/ _ \ | | '_ \                      
 / ___ \| | | (_|  __/ | | | | |                     
/_/   \_\_|_|\___\___| |_|_| |_| _                 _ 
\ \      / /__  _ __   __| | ___| | __ _ _ __   __| |
 \ \ /\ / / _ \| '_ \ / _` |/ _ \ |/ _` | '_ \ / _` |
  \ V  V / (_) | | | | (_| |  __/ | (_| | | | | (_| |
   \_/\_/ \___/|_| |_|\__,_|\___|_|\__,_|_| |_|\__,_|""")

startGame = input('Would You like to play? (Y/N): ')
if startGame == 'N':
    print("Next time")
elif startGame == 'Y':
    play()


firstChoice = input("which path you prefere? (1/2/3): ")
if firstChoice == '1':
    print()
    choice1()
elif firstChoice == '2':
    print()
    choice2()
elif firstChoice == '3':
    print()
    choice3()









