import os, glob

#pathlib
print("\nカレントディレクトリの取得")
print(os.getcwd()) 

print("\n絶対パスの取得")
print(os.path.abspath('./README.md')) 

print("\n相対パスの取得")
print(os.path.relpath('./README.md')) 

print("\nパスを生成")
path = os.path.join(os.getcwd(), 'file_name.txt')
print(path)

print("\nパスをhead部とtail部分離する")
print(os.path.split(path))
print(os.path.split(os.getcwd()))


#glob & Wildcard
print('\n全てのファイルを取得')
print(glob.glob('*'))

print('\n全てのファイルを絶対パスで取得')
globArg = os.path.join(os.getcwd(), '*')
print(glob.glob(globArg))

print('\n任意の拡張子のファイルを習得')
print(glob.glob('*.py'))

print('\n任意の文字列から始まるファイル名を取得')
print(glob.glob('__*'))





