""" This module containts the save and load functionality of the phonebook

"""

__author__ = "6345060: Nico Kotlenga"
__copyright__ = "Copyright 2016 – EPR-Goethe-Uni"
__email__ = "nico.kotlenga@stud.uni-frankfurt.de"

import Entry from logic.py

class FileManager:
    """ This class has methods to open and write phonebook save states

    """
    def load(self, path):
        """ This method will load a phonebook. The path contains the path to
            the file. If the file doesn't exist it will return None

        """
        curFile = open(path, "r")
        if(curFile != None):
            listOfEntries = list()
            for line in curFile:
                # split the comoponents
                first_name = line.split("<first_name>")[0].split("</first_name">)[0]
                line = line.split("<first_name>")[0].split("</first_name>")[1]
                last_name = line.split("<last_name>")[0].split("</last_name>")[0]
                line = line.split("<last_name>")[0].split("</last_name>")[1]
                street = line.split("<street>")[0].split("</street>")[0]
                line = line.split("<street>")[0].split("</street>")[1]
                zipcode = line.split("<zipcode>")[0].split("</zipcode>")[0]
                line = line.split("<zipcode>")[0].split("</zipcode>")[1]
                city = line.split("<city>")[0].split("</city>")[0]
                line = line.split("<city>")[0].split("</city>")[1]
                phone = line.split("<phone>")[0].split("</phone>")[0]
                listOfEntries.append(new Entry(first_name, last_name, street, \
                zipcode, city, phone))
            curFile.close()
            return listOfEntries
        curFile.close()
        return None
    def save(self, path, cur_entries):
        """ This method will save the phonebook into the path. It will return
            a boolean value which describes if the process was successfull

        """

        cur_file = open(path, "w")
        for cur_entry in cur_entries:
            cur_file.write("<first_name>" + cur_entry.get_first_name() + \
            "</first_name><last_name>" + cur_entry.get_last_name() + \
            "</last_name><street>" + cur_entry.get_street() + "</street><zipcode>" + \
            cur_entry.get_zipcode() + "</zipcode><city>" + cur_entry.get_city() + \
            "</city><phone>" + cur_entry.get_phone())
        return False
