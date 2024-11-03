#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from typing import Literal

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
from code.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        current_level_number: Literal[1, 2, 3] = 1
        max_level = 3
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0]  # [Player1, Player2]
                while current_level_number <= max_level:
                    level = Level(self.window, f'Level{current_level_number}', menu_return, player_score, current_level_number)
                    level_return = level.run(player_score)

                    if level_return and current_level_number == max_level:
                        score.save(menu_return, player_score)
                    current_level_number += 1

            elif menu_return == MENU_OPTION[3]:
                score.show()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()  # Close Window
                quit()  # end pygame
            else:
                pygame.quit()
                sys.exit()
