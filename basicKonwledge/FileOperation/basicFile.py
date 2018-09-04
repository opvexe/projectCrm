
import sys,time

# 文件本生也是对象

'''创建文件对象'''
f = open('file.text','r',encoding='utf8')
data =  f.read()
print(data)
f.close()


'''创建加载进度'''
for i in  range(100):
    '''方法一'''
    sys.stdout.write('*')
    sys.stdout.flush() #刷新
    '''方法二'''
    print('*',end='',flush=True)

    time.sleep(0.1)

'''写入文件'''
f = open('file.text','w',encoding='utf8')
f.write('me too')
f.truncate(5)
print(f)
f.close()