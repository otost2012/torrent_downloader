from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from urllib.request import urlretrieve
from lxml.html import etree
import re



class Torrent_down:
    movie_dic_lis=[]
    def __init__(self):
        self.url_sorce=['https://zongzidi.com',
                        'https://www.btrabbit.biz',
                        'https://www.ciliurl.com',
                        'https://www.cili.life'
                        ]
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        self.brower=webdriver.Chrome(chrome_options=option)
        self.wait=WebDriverWait(self.brower,20)#设置等待
        # self.run_project()

    def get_res(self,flag,words,page):#获得初始页
        url=''#搜索页面API
        url_base=''
        url_s=''
        if flag=='1':
            url_base=self.url_sorce[0]
            url='https://zongzidi.com/d/{}/time-1.html'.format(words)
            url_s='https://zongzidi.com/d/{}/time-{}.html'.format(words,page)
        elif flag=='2':
            url_base=self.url_sorce[1]
            url='https://www.btrabbit.biz/search/{}.html'.format(words)
            url_s='https://www.btrabbit.biz/search/{}/default-{}.html'.format(words,page)
        elif flag=='3':
            url_base=self.url_sorce[3]
            url='https://www.cili.life/main-search-kw-{}-1.html'.format(words)
            url_s='https://www.cili.life/main-search-kw-{}-{}.html'.format(words,page)
        try:
            if page==1:
                self.brower.get(url)
                # self.brower.find_element_by_id(words_id).send_keys(words)
                # self.brower.find_element_by_class_name(search_class).click()
            elif page>1:
                self.brower.get(url_s)
                # self.brower.find_element_by_id(words_id).send_keys(words)
                # self.brower.find_element_by_class_name(search_class).click()
            # print(self.brower.page_source)
            html=etree.HTML(self.brower.page_source)
            msg_totle=html.xpath('//div[@class="search-statu"]/span/text()')[0].strip()
            title_lis=html.xpath('//div[@class="item-title"]/h3/a/@title')
            url_lis = html.xpath('//div[@class="item-title"]/h3/a/@href')
            file_size_lis=html.xpath('//div[@class="item-bar"]/span[3]/b/text()')
            file_hot_lis=html.xpath('//div[@class="item-bar"]/span[4]/b/text()')
            url_lis=[url_base+x if not re.match(r'http|https',x) else x for x in url_lis]
            file_size_lis=[''.join(x.split()) for x in file_size_lis]
            movie_dic_lis=[{title:[url,size,hot]} for title,url,size,hot in zip(title_lis,url_lis,file_size_lis,file_hot_lis)]
            self.movie_dic_lis=movie_dic_lis
            print(msg_totle)
            print(len(movie_dic_lis),movie_dic_lis)
            return msg_totle,movie_dic_lis
        except Exception:
            pass

    def write_to_csv(self):
        pass

    def get_movie_link(self,flag,words,page,current_select,movie_index):
        # msg_totle, movie_dic_lis=self.get_res(flag,words,page)
        print('test',self.movie_dic_lis)
        magnet_link=''
        thunder_link=''
        print(type(self.movie_dic_lis[movie_index]),self.movie_dic_lis[movie_index])
        print(self.movie_dic_lis[movie_index][current_select][0])
        self.brower.get(self.movie_dic_lis[movie_index][current_select][0])
        # print(self.brower.page_source)
        html=etree.HTML(self.brower.page_source)
        if flag=='1':
            magnet_link=html.xpath('//div[@id="wall"]/div/p[12]/a[2]/@href')
            thunder_link=html.xpath('//div[@id="wall"]/div/p[13]/a[2]/@href')
        elif flag=='2':
            magnet_link=html.xpath('//div[@class="col-md-8"]/div[1]/div[2]/a/text()')
            thunder_link=html.xpath('//div[@class="col-md-8"]/div[2]/div[2]/a/text()')
        elif flag=='3':
            magnet_link=html.xpath('//div[@class="detail-panel detail-width"]/div[1]/div[2]/div[@id="magnet"]/text()')
            thunder_link=html.xpath('//div[@class="detail-panel detail-width"]/div[2]/div[2]/div[@id="xlurl"]/text()')
        try:
            magnet_link=[x.strip() for x in magnet_link if x.strip()!=''][0]
            thunder_link=[x.strip() for x in thunder_link if x.strip()!=''][0]
            print(magnet_link)
            print(thunder_link)
            return magnet_link,thunder_link
        except Exception as f:
            print(f.args)






#     def run_project(self):
#         self.get_res('1','碧血剑',1)
#         self.get_movie_link('1','碧血剑',1,'[WEBHD修复]碧血剑(国语) Bi.Xie.Jian.1981.WEB-DL.REPACK.1080P.H264.AAC-JBY@WEBHD',2)
#
# if __name__ == '__main__':
#     t=Torrent_down()
#     # t.run_project()
