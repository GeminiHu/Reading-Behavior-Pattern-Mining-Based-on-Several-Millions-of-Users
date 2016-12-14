#������ʵ�֣�
#1.����õ�31��Ĳ�ͬpv���û����ֲ������浽����
#2.����õ�31��ĵ����������������û��������ݷ��࣬Ӫ���������Ĺ�ϵ�����ֵ䲢���浽����
#3.��¼ÿ���û�31��������
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import string
import pickle
import time
#��¼��ʼʱ��
TIME_FORM = '%Y-%m-%d %X'
print '*********************This work began at '+time.strftime(TIME_FORM,time.localtime(time.time())) +'*************************'
print ' '
#������ͳ�Ʊ��
sta = xlrd.open_workbook('F://WSC225//ReadingOnline//STATISTICS.xls')
table = sta.sheets()[0]
#�����ļ���ַ���
a ='F://WSC225//ReadingOnline//ReadingData&BI//ReadingData//guangdong_pagevisit_201110' 
c = '.txt'
pv = range(1,32)#31���pv�����ֵ�洢������б�
c3 = range(1,32)#31��ĵ����������������û��������ݷ��࣬Ӫ���������Ĺ�ϵ�����ֵ�洢������б�
#interval = {}#�洢�û�31��ķ��ʼ�¼�����ڼ������ֲ�
for k in xrange(1,32):
    #ʹbΪ�����ļ�������
    if (k<10):
        b = '0' + str(k)
    else:
        b = str(k)
    #dΪ�����ļ����λ��
    d = a+b+c
    f = open(d)
    #��һЩͳ��������������ֵ
    pre_user = ''#ǰһ���û���ID��ֵ
    pre_city = ''#ǰһ�����еĴ����ֵ
    User_IDs = 0
    N_users = int(table.cell(k,2).value)#��ȡ�û�����
    sta_pv = [0]*N_users#��¼�����û�ÿ��ķ����ܴ���
    pv[k-1] = {}#�洢��k�ղ�ͬ���ʴ�����Ӧ���û�����
    c3[k-1] = {}#�洢��k�յ��������������Ĺ�ϵ
    for i in xrange(1000):
        line = f.readline()
        #print line
    #for line in f.xreadlines():
        index = range(17)#�洢17���ֶε���ʼλ��
        index[0] = 0
        cnt = 0
        for j in xrange(0,len(line)):
            if (line[j]== '\t'):
                cnt += 1  
                index[cnt] = j+1
        city = line[index[3]:index[4]-1]#������¼�ĳ���
        clas = line[index[9]:index[10]-1]#������¼��ͼ�����
        sale = line[index[5]:index[6]-1]#������¼��Ӫ������
        #��clas��sale�����ֵ�c3[k-1]
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
        #���û�pv����д��sta_pv
        user = line[0:11]
        if (user != pre_user):
            User_IDs+=1
            #���Ŀǰ����Ľ���
            if User_IDs%50 == 0:
                print str(User_IDs)+' users have been processed in file'+str(b)+' at '+ time.strftime(TIME_FORM,time.localtime(time.time()))
            #�û��仯�Ժ���interval�м�¼
            #if user in interval.keys():
                #interval[user][k-1] += 1
            #else:
                #interval[user] = [0]*31
                #interval[user][k-1] = 1
            if (city != pre_city):
                c3[k-1][city][0]+=1#�û����о��ı䣬���ոó��м�1    
        sta_pv[User_IDs-1] += string.atoi('0'+line[index[11]:index[12]-1])
        pre_user = user
        pre_city = city
    f.close()
    #��ͳ�Ƶ�sta_pv�����ֵ�pv[k-1]
    for item in sta_pv:
        if item in pv[k-1].keys():
            pv[k-1][item]+=1
        else:
            pv[k-1][item]=1
    #�洢��ÿ���ļ���Ҫ��¼������   
    #�洢ÿ��pv����
    with open('F://WSC225//ReadingOnline//processed_data//pv//pv'+b+'.pickle', 'wb') as f_pickle:
        pickle.dump(pv[k-1], f_pickle)
    f_pickle.close()     
    #�洢ÿ��c3����
    with open('F://WSC225//ReadingOnline//processed_data//city//city_date'+b+'.pickle', 'wb') as f_pickle:
        pickle.dump(c3[k-1], f_pickle)
    f_pickle.close()    
    #���������ÿһ���ļ���ʱ��
    TIME_FORM = '%Y-%m-%d %X'
    print '***************************Processing file'+b+' has been finished at '+time.strftime(TIME_FORM,time.localtime(time.time())) +'***************************'  
    print ' '
#�洢�û���������
#with open('F://WSC225//ReadingOnline//processed_data//interval.pickle', 'wb') as f_pickle:
      #pickle.dump(interval, f_pickle)
#f_pickle.close()    
#�ļ��������ʱ��
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
