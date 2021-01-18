from datetime import datetime


def main(args):
    print('これはゲームサンプル2です')
    print('今日は何日か当ててください。\n')

    while True:
        day = input('今日は何日ですか？ > ')
        try:
            day = int(day)
        except ValueError:
            continue

        now = datetime.now()
        if now.day == day:
            print('正解！')
            break
        else:
            print('はずれです。')
