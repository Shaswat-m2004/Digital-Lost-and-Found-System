import mysql.connector
class MysqlTables:
    def __init__(self):
        self.cursor = None
        self.connection = None
        self.host = 'localhost'
        self.user = 'root'
        self.password = ''
        self.database = 'foundmate'

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
            # Handle the error or raise it to handle at a higher level


    def create_all_table(self):
        self.get_connected()
        self.cursor.execute('''
CREATE DATABASE IF NOT EXISTS foundmate;

USE foundmate;

CREATE TABLE IF NOT EXISTS register (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    mobile VARCHAR(15) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    product_id VARCHAR(7) NOT NULL UNIQUE,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS laptop_table (
    id INT NOT NULL AUTO_INCREMENT,
    userId INT,
    Brand VARCHAR(255),
    model VARCHAR(255),
    color VARCHAR(50),
    operating_system VARCHAR(100),
    securityQ1 VARCHAR(255),
    Q1Ans VARCHAR(255),
    securityQ2 VARCHAR(255),
    Q2Ans VARCHAR(255),
    serial_number VARCHAR(100),
    PRIMARY KEY (id),
    FOREIGN KEY (userId) REFERENCES register(id)
);

CREATE TABLE IF NOT EXISTS mobile_table (
    id INT NOT NULL AUTO_INCREMENT,
    userId INT,
    Brand VARCHAR(255),
    model VARCHAR(255),
    color VARCHAR(50),
    operating_system VARCHAR(100),
    securityQ1 VARCHAR(255),
    Q1Ans VARCHAR(255),
    securityQ2 VARCHAR(255),
    Q2Ans VARCHAR(255),
    imei_number VARCHAR(100),
    PRIMARY KEY (id),
    FOREIGN KEY (userId) REFERENCES register(id)
);

CREATE TABLE IF NOT EXISTS other_data_table (
    id INT NOT NULL AUTO_INCREMENT,
    userId INT,
    name VARCHAR(255),
    color VARCHAR(50),
    securityQ1 VARCHAR(255),
    Q1Ans VARCHAR(255),
    securityQ2 VARCHAR(255),
    Q2Ans VARCHAR(255),
    PRIMARY KEY (id),
    FOREIGN KEY (userId) REFERENCES register(id)
);

CREATE TABLE IF NOT EXISTS reported_laptop (
    id INT NOT NULL AUTO_INCREMENT,
    userId INT,
    Brand VARCHAR(255),
    model VARCHAR(255),
    color VARCHAR(100),
    operating_system VARCHAR(100),
    serial_number VARCHAR(100),
    building_name VARCHAR(255) NOT NULL,
    floor VARCHAR(255) NOT NULL,
    room VARCHAR(255) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (userId) REFERENCES register(id)
);

CREATE TABLE IF NOT EXISTS reported_mobile (
    id INT NOT NULL AUTO_INCREMENT,
    userId INT,
    Brand VARCHAR(255),
    model VARCHAR(255),
    color VARCHAR(100),
    operating_system VARCHAR(100),
    imei_number VARCHAR(100),
    building_name VARCHAR(255) NOT NULL,
    floor VARCHAR(255) NOT NULL,
    room VARCHAR(255) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (userId) REFERENCES register(id)
);

CREATE TABLE IF NOT EXISTS other_reports (
    id INT NOT NULL AUTO_INCREMENT,
    userId INT,
    name VARCHAR(255),
    description TEXT,
    color VARCHAR(100),
    building_name VARCHAR(255) NOT NULL,
    floor VARCHAR(255) NOT NULL,
    room VARCHAR(255) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (userId) REFERENCES register(id)
);

CREATE TABLE IF NOT EXISTS registerdevices (
    id INT NOT NULL AUTO_INCREMENT,
    userId INT,
    laptop_id INT,
    mobile_id INT,
    other_id INT,
    PRIMARY KEY (id),
    FOREIGN KEY (userId) REFERENCES register(id),
    FOREIGN KEY (laptop_id) REFERENCES laptop_table(id),
    FOREIGN KEY (mobile_id) REFERENCES mobile_table(id),
    FOREIGN KEY (other_id) REFERENCES other_data_table(id)
);

CREATE TABLE IF NOT EXISTS reporttable (
    id INT NOT NULL AUTO_INCREMENT,
    userId INT,
    reported_laptop_id INT,
    reported_mobile_id INT,
    other_report_id INT,
    PRIMARY KEY (id),
    FOREIGN KEY (userId) REFERENCES register(id),
    FOREIGN KEY (reported_laptop_id) REFERENCES reported_laptop(id),
    FOREIGN KEY (reported_mobile_id) REFERENCES reported_mobile(id),
    FOREIGN KEY (other_report_id) REFERENCES other_reports(id)
);

CREATE TABLE IF NOT EXISTS requesttable (
    id INT NOT NULL AUTO_INCREMENT,
    userId INT,
    registered_device_id INT,
    category VARCHAR(255) NOT NULL,
    building_name VARCHAR(255) NOT NULL,
    floor VARCHAR(255) NOT NULL,
    room VARCHAR(255) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (userId) REFERENCES register(id),
    FOREIGN KEY (registered_device_id) REFERENCES registerdevices(id)
);

CREATE TABLE IF NOT EXISTS requesttable_unregistered (
    id INT NOT NULL AUTO_INCREMENT,
    userId INT,
    category VARCHAR(255) NOT NULL,
    building_name VARCHAR(255) NOT NULL,
    floor VARCHAR(255) NOT NULL,
    room VARCHAR(255) NOT NULL,
    color VARCHAR(100),
    description TEXT,
    PRIMARY KEY (id),
    FOREIGN KEY (userId) REFERENCES register(id)
);

ALTER TABLE reported_laptop
ADD FOREIGN KEY (userId) REFERENCES register(id);

        ''')

