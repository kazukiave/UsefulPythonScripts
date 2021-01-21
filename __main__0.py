
#Pythonスクリプトを直接実行した時には、そのスクリプトファイルは「__main__」という名前のモジュールとして認識されます。
def test_method():
    print('Hello World')

if __name__ == '__main__':
    test_method()
print('モジュール名: {}'.format(__name__))


#実行結果
"""
Hello World
モジュール名: __main__
"""

"""
直接Pythonスクリプトを実行すると
__name__ は__main__として認識されるため、test_methodが実行される
他からモジュールとしてインポートされたときは__name__が__main__0（ファイル名）として認識されるためtest_methodは実行されない
"""

