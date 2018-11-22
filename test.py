s=()
print(len(s))
p=(30,2)
print(len(p))
print(p[0])
ss='种子帝[zongzidi.com]为你找到了 329 条关于 金刚狼 的磁力链接，耗时 1 ms'
print(ss[ss.find('为'):].replace('磁力链接','记录'))
si='共找到 191 条关于 金刚狼 的结果, 耗时 1 毫秒'
count=0
with open('res/words.txt','r',encoding='utf-8') as f:
    con=f.readlines()
    print(con)
    for i in con:
        if '奶子' in i:
            count+=1
if count>0:
    print('yes')


import re
ms=re.findall('([\d]+).+条',ss)[0]
# print(int(ms))
if not isinstance(ms,int):
    print('i')
    ms=int(ms)
else:
    print('o')
print(type(ms),ms)

R_chose='3'
def calculation_page(totle_num):  # 计算页码
    totle_page = 1
    if R_chose == '1':
        totle_page = totle_num // 10
    elif R_chose == '2':
        totle_page = totle_num // 10
    elif R_chose == '3':
        totle_page = totle_num // 20
    return totle_page

print(calculation_page(329))

dic={'2000碧血剑【国语外挂字幕】gotv源码': ['https://www.cili.life/hash/060c0ce5cfae29a48102280b88943880689859fc.html', '28.51G', '250']}
print(type(dic.values()),dic.values())
print(dic['2000碧血剑【国语外挂字幕】gotv源码'])