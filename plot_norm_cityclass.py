#������ʵ�֣����Ƴ�ȥ�����й�ģӰ���21�����ж�92������ϲ���̶�ͼ��
import pickle
import matplotlib.pyplot as plt
class_city = []#�洢��ȡ���ļ�,���ڼ�����й�ģ
city_class = []#�洢��ȡ���ļ�
norm_cityclass = [range(21)]*92#�洢ϲ����
#��ȡcity�ļ����µ�class_city�ļ�
with open('F://WSC225//ReadingOnline//processed_data//city//class_city.pickle', 'rb') as f_pickle:
   class_city = pickle.load(f_pickle)
f_pickle.close()
#��ȡcity�ļ����µ�city_class�ļ�
with open('F://WSC225//ReadingOnline//processed_data//city//city_class.pickle', 'rb') as f_pickle:
   city_class = pickle.load(f_pickle)
f_pickle.close()
city_users = range(21)#�洢ÿ�����е��û���
a = plt.figure(1)#ȥ�����й�ģ�ĸ�����г��ݶ�
#b = plt.figure(2)#�û��������
#����21�����е��û���
for city in xrange(21):
   city_users[city] = sum(class_city[city])
#����92�������21�����еķֲ�
for clas in xrange(92):
   plot_data1 = [0]*21
   #plot_data2 = [0]*21
   for city in xrange(21):
      plot_data1[city] = float(city_class[clas][city])/city_users[city]
      #plot_data2[city] = city_class[clas][city]
   norm_cityclass[clas] = plot_data1
   a = plt.plot(plot_data1)
   #b = plt.plot(plot_data2)
a = plt.ylabel("Market Share",fontsize = '30')
a = plt.xlabel("City",fontsize = '30')
#b = plt.ylabel("User Numbers",fontsize = '30')
#b = plt.xlabel("City",fontsize = '30')
#��norm_cityclass(ͬһ���ͼ���ڲ�ͬ����ϲ���ȵķֲ�)�洢����
with open('F://WSC225//ReadingOnline//processed_data//city//norm_cityclass.pickle', 'wb') as f_pickle:
   pickle.dump(norm_cityclass, f_pickle)
f_pickle.close() 
plt.show()