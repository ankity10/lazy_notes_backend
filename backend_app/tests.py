from unittest import TestCase
from db import Db
# Create your tests here.

class DbTest(TestCase):

	def setup(self):
		self.db = Db()

	def tearDown(self):
		del self.db

	def test_get_collection_names(self):
		self.collection_names = ['test_collection1', 'test_collection2']
		for collection in self.collection_names:
			self.db[collection].insert({'test': "text just for testing"})
		
		collection_names = db.get_collection_names()
		self.assertEqual(collection_names, self.collection_names)

		for collection in self.collection_names:
			self.db[collection].drop()