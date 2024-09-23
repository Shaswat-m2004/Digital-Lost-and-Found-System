import mysql.connector
from emailSender import sendEmail
import mymsgBox as messagebox

class DatabaseManager:
    def __init__(self,userId):
        self.host = 'localhost'
        self.user = 'root'
        self.password = '11223344'
        self.database = 'foundmate'
        self.connection = None
        self.userId = userId
        self.cursor = None
        self.reported_mobile_id_v =None
        self.other_report_id_v =None 
        self.reported_laptop_id =None
        self.msg = messagebox.Rmsg()
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print("Connected to the database")
        except mysql.connector.Error as e:
            print(f"Error: {e}")

    def disconnect(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Disconnected from the database")

    def execute_query(self, query, data=None):
        try:
            self.cursor.execute(query, data)
            self.connection.commit()
            return self.cursor.lastrowid
        except mysql.connector.Error as e:
            print(f"Error executing query: {e}")
            return None
    def getMydata(self, userId):
        # self.get_connected()
        query = 'select * from register where id=%s '
        self.cursor.execute(query, userId)
        return self.cursor.fetchone()
    
    # def location_match(self,myid, building, floor, room, color, category):
    #     q0 = "SELECT userId FROM requesttable_unregistered WHERE category = %s"
    #     data = (category,)
    #     self.cursor.execute(q0, data)
    #     victim_id = self.cursor.fetchone()
    #     if victim_id:
    #         q = "SELECT id FROM requesttable_unregistered WHERE userId = %s AND building_name = %s AND floor = %s AND room = %s AND color = %s"
    #         data0 = (victim_id[0], building, floor, room, color)
    #         self.cursor.execute(q, data0)
    #         result = self.cursor.fetchone()
    #         if result:
    #             desc = self.fetch_desc(result[0]) 
    #             self.mail(desc,victim_id[0],myid) 
    #         else:
    #             print("No matching record found.")
    #     else:
    #         print("No victim found for the given category.")
    def location_match(self, myid, building, floor, room, color, category):
        q0 = "SELECT userId FROM requesttable_unregistered WHERE category = %s"
        data = (category,)
        self.cursor.execute(q0, data)
        victim_id = self.cursor.fetchone()
        if victim_id is not None:

            q = "SELECT id FROM requesttable_unregistered WHERE userId = %s AND building_name = %s AND floor = %s AND room = %s AND color = %s"
            v_id = victim_id[0]
            # data0 = 
            print("v_id:", v_id, type(v_id))
            print("building:", building, type(building))
            print("floor:", floor, type(floor))
            print("room:", room, type(room))
            print("color:", color, type(color))
            self.cursor.execute(q, (v_id, building, floor, room, color,))
            result = self.cursor.fetchone()
            if result:
                desc = self.fetch_desc(result[0]) 
                self.mail(desc, victim_id[0], myid) 
                return 'request'
            else:
                print("No matching record found.")
                return False
        else:
            print("No victim found for the given category.")
            return False


    def fetch_desc(self, id):
        q = "SELECT description FROM requesttable_unregistered WHERE id = %s"
        self.cursor.execute(q, (id,))
        description = self.cursor.fetchone()
        if description:
            print("Description:", description[0])
            return description[0]
        else:
            print("No description found for the given id.")
    
    def mail(self,desc,victim_id,myid):
        subject = "Thank You So Much For Your Report"
        mydata = self.getMydata((myid,))
        victimData = self.getMydata((victim_id,))
        body = f""" 
{mydata[1]} we have a matching request for your report
Please verify that item you found satifies this description  
{desc}
if yes than Please contact {victimData[1]}
Email:{victimData[2]}
Mobile number:{victimData[3]}
"""
        sendEmail(mydata[2],subject,body)
        self.msg.ShowMsg(f"{mydata[1]},lost item location matched\nPlease check your mail and by verifying the description contact the ower")
        
    def check_for_request(self,userId, name,color,building, floor, room,description):
        # table = 'other_reports'
        if name == 'Laptop' or name =='Mobile phone':
            name1 = "reported_laptop"
            name2 = "reported_mobile"
            name3 = "other_reports"

            q0 = f'select * from {name1} where building_name = %s AND floor = %s AND room = %s AND color = %s'
            data = (building, floor, room,color)
            self.cursor.execute(q0,data)
            r = self.cursor.fetchone()
            if r is None:
                q0 = f'select * from {name2} where building_name = %s AND floor = %s AND room = %s AND color = %s'
                data = (building, floor, room,color)
                self.cursor.execute(q0,data)
                r = self.cursor.fetchone()
                if r is None:
                    q0 = f'select * from {name3} where building_name = %s AND floor = %s AND room = %s AND color = %s'
                    data = (building, floor, room,color)
                    self.cursor.execute(q0,data)
                    r = self.cursor.fetchone()
        else:
                q0 = f'select * from other_reports where building_name = %s AND floor = %s AND room = %s AND color = %s AND name = %s'
                data = (building, floor, room,color,name)
                self.cursor.execute(q0,data)
                r = self.cursor.fetchone()


        # if name == 'Laptop':
        #     table1 = 'reported_laptop'
        # elif name == 'Mobile phone':
        #     table1 = 'reported_mobile'

        # if table is not 'other_reports' and not None:
        #     q = f'select * from {table} where building_name = %s AND floor = %s AND room = %s AND color = %s'
        #     data = (building, floor, room,color)
        #     self.cursor.execute(q,data)
        #     r = self.cursor.fetchone()
           
        # else:
        #     q = f'select * from {table} where name = %s AND building_name = %s AND floor = %s AND room = %s AND color = %s'
        #     data = (name ,building, floor, room,color)
        #     self.cursor.execute(q,data)
        #     r = self.cursor.fetchone()
        print("r:",r)
        if r :
            mydata = self.getMydata((r[1],))
            print("mydata:",mydata)
            victim_data = self.getMydata((userId,))
            print("vi",victim_data)
            subject = "Recived a Request"
            body = f"""
hey,{mydata[1]} we have received a request which matches to your report 
{r}
Please verify this description first 
{description}
contact details of the rquester is :
Email : {victim_data[2]}
mobile number : {victim_data[3]}
"""
            sendEmail(mydata[2],subject,body)
            self.msg.ShowMsg(f"We have a Corresponding Report soon the Reporter will contact you, don't worry now your {name} is/are not too far ")
            return False
        else:
            return True
        

    def fetch_one(self, query, data=None):
        self.cursor.execute(query, data)
        result = self.cursor.fetchone()
        return result[0] if result else None

    def insert_reported_laptop(self, Brand, model, color, operating_system, serial_number, userId,building_name ,floor ,room):
        query = 'INSERT INTO reported_laptop (Brand, model, color, operating_system, serial_number, userId,building_name ,floor ,room) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        data = (Brand, model, color, operating_system, serial_number, userId,building_name ,floor ,room)
        return self.execute_query(query, data)

    def insert_reported_mobile(self, Brand, model, color, operating_system, imei_number, userId, building_name, floor, room):
        query = 'INSERT INTO reported_mobile (Brand, model, color, operating_system, imei_number, userId, building_name, floor, room) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        data = (Brand, model, color, operating_system, imei_number, userId, building_name, floor, room)
        return self.execute_query(query, data)


    def insert_other_report(self, name, color, userId,building ,floor ,room):
        query = 'INSERT INTO other_reports (name, color, userId,building_name ,floor ,room) VALUES (%s, %s, %s, %s, %s, %s)'
        data = (name, color, userId,building ,floor ,room)
        return self.execute_query(query, data)

    def insert_report_table(self, userId, reported_laptop_id, reported_mobile_id, other_report_id):
        query = 'INSERT INTO reporttable (userId, reported_laptop_id, reported_mobile_id, other_report_id) VALUES (%s, %s, %s, %s)'
        data = (userId, reported_laptop_id, reported_mobile_id, other_report_id)
        return self.execute_query(query, data)

    def update_reporttable(self, userId, reported_laptop_id, reported_mobile_id, other_report_id):
        query = 'UPDATE reporttable SET reported_laptop_id = %s, reported_mobile_id = %s, other_report_id = %s WHERE userId = %s '
        data = (reported_laptop_id, reported_mobile_id, other_report_id, userId)
        return self.execute_query(query, data)


    def get_reported_mobile_id(self, userId):
        query = 'SELECT id FROM reported_mobile WHERE userId = %s'
        return self.fetch_one(query, (userId,))

    def get_reported_laptop_id(self, userId):
        query = 'SELECT id FROM reported_laptop WHERE userId = %s'
        return self.fetch_one(query, (userId,))

    def get_other_report_id(self, userId):
        query = 'SELECT id FROM other_reports WHERE userId = %s'
        return self.fetch_one(query, (userId,))
    
    def set(self ):
        self.reported_mobile_id_v = self.get_reported_mobile_id(self.userId)
        self.other_report_id_v = self.get_other_report_id(self.userId)
        self.reported_laptop_id =self.get_reported_laptop_id(self.userId)
        q = "select id from reporttable where userId = %s"
        self.cursor.execute(q,(self.userId,))
        report_id = self.cursor.fetchone()
        print(report_id)

        if report_id is None:
            self.insert_report_table(self.userId, reported_laptop_id=self.reported_laptop_id, reported_mobile_id=self.reported_mobile_id_v, other_report_id=self.other_report_id_v)
        else:
            self.update_reporttable(self.userId, reported_laptop_id=self.reported_laptop_id, reported_mobile_id=self.reported_mobile_id_v, other_report_id=self.other_report_id_v)


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

    def checkForRegister_Report(self, category, myid, Brand, model, color, operating_system, serial_number):
            print("Enter")
            attributes = {
        'Brand': Brand,
        'model': model,
        'color': color,
        'operating_system': operating_system,
        'serial_number': serial_number
        }
            identity = None
            if category == 'mobile_table':
                identity = 'imei_number'
            elif category == 'laptop_table':
                identity = 'serial_number'
            elif category == 'other_data':
                category = 'other_data_table'
            try:
                if serial_number is not None:
                    print("if")
                    query = f"SELECT userId,securityQ1,Q1Ans,securityQ2,Q2Ans FROM {category} WHERE Brand = %s AND model = %s AND color = %s AND operating_system = %s AND {identity} = %s"
                    data = (Brand, model, color, operating_system, serial_number)
                else:
                    print("else")
                    query = f"SELECT userId,securityQ1,Q1Ans,securityQ2,Q2Ans FROM {category} WHERE Brand = %s AND model = %s AND color = %s AND operating_system = %s"
                    data = (Brand, model, color, operating_system)

                self.cursor.execute(query, data)
                result = self.cursor.fetchone()
                print(result)
                if result:
                    print("victim")
                    victim = self.getMydata((result[0],))
                    myData = self.getMydata((myid,))
                    subject = f"FoundMate"
                    content = f'''
Thank you so much for Reporting and being a HERO 
Contact Details of the lost item owner:
Email : {victim[2]}
Mobile No : {victim[3]}
Security Question 1: {result[1]}
Answer: {result[2]}
Security Question 2: {result[3]}
Answer: {result[4]}
Please Contact {victim[1]} for item recovery by asking security questions
                    '''
                    sendEmail(myData[2], subject, content)
                    print(victim)
                    self.msg.ShowMsg(f"Thank you so much {myData[1]} for your report\nwe have mailed you the contact details of the owner\nplease contact him/her\nand ask for security questions for item recovery")
                    return 'registered'
                else:
                    #  def calculate_similarity(self,table_data, query_data):
                    user_id = self.find_user_id(**attributes)
                    if user_id is not None:
                        return user_id
                    else:
                        return False
            except:
                print("hello")


    def check_others(self,userId,name,color,building,floor,room):
        data = (name,color)
        q = "select userId,securityQ1,Q1Ans,securityQ2,Q2Ans from other_data_table where name = %s AND color = %s"
        self.cursor.execute(q,data)
        r = self.cursor.fetchone()
        print(r)
        if r is not None:
            mydata = self.getMydata((userId,))
            owner = self.getMydata((r[0],))
            subject = ''' Report Matched!!!'''
            body = f'''
hey {mydata[1]} Thank you for your report
The contact Deatails of the owner of the lost item you found is :
Email : {owner[2]}
mobile number : {owner[3]}

Security Question:
{r[1]}
ANS :{r[2]}
{r[3]}
ANS :{r[4]}

Please ask these question to the owner before returning the item
'''
            sendEmail(mydata[2],subject,body)
            
            return True
    
    def other_data_report_insertion_check(self,myid,name,color,desc):
        
        data = (name,color,desc)
        query = "select userId from other_data_table where name = %s AND color = %s AND description = %s"
        self.cursor.execute(query,data)
        result = self.cursor.fetchone()
        print(result)
        if result:
            vitcum = self.getMydata(result)
            myData = self.getMydata((myid,))
            subject = f"{vitcum[1]} , we have found somthing"
            content = f'''
    {myData[1]} has found your lost item
    Contact Details:
    Email : {myData[2]}
    Mobile No : {myData[3]}
    Please Contact {myData[1]} for item recovery
                '''
            sendEmail(vitcum[2],subject,content)
            print(vitcum)
            return False
        else:
            return True

def get_user_input():
    Brand = 'HP'
    model = 'HP any'
    color = 'blue'
    operating_system = 'windows'
    unique_identification = 'sam is written on it'
    serial_number = '1234567890'
    return Brand, model, color, operating_system, unique_identification, serial_number

def get_mobile_input():
    Brand = 'Apple'
    model = 'iphone 20'
    color = 'gold'
    operating_system = 'IOS'
    imei_number = '123456789012345'
    unique_identification = 'sam is written on it'
    return Brand, model, color, operating_system, imei_number, unique_identification

def get_other_report_input():
    name = 'bag'
    description = 'sam is written on it'
    color = 'blue'
    return name, description, color

if __name__ == '__main__':
    

    self = DatabaseManager(1)
    # self.connect()

    # Brand, model, color, operating_system, unique_identification, serial_number = get_user_input()
    # self.insert_reported_laptop(Brand, model, color, operating_system, unique_identification, serial_number, userId=1,building_name = 'old building',floor ='7',room = '7')

    # Brand, model, color, operating_system, imei_number, unique_identification = get_mobile_input()
    # self.insert_reported_mobile(Brand, model, color, operating_system, imei_number, unique_identification, userId=1,building_name = 'old building',floor ='7',room = '7')

    # name, description, color = get_other_report_input()
    # self.insert_other_report(name, description, color, userId=1,building_name = 'old building',floor ='7',room = '7')

    
    # self.set()
    # self.checkForRegister_Report(category='mobile_table' ,myid = 1 ,Brand = 'Samsung',model = 'Galaxy S20',color = 'Black',operating_system = 'Android',serial_number ='123456789012345' )
    self.location_match(myid=2,building = "Old building",floor = "10th Floor",room = "1",color = "black",category = "laptop")
    #   1 | laptop   | Old building  | 10th Floor | 1    | black | sam is written on it
    self.disconnect()
   