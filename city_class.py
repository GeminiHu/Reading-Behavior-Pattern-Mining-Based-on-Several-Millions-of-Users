#本程序实现：构造一个m*n（m为图书分类总数，n为地区总数）的矩阵city_class
import pickle 
c3 = range(1,32)
city_class_dic = {}
for date in xrange(1,32):
    #使b为数据文件的日期
    if (date<10):
        b = '0' + str(date)
    else:
        b = str(date)
    #读取city文件夹下各日的city字典
    with open('F://WSC225//ReadingOnline//processed_data//city//city_date'+b+'.pickle', 'rb') as f_pickle:
        c3[date-1] = pickle.load(f_pickle)
    f_pickle.close()
    #将当日的字典录入city_class_dic字典
    for city in c3[date-1].keys():
        if city in city_class_dic.keys():
            for clas in c3[date-1][city][1].keys():
                if clas in city_class_dic[city].keys():
                    city_class_dic[city][clas] += c3[date-1][city][1][clas]
                else:
                    city_class_dic[city][clas]  = c3[date-1][city][1][clas]
        else:
            city_class_dic[city] = c3[date-1][city][1]
#将city_class_dic存储下来
with open('F://WSC225//ReadingOnline//processed_data//city//city_class_dic.pickle', 'wb') as f_pickle:
    pickle.dump(city_class_dic, f_pickle)
f_pickle.close()

n = len(city_class_dic.keys())#城市数
#计算图书分类数
m_city = ''
m = 0
for city in city_class_dic.keys():
    if  m < len(city_class_dic[city].keys()):
        m = len(city_class_dic[city].keys())
        m_city = city
        
#让每一类别对应一个数
number = range(m)
class_number = {}
cnt = 0
for clas in city_class_dic[m_city].keys():
    class_number[clas] = number[cnt]
    cnt += 1         
#让每一城市对应一个数
number = range(n)
city_number = {}
cnt = 0
for city in city_class_dic.keys():
    city_number[city] = number[cnt]
    cnt += 1 
#构造m*n（m为图书分类总数，n为地区总数）的矩阵city_class
import numpy
city_class = range(m)
for i in xrange(m):
    city_class[i] = [0]*n
for city in city_class_dic.keys():
    for clas in city_class_dic[city].keys():
        city_class[class_number[clas]][city_number[city]] = city_class_dic[city][clas]
#将city_class(92个类别，每个类别存储21个城市的用户数)存储下来
with open('F://WSC225//ReadingOnline//processed_data//city//city_class.pickle', 'wb') as f_pickle:
    pickle.dump(city_class, f_pickle)
f_pickle.close() 

#生成class_city(21个城市，每个城市存储92个类别)
class_city = range(n)
for i in xrange(n):
    class_city[i] = [0]*m
for i in xrange(n):
    for j in xrange(m):
        class_city[i][j] = city_class[j][i]
#将class_city(21个城市，每个城市存储92个类别)存储下来
with open('F://WSC225//ReadingOnline//processed_data//city//class_city.pickle', 'wb') as f_pickle:
    pickle.dump(class_city, f_pickle)
f_pickle.close() 

    