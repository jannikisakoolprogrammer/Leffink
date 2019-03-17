from code.DBCol import DBCol
from code.DBColAuto import DBColAuto
from code.DBColForeignKey import DBColForeignKey
from code.DBColForeignKeyPrimaryKey import DBColForeignKeyPrimaryKey
from code.DBColPrimaryKey import DBColPrimaryKey
from code.DBColPrimaryKeyAuto import DBColPrimaryKeyAuto

class DBTable(object):
    """Class that represents a table in a SQLite3 database.

    """
    def __init__(self,
                 _name,
                 _cols):
        self.name = _name
        self.cols = _cols

    def create(self):
        """Creates the table in the SQLite3 database.

        """
        # First we need to build the CREATE statement before we execute it.
        create_table_statement = "CREATE TABLE %s " % self.name
        create_table_col_statement = "(%s)"

        col_statements = []

        # We will iterate through all column definitions first and add those to the statement.
        # Later we will also add the foreign key relations to the statement.
        for c in self.cols:
            col_statements.append(c.build_create_table_col_def())

        # Now add the foreign key relations.
        for c in self.cols:
            if isinstance(c, DBColForeignKey) or isinstance(c, DBColForeignKeyPrimaryKey):
                col_statements.append(c.build_create_table_col_def_fk())

        print(', '.join(col_statements))