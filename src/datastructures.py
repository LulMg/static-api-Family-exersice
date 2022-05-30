
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
        {
            "id": self._generateId(),
            "first_name": "John",
            "last_name": last_name,
            "Age": 33,
            "Lucky Numbers": [7, 13, 22]
        },
        {
            "id": self._generateId(),
            "first_name": "Jane",
            "last_name": last_name,
            "Age": 35,
            "Lucky Numbers": [10, 14, 3]
        },
        {
            "id": self._generateId(),
            "first_name": "Jimmy",
            "last_name": last_name,
            "Age": 5,
            "Lucky Numbers": [1]
        }   
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 999999999)

    def add_member(self, member):
        # fill this method and update the return
        member['id']=self._generateId()
        member['Last_name']=self.last_name
        self._members.append(member)

    def delete_member(self, id):
        # fill this method and update the return
        for position, member in enumerate(self._members):
            if member["id"]== int(id):
                result = self._members.pop(position)
                return self._members

    def get_member(self, id):
        # fill this method and update the return
        for x in self._members:
            if x["id"] == id:
                return x

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
