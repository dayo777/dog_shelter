""" Define Error fields here """

# Missing required values
class Missing(Exception):
    def __init__(self, msg:str):
        self.msg = msg

# Duplicate values in the DB
class Duplicate(Exception):
    def __init__(self, msg:str):
        self.msg = msg

# Database errors
class Database(Exception):
    def __init__(self, msg: str):
        self.msg = msg

# Other errors
class Internal(Exception):
    def __init__(self, msg: str):
        self.msg = msg