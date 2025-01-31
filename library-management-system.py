import numpy as np
import pandas as pd
import mysql.connector

def book_collection():
    print("We have a variety of Books")
    a = input()
    print("The Genres available are Action,Adventure,Horror,Auto-Bio & Comedy")
    a= input()
    Genre = input("Please enter the Genre of your Desired Book: ")
    if(Genre == 'Action'):
        print("The List of Books in",Genre,"are: ")
        a = input()
        print("The Hunger Games by Susan Collins")
        print("The Sentinel by Lee Child")
        print("Predator by Wilbur Smith")
        print("Hard Road by J.B Turner")
    
    elif(Genre == 'Adventure'):
        print("The List of Books in",Genre,"are: ")
        a = input()
        print("Robinson Cruesoe by Daniel Defoe")
        print("Gulliver's Travels by Jonathan Swift")
        print("The Maze Runner by James Dashner")
        print("The Alchemist by Paulo Coelho")
    
    elif(Genre == 'Horror'):
        print("The List of Books in",Genre,"are: ")
        a = input()
        print("Frankenstein by Mary Shelly")
        print("The Silence of the Lambs by Thomas Harris")
        print("Hell House by Richard Matheson")
        print("After the End by Amy Plum")
    
    elif(Genre == 'Auto-Bio'):
        print("The List of Books in",Genre,"are: ")
        a = input()
        print("The Story of My Life by Helen Keller")
        print("A Long Walk to Freedom by Nelson Mandela")
        print("Steve Jobs The Man Who Thought Different by Karen Blumenthal")
        print("Gandhi by Louis Fishcher")
    
    elif(Genre == 'Comedy'):
        print("The List of Books in",Genre,"are: ")
        a = input()
        print("Inside Out and Back Again by Thanhhà Lai")
        print("A Confederacy of Dunces by John Kennedy Toole")
        print("Good Omens by Neil Gaiman and Terry Pratchett")
        print("Cruel Shoes by Steve Martin")
                
    else:
        print("Invalid Selection")
        
def choice():
    a = input()
    print("Do you wish to issue a book?")
    a = input()
    choice3 = input("Enter your choice: ")
    if(choice3 == 'yes'):
        book_issue()
        
    elif(choice3 == 'no'):
        print("Ok, Directing you to the home page.")
        
    else:
        print("Invalid Selection")

def book_issue():
    import mysql.connector
    db = mysql.connector.connect(host = "localhost", user = "root", password = "keagan1234", database = "project")
    cursor = db.cursor()
    a = input()
    print("Please select your book")
    a = input()
    book = input("Enter the Name of the selected book: ")
    print("Book Issued")
    a = input()
    print("Now please enter the required details")
    a = input()
    Id = int(input("Enter your student ID:"))
    Name = input("Enter your name: ")
    Grade = int(input("Enter your grade: "))
    Section = input("Enter your section: ")
    book_issued = input("Enter the name of the book issued: ")
    date_issued = input("Enter the Date Issued: ")
    date_return = input("Enter the Date of Return: ")
    
    try:
        sql = "insert into student values(%s,%s,%s,%s,%s,%s,%s)"
        val = (Id,Name,Grade,Section,book_issued,date_issued,date_return)
        cursor.execute(sql,val)
        db.commit()
        print("Record added")
    except:
        db.rollback()
        print("Record not added")
    
        
def position():
    position = input("Enter your position [1.Staff, 2.Student]:  ")
    if(position == 'Student'):
        student()
        a = input()
        book_collection()
        choice()
    else:
        staff()

def staff():
    Username = input("Enter your user name: ")
    password = input("Enter your password: ")
    a = input()
    print("Login Successfull")
    a = input()
    Library_Members()
        
def student():
    Name = input("Enter your Name: ")
    print("Hello there",Name,"and Welcome to our Library")
    a = input()
    
    choice = input("Are you Registered with us?: ")
    if(choice == 'yes'):
        a = input()
        print("Log in")
        User = input("Enter your user name: ")
        Password = input("Enter your password: ")    # In * type
        a = input()
        print("Successfully Logged in")
    
    elif(choice == 'no'):
        a = input()
        print("Create your Free Account and Sign Up !!!")
        User1 = input("Enter your User name: ")
        password = input("Select password: ")
        a = input()
        print("Account Created Successfully")
    
    else:
        a = input()
        print("Invalid Selection, Please try again")

def Staff_Details():
    import mysql.connector
    db = mysql.connector.connect(host = "localhost", user = "root",password = "keagan1234", database = "project")
    cursor = db.cursor()
    print("Register your self as a Staff member")
    a = input()
    Member_Id = input("Enter the Id No.: ")
    Name = input("Enter your name: ")
    Age = int(input("Enter your age: "))
    Address = input("Enter your address: ")
    
    try:
        sql = "insert into staff values(%s,%s,%s,%s)"
        val = (Member_Id,Name,Age,Address)
        cursor.execute(sql,val)
        db.commit()
        print("Record added")
    except:
        db.rollback()
        print("Record not added")
    
def delete_staff_rec():
    import mysql.connector
    try:
        db = mysql.connector.connect(host = "localhost", user = "root", password = "keagan1234", database = "project")
        cursor = db.cursor()
        name = input("Enter name: ")
        sql = "Delete from staff where name = %s"
        cursor.execute(sql,(name,))
        print(cursor.rowcount, "record deleted")
        db.commit()
    except:
        db.rollback()
        print("Record not deleted")

def delete_student_rec():
    import mysql.connector
    try:
        db = mysql.connector.connect(host = "localhost", user = "root", password = "keagan1234", database = "project")
        cursor = db.cursor()
        Id = int(input("Enter Id: "))
        sql = "Delete from student where Id = %s"
        cursor.execute(sql,(Id,))
        print(cursor.rowcount, "record deleted")
        db.commit()
    except:
        db.rollback()
        print("Record not deleted")
        
def update_student_details():
    import mysql.connector
    try:
        db = mysql.connector.connect(host = "localhost", user = "root", password = "keagan1234", database = "project")
        cursor = db.cursor()
        Id = int(input("Enter Id: "))
        Name = input("Enter Name: ")
        sql = "Update student set Id = %s where Name = %s"
        val = (Id,Name)
        cursor.execute(sql,val)
        print(cursor.rowcount, "record updated")
        db.commit()
    except:
        db.rollback()
        print("Record not updated")

def update_staff_details():
    import mysql.connector
    try:
        db = mysql.connector.connect(host = "localhost", user = "root", password = "keagan1234", database = "project")
        cursor = db.cursor()
        Id = int(input("Enter Id: "))
        Name = input("Enter Name: ")
        sql = "Update staff set Name = %s where Id = %s"
        val = (Name,Id)
        cursor.execute(sql,val)
        print(cursor.rowcount, "record updated")
        db.commit()
    except:
        db.rollback()
        print("Record not updated")
    
    
def Library_Members():
    positon = input("Please enter your position [1.Staff , 2.Student]: ")
    a = input()
    if(positon == 'Student'):
        print("Sorry, You dont have access to the Database")
        
    elif(positon == 'Staff'):
        print("Password Accepted")
        a = input()
        choice = input("What do you want to do?: ")
        if(choice == 'Display Records of Student'):
            try:
                db = mysql.connector.connect(host = "localhost", user = "root", password = "keagan1234", database = "project")
                cursor = db.cursor()
                cursor.execute("SELECT * FROM student")
                results = cursor.fetchall()
                print("Id\t","Name\t","Grade\t","Section\t","book_issued\t","date_issued\t","date_return\t")
                for x in results:
                    print(x[0],"\t",x[1],"\t",x[2],"\t",x[3],"\t",x[4],"\t",x[5],"\t",x[6])
            
            except:
                print("Error, unable to fetch data")
                
        elif(choice == 'Add Staff Records'):
            Staff_Details()
            
        elif(choice == 'Display Staff Records'):
            try:
                db = mysql.connector.connect(host = "localhost", user = "root", password = "keagan1234", database = "project")
                cursor = db.cursor()
                cursor.execute("SELECT * FROM staff")
                results = cursor.fetchall()
                print("Member_Id\t","Name\t","Age\t","Address\t")
                for x in results:
                    print(x[0],"\t",x[1],"\t",x[2],x[3])
            
            except:
                print("Error, unable to fetch data")
            
        elif(choice == 'Delete Record of Staff'):
            delete_staff_rec()
            
        elif(choice == 'Delete Record of Student'):
            delete_student_rec()
            
        elif(choice == 'Update Student Details'):
            update_student_details()
        
        elif(choice == 'Update Staff Details'):
            update_staff_details()
            
        else:
            print("You have selected an Invalid Option")
            a = input()
            print("Do you want to continue?")
            a = input()
            decision = input("Enter your decision: ")
            if(decision == 'yes'):
                Library_Members()
            else:
                print("Exiting the Application")
                a = input()
                print("Log Out Successful")

def menu():
    a = input()
    print("Do you want to continue?")
    a = input()
    choice2 = input("Enter your choice: ")
    if(choice2 == 'yes'):
        position()
    elif(choice2 == 'no'):
        a = input()
        print("Thank You, Please visit again!!")
        a = input()
        print("Exiting the Application")
    else:
        a = input()
        print("Invalid Selection")
        print("Logging Out")

a = input()
print("*"*80)
print("Welcome to Phoenix Library")
print("*"*80)
a = input()
position()
menu()