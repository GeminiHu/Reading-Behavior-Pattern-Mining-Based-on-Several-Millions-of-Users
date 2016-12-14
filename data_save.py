#本程序实现：
#1.计算得到31天的不同pv的用户数分布并保存到本地
#2.计算得到31天的地区与三个变量（用户数，内容分类，营销参数）的关系数据字典并保存到本地
#3.记录每个用户31天访问与否
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import string
import pickle
import time
#记录开始时间
TIME_FORM = '%Y-%m-%d %X'
print '*********************This work began at '+time.strftime(TIME_FORM,time.localtime(time.time())) +'*************************'
print ' '
#打开整体统计表格
sta = xlrd.open_workbook('F://WSC225//ReadingOnline//STATISTICS.xls')
table = sta.sheets()[0]
#数据文件地址拆分
a ='F://WSC225//ReadingOnline//ReadingData&BI//ReadingData//guangdong_pagevisit_201110' 
c = '.txt'
pv = range(1,32)#31天的pv数据字典存储于这个列表
c3 = range(1,32)#31天的地区与三个变量（用户数，内容分类，营销参数）的关系数据字典存储于这个列表
#interval = {}#存储用户31天的访问记录，用于计算间隔分布
for k in xrange(1,32):
    #使b为数据文件的日期
    if (k<10):
        b = '0' + str(k)
    else:
        b = str(k)
    #d为数据文件存放位置
    d = a+b+c
    f = open(d)
    #对一些统计量或辅助量赋初值
    pre_user = ''#前一个用户的ID初值
    pre_city = ''#前一个城市的代码初值
    User_IDs = 0
    N_users = int(table.cell(k,2).value)#获取用户个数
    sta_pv = [0]*N_users#记录单个用户每天的访问总次数
    pv[k-1] = {}#存储第k日不同访问次数对应的用户数量
    c3[k-1] = {}#存储第k日地区与三个变量的关系
    for i in xrange(1000):
        line = f.readline()
        #print line
    #for line in f.xreadlines():
        index = range(17)#存储17个字段的起始位置
        index[0] = 0
        cnt = 0
        for j in xrange(0,len(line)):
            if (line[j]== '\t'):
                cnt += 1  
                index[cnt] = j+1
        city = line[index[3]:index[4]-1]#该条记录的城市
        clas = line[index[9]:index[10]-1]#该条记录的图书分类
        sale = line[index[5]:index[6]-1]#该条记录的营销参数
        #将clas，sale存入字典c3[k-1]
        if city in c3[k-1].keys():
            if clas in c3[k-1][city][1].keys():
                c3[k-1][city][1][clas]+=1
            else:
                c3[k-1][city][1][clas]=1
            if sale in c3[k-1][city][2].keys():
                c3[k-1][city][2][sale]+=1
            else:
                c3[k-1][city][2][sale]=1
        else:
            c3[k-1][city] = range(3)
            c3[k-1][city][1] = {}
            c3[k-1][city][2] = {}
        #将用户pv数据写入sta_pv
        user = line[0:11]
        if (user != pre_user):
            User_IDs+=1
            #输出目前处理的进度
            if User_IDs%50 == 0:
                print str(User_IDs)+' users have been processed in file'+str(b)+' at '+ time.strftime(TIME_FORM,time.localtime(time.time()))
            #用户变化以后，在interval中记录
            #if user in interval.keys():
                #interval[user][k-1] += 1
            #else:
                #interval[user] = [0]*31
                #interval[user][k-1] = 1
            if (city != pre_city):
                c3[k-1][city][0]+=1#用户城市均改变，当日该城市加1    
        sta_pv[User_IDs-1] += string.atoi('0'+line[index[11]:index[12]-1])
        pre_user = user
        pre_city = city
    f.close()
    #将统计的sta_pv存入字典pv[k-1]
    for item in sta_pv:
        if item in pv[k-1].keys():
            pv[k-1][item]+=1
        else:
            pv[k-1][item]=1
    #存储下每个文件需要记录的数据   
    #存储每日pv数据
    with open('F://WSC225//ReadingOnline//processed_data//pv//pv'+b+'.pickle', 'wb') as f_pickle:
        pickle.dump(pv[k-1], f_pickle)
    f_pickle.close()     
    #存储每日c3数据
    with open('F://WSC225//ReadingOnline//processed_data//city//city_date'+b+'.pickle', 'wb') as f_pickle:
        pickle.dump(c3[k-1], f_pickle)
    f_pickle.close()    
    #输出处理完每一个文件的时间
    TIME_FORM = '%Y-%m-%d %X'
    print '***************************Processing file'+b+' has been finished at '+time.strftime(TIME_FORM,time.localtime(time.time())) +'***************************'  
    print ' '
#存储用户访问数据
#with open('F://WSC225//ReadingOnline//processed_data//interval.pickle', 'wb') as f_pickle:
      #pickle.dump(interval, f_pickle)
#f_pickle.close()    
#文件处理完的时间
TIME_FORM = '%Y-%m-%d %X'
print 'All the work has been finished at '+time.strftime(TIME_FORM,time.localtime(time.time()))        
    
    
    #sorted_pv = sorted(sta_pv,reverse = True)
    #x = range(N_users)
    #plt.figure(1)
    #plt.plot(x,sorted_pv,'r.')
    #plt.show()
    #plt.figure(2)
    #plt.semilogx(x,sorted_pv,'r.')
    #plt.show()
    #plt.figure(3)
    #plt.semilogy(x,sorted_pv,'r.') 
    #plt.show()
