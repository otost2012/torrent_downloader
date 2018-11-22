from tkinter.ttk import Entry,Button
from tkinter import Tk,Label,StringVar,Scrollbar,END,messagebox,Listbox,VERTICAL,HORIZONTAL,SINGLE,PhotoImage,Radiobutton
from tkinter.filedialog import askdirectory
from 种子下载器.torrent_downloader import Torrent_down
import os,re


path_file=['res/1.png','res/3.png']
class App:
    movie_dic_lis=[]
    page=1#全局变量
    def __init__(self):
        self.w=Tk()
        self.w.title('   种子下载器')
        self.w.iconbitmap('res/logo.ico')
        self.w.geometry('340x370')
        self.creat_res()#创建资源
        self.res_config()#配置
        self.w.mainloop()

    def creat_res(self):
        self.E_get=StringVar()#搜索
        self.E_down=StringVar()#下载
        self.R_chose=StringVar()#选择
        self.L_message_title=Label(self.w,text='torrrent下载',fg='red')
        self.R1=Radiobutton(self.w,text='源♥',value='1',variable=self.R_chose)
        self.R2=Radiobutton(self.w,text='源♣',value='2',variable=self.R_chose)
        self.R3=Radiobutton(self.w,text='源♠',value='3',variable=self.R_chose)
        self.E_search=Entry(self.w,textvariable=self.E_get)
        self.B_search=Button(self.w,text='搜索➢')
        self.E_download=Entry(self.w,textvariable=self.E_down)
        self.B_save=Button(self.w,text='选择目录')
        self.L_search=Label(self.w,text='搜索:')
        self.L_save=Label(self.w,text='存储路径:')
        self.L_box=Listbox(self.w,selectmode=SINGLE)
        self.B_down=Button(self.w,text='下载')
        self.S_coll_vertical=Scrollbar(self.w,orient=VERTICAL)
        self.S_coll_level=Scrollbar(self.w,orient=HORIZONTAL)
        self.L_message_show=Label(self.w,bg='#DEDEDE')
        self.L_show_pic=Label(self.w,bg='#DEDEDE')#显示图片
        self.B_page_down=Button(self.w,text='☜上页')
        self.B_page_up=Button(self.w,text='下页☞')
        self.L_totle_msg=Label(self.w,bg='pink')
        self.L_movie_info=Label(self.w)
        self.L_page_show=Label(self.w,text='页码:',bg='#DEDEDE')
        self.B_info=Button(self.w,text='说明')
        self.res_place()

    def res_place(self):
        self.L_message_title.place(x=10,y=7,width=80,height=30)
        self.R1.place(x=110,y=7,width=40,height=30)
        self.R2.place(x=170,y=7,width=40,height=30)
        self.R3.place(x=230,y=7,width=40,height=30)
        self.B_info.place(x=290,y=40,width=40,height=30)
        self.E_search.place(x=65,y=40,width=150,height=30)
        self.B_search.place(x=230,y=40,width=50,height=30)
        self.E_download.place(x=65,y=80,width=150,height=30)
        self.B_save.place(x=230,y=80,width=65,height=30)
        self.L_search.place(x=5,y=40,width=60,height=30)
        self.L_save.place(x=5,y=80,width=60,height=30)
        self.L_box.place(x=5,y=150,width=190,height=140)
        self.B_down.place(x=283,y=150,width=50,height=50)
        self.S_coll_vertical.place(x=194,y=150,width=15,height=140)
        self.S_coll_level.place(x=5,y=289,width=190,height=15)
        self.L_message_show.place(x=5,y=337,width=200,height=30)
        self.L_show_pic.place(x=213,y=220,width=120,height=140)
        self.B_page_down.place(x=10,y=308,width=60,height=25)
        self.B_page_up.place(x=145,y=308,width=60,height=25)
        self.L_page_show.place(x=73,y=308,width=70,height=25)
        self.L_totle_msg.place(x=5,y=115,width=330,height=30)
        self.L_movie_info.place(x=210,y=150,width=70,height=70)


    def res_config(self):
        self.B_search.config(command=self.search_torrent)#搜索命令
        self.B_down.config(command=self.down_torrent)#下载命令
        self.B_save.config(command=self.open_file_savepath)#存储命令
        self.R_chose.set('1')
        self.S_coll_vertical.config(command=self.L_box.yview)
        self.L_box['yscrollcommand']=self.S_coll_vertical.set
        self.S_coll_level.config(command=self.L_box.xview)
        self.L_box['xscrollcommand'] = self.S_coll_level.set
        self.L_box.bind('<Double-Button-1>',self.show_info)
        self.B_page_down.config(command=self.button_down)#页码-
        self.B_page_up.config(command=self.button_add)#页码+
        self.B_info.config(command=self.show_info_msg)

    def show_info_msg(self):
        print('ok')
        msg1='1.查看下一页内容请点击翻页后，再次点搜索'
        msg2='2.如果搜索不到资源，请切换源'
        msg3='3.点击下载后会自动将下载的种子存储在指定目录'
        messagebox.showinfo(title='使用说明',message=msg1+'\n'+msg2+'\n'+msg3)

    def warning_msg(self):
        self.img1 = PhotoImage(file=path_file[1])
        self.L_show_pic.config(image=self.img1)
        self.L_totle_msg.config(text='此内容少儿不宜')
        soe = messagebox.askyesno(title='警告', message='您访问的数据需要年满18岁以上，您确定要浏览？')
        if not soe:
            self.w.quit()

    def show_pics(self):
        count=0
        with open('res/words.txt','r',encoding='utf-8') as f:
            content=f.readlines()
            for con in content:
                if self.E_get.get() in con:
                    count+=1
                else:
                    self.img1=PhotoImage(file=path_file[0])
                    self.L_show_pic.config(image=self.img1)
        if count>0:
            self.warning_msg()

    def calculation_page(self,totle_num):#计算页码
        totle_page=1
        if self.R_chose.get()=='1':
            totle_page=totle_num//10
        elif self.R_chose.get()=='2':
            totle_page = totle_num // 10
        elif self.R_chose.get()=='3':
            totle_page = totle_num // 20
        return totle_page


    def button_add(self):
        self.page+=1
        self.L_page_show.config(text='页码:'+str(self.page))

    def button_down(self):
        self.page=1
        self.L_page_show.config(text='页码:'+str(self.page))

    def deal_page(self,full_page):
        if self.page>full_page:#如果页面超过最大页码
            self.page-=1
        elif self.page<0:
            self.page=1
        return self.page

    def search_torrent(self):
        self.t=Torrent_down()
        print(self.R_chose.get(), self.E_get.get())
        if self.E_get.get()!='':
            try:
                msg_totle, movie_dic_lis=self.t.get_res(self.R_chose.get(),self.E_get.get(),self.page)
                totle_num=re.findall('([\d]+).+条',msg_totle)[0]
                if not isinstance(totle_num,int):
                    totle_num=int(totle_num)
                full_page=self.calculation_page(totle_num)
                print(type(full_page),'页码',full_page)
                self.show_pics()
                self.movie_dic_lis=movie_dic_lis
                self.show_torrent(movie_dic_lis)
                self.L_totle_msg.config(text=msg_totle[msg_totle.find('找'):].replace('磁力链接','记录'))
                page=self.deal_page(full_page)#处理页码
                print(page)
            except Exception:
                soe=messagebox.askretrycancel(title='提示',message='程序崩溃，请重试')
                if not soe:
                    self.w.quit()
        else:
            messagebox.showwarning(title='警告',message='请输入搜索的字段')

    def clear_box(self):#清空列表
        self.L_box.delete(0,END)

    def show_torrent(self,lis_dic):
        self.clear_box()
        for title in lis_dic:
            for s,p in title.items():
                self.L_box.insert(END,s)

    def write_to_txt(self,title,magnet,thunder):
        path_file_text='res/文件.txt'
        if not os.path.exists(path_file_text):
            with open(file=path_file_text,mode='a+',encoding='utf-8') as f:
                f.write(title+'\n')
                f.write(magnet+'\n')
                f.write(thunder+'\n')

    def show_info(self,lis):
        print(self.movie_dic_lis)
        print(self.L_box.curselection())
        msg=self.movie_dic_lis[self.L_box.curselection()[0]]
        size,hot=msg[self.L_box.get(self.L_box.curselection())][1],msg[self.L_box.get(self.L_box.curselection())][2]
        self.L_movie_info.config(text='文件大小:'+'\n'+size+'\n'+'文件热度：'+'\n'+hot)


    def down_torrent(self):
        if os.path.exists(self.E_down.get()):
            if len(self.L_box.curselection())>0:#如果选中了
                print(self.L_box.get(self.L_box.curselection()))
                print(self.R_chose.get(),self.E_get.get(),self.page,self.L_box.get(self.L_box.curselection()),self.L_box.curselection()[0])
                magnet_link, thunder_link=self.t.get_movie_link(self.R_chose.get(),self.E_get.get(),
                                      self.page,self.L_box.get(self.L_box.curselection()),self.L_box.curselection()[0])
                print(magnet_link,thunder_link)
                self.write_to_txt(self.L_box.get(self.L_box.curselection()),magnet_link,thunder_link)
            elif len(self.L_box.curselection())==0:#判断是否选择
                messagebox.showwarning(title='警告',message='请选择电影名')
        else:
            messagebox.showwarning(title='警告',message='请选择存储目录')

    def open_file_savepath(self):
        self.file=askdirectory()
        self.E_down.set(self.file)

if __name__ == '__main__':
    a=App()
