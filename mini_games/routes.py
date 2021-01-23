# 必要なモジュールをインポート
from mini_games.games.sample1.main import main as sample1_main
from mini_games.games.sample2.main import main as sample2_main
from mini_games.games.omikuzi.main import main as omikuzi_main
from mini_games.games.niboshi.main import main as niboshi_main

# ルート情報を表す辞書
# ゲーム名をキーに指定し、ゲームのエントリーポイントを値に設定
routes = {
    'sample1': sample1_main,
    'sample2': sample2_main,    
    'omikuzi': omikuzi_main,
    'niboshi': niboshi_main,
}
