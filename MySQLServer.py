import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server
    mydb = mysql.connector.connect(
        host="localhost",
        user="myusername",  # Replace with your MySQL username
        password="mypassword"  # Replace with your MySQL password
    )
    
    mycursor = mydb.cursor()
    
    # Create database if it doesn't exist
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")
    
except mysql.connector.Error as err:
    print(f"Error: {err}")
    
finally:
    if mycursor:
        mycursor.close()
    if mydb:
        mydb.close()
        
