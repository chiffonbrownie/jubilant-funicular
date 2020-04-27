#number guessing game

while True: #asks user for name, if not string ask user again for name
        playerName = input("Enter your name>")
        try: #if an int, set input as int and ask user again
            int(playerName)
            playerNameType = "int"
        except ValueError:
            try: #if not int, try float, set input as float and ask user again
                float(playerName)
                playerNameType = "float"
            except ValueError: #if neither, set as string and break loop
                playerNameType = "string"
        if playerNameType != "string":
            print("Please try again")
            continue
        else: #says hello to user w/ name
            print("Hi, "+str(playerName)+"!")
            break

playerReply=""
while playerReply != ("y" or "n"): #asks user y/n and compares input
    playerReply=input("Would you like to guess a number? (y/n)>")
    if playerReply == "y":

        play = True
        while play: #part 1/2 of playAgain loop
            guess = 0 #sets used variables
            guessesTaken = 0
            tries = 0
            difficulty = ""

            bounds = [] #seeting up guess range
            maxLengthBounds = 2
            while len(bounds) < maxLengthBounds:
                lowerBound = input("Enter the start of the guess range>")
                if lowerBound.isnumeric():
                    bounds.append(lowerBound)
                else:
                    print("Please enter a number")
                    continue
                while True:
                    upperBound = input("Enter the end of the guess range>")
                    if upperBound.isnumeric():
                        if upperBound < lowerBound: #double checks valid range
                            print("Please enter a number that is bigger than "+str(int(lowerBound)+1)+".")
                            #continue
                        else:
                            bounds.append(upperBound)
                            break
                    else:
                        print("Please enter a number")

            print("You will have to guess a number from "+str(lowerBound)+" and "+str(upperBound))

            while tries == 0:
                difficulty=input("Okay, "+playerName+", would you like to play on (e)asy, (m)edium, (h)ard or e(x)treme?>")
                if difficulty == "e":
                    tries = 15
                elif difficulty == "m":
                    tries = 10
                elif difficulty == "h":
                    tries = 5
                elif difficulty == "x":
                    tries = 1
                    print("You're crazy")
                else:
                    print("Please enter a difficulty of 'e', 'm', 'h' or 'x'.")
                    continue

            import random
            number=random.randint(int(lowerBound),int(upperBound))

            attempts=tries

            while guessesTaken < attempts:
                print("Take a guess.")
                print("You have "+str(tries)+" tries.")
                guess = input()
                if (guess.isnumeric()):
                    guess = int(guess)
                    guessesTaken = guessesTaken + 1
                    tries = tries - 1
                    if guess != number:
                        if guess < number:
                            print("Your guess is too low")
                        if guess > number:
                            print("Your guess is too high")
                    else:
                        print("You've guessed the number in "+str(guessesTaken)+" attempts")
                        break
                else:
                    print("Please enter a number")

            if guess != number:
                print("The correct number was "+str(number))

            playAgain=True
            while playAgain:
                again=input("Would you like to play again? (y/n)>")
                if again == "n":
                    print(r"""
                        88
                        88
                        88
                        88,dPPYba,  8b       d8  ,adPPYba,
                        88P'    "8a `8b     d8' a8P_____88
                        88       d8  `8b   d8'  8PP"""""""
                        88b,   ,a8"   `8b,d8'   "8b,   ,aa
                        8Y"Ybbd8"'      Y88'     `"Ybbd8"'
                                        d8'
                                    d8'
                        """)
                    print("Goodbye")
                    play = False
                    playAgain=False
                    #break
                elif again != "n":
                    if again =="y":
                        playAgain=False
                        break
                    else:
                        print("Please enter 'y' or 'n'.")
                        continue

    #easter eggs + conditions for 'n' and invalid options
    elif playerReply == "phoenix":
        print(r"""
              _,     ,_
            .'/  ,_   \'.
           |  \__( >__/  |
           \             /
            '-..__ __..-'
                 /_\

        """)
    elif playerReply == "atari":
        print(r"""

                      $$ $$$$$ $$
                      $$ $$$$$ $$
                     .$$ $$$$$ $$.
                     :$$ $$$$$ $$:
                     $$$ $$$$$ $$$
                     $$$ $$$$$ $$$
                    ,$$$ $$$$$ $$$.
                   ,$$$$ $$$$$ $$$$.
                  ,$$$$; $$$$$ :$$$$.
                 ,$$$$$  $$$$$  $$$$$.
               ,$$$$$$'  $$$$$  `$$$$$$.
             ,$$$$$$$'   $$$$$   `$$$$$$$.
          ,s$$$$$$$'     $$$$$     `$$$$$$$s.
        $$$$$$$$$'       $$$$$       `$$$$$$$$$
        $$$$$Y'          $$$$$          `Y$$$$$

        """)
    elif playerReply == "save":
        print(r"""
         ____________________
        |# :              : #|
        |  :              :  |
        |  :              :  |
        |  :              :  |
        |  :______________:  |
        |     ____________   |
        |    | ____       |  |
        |    ||    |      |  |
        \____||____|______|__|

        """)
    elif playerReply == "facepalm":
        print(r"""
                    . . . . . . . . . . . . . . . . . . . ________
            . . . . . .. . . . . . . . . . . ,.-‘”. . . . . . . . . .``~.,
            . . . . . . . .. . . . . .,.-”. . . . . . . . . . . . . . . . . .“-.,
            . . . . .. . . . . . ..,/. . . . . . . . . . . . . . . . . . . . . . . ”:,
            . . . . . . . .. .,?. . . . . . . . . . . . . . . . . . . . . . . . . . .\,
            . . . . . . . . . /. . . . . . . . . . . . . . . . . . . . . . . . . . . . ,}
            . . . . . . . . ./. . . . . . . . . . . . . . . . . . . . . . . . . . ,:`^`.}
            . . . . . . . ./. . . . . . . . . . . . . . . . . . . . . . . . . ,:”. . . ./
            . . . . . . .?. . . __. . . . . . . . . . . . . . . . . . . . :`. . . ./
            . . . . . . . /__.(. . .“~-,_. . . . . . . . . . . . . . ,:`. . . .. ./
            . . . . . . /(_. . ”~,_. . . ..“~,_. . . . . . . . . .,:`. . . . _/
            . . . .. .{.._$;_. . .”=,_. . . .“-,_. . . ,.-~-,}, .~”; /. .. .}
            . . .. . .((. . .*~_. . . .”=-._. . .“;,,./`. . /” . . . ./. .. ../
            . . . .. . .\`~,. . ..“~.,. . . . . . . . . ..`. . .}. . . . . . ../
            . . . . . .(. ..`=-,,. . . .`. . . . . . . . . . . ..(. . . ;_,,-”
            . . . . . ../.`~,. . ..`-.. . . . . . . . . . . . . . ..\. . /\
            . . . . . . \`~.*-,. . . . . . . . . . . . . . . . . ..|,./.....\,__
            ,,_. . . . . }.>-._\. . . . . . . . . . . . . . . . . .|. . . . . . ..`=~-,
            . .. `=~-,_\_. . . `\,. . . . . . . . . . . . . . . . .\
            . . . . . . . . . .`=~-,,.\,. . . . . . . . . . . . . . . .\
            . . . . . . . . . . . . . . . . `:,, . . . . . . . . . . . . . `\. . . . . . ..__
            . . . . . . . . . . . . . . . . . . .`=-,. . . . . . . . . .,%`>--==``
            . . . . . . . . . . . . . . . . . . . . _\. . . . . ._,-%. . . ..`\
                """)
    elif playerReply == "shamrock":
        print(r"""
            ______________MMMMMMMM MMMMM
            _____________MMMMMMMMM MMMMMMM
            ____________MMMMMMMMMM__MMMMMMMM
            ___________MMM____MMMMMMMMMMMMMMMM
            ___________MM______MMMMMMMMMMMMMMM
            ___________MM_____MMMMMMMMMMMMMMMMM
            ____________MM___MMMMMMMMMMMMMMMMM
            _____________MMMMMMMMMMMMMMMMMMMM
            ______________MMMMMMMMMMMMMMMMM
            ____MMMMM______MMMMMMMMMMMMMM_____MMMMMM
            __MMMMMMMMMM_____MMMMMMMMMM____MMMMMMMMMMM
            _MMMM_____MMMMMM___MMMMMM___MMMMMMMMMMMMMMM
            _MMM______MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
            _MMM_MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
            _MMMMMMMMMMMMMMMMMMMMMMMMM_MMMMMMMMMMMMMMMM
            __MMMMMMMMMMMMMMMMMMMM__MM___MMMMMMMMMMMMM
            _____MMMMMMMMMMMMMMM_M__MMM_____MMMMMMM
            _____MMMMMMMMMMMMMM__M___MMM______MMMMM
            _____MMMMMMMMMMMMM___MM___MM_______MMMMM
            ____MMMMMMMMMMMMMM___MM____MM_______MMMM
            _____MMMMMMMMMMMM____MMM____MMM_____MMM
            ______MMMMMMMMMM_____MMMM____MMMMMMMMM
            ________MMMMMM________MMMM_____MMMMM
            _______________________MMMMM
            _________________________MM
                """)
    elif playerReply == "sellout":
        print(r"""
            888888888888888888888888888888888888888888888888
            88888888888888888__________________________88888
            88888888888888888__________________________88888
            8888888888888____8888888___________________88888
            888888888______88____8888888_______________88888
            888888_____888888________88888_____________88888
            8888____88888____888888____88888___________88888
            88____8888____888___88888____8888__________88888
            88____888____8888____888____8888___________88888
            888____888____888_________8888_____88______88888
            8888_____888___88_______8888_____888888____88888
            888888____888____888888888_____88888888____88888
            8888888_____888888888_______88888888_______88888
            8888888888______8______888888888___________88888
            8888888888888____8888888888________________88888
            88888888888888888__________________________88888
            88888888888888888__________________________88888
            888888888888888888888888888888888888888888888888
            888888888888888888888888888888888888888888888888
            888888888888888888888888888888888888888888888888
            888888888888888888888888888888888888888888888888
            8_______88__8888__8__88______888__8888____888888
            8________8___88___8__88__888__88__888__88__88888
            8___888__88__88__88__88__8888__8__88__8888__8888
            8___888___88____888__88__8888__8__88__8888__8888
            8___888___88____888__88__888__88__88________8888
            8___888___888__8888__88______888__88__8888__8888
            888888888888888888888888888888888888888888888888
                """)
    elif playerReply == "n":
        print(r"""
                           ((((((
                         ((::::::(
                       ((:::::::(
                      (:::::::((
                      (::::::(
             ::::::   (:::::(
             ::::::   (:::::(
             ::::::   (:::::(
                      (:::::(
                      (:::::(
                      (:::::(
             ::::::   (::::::(
             ::::::   (:::::::((
             ::::::    ((:::::::(
                         ((::::::(
                           ((((((
                """)
        print("Goodbye")
        break
    else: #ensures correct input
        print("Please enter 'y' or 'n'. ")
        continue
