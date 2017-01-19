import .db
# this file willl have all the functional code

def index_route():
	return db.objects.all()