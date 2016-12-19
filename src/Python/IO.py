""" This module containts the save and load functionality of the phonebook

"""

__author__ = "6345060: Nico Kotlenga"
__copyright__ = "Copyright 2016 – EPR-Goethe-Uni"
__email__ = "nico.kotlenga@stud.uni-frankfurt.de"

class FileManager:
    """ This class has methods to open and write phonebook save states

    """
    def load(self, path):
        """ This method will load a phonebook. The path contains the path to
            the file. If the file doesn't exist it will return None

        """
        curFile = open(path, "r")
        if(curFile != None):
            
        return None
    def save(self, path, cur_entries):
        """ This method will save the phonebook into the path. It will return
            a boolean value which describes if the process was successfull

        """
        pass
