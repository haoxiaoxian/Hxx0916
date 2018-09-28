import socket

step = 'a'

menu = '''
-----welcome-----

    1.上传文件
    2.下载文件

选择要执行的步骤:
'''

menu2 = '''
-----------------
1.上传到server_dir
2.新建文件夹
'''

sk = socket.socket()
sk.connect(('127.0.0.1', 8080))

while 1:
    username = input('输入用户名:')
    password = input('输入密码:')
    sk.send(bytes(("{},{}".format(username, password)), encoding='utf-8'))
    ret = sk.recv(1024)
    if ret:
        break

choice = input(menu)
if choice == '1':  # 上传文件
    step = '1'
    choice2 = input(menu2)
    if choice2 == '1':
        step += '1'  # 上传到server_dir
        sk.send(bytes(step, encoding='utf-8'))
        sk.send(bytes('test1', encoding='utf-8'))
        sk.send(bytes('这是要测试的内容', encoding='utf-8'))
    elif choice2 == '2':
        step += '2'  # 新建目录并且上传
        sk.send(bytes(step, encoding='utf-8'))
        sk.send(bytes('server_dirtest', encoding='utf-8'))
        sk.send(bytes('test2', encoding='utf-8'))
        sk.send(bytes('这是要测试的内容2222', encoding='utf-8'))
elif choice == '2':  # 下载文件
    step = '2'  # 选择下载目录并且下载
    sk.send(bytes(step, encoding='utf-8'))
    ret = sk.recv(10000).decode('utf-8')
    print(ret)
    filename = input('输入要下载的文件名:')
    sk.send(bytes(filename, encoding='utf-8'))
    file_content = sk.recv(100000).decode('utf-8')
    with open(file='client_dir/%s' % filename, mode='w', encoding='utf-8') as f:
        f.write(file_content)
