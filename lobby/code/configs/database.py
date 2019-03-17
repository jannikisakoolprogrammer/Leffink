from code.DBCol import DBCol
from code.DBColForeignKey import DBColForeignKey
from code.DBColPrimaryKey import DBColPrimaryKey
from code.DBColForeignKeyPrimaryKey import DBColForeignKeyPrimaryKey
from code.DBColPrimaryKeyAuto import DBColPrimaryKeyAuto
from code.DBColAuto import DBColAuto

from code.configs import database_col_types

# Name of the database.
DATABASE = "leffink.db"

# Table names.
TABLE_PLAYER = "player"
TABLE_PLAYER_COL_DEFS = (
    DBColPrimaryKeyAuto("id", database_col_types.INTEGER),
    DBCol("name", database_col_types.TEXT),
    DBCol("password", database_col_types.TEXT),
	DBColForeignKey("test", database_col_types.TEXT, "other_table", "other_table_test")
)
