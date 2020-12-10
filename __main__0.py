
#Pythonスクリプトを直接実行した時には、そのスクリプトファイルは「__main__」という名前のモジュールとして認識されます。
def test_method():
    print('Hello World')

if __name__ == '__main__':
    test_method()
print('モジュール名: {}'.format(__name__))


"""
Hello World
モジュール名: __main__


"""
