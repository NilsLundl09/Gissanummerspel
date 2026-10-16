


'''
__author__  = "Nils Lundell"
__version__ = "1.0.0"
__email__   = "Nils.Lundell@elev.ga.dbgy.se"
'''
import os
import subprocess
import random
from bcolors import bcolors
subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
while True:
    gissningar = 0
    number = random.randint(1,100)
    print(bcolors.GREEN +f"Du ska gissa ett nummer mellan 1 och 100. Du får 7 gissningar. \n Skriv 0 för att avsluta spelet")
    print("____________________________________________________________________________")
    while True:
        try:
            
            if gissningar == 7:
                print(bcolors.RED +f"Du förlorade. Det rätta numret var:", number)
                break
            else:
                guess = int(input(bcolors.YELLOW +f"Skriv din gissning:"))
                if guess == 0:
                    exit()
                if guess == number:
                    print(bcolors.GREEN +f"Grattis! Du gissade rätt")
                    print (bcolors.DEFAULT +f"du hade", 7 - gissningar, "gissningar kvar")
                    break
                elif guess < number:
                    print(bcolors.RED + f"Dit nummer var för LÅGT, försök igen.")
                    gissningar += 1
                    print(bcolors.YELLOW +f"Du har", 7 - gissningar, "gissningar kvar")
                else:
                    print(bcolors.RED +f"Ditt nummer var för HÖGT, försök igen.")
                    gissningar += 1
                    print(bcolors.YELLOW +f"Du har", 7 - gissningar, "gissningar kvar")
        except ValueError:
                    print(bcolors.RED +f"Du måste ange ett giltigt heltal.")


    print("Vill du avsluta spelet?")
    avslut = input(bcolors.RED +f"(J)a" + " " + bcolors.DEFAULT + f"eller" + " " + bcolors.GREEN + f"(N)ej:" + bcolors.YELLOW)
    if avslut == "J" or avslut == "j" or avslut == "Ja" or avslut == "ja":
        print("Tack för att du spelade!")
        break
exit()

