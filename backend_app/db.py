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