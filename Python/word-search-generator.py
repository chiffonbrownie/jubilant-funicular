
import string
import random
import re

while True:     #asks for a size of puzzle
        n = input("How big? ")
        if n.isdigit():
            j = 5
            if int(n) < j:      #double checks requirements
                print("Please enter a number greater than "+str(j-1))
            else:
                width = int(n)
                height = int(n)
                print("The puzzle is "+n+" x "+n)
                break
        else:
            print("Please enter a number")

while True:     #asks for the amount of words
    k = input("How many words? ")
    if k.isdigit():
        k = int(k)
        if k < 7:       #double check requirements
            print("Please enter a number greater than 6")
        else: #opens a wordlist and filters using list comprehension
            givenwords = open("wordlist.txt").read().splitlines() #reads and splits by line
            filteredwords = [word for word in givenwords if word.isalpha() if len(word) < int(n)] #filters alpha only words and a lenngth < n
            chosenwords = random.sample(filteredwords, k) #keeps random k amount of words
            chosenwords = [word.upper() for word in chosenwords] #capitalizes leftover words
            print("You will have to find the following words:")
            for word in chosenwords: #prints words to find
                print(word)

            break
    else:
        print("Please enter a number")

def insert_word(word,grid): #word inserting into grid
    word = random.choice([word,word[::-1]]) #chooses whether word is forward/backward

    #chooses random direction for word
    #[1,0] being horizontall
    #[0,1] being vertical
    #[1,1] being -y/x diagonal
    #[1,-1] being y/x diagonal
    d = random.choice([[1,0],[0,1],[1,1],[1,-1]])

    xsize = width if d[0] == 0 else width - len(word) #checks if word is in grid
    ysize = height if d[1] == 0 else height - len(word)


    while True:
        
        x = random.randrange(0,xsize) #sets start point
        y = random.randrange(0,ysize)

        for i in range(0,len(word)):
            if grid[y + d[1]*i][x + d[0]*i] not in [' ',word[i]]: #checks for overlaps
                break
        else:
            break

    #print([x,y])

    for i in range(0,len(word)): # if no overlap, inserts word into grid
        grid[y + d[1]*i][x + d[0]*i] = word[i]

    return grid

#creates empty grid of spaces to fill
grid = [[" " for i in range(0,width)] for j in range(0,height)]

for word in chosenwords:
    grid = insert_word(word, grid)

#creates grid with spaces for solution
solution = "\n".join(map(lambda row: " ".join(row), grid))

#fills individual spaces in grid with random distinct alpha characters
for row in grid:
    for i, letter in enumerate(row):
        if letter == " ":
            row[i] = random.choice(string.ascii_uppercase)

#grid is created as a list of lists
#using lambda, it joins the letters in the row with spaces
#it then joins the rows together with return characters from a map created from the grid
complete = "\n".join(map(lambda row: " ".join(row), grid))
print("""---
Solve this!
---
"""+
        complete)

#creates grid with commas substuting spaces for csv
comma = re.sub("[ ]", ",",complete)

#print(comma)

#creates .csv
outputFile = open("puzzle.csv","w")
outputFile.write(comma)
outputFile.close()

print("""---
Have Fun!
The puzzle is also saved as 'puzzle.csv' in the current file
---""")

while True: #asks if user would like to see solution
    repsonse = input("Would you like to see the solution? [y/press any other chacter to exit] ")
    if repsonse.lower() == "y":
        print("""
solution:
---
                """+solution+"""
---""")
        break
    else:
        print("""
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
        break
