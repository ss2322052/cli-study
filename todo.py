import sys
import json
import os

# sys… コマンドライン引数を使うためのモジュール
# json… タスクを保存するため（ファイルとやり取りするため）
# os… ファイルの存在確認に使う

FILENAME = "tasks.json"

# --------------------------------
# 1.タスクをファイルから読み込む関数定義
# --------------------------------
def load_tasks():
    # tasks.json がまだ存在しない場合（初回起動など）
    if not os.path.exists(FILENAME):
        #空のリストを返す
        return []
    
    # ファイルを開いて読み込む
    # encoding="utf-8" は日本語を扱うために必要
    with open(FILENAME, "r", encoding="utf-8") as f:
        # json形式をPythonのリストに戻す
        return json.load(f)

# ---------------------------
# 2.タスクをファイルに保存する関数
# ---------------------------
def save_tasks(tasks):
    # "w"は書き込みモード
    # indent=2 はファイルを読みやすく整形して保存してくれる
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

# ------------------------------------------------------
# ③ メイン処理（コマンドライン引数を読み取る）
# ------------------------------------------------------
def main():
    # sys.argv にはコマンドの引数が入る
    # sys.argv[0] → スクリプト名（todo.py）
    # sys.argv[1] → コマンド（add / list / done）
    # まず引数が足りているか確認
    if len(sys.argv) < 2:
        print("使い方　python todo.py [add/list/done] [内容]")
        return
    
    # コマンド名(add / list / done)を取り出す
    command = sys.argv[1]

    # 現在のタスク一覧を読み込む
    tasks = load_tasks()

    # --------------------------------------------------
    # add（タスク追加）
    # --------------------------------------------------
    if command == "add":
        # add の場合はタスクの内容に変更が必要
        if len(sys.argv) < 3:
            print("タスクの内容を入力してください")
            return
        
        # タスクに内容を取得
        task = sys.argv[2]

        # リストに追加
        tasks.append(task)

        # ファイルに保存
        save_tasks(tasks)

        print(f"{task} を追加しました")

if __name__ == "__main__":
    main()
