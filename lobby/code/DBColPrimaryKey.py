from code.DBCol import DBCol

class DBColPrimaryKey(DBCol):
	def __init__(self,
			  _name,
			  _type):
		super(DBColPrimaryKey, self).__init__(_name,
										      _type)

	def build_create_table_col_def(self):
		return "%s %s" % (super(DBColPrimaryKey, self).build_create_table_col_def(), "PRIMARY KEY")