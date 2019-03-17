import pygame
pygame.init()

from code.models.RegisterModel import RegisterModel
from code.configs import database
from code.DBTable import DBTable

dbtable_player = DBTable(database.TABLE_PLAYER,
                         database.TABLE_PLAYER_COL_DEFS)
dbtable_player.create()