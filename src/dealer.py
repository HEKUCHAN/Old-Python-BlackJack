from .card import Card
from .player import Player
import time

class Dealer(Player):
    def set_Card(self, cards):
        self.cards = cards

    def is_more_17(self):
        total = Card.counter(self.cards)
        self.total = total

        return True if total >= 17 else False

    def show(self):
        total = Card.counter(self.cards)
        self.total = total

        print("ディーラーのカードは...")
        print(f"| {self.cards[0]} | © |", f"【{self.total}】")

        time.sleep(1)
    
    def show_all(self):
        total = Card.counter(self.cards)
        self.total = total

        print("ディーラーのカードは...")
        print(f"| " + " | ".join(self.cards) + " |", f"【{self.total}】")

        time.sleep(1)
