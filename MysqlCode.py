import mysql.connector
import bcrypt
import mymsgBox as messagebox
import random
from emailSender import sendEmail
from createMysqlTables import MysqlTables 

class Database:
    def __init__(self):
        self.cursor = None
        self.connection = None
        self.host = 'localhost'
        self.user = 'root'
        self.password = ''
        self.database = ''
        self.msg = messagebox.Rmsg()
        self.laptop_id=None
        self.mobile_id=None
        self.other_id=None
        self.r_laptop_id=None
        self.r_mobile_id=None
        self.r_other_id=None
        self.building = None
        self.room = None
        self.floor = None
        # self.userId = None
        # self.MysqlTables=MysqlTables()

    def get_connected(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
        except mysql.connector.Error as e:
            print(f"Error: {e}")

    # def find_user_id(self, brand, model, color, operating_system, security_q1, q1_ans, security_q2, q2_ans, serial_number):
    #     # cursor = connection.cursor()
    #     self.get_connected()
        
    #     # Counting the number of non-null attributes
    #     non_null_attributes = sum(1 for attr in [brand, model, color, operating_system, security_q1, q1_ans, security_q2, q2_ans, serial_number] if attr is not None)
        
    #     # Query to find userId based on matching attributes
    #     query = """
    #     SELECT userId,
    #         (IF(brand = %s, 1, 0) + IF(model = %s, 1, 0) + IF(color = %s, 1, 0) +
    #             IF(operating_system = %s, 1, 0) + IF(securityQ1 = %s, 1, 0) + IF(Q1Ans = %s, 1, 0) +
    #             IF(securityQ2 = %s, 1, 0) + IF(Q2Ans = %s, 1, 0) + IF(serial_number = %s, 1, 0)) / %s AS matching_percentage
    #     FROM laptop_table
    #     HAVING matching_percentage >= 0.6
    #     """
        
    #     # Executing the query
    #     self.cursor.execute(query, (brand, model, color, operating_system, security_q1, q1_ans, security_q2, q2_ans, serial_number, non_null_attributes))
    #     result = self.cursor.fetchone()
    #     print(result)
    
    #     if result:
    #         return result[0]  # Returning the userId if found
    #     else:
    #         return None  # Returning None if no matching userId found
    
    # def find_user_id(self, **attributes):
    #     # Constructing the query dynamically
    #     self.get_connected()
    #     query = "SELECT userId FROM laptop_table WHERE "
    #     conditions = []
    #     values = []
    #     for key, value in attributes.items():
    #         if value is not None:
    #             conditions.append(f"{key} = %s")
    #             values.append(value)
    #     query += " AND ".join(conditions)
        
    #     # Execute the query
    #     self.cursor.execute(query, tuple(values))
        
    #     # Fetching results
    #     result = self.cursor.fetchone()
        
    #     return result[0] if result else print("no")
    def calculate_similarity(self,table_data, query_data):
        # Function to calculate similarity score excluding security questions and answers
        total_attributes = len(table_data) - 4  # Exclude security questions and answers
        matched_attributes = sum(1 for key, value in query_data.items() if value is not None and key in table_data and key not in ('securityQ1', 'Q1Ans', 'securityQ2', 'Q2Ans') and value == table_data[key])
        similarity_score = (matched_attributes / total_attributes) * 100
        return similarity_score

    def find_user_id(self, **attributes):
        self.get_connected()
        # Execute query to get all data from laptop_table
        self.cursor.execute("SELECT * FROM laptop_table")
        results = self.cursor.fetchall()

        max_similarity_score = 0
        matching_user_id = None

        # Iterate through each row in the table
        for row in results:
            table_data = dict(zip(self.cursor.column_names, row))
            similarity_score = self.calculate_similarity(table_data, attributes)
            if similarity_score > max_similarity_score:
                max_similarity_score = similarity_score
                matching_user_id = table_data['userId']

        # Check if similarity score is above 60%
        if max_similarity_score >= 30:
            return matching_user_id
        else:
            return None


    def login(self, email, password):
        try:
            self.get_connected()
            query = "SELECT id , password  FROM register WHERE email = %s "
            self.cursor.execute(query, (email,))
            fetched_data = self.cursor.fetchone()
            print("fetch",fetched_data)
            if fetched_data is not None:
                id = fetched_data[0]

                stored_hashed_password = fetched_data[1].encode()
                print("password",stored_hashed_password)

                if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password):
                    self.msg.ShowMsg("Login successful!")
                    print("id" , id)
                    data = id 
                    return data
            else:
                self.msg.ShowMsg("Invalid email or password from mysql")

        except mysql.connector.Error as e:
            self.msg.ShowMsg(f"Error connecting to MySQL: {e}")

        finally:
            if self.cursor:
                self.cursor.close()

   


    def generate_unique_product_id(self):
        alphabet_part = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(3))
        number_part = ''.join(random.choice('1234567890') for _ in range(4))
        return alphabet_part + number_part

    def insert_user(self, name, email, mobile, password):
        try:
            self.get_connected()
            unique_product_id = self.generate_unique_product_id()
            # self.MysqlTables.create_user_table()
            query = "INSERT INTO register (name, email, mobile, password,product_id) VALUES (%s, %s, %s, %s,%s)"
            data = (name, email, mobile, password, unique_product_id)
            self.cursor.execute(query,data)
            self.connection.commit()
            print("Data Stored in Table Successfully")
            return self.cursor.lastrowid
        except mysql.connector.errors.IntegrityError as e:
            if "Duplicate entry" in str(e):
                self.msg.ShowMsg("Email or mobile number is already in use.")
            else:
                self.msg.ShowMsg("An error occurred during registration.")
        return None

    def checkReport(self, userId, category, lost_item_name, building_name, floor, room, image_path):
        self.get_connected()

        try:
            matched_query = 'select userId from requestTable where category=%s and building_name=%s and floor=%s and room=%s'
            self.cursor.execute(matched_query, (category, building_name, floor, room))
            matched_result = self.cursor.fetchone()

            if matched_result:
                self.msg.ShowMsg("Report Matched")
                return matched_result[0]

            else:
                # self.MysqlTables.create_report_tabel()

                insert_query = """
                INSERT INTO reporttable (userId ,category, lost_item_name, building_name, floor, room, image_data)
                VALUES (%s ,%s, %s, %s, %s, %s, %s)
                """
                insert_values = (userId ,category, lost_item_name, building_name, floor, room, image_path)
                self.cursor.execute(insert_query, insert_values)
                self.connection.commit()

                print("Data inserted into reportTable")

                self.msg.ShowMsg("No matching request found. But Thanks for Your Support. Once We Will find the owner WE Will Inform You ")
                return False  

        except mysql.connector.Error as e:
            print(e)
            self.msg.ShowMsg(f"Error connecting to MySQL: {e}")

    def checkRequest(self, userId, category, building, floor, room):
        self.get_connected()
        registered_lost_item_data = None
        id = None
        result = None
        table_name = ''
        
        if category == 'Mobile phone':
            table_name = 'reported_mobile'
            registered_lost_item_data = self.getData(userId, 'mobile_table')
            print("getdata", registered_lost_item_data)
            id = 'imei_number'
        elif category == 'Laptop':  
            table_name = 'reported_laptop'
            registered_lost_item_data = self.getData(userId, 'laptop_table')
            print("getdata", registered_lost_item_data)
            id = 'serial_number'
        else:
            table_name = 'other_reports'
            registered_lost_item_data = self.getData(userId, 'other_data_table')

        if registered_lost_item_data != 'other_reports':  
            matched_query = f"SELECT id,userId FROM {table_name} WHERE Brand = %s AND model = %s AND color = %s AND operating_system = %s AND {id} = %s AND building_name = %s AND floor = %s AND room = %s"
            self.cursor.execute(matched_query, (registered_lost_item_data[2], registered_lost_item_data[3], registered_lost_item_data[4], registered_lost_item_data[5], registered_lost_item_data[10], building, floor, room))
            result = self.cursor.fetchone()
            print("result if", result)
        elif registered_lost_item_data == 'other_reports':
            matched_query = f"SELECT id,userId FROM {table_name} WHERE name = %s AND color = %s AND building_name = %s AND floor = %s AND room = %s"
            self.cursor.execute(matched_query, (registered_lost_item_data[2], registered_lost_item_data[3], building, floor, room))
            result = self.cursor.fetchone()
            print("result else", result)
            print("Type of result:", type(result))
        if result :  
            self.msg.ShowMsg("Request Matched")
            print("myresult",result)
            return result[1]
        else:
            unmatched_query = "INSERT INTO requesttable (userId,registered_device_id, category, building_name, floor, room) VALUES (%s, %s, %s, %s, %s, %s)"
            unmatched_values = (userId,registered_lost_item_data[0], category, building, floor, room)
            self.cursor.execute(unmatched_query, unmatched_values)
            self.connection.commit()

            self.msg.ShowMsg("No matching Report found. But don't Worry, We Have Stored Your Response. Whenever We Find Any Match We Will Inform You")
            return False


    def getMydata(self, userId):
        self.get_connected()
        query = 'select * from register where id=%s '
        self.cursor.execute(query, userId)
        return self.cursor.fetchone()

    def getData(self,userId,table_name):
        self.get_connected()
        query = f"select * from {table_name} where userId = %s "
        self.cursor.execute(query , (userId,))
        result = self.cursor.fetchone()
        return result
        
   
    # def checkRequest(self, userId, category, building, floor, room):
    #     self.get_connected()
    #     # getData = self.getData
    #     registered_lost_item_data = None
    #     id = None
    #     result = None
    #     table_name = ''

    #     # Use a dictionary to map category to corresponding table name and id
    #     category_mapping = {
    #         'Mobile phone': ('reported_mobile', 'imei_number'),
    #         'Laptop': ('reported_laptop', 'serial_number'),
    #     }

    #     # If category exists in the mapping, extract table_name and id
    #     if category in category_mapping:
    #         table_name, id = category_mapping[category]
    #         registered_lost_item_data = self.getData(userId, f'{category.lower()}_table')
    #         print("getdata", registered_lost_item_data)

    #     # If table_name is still empty, assign it to 'other_reports'
    #     if not table_name:
    #         table_name = 'other_reports'
    #         registered_lost_item_data = self.getData(userId, 'other_data_table')

    #     if registered_lost_item_data != 'other_reports':
    #         matched_query = f"SELECT userId FROM {table_name} WHERE Brand = %s AND model = %s AND color = %s AND operating_system = %s AND {id} = %s AND building_name = %s AND floor = %s AND room = %s"
    #         self.cursor.execute(matched_query, (registered_lost_item_data[2], registered_lost_item_data[3], registered_lost_item_data[4], registered_lost_item_data[5], registered_lost_item_data[10], building, floor, room))
    #         result = self.cursor.fetchone()
    #         print("result if", result)
    #     else:
    #         matched_query = f"SELECT userId FROM {table_name} WHERE name = %s AND color = %s AND building_name = %s AND floor = %s AND room = %s"
    #         self.cursor.execute(matched_query, (registered_lost_item_data[2], registered_lost_item_data[3], building, floor, room))
    #         result = self.cursor.fetchone()
    #         print("result else", result)
        
    #     print("Type of result:", type(result))
        # if result is not None:
        #     self.msg.ShowMsg("Request Matched")
        #     print(result)
        #     return result[0]
        # else:
        #     unmatched_query = "INSERT INTO requesttable (userId, category, building_name, floor, room) VALUES (%s, %s, %s, %s, %s)"
        #     unmatched_values = (userId, category, building, floor, room)
        #     self.cursor.execute(unmatched_query, unmatched_values)
        #     self.connection.commit()

        #     self.msg.ShowMsg("No matching Report found. But don't Worry, We Have Stored Your Response. Whenever We Find Any Match We Will Inform You")
        #     return False

    
    def changePassword(self, email, password):
        self.get_connected()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        query = "UPDATE register SET password=%s WHERE email=%s"
        self.cursor.execute(query, (hashed_password, email))
        self.connection.commit()
        print("Password updated successfully")
        self.msg.ShowMsg("Password updated successfully")
        return True

    def checkMail(self, email):
        self.get_connected()
        q = "select * from register where email = %s"
        self.cursor.execute(q , (email,))
        result = self.cursor.fetchone()
        if result is not None:
            return True
        else:
            self.msg.ShowMsg("No user Found with this Email")
            return False

    def reportUsingId(self, victim_product_id, reporter_product_id):
        self.get_connected()
        victim_query = 'SELECT name, email FROM register WHERE product_id=%s'
        self.cursor.execute(victim_query, (victim_product_id,))
        victim_result = self.cursor.fetchone()

        reporter_query = 'SELECT name,email, mobile FROM register WHERE product_id=%s'
        self.cursor.execute(reporter_query, (reporter_product_id,))
        reporter_result = self.cursor.fetchone()

        if reporter_result:
            self.reporter_name, self.reporter_email, self.reporter_mobile = reporter_result
            print(f"reporter name: {self.reporter_name}, reporter mobile: {self.reporter_mobile}")
            print(reporter_product_id)
        else:
            print("Please Login First")

        if victim_result:
            self.victim_name, self.victim_email = victim_result
            print(f"victim Name: {self.victim_name}, victim Email: {self.victim_email}")
            print(victim_product_id)
        else:
            print("No match found")

        self.message = f'Hey {self.victim_name} ! We just found something from Your Product Id {victim_product_id}. If You have Lost something So You Can contact {self.reporter_mobile} Number or Email {self.reporter_email}'
        sendEmail(self.victim_email, "We Found Something", self.message)
        self.msg.ShowMsg(f'Hey {self.reporter_name} ! We Have Successfully Send Email To the User with Product Id {victim_product_id}. Thanks For Your Contribution')

            # userId=self.userId,
            # Brand=self.selected_brand.get(),
            # model=self.selected_model.get(),
            # color=self.selected_laptop_color.get(), 
            # operating_system=self.selected_os_option.get(),
            # serial_number=self.serial_textBox.get("1.0", "end-1c"),
            # security_qustion1=self.selected_question1.get(),
            # security_answer1=self.question1_textBox.get("1.0", "end-1c"),
            # security_qustion2=self.selected_question2.get(),
            # security_answer2=self.question2_textBox.get("1.0", "end-1c")
    def insert_laptop_data(self, userId, Brand, model, color,operating_system,serial_number ,security_qustion1,security_answer1,security_qustion2,security_answer2):
            
            try:
                self.get_connected()
                # self.MysqlTables.create_insert_laptop()
                if "" in (userId, Brand, model, color,serial_number, operating_system,security_qustion1,security_answer1,security_qustion2,security_answer2 ):
                    self.msg.ShowMsg("One or more input values are None. Data not inserted.")
                    return None
                if len(serial_number) != 10:
                    self.msg.ShowMsg("Enter a vaild Serial Number")
                    return None

                query = """INSERT INTO laptop_table (userId, Brand, model, color, operating_system, securityQ1, Q1Ans, securityQ2, Q2Ans ,serial_number)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s ,%s)"""
                data = (userId, Brand, model, color, operating_system,security_qustion1,security_answer1,security_qustion2,security_answer2,serial_number)
                self.cursor.execute(query, data)
                self.connection.commit()
                print("Data inserted successfully")
                self.laptop_id = self.cursor.lastrowid
                self.register_devices(self.cursor ,userId)
                return True
            except mysql.connector.Error as error:
                print("Error inserting data into laptop_table:", error)
                return None
           
    def check_already(self,userId,name):
        if name == 'laptop':
            table = 'laptop_table'
        if name == 'mobile':
            table = 'mobile_table'
        if name == 'other':
            table = 'other_data_table'
        self.get_connected()
        print(table)
        q = f"select * from {table} where userId = %s"
        data = (userId,)
        print(data)
        self.cursor.execute(q,data)
        r = self.cursor.fetchone()
        print(r)
        if r is not None:
            self.msg.ShowMsg(f"You have already registered one")
            return False
        else:
            return True
            

    def insert_mobile_data(self, userId, Brand, model, color, operating_system, imei_number,security_qustion1,security_answer1,security_qustion2,security_answer2 ):
        try:
            self.get_connected()
            # self.MysqlTables.create_insert_mobile()
            if "" in (userId, Brand, model, color, operating_system, imei_number,security_qustion1, security_answer1,security_qustion2,security_answer2):
                self.msg.ShowMsg("One or more input values are None. Data not inserted.")
                return None
            if len(imei_number) != 15:
                self.msg.ShowMsg("Enter a vaild IMEI Number")
                return None

            query =  """INSERT INTO mobile_table (userId, Brand, model, color, operating_system, imei_number, securityQ1, Q1Ans, securityQ2, Q2Ans)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            data = (userId, Brand, model, color, operating_system, imei_number,security_qustion1, security_answer1,security_qustion2,security_answer2)
            self.cursor.execute(query, data)
            self.connection.commit()
            print("Data inserted successfully")
            self.mobile_id =  self.cursor.lastrowid
            self.register_devices(self.cursor , userId)
            return True
        except mysql.connector.Error as error:
            print("Error inserting data into mobile_table:", error)
            return None


# c = self.db.insert_other_data(
#             userId=self.userId,
#             name=self.selected_category_option.get("1.0", "end-1c"),
#             color=self.selected_mobile_color.get(),
#             security_qustion1=self.selected_question1.get(),
#             security_answer1=self.question1_textBox.get("1.0", "end-1c"),
#             security_qustion2=self.selected_question2.get(),
#             security_answer2=self.question2_textBox.get("1.0", "end-1c")
#         )
#         if c is True:
#             self.parentApp.label3.place(x=510, y=250, height=40, width=80)
#             self.master.destroy()
    def insert_other_data(self, userId, name, color, security_qustion1,security_answer1,security_qustion2,security_answer2):
        try:
            self.get_connected()
            # self.MysqlTables.create_insert_other()
            if "" in (userId, name, color, security_qustion1,security_answer1,security_qustion2,security_answer2):
                self.msg.ShowMsg("One or more input values are None. Data not inserted.")
                return None

            query = """INSERT INTO other_data_table (userId, name, color, securityQ1,Q1Ans,securityQ2,Q2Ans) 
                       VALUES (%s, %s, %s,%s, %s, %s, %s)"""
            data = (userId, name, color, security_qustion1,security_answer1,security_qustion2,security_answer2)
            self.cursor.execute(query, data)
            self.connection.commit()
            self.msg.ShowMsg("Data inserted successfully")
            self.other_id = self.cursor.lastrowid
            self.register_devices(self.cursor, userId)
            return True
        except mysql.connector.Error as error:
            print("Error inserting data into other_data_table:", error)
            return None
        

    def register_devices(self, cursor, userId):
        try:
            # self.get_connected()
            # self.create_registerDevices()
            flag = 0
            check_query = 'SELECT laptop_id, mobile_id, other_id FROM registerdevices WHERE userId = %s'
            cursor.execute(check_query, (userId,))
            result = cursor.fetchone()

            if result:
                for device_id in result:
                    if device_id is not None:
                        flag += 1
                        break
                if flag == 1:
                    if result[0] is None:
                        self.putdata(userId, cursor, 'laptop_id', self.laptop_id)
                    if result[1] is None:
                        self.putdata(userId, cursor, 'mobile_id', self.mobile_id)
                    if result[2] is None:
                        self.putdata(userId, cursor, 'other_id', self.other_id)
            else:
                query = "INSERT INTO registerdevices (userId, laptop_id, mobile_id, other_id) VALUES (%s, %s, %s, %s)"
                data = (userId, self.laptop_id, self.mobile_id, self.other_id)
                cursor.execute(query, data)
                self.connection.commit()
                print("Data inserted into registerdevices successfully")
                return cursor.lastrowid

        except mysql.connector.Error as error:
            print("Error inserting data into registerdevices:", error)
            # Log the error for debugging
            return None
        

    # def insert_Reportlaptop_data(self, userId, brand, model, color, serial_number, operating_system, unique_identification, building, floor, room):
    #     self.building = building
    #     self.floor = floor
    #     self.room = room
    #     try:
    #         self.get_connected()
            
    #         if "" in (userId, brand, model, color, serial_number, operating_system, unique_identification, building, floor, room):
    #             self.msg.ShowMsg("One or more input values are None. Data not inserted.")
    #             return None
    #         if len(serial_number) != 10:
    #             self.msg.ShowMsg("Enter a valid Serial Number")
    #             return None
            
    #         query1 = """INSERT INTO reported_laptop (userId, brand, model, color, operating_system, unique_identification, serial_number) 
    #                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    #         data1 = (userId, brand, model, color, operating_system, unique_identification.upper(), serial_number)
    #         self.cursor.execute(query1, data1)
    #         self.connection.commit()
           
    #         self.insert_into_report(userId)

    #     except mysql.connector.Error as error:
    #         print("Error inserting data into LaptopReports table:", error)
    #         return None


    # def insert_ReportMobile_data(self, userId, brand, model, color, imei_number, operating_system, unique_identification, building, floor, room):
    #     self.building = building
    #     self.floor = floor
    #     self.room = room
    #     try:
    #         self.get_connected()
            
    #         if "" in (userId, brand, model, color, imei_number, operating_system, unique_identification, building, floor, room):
    #             self.msg.ShowMsg("One or more input values are None. Data not inserted.")
    #             return None
    #         if len(imei_number) != 15:
    #             self.msg.ShowMsg("Enter a valid IMEI Number")
    #             return None

    #         query = """INSERT INTO reported_mobile (userId, brand, model, color, operating_system, unique_identification, imei_number) 
    #                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    #         data = (userId, brand, model, color, operating_system, unique_identification.upper(), imei_number)
    #         self.cursor.execute(query, data)
    #         self.connection.commit()
           
            
    #         self.insert_into_report( userId)

    #     except mysql.connector.Error as error:
    #         print("Error inserting data into mobile table:", error)
    #         return None

    
    def insert_ReportOthers_data(self, userId, name,color,building, floor, room,description ):
        self.building = building
        self.floor = floor
        self.room = room
        try:
            self.get_connected()

            if "" in (userId, name, description, building, floor, room, color):
                self.msg.ShowMsg("One or more input values are None. Data not inserted.")
                return None

            query = """INSERT INTO requesttable_unregistered ( userId, category,color,building_name, floor, room,description) 
                    VALUES (%s, %s, %s,%s, %s, %s,%s)"""
            data = ( userId, name,color,building, floor, room,description)
            self.cursor.execute(query, data)
            self.connection.commit()
            # self.msg.ShowMsg("Data inserted")
            
            
            self.msg.ShowMsg("Currently we don't have any match but don't worry we are working on your request")

        
            # self.insert_into_report( userId)
            
            
        except mysql.connector.Error as error:
            print("Error inserting data into OthersReports table:", error)
            return None


    def putdata(self, userId, cursor, column, value):
        try:
            query = f'UPDATE registerdevices SET {column} = %s WHERE userId = %s'
            data = (value, userId)
            cursor.execute(query, data)
            self.connection.commit()
            print(f"Data inserted into registerdevices successfully for {column}")

        except mysql.connector.Error as error:
            print(f"Error updating data in registerdevices for {column}:", error)
            # Log the error for debugging
            return None

        finally:
            cursor.close()
    # def setFrKeys(self,userId):
    #     self.get_connected()
    #     q1 = 'select id from reported_laptop where userId = %s'
    #     self.cursor.execute(q1 , (userId,))
    #     self.r_laptop_id = self.cursor.fetchone()
    #     q2 = 'select id from reported_mobile where userId = %s'
    #     self.cursor.execute(q2 , (userId,))
    #     self.r_mobile_id = self.cursor.fetchone()
    #     q3 = 'select id from other_reports where userId = %s'
    #     self.cursor.execute(q3 , (userId,))
    #     self.r_other_id = self.cursor.fetchone()
    #     if self.r_laptop_id is not None:
    #         self.r_laptop_id = self.r_laptop_id[0]
    #         self.setFr(self.cursor,userId,'reported_laptop_id',self.r_laptop_id)
    #     if self.r_mobile_id is not None:
    #         self.r_mobile_id = self.r_mobile_id[0]
    #         self.setFr(self.cursor,userId,'reported_mobile_id',self.r_mobile_id)
    #     if self.r_other_id is not None:
    #         self.r_other_id = self.r_other_id[0]
    #         self.setFr(self.cursor,userId,'other_report_id',self.r_other_id)

        
    # def setFr(self,cursor,userId,cell,data):# q4 = 'INSERT INTO reporttable(reported_laptop_id , reported_mobile_id ,other_report_id)VALUES(%s,%s,%s)'
    #     q4 = f' UPDATE reporttable SET {cell}'+' = %s WHERE userId = %s;'
    #     cursor.execute(q4,(data,userId))
    #     self.connection.commit()
    #     print("done")

    # def insert_into_report(self , userId):
    #     self.get_connected()
    #     q0 = 'select id from reporttable where userId = %s'
    #     self.cursor.execute(q0 , (userId,))
    #     result = self.cursor.fetchone()
    #     if result is not None:
    #         self.setFrKeys(userId)
    #     else:
    #         query2 = 'INSERT INTO reporttable(userId, building_name, floor, room) VALUES (%s, %s, %s, %s)'
    #         # data2 = (userId, self.building, self.floor, self.room)
    #         data2 = (userId, 'a', 'v', 'l')
    #         self.cursor.execute(query2, data2)
    #         self.setFrKeys(userId)
    #         self.connection.commit()
    #     print("Data inserted successfully")
        # return True

        


if __name__ == '__main__':
    d = Database()
    # print(d.getData(1,'Mobile_table'))

    # d.insert_into_report(1) 
    d.checkRequest( userId = 1, category = 'Laptop', building = 'Old building', floor = '10th Floor', room = '1')
    # d.insert_ReportOthers_data( userId = 1, name = 'calculator',color = 'black',building = 'Old building', floor = '10th Floor', room = '1',description = 'sam is written on it' )


    # k = d.insert_laptop_data( userId=17, Brand='a', model='b', color='c', operating_system='l')
    # k = d.insert_laptop_data( userId = 1, Brand ='q', model = 'a', color = 'b',operating_system = 'c',serial_number = 'd' ,security_qustion1 = 'f',security_answer1 = 'g',security_qustion2 = 'h',security_answer2 = 'i')
    # print(k)
    # d.setFrKeys(3)
    # d.insert_Reportlaptop_data( userId=1, brand='a', model='b', color='c', serial_number='d', operating_system='e', unique_identification='f', building='g', floor='h', room='i')
    
    # d.find_user_id( brand, model, color, operating_system, security_q1, q1_ans, security_q2, q2_ans, serial_number)
    # attributes = {
    # 'Brand': 'Lenovo',
    # 'model': 'Yoga C940',
    # 'color': 'Black',
    # 'operating_system': 'Windows 10',
    # 'serial_number': '1234567777'
    # }
    # 'Brand': 'ExampleBrand',
    # 'model': 'ExampleModel',
    # 'color': None,  # ExampleColor
    # 'operating_system': None,  # ExampleOS
    # 'securityQ1': 'ExampleQuestion1',
    # 'Q1Ans': None,  # ExampleAnswer1
    # 'securityQ2': None,  # ExampleQuestion2
    # 'Q2Ans': 'ExampleAnswer2',
    # 'serial_number': 'ExampleSerialNumber'
    # user_id = d.find_user_id( **attributes)
    # print(user_id)