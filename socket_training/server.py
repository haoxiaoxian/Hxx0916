import os
import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()
conn, addr = sk.accept()

while 1:
    ret = conn.recv(1024).decode('utf-8')  # 接收用户名密码
    with open('userinfo.txt', 'r') as f:  # 登陆模块
        for line in f:
            if ret == line.strip():
                conn.send(bytes(1))
                break
    break

ret = conn.recv(1024).decode('utf-8')
if ret == '11':
    filename = conn.recv(1024).decode('utf-8')
    content = conn.recv(1024).decode('utf-8')
    if filename in os.listdir('server_dir'):
        with open(r'server_dir/%s' % filename, mode='ab', encoding='utf-8') as f:
            f.write(content)
    else:
        with open(r'server_dir/%s' % filename, mode='w', encoding='utf-8') as f:
            f.write(content)
elif ret == '12':
    dirname = conn.recv(1024).decode('utf-8')
    filename = conn.recv(1024).decode('utf-8')
    content = conn.recv(1024).decode('utf-8')
    os.mkdir(dirname)
    os.chdir(dirname)
    with open(filename,mode='w',encoding='utf-8') as f:
        f.write(content)
elif ret == '2':
    conn.send(bytes('---'.join(os.listdir('server_dir')), encoding='utf-8'))
    filename = conn.recv(1024).decode('utf-8')
    with open(r'server_dir/%s' % filename, mode='r', encoding='utf-8') as f:
        conn.send(bytes(filename, encoding='utf-8'))
        conn.send(bytes(f.readline(), encoding='utf-8'))
