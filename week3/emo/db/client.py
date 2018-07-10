# This file contains helper methods for communicating with the database

class Client(object):
    """ Helper class for interacting with the database
        param: database connection
    """
    def __init__(self, connection, *args):
        self.connection = connection

    def getItem(self, key):
        """ method for getting items from db  """
        result = self.connection.get(key)

        if result == 'nil':
            result = None

        return result

    def setItem(self, key, item):
        """ method for setting items in db """
        self.connection.set(key, item)
