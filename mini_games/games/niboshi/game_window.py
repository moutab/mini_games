import time
import curses

# 画面後処理のラッパ
def wrapper(func):
    curses.wrapper(func)

class GameWindow:
    def __init__(self, h, w, _timeout_ms):
        self.window = curses.newwin(h, w, 0, 0)
        curses.noecho() # キーボード入力を画面に出力しない
        curses.curs_set(0) # 画面にカーソルを表示しない
        self.window.keypad(1) # キー入力を受け付ける
        self.window.border(0) # ゲームウィンドウに枠を付ける
        self.window.timeout(_timeout_ms) # getch()によるキー入力の待ち時間(ミリ秒) 負の数だとずっと待つ、タイムアウトしたら、getchは-1を返す
        self.timeout = _timeout_ms
        self.color_id = 1

    # 画面クリア
    def clear(self):
        self.window.clear()
        self.window.border(0)

    # 画面描画
    def refresh(self):
        self.window.refresh()

    # キーボード入力受付け
    def getch(self):
        return self.window.getch()

    # 1行を描画予定に追加
    def add_string(self, row, column, string, color_ch=curses.COLOR_WHITE, color_bg=curses.COLOR_BLACK):
        curses.init_pair(self.color_id, color_ch, color_bg) # カラーIDを毎回割り当てているが、効率などの問題が起きないか？
        self.window.addstr(row, column, string, curses.color_pair(self.color_id))
        self.color_id += 1

    # strの配列描画予定に追加
    def add_ascii_art(self, row, column, ascii_art):
        i = 0
        for string in ascii_art:
            self.add_string(row+i, column, string)
            i += 1

    # 1行を点滅させながら描画
    def blink_string(self, row, column, string, color_1=curses.COLOR_RED, color_2=curses.COLOR_CYAN, times=-1):
        i = 0
        colors = [color_1, color_2]
        while(1):
            # 画面描画
            self.add_string(row, column, string, colors[i%2])
            i += 1
            self.window.refresh()

            if(times <= 0):
                # timesが指定されなかった場合、キー入力を待つ
                self.window.timeout(500)
                ch = self.window.getch()
                if ch != -1:
                    self.window.timeout(self.timeout)
                    return ch
            else:
                # timesが指定された場合、その回数ループ
                time.sleep(0.5)
                if(i == times*2):
                    return 0

    # 1行を表示し、キー入力を待つ
    def print_string_and_block(self, row, column, string, color_ch=curses.COLOR_WHITE, color_bg=curses.COLOR_BLACK):
        self.add_string(row, column, string, color_ch, color_bg)
        self.window.refresh()
        self.window.timeout(-1)
        ch = self.window.getch()
        self.window.timeout(self.timeout)
        return ch
