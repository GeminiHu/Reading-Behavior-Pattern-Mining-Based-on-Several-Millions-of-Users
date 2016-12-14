#本程序实现：构造一个31*n（地区总数)的字典city_date存储并绘图
import pickle 
import matplotlib.pyplot as plt
c3 = range(1,32)
city_date = {}
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
    #将当日的字典录入city_date字典
    for city in c3[date-1].keys():
        if city in city_date.keys():
            city_date[city][date-1]=c3[date-1][city][0]
        else:
            city_date[city] = [0]*31
            city_date[city][date-1]=c3[date-1][city][0]
#去掉10月3日数据后绘图
temp = range(3)
for city in city_date.keys():
    temp = city_date[city][0:2]
    for i in xrange(3,31):
        temp.append(city_date[city][i])
    plt.plot(temp)
plt.xlabel("Date",fontsize = '30')
plt.ylabel("User Numbers",fontsize = '30')
plt.show()
#将city_date存储下来
with open('F://WSC225//ReadingOnline//processed_data//city//city_date.pickle', 'wb') as f_pickle:
    pickle.dump(city_date, f_pickle)
f_pickle.close()            
    