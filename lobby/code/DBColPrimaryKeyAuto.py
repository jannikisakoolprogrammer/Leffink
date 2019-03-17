from code.DBColPrimaryKey import DBColPrimaryKey

class DBColPrimaryKeyAuto(DBColPrimaryKey):
	def __init__(self,
			  _name,
			  _type):
		super(DBColPrimaryKeyAuto, self).__init__(_name,
										   _type)

	def build_create_table_col_def(self):
		return "%s %s" % (super(DBColPrimaryKeyAuto, self).build_create_table_col_def(), "AUTOINCREMENT")