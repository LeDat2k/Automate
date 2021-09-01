import os, time, simplenote

sourceFile = 'D:\\znote.txt'

user = 'hsddung92.lpdat@gmail.com'
password = 'LinD2018'

sn = simplenote.Simplenote(user, password)

# sn.get_note_list(data=True, since=cursor, tags=[])  # Supports optional `tags` parameter that takes a list of tags
                                                    # to return only notes that contain at least one of these tags.
                                                    # Also supports a `since` parameter, but as per the Simperium
                                                    # API this is no longer a date, rather a cursor.
                                                    # Lastly, also supports a  `data` parameter (defaults to True)
                                                    # to only return keys/ids and versions

# sn.get_note(note_id)                                # note id is value of key `key` in note dict as returned
                                                    # by get_note_list. Supports optional version integer as
                                                    # argument to return previous versions

# sn.add_note(note)                                   # A ``note`` object is a dictionary with at least a
                                                    # ``content`` property, containing the note text.

# sn.update_note(note)                                # The ``update_note`` method needs a note object which
                                                    # also has a ``key`` property.
# sn.trash_note(note_id)

# simplenote.delete_note(note_id)

if __name__ == '__main__':
	# note = sn.get_note_list(data=True, since=cursor, tags=['test'])
	note_list = sn.get_note_list(data=True, tags=['test'])
	# note = sn.get_note_list(data=False, tags=['test'])
	print(note_list[0]["key"])
	note = sn.get_note('12846956-5135-48e9-8b49-6d0d5864fb5d',version=12)
	print(note)

	# https://simplenotepy.readthedocs.io/en/latest/index.html

