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
from backend_app.models import *

DEBUG = True


def dprint(text):
	text = str(text)
	if DEBUG:
		from colorama import init, Fore, Style
		init(autoreset=True)
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
			db_name = db
		self.db = self.db_client[db_name]

	def __del__(self):
		try:
			self.db_client.close()
		except Exception as e:
			print(e)

	def get_collection_names(self):
		try:
			return (self.db.collection_names())
		except Exception as e:
			print(e)

	def disconnect(self):
		self.__del__()

	def is_collection_present(self, collection_name):
		return collection_name in self.get_collection_names()

	def insert_note(self, username, note):
		try:
			self.db[username + "_notes"].insert_one(note)
			print("Note inserted successfully")
		except Exception as e:
			print(e)

	def update_note(self, username, client_id, note):
		try:
			self.db[username + "_notes"].find_one_and_replace({'note_hash': note['note_hash']}, note)
			print("Note updated successfully")
		except Exception as e:
			print(e)

	def read_note(self, username, note_hash):
		try:
			return self.db[username + "_notes"].find_one({'note_hash': note_hash})
		except Exception as e:
			print(e)

	def is_log_present(self, username, note_hash, from_client_id, to_client_id):
		try:
			return (self.db[username + "_notes"].find_one({
										'to_client_id': to_client_id, 
										'from_client_id': from_client_id,
										'note_hash': note_hash }) is not None)
		except Exception as e:
			print(e)

	def insert_log(self, username, log):
		try:
			self.db[username + "_logs"].insert_one(dict(log))
			print("Log inserted successfully!")
		except Exception as e:
			print(e)

	def read_logs(self, username, client_id):
		try:
			return self.db[username + "_logs"].find({'to_client_id': client_id})

		except Exception as e:
			print(e)

	def delete_log(self, username, to_client_id, from_client_id, note_hash):
		try:
			self.db[username + "_logs"].find_one_and_delete({
										'to_client_id': client_id, 
										'from_client_id': from_client_id,
										'note_hash': note_hash })
			print("Log deleted successfully!")
		except Exception as e:
			print(e)

def get_clients(username):
	clients = Clients.objects.filter(username=username)
	print(list(clients))
