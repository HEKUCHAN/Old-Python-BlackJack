from .controll import Controll as Ctl
from .player import Player
from .dealer import Dealer
from .card import Card
import sys

class Game():
    def __init__(self):
        self.status = "Start"
        self.round = 0

    def Start(self, Card_list, player, dealer):
        self.status = "Start"
        
        if self.round == 0:
            answer = Ctl.gets_answer("ゲームを開始しますか？")
        
            if answer:
                print("ゲームを終了します。")
                sys.exit()
            else:
                Ctl.clear()
                print("ゲームが開始されました。")
                self.round += 1
                dealer.show()
                player.show()
        else:
            Ctl.clear()
            print("ゲームが開始されました。")
            dealer.show()
            player.show()

        if player.total == dealer.total and player.is_21():
            Ctl.clear()
            player.show()
            dealer.show_all()

            print("二人ともブラックジャック！！")
            print("引き分けです！")
            self.End()
        elif dealer.is_21():
            Ctl.clear()
            player.show()
            dealer.show_all()

            print("ブラックジャック！")
            print("ディーラーの勝ちです")
            self.End()
        elif player.is_21():
            Ctl.clear()
            player.show()
            dealer.show_all()
            
            print("ブラックジャック！")
            print("あなたの勝ち！")
            self.End()
        else:
            self.Next(Card_list, player, dealer)
    
    def Next(self, cards, player, dealer):
        answer = Ctl.gets_answer("HIT or STAND", ["H", "Hit"], ["S", "Stand"])

        if answer:
            self.Battle(cards, player, dealer)
        else:
            player.cards.append(cards.hit())
            player.show()

            if player.is_bust():
                print("バースト！")
                print("ディーラーの勝ち！")
                self.End()
            elif player.is_21():
                print("ブラックジャック")
                print("あなたの勝ち！")
                self.End()
            else:
                self.Next(cards, player, dealer)
        
    def Battle(self, cards, player, dealer):
        Ctl.clear()
        dealer.show_all()

        if dealer.is_more_17 and dealer.total > player.total:
            print("ディーラーの勝ち！")
            self.End()
        else:
            while True:
                dealer.cards.append(cards.hit())
                dealer.total = Card.counter(dealer.cards)
                dealer.show_all()

                if dealer.is_bust():
                    print("ディーラーがバーストした！")
                    print("あなたの勝ち！")
                    self.End()
                    break
                elif dealer.is_more_17:
                    if player.total == dealer.total:
                        print("引き分けです！")
                        player.show()
                        self.End()
                        break
                    elif dealer.is_21():
                        print("ブラックジャック！")
                        player.show()
                        self.End()
                        break
                    elif player.total > dealer.total:
                        print("あなたの勝ち！")
                        player.show()
                        self.End()
                        break
                    else:
                        print("ディーラーの勝ち！")
                        player.show()
                        self.End()
                        break
                else:
                    pass



    def End(self):
        self.status = "End"

        if Ctl.gets_answer("もう一度プレイしますか？"):
            sys.exit()
        else:
            Card_list = Card()
            player = Player(Card_list)
            dealer = Dealer(Card_list)
            self.Start(Card_list, player, dealer)
