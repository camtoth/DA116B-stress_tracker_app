import configparser

import mysql.connector

config = configparser.ConfigParser()
# read the configuration file to get the
config.read("config.ini")


class Database:
    def connect_database():
        try:
            mydb = mysql.connector.connect(
                host=config.get(
                    "database", "db_host_key"
                ),  # get the credential from the config file
                user=config.get("database", "db_user_key"),
                password=config.get("database", "db_password_key"),
                database=config.get("database", "db_database_key"),
            )
            return mydb
        except Exception as er:
            print(er)

    def select_user(connect):
        mycursor = connect.cursor()
        mycursor.execute("SELECT * FROM user")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)

    def select_admin(connect):
        mycursor = connect.cursor()
        mycursor.execute("SELECT * FROM admin")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)

    def insert_user(
        connect,
        first_name,
        last_name,
        gender,
        email,
        program,
        degree,
        password,
        age,
        study_year,
    ):
        try:
            mycursor = connect.cursor()
            query = f"""INSERT INTO user (user_firstname, user_lastname, user_gender, user_email, user_program, user_degree, user_password, user_age, user_studyYear)
            VALUES ("{first_name}", "{last_name}", "{gender}", "{email}", "{program}", "{degree}", "{password}", "{age}", "{study_year}")"""
            mycursor.execute(query)
        except Exception as er:
            print(er)

    def insert_admin(connect, first_name, last_name, email, password, title):
        try:
            mycursor = connect.cursor()
            query = f"""INSERT INTO admin (admin_firstname, admin_lastname, admin_email, admin_password, admin_title)
                VALUES ("{first_name}", "{last_name}", "{email}", "{password}", "{title}")"""
            mycursor.execute(query)
        except Exception as er:
            print(er)


connect = Database.connect_database()
Database.insert_user(
    connect,
    "Ahmed",
    "moh",
    "male",
    "ahmed@gmail.com",
    "management",
    "master",
    "ahmed123",
    "21",
    "second year",
)
# Database.insert_admin(connect, "lisa", "adem", "lisa@gmail.com", "lisa123", "IT")
Database.select_user(connect)
# Database.select_admin(connect)
