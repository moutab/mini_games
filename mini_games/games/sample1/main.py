def main(args):
    print('これはゲームサンプル1です')
    print('正しくタイプしてください。\n')

    while True:
        cmd = input('"Exit"と正しくタイプしてください > ')
        if cmd == 'Exit':
            print('Good!')
            break
