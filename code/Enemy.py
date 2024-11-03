#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.is_going_down = True
        self.up_speed = ENTITY_SPEED.get(f'{self.name}UpSpeed', 0)
        self.down_speed = ENTITY_SPEED.get(f'{self.name}DownSpeed', 0)
        self.x_move = False
        if self.up_speed > 0 and self.down_speed > 0:
            self.x_move = True

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

        if self.x_move:
            if self.is_going_down:
                self.rect.centery += self.down_speed
                if self.rect.centery >= WIN_HEIGHT:
                    self.is_going_down = False
            else:
                self.rect.centery -= self.up_speed
                if self.rect.centery <= 0:
                    self.is_going_down = True

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
