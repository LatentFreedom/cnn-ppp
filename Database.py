# System
import os
from os.path import join, dirname
# Installed
import mysql.connector
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

class Database:

	def __init__(self):
		self.getConnection()

	def getConnection(self):
		self.connection = mysql.connector.connect(
		user=os.environ.get("DB_USER"),
		password=os.environ.get("DB_PASS"),
		database=os.environ.get("DB_NAME"),
        allow_local_infile=1,
		autocommit=True)

	def closeConnection(self):
		self.connection.close()
		self.cursor.close()

	def insert_record(self, table, record):
		placeholders = ', '.join(['%s'] * len(record))
		columns = ', '.join(record.keys())
		sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % (
			table, columns, placeholders)
		self.cursor = self.connection.cursor()
		self.cursor.execute(sql, list(record.values()))
