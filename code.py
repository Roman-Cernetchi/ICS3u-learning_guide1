#!/usr/bin/env python3

# Created by: Roman Cernetchi
# Created on: November 2020
# This is a "Hello, World!" program on Pybadge

import ugame
import stage


def game_scene():
    # this function shows hello world on Pybadge

    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    background = stage.Grid(image_bank_background, 10, 8)

    game = stage.Stage(ugame.display, 60)
    game.layers = [background]
    game.render_block()

    while True:
        # repeat forever, or you turn it off
        pass # just a placeholder for now


if __name__ == "__main__":
    game_scene()