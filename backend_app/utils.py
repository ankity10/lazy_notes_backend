import .db
# this file will have all the functional code

class log:
    def __init__(self, note_hash, note_text, from_client_id, to_client_id):
        self.note_hash = note_hash
        self.note_text = note_text
        self.from_client_id = from_client_id
        self.to_client_id = to_client_id

    def __iter__(self):
        for key in self.__dict__:
            yield(key, self.__dict__[key]) 

db_obj = db.Db()

def insert_notes(username, note_hash, note_text, from_client_id, window_title, process_name):
    to_clients = all_clients = db_obj.get_clients(username)
    to_clients.remove(from_client_id)
    #Updating logs
    for to_client_id in to_clients:
        new_log = log(note_hash, note_text, from_client_id, to_client_id)
        if(db_obj.is_log_present(username, 
                                 note_hash, 
                                 from_client_id, 
                                 to_client_id)):
            db_obj.update_log(username, dict(new_log))
        else:
            db_obj.insert_log(username, dict(new_log))
    #Updating Notes
    notes_dict = read_note(username, note_hash) 
    if(notes_dict == None): #Note not present
        client = {from_client_id: note_text}
        notes_dict = {'note_hash': note_hash, 
                      'client': client, 
                      'window_title': window_title, 
                      'process_name': process_name}
        db_obj.insert_note(username, notes_dict)
    else: #Note is present
        notes_dict['client'][from_client_id] = note_text
        db_obj.update_note(username, notes_dict)

def resolve_merge_conflict(username, note_hash, from_client_id, note_text, window_title, process_name):
    to_clients = all_clients = db_obj.get_clients(username)
    to_clients.remove(from_client_id)
    #Updating logs
    for from_client in all_clients:
        for to_client in all_clients:
            if from_client != to_client:
                if(db_obj.is_log_present(username, 
                                         note_hash, 
                                         from_client, 
                                         to_client)):
                    db_obj.delete_log(username, note_hash, from_client, to_client)
    for to_client in to_clients:
        new_log = log(note_hash, note_text, from_client_id, to_client)
        db_obj.insert_log(dict(new_log))
    #Updating Notes
    notes_dict = read_note(username, note_hash)
    client = {from_client_id: note_text}
    new_note_dict = {'note_hash': note_hash,
                     'client': client,
                     'window_title': window_title,
                     'process_name': process_name}
    if(notes_dict == None): #Note not present
        db_obj.insert_note(username, notes_dict)
    else:
        db_obj.update_note(username, notes_dict)
