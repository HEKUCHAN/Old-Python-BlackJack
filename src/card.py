import random

class Card():
    def __init__(self):
        self.cards = [
            'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
            'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
            'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
            'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'
        ]

    def startDraw(self) -> list:
        """
        初期のカードを二枚渡してくれる。
        とても便利な関数さ
        """
        cards_length = len(self.cards) - 1

        first_card = self.cards[random.randrange(cards_length)]
        self.cards.remove(first_card)

        second_card = self.cards[random.randrange(cards_length)]
        self.cards.remove(second_card)

        return [
            first_card,
            second_card
        ]

    def hit(self) -> str:
        """
        cardsからランダムにカードを引いて帰り値として渡す関数
        """
        cards_length = len(self.cards) - 1
        random_num = random.randrange(cards_length)
        selected_card = self.cards[random_num]
        self.cards.remove(selected_card)

        return selected_card

    @staticmethod
    def counter(cards) -> int:
        """
        渡されたカードを計算してくれる
        """
        counter = 0

        for card in cards:
            if card == "A":
                counter += 11
            elif card.isdecimal():
                counter += int(card)
            else:
                counter += 10
        
        if counter > 21 and "A" in cards:
            for i in range(cards.count("A")):
                if counter <= 21:
                    break
                counter -= 10
        
        return counter

