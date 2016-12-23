""" This module contains the data classes  for the PhoneBook Project

"""

__author__ = "6345060: Nico Kotlenga, 6293280: Umut Yilmaz"
__copyright__ = "Copyright 2016 – EPR-Goethe-Uni"
__email__ = "nico.kotlenga@stud.uni-frankfurt.de"

from copy import deepcopy

class Entry:
    """ This class represents one phonebook entry. It's a data class with
        setter and getter methods for all attributes

    """

    def __init__(self, first_name, last_name, street, zipcode, city, phone):
        """ This method will be called to initilialize an object of this class

        """
        self.first_name = first_name
        self.last_name = last_name
        self.street = street
        self.zipcode = zipcode
        self.city = city
        self.phone = phone

    def get_first_name(self):
        """ This method will return the attribute first_name

        """

        return self.first_name

    def set_first_name(self, first_name):
        """ This method will change the attribute first_name

        """
        self.first_name = first_name

    def get_last_name(self):
        """ This method will return the last_name

        """
        return self.last_name

    def set_last_name(self, last_name):
        """ This method will change the attribute last_name

        """
        self.last_name = last_name

    def get_street(self):
        """ This method will return the street

        """
        return self.street

    def set_street(self, street):
        """ This method will change the attribute street

        """
        self.street = street

    def get_zipcode(self):
        """ This method will return the zipcode

        """
        return self.zipcode

    def set_zipcode(self, zipcode):
        """ This method will cahnge the attribute zipcode

        """
        self.zipcode = zipcode

    def get_city(self):
        """ This method will return the city

        """
        return self.city

    def set_city(self, city):
        """ This method will change the attribute city

        """
        self.city = city

    def get_phone(self):
        """ This method will return the phonenumber

        """
        return self.phone

    def set_phone(self, phone):
        """ This method will change the attribute phone

        """
        self.phone = phone

class PhoneBook:
    """ This class represents a phonebook. It has a list with all entries
        and contains methods for search, add, sort, delete and modify

    """

    def __init__(self, cur_book):
        """ This method will be called during the initialization process

        """
        if(cur_book == None):
            self.phonebook = list()
        else:
            self.phonebook = cur_book

    def add(self, first_name, last_name, street, zipcode, city, phone):
        """ This method adds an entry to the phonebook

        """
        self.phonebook.append(Entry(first_name, last_name, street, \
        zipcode, city, phone))

    def delete(self, index):
        """ This method deletes a phonebook entry

        """
        self.phonebook.remove(self.phonebook[index])

    def update(self, new_information, index):
        """ This method updates a phonebook entry

        """
        current_entry = self.phonebook[index]
        current_entry.set_first_name = new_information["firstName"]
        current_entry.set_last_name = new_information["lastName"]
        current_entry.set_street = new_information["street"]
        current_entry.set_city = new_information["city"]
        current_entry.set_zipcode = new_information["zipcode"]
        current_entry.set_phone = new_information["phone"]

    def search(self, searchKey):
        """ This method will search a specif phone entry. searchKey is a string
            which contains the search request
            As a return value there will be a list with all possible results

        """
        return_value = list()
        for cur_contact in self.phonebook:
            if(cur_contact.first_name in searchKey or \
            cur_contact.last_name in searchKey or \
            cur_contact.street in searchKey or \
            cur_contact.city in searchKey or \
            cur_contact.zipcode in searchKey or \
            cur_contact.phone in searchKey):
                return_value.append(cur_contact)
        return return_value
    def sort(self, sort_method):
        """ This method will search for a phonebook entry.
            The search_method parameter is an integer value which describes the
            column for searching.

            sort_method == 0 : first_name
            sort_method == 1 : last_name
            sort_method == 2 : street
            sort_method == 3 : city
            sort_method == 4 : zipcode
            sort_method == 5 : phone

            As a return value there will be a list with all results

        """
        return_value = deepcopy(self.phonebook)

        for i in range(0, len(self.phonebook), 1):
            for k in range(i + 1, len(self.phonebook), 1):
                for t in range(0, 3, 1):
                    if(sort_method == 0):
                        if(return_value[i].first_name[t] != \
                        return_value[k].first_name[t]):
                            if(return_value[i].first_name > \
                            return_value[k].first_name):
                                return_value[i], return_value[k] = \
                                return_value[k], return_value[i]
                    elif(sort_method == 1):
                        if(return_value[i].last_name[t] != \
                        return_value[k].last_name[t]):
                            if(return_value[i].last_name > \
                            return_value[k].last_name):
                                return_value[i], return_value[k] = \
                                return_value[k], return_value[i]
                    elif(sort_method == 2):
                        if(return_value[i].street[t] != \
                        return_value[k].street[t]):
                            if(return_value[i].street > \
                            return_value[k].street):
                                return_value[i], return_value[k] = \
                                return_value[k], return_value[i]
                    elif(sort_method == 3):
                        if(return_value[i].city[t] != \
                        return_value[k].city[t]):
                            if(return_value[i].city > \
                            return_value[k].city):
                                return_value[i], return_value[k] = \
                                return_value[k], return_value[i]
                    elif(sort_method == 4):
                        if(return_value[i].zipcode[t] != \
                        return_value[k].zipcode[t]):
                            if(return_value[i].zipcode > \
                            return_value[k].zipcode):
                                return_value[i], return_value[k] = \
                                return_value[k], return_value[i]
                    else:
                        if(return_value[i].phone[t] != \
                        return_value[k].phone[t]):
                            if(return_value[i].phone > \
                            return_value[k].phone):
                                return_value[i], return_value[k] = \
                                return_value[k], return_value[i]

""" TESTCASES

Testing Entry class

>>> new = Entry('Max', 'Mustermann', 'Musterstreet', '67349', 'Mustercity', '098234')

>>> new.get_first_name
<bound method Entry.get_first_name of <__main__.Entry object at 0x03E40F90>>
>>> new.get_last_name
<bound method Entry.get_last_name of <__main__.Entry object at 0x03E40F90>>
>>> new.get_phone
<bound method Entry.get_phone of <__main__.Entry object at 0x03E40F90>>
>>> new.get_street
<bound method Entry.get_street of <__main__.Entry object at 0x03E40F90>>
>>> new.get_zipcode
<bound method Entry.get_zipcode of <__main__.Entry object at 0x03E40F90>>

Testing setter method.

>>> new.set_first_name('Maximilian')
>>> new.first_name
'Maximilian'
>>> new.set_last_name('Mustermanno')
>>> new.last_name
'Mustermanno'
>>> new.set_street('Musterstreet12')
>>> new.street
'Musterstreet12'
>>> new.set_zipcode('007')
>>> new.zipcode
'007'
>>> new.set_city('Changedtown')
>>> new.city
'Changedtown'
>>> new.set_phone('911')
>>> new.phone
'911'

Testing PhoneBook class

#Creating new PhoneBook object new_pb

>>> new_pb = PhoneBook(None)
Given the parameter None the __init__ will create an empty list called cur_book

Adding Entry
>>> new_pb.add('Max', 'Mustermann', 'Musterstreet', '67349', 'Mustercity', '098234')
>>> new_pb.phonebook
[<__main__.Entry object at 0x03BD0D50>]

Removing Entry
>>> new_pb.delete(0)
deletes the first and only entry in this example, which leaves us with the empty list.
>>> new_pb.phonebook
[]


Update Entry
>>> new_pb.add('Max', 'Mustermann', 'Musterstreet', '67349', 'Mustercity', '098234')
>>> new_pb.phonebook
[<__main__.Entry object at 0x03BD0D50>]
>>> __main__.Entry.get_first_name
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    __main__.Entry.get_first_name
NameError: name '__main__' is not defined
>>> new_pb.update('Maximus', 0)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    new_pb.update('Maximus', 0)
  File "C:\Users\diego\Google Drive\CS\WS1617\EPR\EPR_Blatt5_Umut_Yilmaz\EPR_05_final\EPR_Phone_Book-master\EPR_Phone_Book-master\src\Python\logic.py", line 134, in update
    current_entry.set_first_name = new_information["firstName"]
TypeError: string indices must be integers


Search Entry
new_pb.search('Max')
[<__main__.Entry object at 0x03BD0D50>]


Sort Entry
>>> new_pb.add('Clark', 'Kent', 'Metrostreet', '0010', 'Metropolis', '098')
>>> new_pb.sort(0)
"""
