import random
import sys
import sqlite3
from datetime import date

def HighScore():
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
               
        print("Successfully Connected to SQLite")

        sqlite_query = '''SELECT  * FROM RPS_HighScores ORDER BY Score desc, Date desc'''
       
        cursor.execute(sqlite_query)
        records = cursor.fetchmany(5)

        print("The top 5 highscores are...")

        for row in records:
            print("Name: ", row[0])
            print("Score: ", row[1])     
            print("Date: ", row[2])
            print("\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Error", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("sqlite connection is closed")


sqliteConnection = sqlite3.connect('SQLite_Python.db')
newscore_cursor = sqliteConnection.cursor()
insert_cursor = sqliteConnection.cursor()
print("Successfully Connected to SQLite")

rps = ["Rock", "Paper", "Scissors"]
option = ["Play", "Highscores"]
yesno = ["Yes", "No"]

play = False
high = False
name_entered = False
score = 0

while play == False and high == False:
    choice = input("Would you like to play or view highscores?: (Play / Highscores) ")
    choice = choice.capitalize()
    while choice not in option:
        print("Sorry, that's not an option!")
        choice = input("Would you like to play or view highscores?: (Play / Highscores) ").capitalize()
            
    if choice != "Highscores":
        play = True
        break
    else:
        high = True
        break

while name_entered == False and play == True:
    name = input("Please enter your name: ")
    name = str(name.capitalize())
    name_entered = True
    
while play == True and name_entered == True:

    now = date.today()
       
    user = input("Please choose Rock, Paper or Scissors: ")
    user = user.capitalize()
    
    while user.capitalize() not in rps:
        print("Sorry " + name + ", that's not one of the three options. Please try again")
        user = input("Please choose Rock, Paper or Scissors: ").capitalize()
        
    comp = random.choice(rps)
    print("I choose " + comp) #fix
    
    while user != comp and play == True:
        if user == "Rock" and comp == "Scissors":
            print("You win!")
            score += 1
            again = input("Play again? Yes / No ")
            
            while again.capitalize() not in yesno:
                again = input("Play again? Yes / No ").capitalize()
                
            if again.capitalize() == "No":
                play = False
            else:
                break

        elif user == "Paper" and comp == "Rock":
            print("You win!")
            score += 1
            again = input("Play again? Yes / No ")
            
            while again.capitalize() not in yesno:
                again = input("Play again? Yes / No ").capitalize()
                
            if again.capitalize() == "No":
                play = False
            else:
                break
                
        elif user == "Scissors" and comp == "Paper":
            print("You win!")
            score += 1
            again = input("Play again? Yes / No ")
            
            while again.capitalize() not in yesno:
                again = input("Play again? Yes / No ").capitalize()
                
            if again.capitalize() == "No":
                play = False
            else:
                break

        elif user == "Rock" and comp == "Paper":
            print("You lose!")
            again = input("Play again? Yes / No ")
            
            while again.capitalize() not in yesno:
                again = input("Play again? Yes / No ").capitalize()
                
            if again.capitalize() == "No":
                play = False
            else:
                break

        elif user == "Paper" and comp == "Scissors":
            print("You lose!")
            again = input("Play again? Yes / No ")
            
            while again.capitalize() not in yesno:
                again = input("Play again? Yes / No ").capitalize()
                
            if again.capitalize() == "No":
                play = False
            else:
                break

        elif user == "Scissors" and comp == "Rock":
            print("You lose!")
            again = input("Play again? Yes / No ")
            
            while again.capitalize() not in yesno:
                again = input("Play again? Yes / No ").capitalize()
                
            if again.capitalize() == "No":
                play = False
            else:
                break    

    if play == True and user == comp:   
        print("It's a tie! Let's try again!")
        continue

    if play == False:
        print("Thanks for playing! Your score is: " + str(score))

        sqlite_newscore = '''SELECT Score FROM RPS_HighScores ORDER BY Score desc'''
        
        newscore_cursor.execute(sqlite_newscore)        
        topscore_tup = newscore_cursor.fetchmany(1)

        topscore =  [int(record[0]) for record in newscore_cursor.fetchmany(1)]

        if score > topscore[0]:
            print("Congrats, that's a new highscore!")
            newscore_cursor.close()
        
        sqlite_insert_score = '''INSERT INTO RPS_HighScores
                                        (Player, Score, Date)
                                        VALUES (?, ?, ?);'''
                
        data_tuple = (name, score, now)

        insert_cursor.execute(sqlite_insert_score, data_tuple)
        sqliteConnection.commit()

        print("Your score has been added to the leaderboard!")

        insert_cursor.close()
                                        
        if (sqliteConnection):
            sqliteConnection.close()
            print("sqlite connection is closed")
            continue
                
        sys.exit()

while play == False and high == True:
    HighScore()
    sys.exit()
    
      
  
