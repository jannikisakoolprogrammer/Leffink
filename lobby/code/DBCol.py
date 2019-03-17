class DBCol(object):
	"""Represents a column in a database table.

	This is used for creating tables.
	"""

	def __init__(self,
				 _name,
				 _type
	    ):
	    """Initialises an instance of this class.
		
	    """
	    self.name = _name
	    self.type = _type


	def build_create_table_col_def(self):
		"""Builds and returns the string to create this column inside a CREATE SQLite3 statement.
        
		"""
		return "%s %s" % (self.name, self.type)
