def insert(self, cursor, new_name, new_price):
        query = f'''
        INSERT INTO users (first_name, last_name, email, phone, city)
        
        '''
        cursor.execute(query)