#������ʵ�֣�����һ��m*n��mΪͼ�����������nΪ�����������ľ���city_class
import pickle 
c3 = range(1,32)
city_class_dic = {}
for date in xrange(1,32):
    #ʹbΪ�����ļ�������
    if (date<10):
        b = '0' + str(date)
    else:
        b = str(date)
    #��ȡcity�ļ����¸��յ�city�ֵ�
    with open('F://WSC225//ReadingOnline//processed_data//city//city_date'+b+'.pickle', 'rb') as f_pickle:
        c3[date-1] = pickle.load(f_pickle)
    f_pickle.close()
    #�����յ��ֵ�¼��city_class_dic�ֵ�
    for city in c3[date-1].keys():
        if city in city_class_dic.keys():
            for clas in c3[date-1][city][1].keys():
                if clas in city_class_dic[city].keys():
                    city_class_dic[city][clas] += c3[date-1][city][1][clas]
                else:
                    city_class_dic[city][clas]  = c3[date-1][city][1][clas]
        else:
            city_class_dic[city] = c3[date-1][city][1]
#��city_class_dic�洢����
with open('F://WSC225//ReadingOnline//processed_data//city//city_class_dic.pickle', 'wb') as f_pickle:
    pickle.dump(city_class_dic, f_pickle)
f_pickle.close()

n = len(city_class_dic.keys())#������
#����ͼ�������
m_city = ''
m = 0
for city in city_class_dic.keys():
    if  m < len(city_class_dic[city].keys()):
        m = len(city_class_dic[city].keys())
        m_city = city
        
#��ÿһ����Ӧһ����
number = range(m)
class_number = {}
cnt = 0
for clas in city_class_dic[m_city].keys():
    class_number[clas] = number[cnt]
    cnt += 1         
#��ÿһ���ж�Ӧһ����
number = range(n)
city_number = {}
cnt = 0
for city in city_class_dic.keys():
    city_number[city] = number[cnt]
    cnt += 1 
#����m*n��mΪͼ�����������nΪ�����������ľ���city_class
import numpy
city_class = range(m)
for i in xrange(m):
    city_class[i] = [0]*n
for city in city_class_dic.keys():
    for clas in city_class_dic[city].keys():
        city_class[class_number[clas]][city_number[city]] = city_class_dic[city][clas]
#��city_class(92�����ÿ�����洢21�����е��û���)�洢����
with open('F://WSC225//ReadingOnline//processed_data//city//city_class.pickle', 'wb') as f_pickle:
    pickle.dump(city_class, f_pickle)
f_pickle.close() 

#����class_city(21�����У�ÿ�����д洢92�����)
class_city = range(n)
for i in xrange(n):
    class_city[i] = [0]*m
for i in xrange(n):
    for j in xrange(m):
        class_city[i][j] = city_class[j][i]
#��class_city(21�����У�ÿ�����д洢92�����)�洢����
with open('F://WSC225//ReadingOnline//processed_data//city//class_city.pickle', 'wb') as f_pickle:
    pickle.dump(class_city, f_pickle)
f_pickle.close() 

    