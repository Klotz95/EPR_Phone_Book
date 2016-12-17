""" This module contains the data classes  for the PhoneBook Project

"""

__author__ = "6345060: Nico Kotlenga"
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

    def __init__(self):
        """ This method will be called during the initialization process

        """
        self.phonebook = list()

    def add(self, first_name, last_name, street, zipcode, city, phone):
        """ This method adds an entry to the phonebook

        """
        self.phonebook.append(new Entry(first_name, last_name, street, \
        zipcode, city, phone))

    def delete(self, index):
        """ This method deletes a phonebook entry

        """
        self.phonebook.remove(index)

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

    def search(self, search_method):
        """ This method will search for a phonebook entry.
            The search_method parameter is an integer value which describes the
            column for searching.

            search_method == 0 : first_name
            search_method == 1 : last_name
            search_method == 2 : street
            search_method == 3 : city
            search_method == 4 : zipcode
            search_method == 5 : phone

            As a return value there will be a list with all results

        """
        return_value = deepcopy(self.phonebook)

        for i in range(0, len(self.phonebook), 1):
            for k in range(i + 1, len(self.phonebook), 1):
                for t in range(0, 3, 1):
                    if(search_method == 0):
                        if(return_value[i].first_name[t] != \
                        return_value[k].first_name[t]):
                            if(return_value[i].first_name > \
                            return_value[k].first_name):
                                return_value[i], return_value[k] = \
                                return_value[k], return_value[i]
                    elif(search_method == 1):
                        if(return_value[i].last_name[t] != \
                        return_value[k].last_namet]):
                            if(return_value[i].last_name > \
                            return_value[k].last_name):
                                return_value[i], return_value[k] = \
                                return_value[k], return_value[i]
                    elif(search_method == 2):
                        if(return_value[i].street[t] != \
                        return_value[k].street[t]):
                            if(return_value[i].street > \
                            return_value[k].street):
                                return_value[i], return_value[k] = \
                                return_value[k], return_value[i]
                    elif(search_method == 3):
                        if(return_value[i].city[t] != \
                        return_value[k].city[t]):
                            if(return_value[i].city > \
                            return_value[k].city):
                                return_value[i], return_value[k] = \
                                return_value[k], return_value[i]
                    elif(search_method == 4):
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
