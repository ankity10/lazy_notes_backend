# This file is an interface between python and mongodb
# required queries:
	
# 	db.connect()
# 	db.disconnect()

# 	db.create_collection("collection_name")
# 	db.is_collection_present("collection_name")
# 	db.insert_log(username, client_id, log[note_hash])
# 	db.read_log(username, client_id)
# 	db.delete_log(username, client_id, note_hash)
# 	db.insert_note(username, note, client_id)
# 	db.update_note(username, note, client_id)
# 	db.read_note(username, note_hash)
import pymongo

DEBUG = True
if DEBUG:
	from colorama import init, Fore, Style
	init(autoreset=True)
else:
	def 

def dprint(text):
	if DEBUG:
		print(Fore.RED + Style.BRIGHT 
			  + text)
	else:
		print(text)

class Db:

	DB_NAME = "online_db"
	HOST = "localhost"
	PORT = 27017

	def __init__(self, db=None):
		self.db_client = pymongo.MongoClient(host=Db.HOST,
											 port=Db.PORT,
											 connectTimeoutMS=10000, 
											 serverSelectionTimeoutMS=8000)
		try:
			self.db_client.admin.command('ismaster')	
			print("Connected to database....!!")
		except pymongo.errors.ConnectionFailure:
			dprint("Could not connect to MongoDB")
			dprint("Application startup cannot proceed. Apllication is exiting.")
			dprint("Please check your mongoDB connection and try again.")
			exit()
		if db==None:
			db_name = Db.DB_NAME
		else:
			db_name = 
		self.db = self.db_client[db_name]

	def __del__(self):
		try:
			self.db_client.close()
		except Exception as e:
			dprint(e)

	def get_collection_names(self):
		try:
			return (self.db.collection_names())
		except Exception as e:
			dprint(e)

	def discconect(self):
		self.__del__()

	def is_collection_present(self, collection_name):
		return collection_name in self.get_collection_names()

	def insert_note(self, username, client_id, note):
		try:
			self.db[username + "_notes"].insert_one(note)
			print("Note inserted successfully")
		except Exception as e:
			dprint(e)

	def update_note(self, username, client_id, note):
		try:
			self.db[username + "_notes"].find_one_and_replace({'note_hash': note['note_hash']}, note)
			print("Note updated successfully")
		except Exception as e:
			dprint(e)

	def read_note(self, username, note_hash):
		try:
			return self.db[username + "_notes"].find_one({'note_hash': note_hash})
		except Exception as e:
			dprint(e)

	def insert_log(self, username, log):
		try:
			self.db[username + "_logs"].insert_one(dict(log))
			print("Log inserted successfully!")
		except Exception as e:
			dprint(e)

	def read_log(self, username, client_id):
		try:
			return self.db[username + "_logs"].find_one({'client_id': client_id})
		except Exception as e:
			dprint(e)

	def delete_log(self, username, client_id, note_hash):
		try:
			self.db[username + "_logs"].find_one_and_delete({'client_id': client_id, 'note_hash': note_hash})
			print("Log deleted successfully!")
		except Exception as e:
			dprint(e)