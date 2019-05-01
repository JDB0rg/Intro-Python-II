# Implement a class to hold room information. This should have name and
# description attributes.
class Room():
    def __init__(self, name, description)
        self.name = name 
        self.description = description
        self.room_storage = []
        self.in_room = False
        
    def add_items(self, item):
        self.room_storage.append(item)

    