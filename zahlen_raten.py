import random

print("==== Zahlenrate-Spiel ====")

highscore = 0

while True:

    choice = int(input("Bitte wählen Sie Schwierigkeitsgrad 1 oder 2. (zum abbrechen 999 eingeben): "))

    try: 

        if choice == 1:

            number_int = random.randint(0, 20)

            while True:

                try:

                    guess_int = int(input("Bitte geben Sie eine ganze Zahl zwischen 0 und 20 ein (zum abbrechen 999 eingeben): "))

                    if guess_int == 999:
                        break
                    elif guess_int <= 20:
                 
                        if guess_int < number_int:
                            print("Die Zahl ist größer als Ihre Zahl.")
                            highscore -= 5
                        elif guess_int > number_int:
                            print("Die Zahl ist kleiner als Ihre Zahl.")
                            highscore -= 5
                        elif guess_int == number_int:
                            print("Herzlichen Glückwunsch! Sie haben die Zahl korrekt erraten!")
                            highscore += 20
                            print(f"Ihr Highscore beträgt {highscore} Punkte.")
                            break
                    
                except ValueError:
                    print("Falsche Eingabe. Bitte geben Sie eine ganze Zahl ein!")    

        if choice == 2: 

            number_float = round(random.uniform(0.0, 20.0), 1)

            while True:

                try:

                    guess_float = float(input("Bitte geben Sie eine Gleitkommazahl zwischen 0 und 20 ein (zum abbrechen 999 eingeben): "))

                    if guess_float == 999:
                        break
                    elif guess_float <= 20.0: 

                        if guess_float < number_float:
                            print("Die Zahl ist größer als Ihre Zahl.")
                            highscore -= 5
                        elif guess_float > number_float:
                            print("Die Zahl ist kleiner als Ihre Zahl.")
                            highscore -= 5
                        elif guess_float == number_float:
                            print("Herzlichen Glückwunsch! Sie haben die Zahl korrekt erraten!")
                            highscore += 20
                            print(f"Ihr Highscore beträgt {highscore} Punkte.")
                            break

                except ValueError:
                    print("Falsche Eingabe. Bitte geben Sie eine Gleitkommazahl ein!")

        if choice == 999:
            print("=== Spiel beendet ===")
            break

    except(TypeError, ValueError):
        print("Falsche Eingabe!")
        break
    