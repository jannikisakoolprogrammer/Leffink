from code.DBCol import DBCol

from code.configs import database_col_types

class DBColAuto(DBCol):
	def __init__(self,
				 _name):
		super(DBColAuto, self).__init__(_name,
										database_col_types.INTEGER)

	def build_create_table_col_def(self):
		return "%s %s" % (super(DBCol, self).build_create_table_col_def(), "AUTOINCREMENT")