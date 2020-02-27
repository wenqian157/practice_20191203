# gcount = 0

# def get_global():
#     return gcount

# def add_global():
#     global gcount
#     gcount +=1
#     return gcount

# add_global()
# add_global()
# print(gcount)

# def make_counter():
#     count = 0
#     def counter():
#         nonlocal count 
#         count += 1
#         return count
    
#     return counter

# counter = make_counter()

# print(counter())
# print(counter())\

# import tkinter
# import tkinter.messagebox

# def main():
#     flag = True

#     # 修改标签上的文字
#     def change_label_text():
#         nonlocal flag
#         flag = not flag
#         color, msg = ('red', 'Hello, world!')\
#             if flag else ('blue', 'Goodbye, world!')
#         label.config(text=msg, fg=color)

#     # 确认退出
#     def confirm_to_quit():
#         if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗?'):
#             top.quit()

#     # 创建顶层窗口
#     top = tkinter.Tk()
#     # 设置窗口大小
#     top.geometry('240x160')
#     # 设置窗口标题
#     top.title('小游戏')
#     # 创建标签对象并添加到顶层窗口
#     label = tkinter.Label(top, text='Hello, world!', font='Arial -32', fg='red')
#     label.pack(expand=1)
#     # 创建一个装按钮的容器
#     panel = tkinter.Frame(top)
#     # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
#     button1 = tkinter.Button(panel, text='修改', command=change_label_text)
#     button1.pack(side='left')
#     button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
#     button2.pack(side='right')
#     panel.pack(side='bottom')
#     # 开启主事件循环
#     tkinter.mainloop()


# if __name__ == '__main__':
#     main()

# str1, str2 = 'abc', '123'
# print(f'{str1} and {str1}' )
# print('{00} and {01}'.format(str1, str2))
# print('\\ and \'')

# import os 

# HERE = os.path.dirname(__file__)
# FILE = os.path.join(HERE, 'test1.txt')

# f = open(FILE, 'r', encoding ='utf-8')
# print(f.read())
# f.close()

# f = None
# try:
#     f = open(FILE,'r', encoding='utf-8')
#     print(f.read())
# except FileNotFoundError:
#     print('no file found')
# except UnicodeDecodeError:
#     print ('decode error')
# finally:
#     if f:
#         f.close()

# try:
#     with open(FILE, 'w', encoding='utf-8') as f:
#         print(f.read())
# except BaseException:
#     print('not found') 
# else:
#     print('writing succeed')

# f = None
# try:
#     f = open(FILE,'w', encoding='utf-8')
#     f.write('override content')
# except FileNotFoundError:
#     print('no file found')
# except UnicodeDecodeError:
#     print ('decode error')
# else:
#     f.close()
#     with open(FILE, 'r') as f:
#         print(f.read())

# import os
# import time

# HERE = os.path.dirname(__file__)
# FILE = os.path.join(HERE, 'test2.txt')

# with open(FILE,'r')as f:
#     print(f.read())

# with open(FILE, 'r') as f:
#     for line in f:
#         print(line, end='')
#         time.sleep(0.5)

# with open(FILE, 'r') as f:
#     lines = f.readlines()
# print(lines)

# with open(FILE,'a') as f:
#     f.write('\nrow 4\nrow 5\n')
#     f.write('row 6\n')

# with open(FILE, 'r') as f:
#     print(f.read()) 

# dic =dict(a=1,b=2,c=3)
# list1 = list(dic.items())
# print(list1)

# import os
# import time

# HERE = os.path.dirname(__file__)
# FILE = os.path.join(HERE, 'test2.txt')

# filenames = ['num1.txt','num2.txt','num3.txt']
# filepaths = [os.path.join(HERE, f) for f in filenames]

# f_list=[]

# try:
#     for filename in filepaths:
#         f = open(filename,'w')
#         f_list.append(f)
#         f.write(str(100)+'\n')
# except IOError as ex:
#     print(ex)

# finally:
#     for f in f_list:
#         f.close()
    
# with open(filepaths[0],'w') as f:
#     f.write('a')

# try:
#     with open('00_image.png','rb')as fs1:
#         data = fs1.read()
#         print(type(data))
#     with open('01_copy.png','wb')as fs2:
#         fs2.write(data)
# except IOError as ex:
#     print(ex) 

# def test(level):
#     if level<1:
#         raise Exception('invalid')
#     else:
#         print('fine')

# try:
#     test(0)
# except Exception:
#     print('excpetion') 

# import json

# mydict={
#     'name':'Ab',
#     'age':18,
#     'phone':[110,119],
#     'program':[
#         {'first':'math'},
#         {'second':'art'}
#     ],
#     'friends':['Bob','Cat']
# }
# print(json.dumps(mydict))

# with open('data3.json','w')as fs3:
#     fs3.write(json.dumps(mydict))

# try:
#     with open('data.json','w', encoding='utf-8')as fs:
#         json.dump(mydict,fs)
# except IOError as e:
#     print(e)

# print('succeed')

# with open('data.json','r')as f:
#     data = (f.read())

# with open('data2.json','w')as f2:
#     f2.write(data)

# import json

# with open('data.json','r')as f:
#     data = json.load(f)
#     print(data)