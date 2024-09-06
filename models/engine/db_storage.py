#!/usr/bin/python3
"""
    This Model contains the DataBase Storage Engine
"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

class DBStorage:
    """
        This is the Database Storage CLass

        Attributes:
            user: the user
            password: the password
            host: the host
            db: the database
            dialect: the dialect
            driver: the driver
    """
    __engine = ""
    __session = ""

    def __init__(self):
        """
            This is the initialization of the DBstorage
        """
        user = getenv('S_MYSQL_USER')
        password = getenv('S_MYSQL_PWD')
        host = getenv('S_MYSQL_HOST')
        db = getenv('S_MYSQL_DB')
        dialect = 'mysql'
        driver = 'mysqldb'
        self.__engine = create_engine("{}+{}://{}:{}@{}/{}"
                                      .format(dialect, driver, user, password,
                                              host, db), pool_pre_pind=True)
        
    def add(self, cls=None):
        """
            Query on the current database session all objects
            depending of the class name argumnets.

            Attributes:
                cls: the class
                if cls=None: 
        """

    def new(self, obj):
        """
            This function adds an object to the current database session

            Argument:
                obj: the object to be added
        """

    def save(self):
        """
            This function commits all the changes of the database session

            Argument:
                None
        """

    def delete(self, obj=None):
        """
            This function delete and object from the current session

            Argument:
                obj: the object to be removed

            if obj is None: nothing is removed
        """
    
    def reload(self):
        """
            Create all tables in the database and the current database session
            from the engine.
        """

    def close(self):
        """Close the working SQLAlchemy session."""