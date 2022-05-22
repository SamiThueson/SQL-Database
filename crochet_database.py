import sqlite3

# Connect to the database
connection = sqlite3.connect('stiches.db')
cursor = connection.cursor()

# Create table (if it does not already exist)
cursor.execute("CREATE TABLE IF NOT EXISTS stiches (name TEXT, photo TEXT)")

# Display the whole database
def display():
    cursor.execute("SELECT * FROM stiches")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Display one stich from the database
def display_by_name():
    name = input("Name: ")
    print()
    if name == None:
        return
    values = (name, )
    cursor.execute("SELECT * FROM stiches WHERE name = ?", values)
    row = cursor.fetchone()
    print(row)

# Insert a new stich and photo into the database
def insert():
    name = input("Name: ")
    photo = input("Photo: ")
    values = (name, photo)
    cursor.execute("INSERT INTO stiches VALUES (?,?)", values)
    connection.commit()

# Change the photo of a stich by specifiying the name 
def modify_photo():
    name = input("Name: ")
    photo = input("New Photo: ")
    values = (photo, name) # Make sure order is correct
    cursor.execute("UPDATE stiches SET photo = ? WHERE name = ?", values)
    connection.commit()
    if cursor.rowcount == 0:
        print("Invalid name!")

# Change the name of a stich by specifiying a photo
def modify_name():
    photo = (input("Photo: "))
    name = input("New Name: ")
    values = (name, photo) # Make sure order is correct
    cursor.execute("UPDATE stiches SET name = ? WHERE photo = ?", values)
    connection.commit()
    if cursor.rowcount == 0:
        print("Invalid name!")

# Gets all of the names of the stiches and gives them an id
def get_name():
    cursor.execute("SELECT name FROM stiches")
    results = cursor.fetchall()
    if len(results) == 0:
        print("No names in database")
        return None
    for i in range(len(results)):
        print(f"{i+1} - {results[i][0]}")
    choice = 0
    while choice < 1 or choice > len(results):
        choice = int(input("Name ID: "))
    return results[choice-1][0]

# Deletes stich by provided name
def delete_by_name():
    name = get_name()
    if name == None:
        return
    values = (name, )
    cursor.execute("DELETE FROM stiches WHERE name = ?", values)
    connection.commit()

# Delete the whole database
def delete_all():
    cursor.execute("DELETE FROM stiches")
    connection.commit()

# The actions that a user can do
def user_mode():
    choice = None
    while choice != "4":
        print("You are in User mode!")
        print("1) Display All Crochet Stiches")
        print("2) Display 1 Stich")
        print("3) Add a Stich To The Database")
        print("4) Back to Main Menu")
        choice = input("> ")
        print()
        if choice == "1":
            display()
        elif choice == "2":
            display_by_name()
        elif choice == "3":
            insert()
        print()

# The actions that an administrator can do
def admin_mode():
    choice = None
    while choice != "8":
        print("You are in Administrator mode!")
        print("1) Display the Whole Database")
        print("2) Display 1 Stich")
        print("3) Insert a Stich")
        print("4) Modify a Photo")
        print("5) Modify a Stich Name")
        print("6) Delete Stich By Name")
        print("7) Delete the Whole Database")
        print("8) Back to Main Menu")
        choice = input("> ")
        print()
        if choice == "1":
            display()
        elif choice == "2":
            display_by_name()
        elif choice == "3":
            insert()
        elif choice == "4":
            modify_photo()
        elif choice == "5":
            modify_name()
        elif choice == "6":
            delete_by_name()
        elif choice == "7":
            delete_all()
        print()

def main():
    choice = None
    while choice != "3":
        print("1) User Privileges")
        print("2) Administrator Privileges")
        print("3) Quit")
        choice = input("> ")
        print()
        if choice == "1":
            user_mode()
        elif choice == "2":
            admin_mode()
        print()

main()

# Close the database connection before exiting
connection.close()