from .card import Card
import time

class Player():
    def __init__(self, Cards):
        self.cards = Cards.startDraw()
        self.total = Card.counter(self.cards)

    def set_Card(self, cards):
        self.cards = cards
    
    def is_bust(self):
        total = Card.counter(self.cards)

        return total > 21
    
    def is_21(self):
        total = Card.counter(self.cards)
        self.total = total

        return self.total == 21

    def show(self):
        total = Card.counter(self.cards)
        self.total = total

        print("あなたのカードは...")
        print(f"| " + " | ".join(self.cards) + " |", f"【{self.total}】")

        time.sleep(1)
