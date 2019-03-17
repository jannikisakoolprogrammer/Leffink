from code.DBColPrimaryKey import DBColPrimaryKey

class DBColForeignKeyPrimaryKey(DBColPrimaryKey):
    def __init__(self,
                 _name,
                 _type,
                 _is_primary,
                 _fk_table,
                 _fk_col):
        super(DBColForeignKeyPrimaryKey, self).__init__(_name,
                                                     _type,
                                                     _is_primary)
    
    def build_create_table_col_def_fk(self):
        return "FOREIGN KEY (%s) REFERENCES %s(%s)" % (self.name,
                                                       self.fk_table,
                                                       self.fk_col)