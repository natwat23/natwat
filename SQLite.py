import sqlite3

def HighScore():
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")

        sqlite_query = '''SELECT  * FROM RPS_HighScores ORDER BY Score desc, Date desc'''
       
        cursor.execute(sqlite_query)
        records = cursor.fetchmany(5)

        #print("The top 5 highscores are...")

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

def delete():
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")

        sqlite_query = '''DELETE FROM RPS_HighScores'''
       
        cursor.execute(sqlite_query)

        sqliteConnection.commit()

        print("Records deleted")

        cursor.close()
        

    except sqlite3.Error as error:
        print("Error", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("sqlite connection is closed")


delete()
HighScore()
