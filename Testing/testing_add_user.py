import config
import psycopg2


class addUser:
    def __init__(self,first_name, last_name, email, phone, city):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.city = city 
        self.conn = psycopg2.connect(
            dbname = config.DATABASE,
            user = config.USERNAME, 
            password = config.PASSWORD,
            host = config.HOSTNAME, 
            port = config.PORT
        )
    def add_user_to_db(self):
        cursor = self.conn.cursor()
        query = """
INSERT INTO users(first_name, last_name, email, phone, city) Values (%s,%s,%s,%s,%s)"""
        cursor.execute(query,(self.first_name, self.last_name, self.email, self.phone, self.city))
        self.conn.commit()
        cursor.close()
        self.conn.close()
    

    # def get_user_info(self):
    #     conn = psycopg2.connect(
    #         dbname=config.DATABASE,
    #         user=config.USERNAME, 
    #         password=config.PASSWORD,
    #         host=config.HOSTNAME, 
    #         port=config.PORT
    #     )
    #     cursor = conn.cursor()
    #     query = """
    #     SELECT * FROM users
    #     """
    #     cursor.execute(query)
    #     user_info_list = cursor.fetchall()
    #     cursor.close()
    #     conn.close()
    #     return user_info_list
    def get_user_info(self):
        conn = psycopg2.connect(
            dbname=config.DATABASE,
            user=config.USERNAME, 
            password=config.PASSWORD,
            host=config.HOSTNAME, 
            port=config.PORT
        )
        cursor = conn.cursor()
        query = """
        SELECT * FROM users ORDER BY timestamp DESC LIMIT 1;
        """
        cursor.execute(query)
        user_info_list = []
        for row in cursor.fetchall():
            for item in row:
                user_info_list.append(item)  # Append each item to the list
        cursor.close()
        conn.close()
        return user_info_list


def show_user_menu():
       user_input = input('This program is used to help you find volunteering. Please enter your first name, last name, email, phone, and city separated by commas (e.g., "John, Doe, johndoe@gmail.com, 0555555555, Jerusalem"): ')
       user_data = user_input.split(', ')
    
       if len(user_data) != 5:
        print("Invalid input. Please provide all the required information separated by commas.")
        return

       first_name, last_name, email, phone, city = user_data
    
       new_user = addUser(first_name, last_name, email, phone, city)
       new_user.add_user_to_db()
       

# show_user_menu()

