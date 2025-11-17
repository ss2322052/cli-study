import sys

if len(sys.argv) < 2:
    print("名前を入力してください")
else:
    name = sys.argv[1]
    print(f"Hello, {name}!")