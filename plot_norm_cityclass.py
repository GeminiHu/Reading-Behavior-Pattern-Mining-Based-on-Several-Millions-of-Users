#本程序实现：绘制出去掉城市规模影响后，21个城市对92个类别的喜爱程度图像
import pickle
import matplotlib.pyplot as plt
class_city = []#存储读取的文件,便于计算城市规模
city_class = []#存储读取的文件
norm_cityclass = [range(21)]*92#存储喜爱度
#读取city文件夹下的class_city文件
with open('F://WSC225//ReadingOnline//processed_data//city//class_city.pickle', 'rb') as f_pickle:
   class_city = pickle.load(f_pickle)
f_pickle.close()
#读取city文件夹下的city_class文件
with open('F://WSC225//ReadingOnline//processed_data//city//city_class.pickle', 'rb') as f_pickle:
   city_class = pickle.load(f_pickle)
f_pickle.close()
city_users = range(21)#存储每个城市的用户数
a = plt.figure(1)#去掉城市规模的各类别市场份额
#b = plt.figure(2)#用户数与类别
#计算21个城市的用户数
for city in xrange(21):
   city_users[city] = sum(class_city[city])
#绘制92个类别在21个城市的分布
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
#将norm_cityclass(同一类别图书在不同城市喜爱度的分布)存储下来
with open('F://WSC225//ReadingOnline//processed_data//city//norm_cityclass.pickle', 'wb') as f_pickle:
   pickle.dump(norm_cityclass, f_pickle)
f_pickle.close() 
plt.show()