from code.DBCol import DBCol

class DBColForeignKey(DBCol):
    def __init__(self,
                 _name,
                 _type,
                 _fk_table,
                 _fk_col):
        super(DBColForeignKey, self).__init__(_name,
                                              _type)

        self.fk_table = _fk_table
        self.fk_col = _fk_col

    def build_create_table_col_def_fk(self):
        return "FOREIGN KEY (%s) REFERENCES %s(%s)" % (self.name,
                                                       self.fk_table,
                                                       self.fk_col)