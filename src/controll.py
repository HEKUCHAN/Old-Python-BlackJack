import shutil

class Controll():
    @staticmethod
    def get_input(word, num=False):
        """
        文字列と数値の入力を限定させる
        """
        ask = True
        attention = "数値" if num else "文字"

        while ask:
            input_hoge = input(word)

            if num and input_hoge.isdecimal():
                answer = int(input_hoge)
                break
            elif not num and not input_hoge.isdecimal():
                answer = input_hoge
                break
            else:
                print(f"\033[31m{attention}を入力してください！\033[0m")
        
        return answer

    @classmethod
    def gets_answer(cls, word, first=["Y","Yes"], second=["N", "No"]):
        ask = True
        while ask:
            input_word = cls.get_input(f"{word} {first[0]}/{second[0]}:")
            input_word = input_word.lower()

            if input_word == first[0].lower() or input_word == first[1].lower():
                return False
            if input_word == second[0].lower() or input_word == second[1].lower():
                return True
            else:
                print(f"\033[31m指定された文字を入力してください！\033[0m")

    @staticmethod
    def clear():
        terminal_size = shutil.get_terminal_size()
        print("\n" * terminal_size.lines)
