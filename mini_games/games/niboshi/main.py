from . import game_window
import random

WINDOW_HEIGHT = 12
WINDOW_WIDTH = 60
KEY_TIMEOUT = 250 # にぼしリールの秒数にもなっている

class Niboshi:
    def __init__(self, _window):
        self.window = _window
        self.half_height = 4
        self.width = 20
        self.upper_ascii_art = ['　　　　　　/＞', '       　 ／/', '　　　　／ﾐﾉ', '　　 ＿/@)ﾂ']
        self.lower_ascii_art = ['　 ／@/￣', '　/ﾐシ', '_/／', 'Ｖ']
        self.set_pos(0, random.randint(0, 2))

    def set_pos(self, _upper_pos=-1, _lower_pos=-1):
        if _upper_pos >= 0:
            self.upper_pos = _upper_pos

        if _lower_pos >= 0:
            self.lower_pos = _lower_pos

    def add_upper_niboshi(self, pos):
        self.window.add_ascii_art(0+1, self.width*pos+2, self.upper_ascii_art)

    def add_lower_niboshi(self, pos):
        self.window.add_ascii_art(self.half_height+1, self.width*pos+2, self.lower_ascii_art)

    def add_niboshi(self):
        self.add_upper_niboshi(self.upper_pos)
        self.add_lower_niboshi(self.lower_pos)

    def move_upper_niboshi(self, pos):
        self.set_pos((niboshi.upper_pos + 1) % 3)

    def print_docking_result(self):
        row = 11
        column = 43
        if self.upper_pos == self.lower_pos:
            self.window.blink_string(row, column, "ﾄﾞｯｷﾝｸﾞ にぼし")
        else:
            self.window.print_string_and_block(row, column, "ﾉｰ ﾄﾞｯｷﾝｸﾞ にぼし")

def game(stdscr):
    # ゲームウィンドウの初期化
    window = game_window.GameWindow(WINDOW_HEIGHT+2, WINDOW_WIDTH+2, KEY_TIMEOUT)

    # にぼしの初期化
    niboshi = Niboshi(window)

    # にぼしを描画予定に追加
    niboshi.add_niboshi()

    # ゲームスタート
    while(1):
        # 画面描画
        window.refresh()

        # キー入力受付
        ch = window.getch()
        if ch != -1:
            # 何らかのキーを押してにぼしリールストップ
            break

        # 画面クリア
        window.clear()

        # にぼしの上半分を移動
        niboshi.set_pos((niboshi.upper_pos + 1) % 3)
        niboshi.add_niboshi()

    # 結果を表示　何かキーを押して終了
    niboshi.print_docking_result()

def main(args):
    game_window.wrapper(game) # おまじない

if __name__ == '__main__':
    main()
