import os
import requests

# 定义网页状态码正常列表
scode=[200,301,302,403]
with open('1.csv','a') as fp:
    fp.write('\n')
ls=[]
ls2=[]
k=''
z=''
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 HBPC/11.0.6.301',
}

# 读取文件作为对象，输出子域名到列表
with open('htu.edu.cn.csv','r') as fp:
    f=fp.readlines()
    for i in f:
        subdomain=i.split(",")[5]
        if subdomain not in ls:
            ls.append(subdomain)
        else:
            pass
    ls.remove("subdomain")
    

for i in ls:
    url='http://'+i
    print(url)
    try:
        rcode=requests.get(url=url,headers=headers,timeout=5).status_code
        print(rcode)
        k+=i+','+str(rcode)+'\n'
    except:
        z+=i+'\n'
with open('1.csv','w') as fp:
    fp.write('True,\n'+k+'\nFalse,\n'+z)
   