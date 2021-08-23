from .card import Card
from .controll import Controll as Ctl
from .player import Player
from .dealer import Dealer
from .game import Game

import time
import sys

def main():
    game = Game()
    Card_list = Card()
    player = Player(Card_list)
    dealer = Dealer(Card_list)
    game.Start(Card_list, player, dealer)
