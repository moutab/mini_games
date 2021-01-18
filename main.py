from mini_games.routes import routes
import sys


def show_usage():
    """
    使い方を表示する
    """
    print('''ミニゲーム集です。

コマンド:

    show-all ... 登録されているゲーム名をすべて表示します。
    play     ... ゲーム名を指定するとそのゲームをプレイできます。

コマンドの使用例:
    
    $ # ゲーム名をすべて表示
    $ python main.py show-all

    $ # 特定のゲームをプレイ
    $ python main.py play sample1
''')     


def show_all_game_names():
    """
    すべてのゲームの名前を表示する
    """
    for name in routes.keys():
        print(name)


def play_game(args):
    """
    game_nameのゲームをプレイする
    """
    game_name = args[0]
    if game_name not in routes.keys():
        return

    game_main = routes[game_name]

    try:
        game_main(args)
    except (KeyboardInterrupt, EOFError):
        pass


def main():
    """
    メインルーチン
    """
    if len(sys.argv) < 2:
        return show_usage()

    cmd = sys.argv[1]
    if cmd == 'show-all':
        show_all_game_names()
    elif cmd == 'play':
        if len(sys.argv) < 3:
            return show_usage()

        play_game(sys.argv[2:])
    else:
        show_usage()


main()
