#������ʵ�֣�����һ��31*n����������)���ֵ�city_date�洢����ͼ
import pickle 
import matplotlib.pyplot as plt
c3 = range(1,32)
city_date = {}
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
    #�����յ��ֵ�¼��city_date�ֵ�
    for city in c3[date-1].keys():
        if city in city_date.keys():
            city_date[city][date-1]=c3[date-1][city][0]
        else:
            city_date[city] = [0]*31
            city_date[city][date-1]=c3[date-1][city][0]
#ȥ��10��3�����ݺ��ͼ
temp = range(3)
for city in city_date.keys():
    temp = city_date[city][0:2]
    for i in xrange(3,31):
        temp.append(city_date[city][i])
    plt.plot(temp)
plt.xlabel("Date",fontsize = '30')
plt.ylabel("User Numbers",fontsize = '30')
plt.show()
#��city_date�洢����
with open('F://WSC225//ReadingOnline//processed_data//city//city_date.pickle', 'wb') as f_pickle:
    pickle.dump(city_date, f_pickle)
f_pickle.close()            
    