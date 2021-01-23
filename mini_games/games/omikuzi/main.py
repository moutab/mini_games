import random

def daikichi():
    print('\033[33m'+ "    =    ")
    print('\033[33m'+ "    =    ")
    print('\033[33m'+ "=========")
    print('\033[33m'+ "    =    ")
    print('\033[33m'+ "    =    ")
    print('\033[33m'+ "   = =   ")
    print('\033[33m'+ "  =   =  ")
    print('\033[33m'+ "=       =")
    print('\033[33m'+ "    =    ")
    print('\033[33m'+ "=========")
    print('\033[33m'+ "    =    ")
    print('\033[33m'+ " ======= ")
    print('\033[33m'+ "         ")
    print('\033[33m'+ " ======= ")
    print('\033[33m'+ " =     = ")
    print('\033[33m'+ " =     = ")
    print('\033[33m'+ " ======= ")
    print ( '\033[33m'+"大吉です。良かったですね"+'\033[0m')

def kichi():
    print('\033[32m'+ "    =    ")
    print('\033[32m'+ "=========")
    print('\033[32m'+ "    =    ")
    print('\033[32m'+ " ======= ")
    print('\033[32m'+ "         ")
    print('\033[32m'+ " ======= ")
    print('\033[32m'+ " =     = ")
    print('\033[32m'+ " =     = ")
    print('\033[32m'+ " ======= ")
    print ( '\033[32m'+"吉です。普通っすね。"+'\033[0m')

def kyou():
    print('\033[31m'+ "==   ==")
    print('\033[31m'+ "= = = =")
    print('\033[31m'+ "=  =  =")
    print('\033[31m'+ "= = = =")
    print('\033[31m'+ "=======")
    print ( '\033[31m'+"凶です。ということでこの後の文字の色が赤色になります。色を戻したいときはもう一度おみくじを引いて凶以外を出してね")

def main(args):
    print("Enterキーを押すことでおみくじが始まります。\n")
    input("Enterキーを押しておみくじを始める")

    result = random.randrange(1, 100)

    if result % 2 == 0: 
        kichi()
    elif result % 7 == 0: 
        daikichi()
    else:
       kyou()
