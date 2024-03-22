import test_config as test_config
import psycopg2


class addUser:
    def __init__(self,first_name, last_name, email, phone, city):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.city = city 
        self.conn = psycopg2.connect(
            dbname = test_config.DATABASE,
            user = test_config.USERNAME, 
            password = test_config.PASSWORD,
            host = test_config.HOSTNAME, 
            port = test_config.PORT
        )
    def add_user_to_db(self):
        cursor = self.conn.cursor()
        query = """
INSERT INTO users(first_name, last_name, email, phone, city) Values (%s,%s,%s,%s,%s)"""
        cursor.execute(query,(self.first_name, self.last_name, self.email, self.phone, self.city))
        self.conn.commit()
        cursor.close()
        self.conn.close()
    
    def get_user_info(self):
        conn = psycopg2.connect(
            dbname=test_config.DATABASE,
            user=test_config.USERNAME, 
            password=test_config.PASSWORD,
            host=test_config.HOSTNAME, 
            port=test_config.PORT
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





