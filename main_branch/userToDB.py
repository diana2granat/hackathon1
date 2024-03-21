import psycopg2
from userInterface import UserInterface

user_information = UserInterface()
user_information.show_user_menu()

def add_user_to_DB():
    try:
        conn = psycopg2.connect(
        dbname = config.DATABASE,
        user = config.USERNAME,
        password = config.PASSWORD,
        host = config.HOSTNAME,
        port = config.PORT
    )
    cursor = conn.cursor()
    # Retrieve all items
    user_information = UserInterface()
    user_information = UserInterface.show_user_menu(cursor,)
    conn.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()