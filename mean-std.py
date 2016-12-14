############################################################本程序未修改完善，以下只是把之前代码的方差改为标准差##############################
#本程序实现：绘制以下几个变量之间的关系
#1.92个类别的图书喜爱度关于21个城市的期望与方差的关系
#2.92个类别的图书用户数关于21个城市的期望与方差的关系
#3.除去10月3日数据后，31天用户访问量关于时间的期望与方差的关系
import pickle
import matplotlib.pyplot as plt
import numpy as np
import math as m
from scipy.optimize import curve_fit

#############################################################实现92个类别的图书喜爱度关于21个城市的期望与方差的关系#####################################################
#读取city文件夹下的norm_cityclass文件
with open('F://WSC225//ReadingOnline//processed_data//city//norm_cityclass.pickle', 'rb') as f_pickle:
   norm_cityclass = pickle.load(f_pickle)
f_pickle.close()
#存储均值与方差的向量
mean1 = range(92)
std1  = range(92)
#存储双对数处理后的均值和方差
log_mean1 = range(92)
log_std1  = range(92)
for clas in xrange(92):
   mean1[clas] = np.mean(norm_cityclass[clas])
   log_mean1[clas] = m.log(mean1[clas])
   std1 [clas] = np.std(norm_cityclass[clas])
   log_std1[clas] = m.log(std1[clas])
#需要用到的函数
func = lambda x,a,b: a*x+b#线性规划的函数
f1 = lambda x,a: m.pow(x,a)
f2 = lambda x: m.sqrt(x*(1-x))
#f3 = lambda x,a: m.sqrt(x*(1+a*x))
#拟合直线
popt1,pcov1 = curve_fit(func,log_mean1,log_std1)
xn1 = range(92)
yn1 = range(92)
th1 = range(92)
th2 = range(92)
th3 = range(92)
for i in xrange(92):
   xn1[i] = m.exp(log_mean1[i])
   yn1[i] = m.exp(func(log_mean1[i],float(popt1[0]),float(popt1[1])))
   #th1[i] = m.exp(f1(log_mean1[i],float(popt1[0])))
   #th2[i] = m.exp(f2(log_mean1[i]))
   #th3[i] = m.exp(f3(log_mean1[i],float(popt1[0])))

plt.figure(1)
#plt.title("92个图书类别市场份额分布的期望与标准差双对数关系图")
plt.loglog(mean1,std1,'.',xn1,yn1)#,xn1,th2,xn1,th3)
plt.text(10**(-3),10**(-5),'k = '+str(float(popt1[0]))[0:4],fontsize = '20')
plt.xlabel("Mean",fontsize = '30')
plt.ylabel("STD",fontsize = '30')





###############################################################实现92个类别的图书用户数关于21个城市的期望与方差的关系########################################################
#读取city文件夹下的city_class文件
with open('F://WSC225//ReadingOnline//processed_data//city//city_class.pickle', 'rb') as f_pickle:
   city_class = pickle.load(f_pickle)
f_pickle.close()
#存储均值与方差的向量
mean2 = range(92)
std2  = range(92)
#存储双对数处理后的均值和方差
log_mean2 = range(92)
log_std2  = range(92)
for clas in xrange(92):
   mean2[clas] = np.mean(city_class[clas])
   log_mean2[clas] = m.log(mean2[clas])
   std2 [clas] = np.std(city_class[clas])
   log_std2[clas] = m.log(std2[clas])
#拟合直线
popt2,pcov2 = curve_fit(func,log_mean2,log_std2)
xn2 = range(92)
yn2 = range(92)
th1 = range(92)
#th2 = range(92)
th3 = range(92)
log_th3 = range(92)
for i in xrange(92):
   xn2[i] = m.exp(log_mean2[i])
   yn2[i] = m.exp(func(log_mean2[i],float(popt2[0]),float(popt2[1])))
   #th1[i] = m.exp(f1(log_mean2[i],float(popt2[0])))
   #th2[i] = m.exp(f2(log_mean2[i]))
   #th3[i] = m.exp(f3(log_mean2[i],float(popt2[0])))
   #log_th3[i] = f3(log_mean2[i],float(popt2[0]))

#绘制理论3的曲线 
#拐点前的数据
log_th3_sub1 = []#拟合直线用的纵坐标
log_xn2_sub1 = []#拟合直线用的横坐标
th3_sub1 = []#绘图用的纵坐标
xn2_sub1 = []#绘图用的横坐标
#拐点后的数据
log_th3_sub2 = []#拟合直线用的纵坐标
log_xn2_sub2 = []#拟合直线用的横坐标
th3_sub2 = []#绘图用的纵坐标
xn2_sub2 = []#绘图用的横坐标
for i in xrange(92):
   if (xn2[i] < 1):
      xn2_sub1.append(xn2[i])
      th3_sub1.append(th3[i])
      log_xn2_sub1.append(log_mean2[i])
      log_th3_sub1.append(log_th3[i])      
   else:
      xn2_sub2.append(xn2[i])
      th3_sub2.append(th3[i])
      log_xn2_sub2.append(log_mean2[i])
      log_th3_sub2.append(log_th3[i]) 
#拟合拐点前理论值曲线并设定绘图数据
popt_th3_sub1,pcov_th3_sub1 = curve_fit(func,log_xn2_sub1,log_th3_sub1)
#x_th3_sub1 = [0.01,1]
#y_th3_sub1 = [func(x_th3_sub1[0],popt_th3_sub1[0],popt_th3_sub1[1]),func(x_th3_sub1[1],popt_th3_sub1[0],popt_th3_sub1[1])]
#print popt_th3_sub1,y_th3_sub1
#拟合拐点后理论值曲线并设定绘图数据
popt_th3_sub2,pcov_th3_sub2 = curve_fit(func,log_xn2_sub2,log_th3_sub2)
#x_th3_sub2 = [1,10**(7)]
#y_th3_sub2 = [func(x_th3_sub2[0],popt_th3_sub2[0],popt_th3_sub2[1]),func(x_th3_sub2[1],popt_th3_sub2[0],popt_th3_sub2[1])]
#y_th3_sub2[0] = m.exp(y_th3_sub2[0])
##y_th3_sub2[1] = m.exp(y_th3_sub2[1])
#print popt_th3_sub2,y_th3_sub2

plt.figure(2)
#plt.title("92个图书类别用户数分布的期望与标准差双对数关系图")
#plt.loglog(mean2,std2,'.',xn2,yn2,xn2,th3,'r*',xn2_sub1,th3_sub1,xn2_sub2,th3_sub2)
plt.loglog(mean2,std2,'.',xn2,yn2)
plt.text(10**4,10,'k1 = '+str(float(popt2[0]))[0:4],fontsize = '20')
#plt.text(0.02,1000,'k1_th3 = '+str(float(popt_th3_sub1[0]))[0:4],fontsize = '20')
#plt.text(1000,1000,'k2_th3 = '+str(float(popt_th3_sub2[0]))[0:4],fontsize = '20')
plt.xlabel("Mean",fontsize = '30')
plt.ylabel("STD",fontsize = '30')



#######################################################实现除去10月3日数据后，31天用户访问量关于时间的期望与方差的关系#####################################################
c3 = range(1,32)
total_citydate = {}
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
    #将31天的数据存入21行31列的total_citydate
   for city in c3[date-1].keys():
      if (date == 1):
            total_citydate[city] = range(31)
      total_citydate[city][date-1] = c3[date-1][city][0]

#存储均值与方差的向量
mean3 = range(21)
std3  = range(21)
#存储双对数处理后的均值和方差
log_mean3 = range(21)
log_std3  = range(21)
cnt = 0
for city in c3[0].keys():
    #去掉10月3日数据
   plot_data = range(30)
   for i in xrange(31):
      if (i < 2):
            plot_data[i] = total_citydate[city][i]
      elif (i > 2):
            plot_data[i-1] = total_citydate[city][i]
   mean3[cnt] = np.mean(plot_data)
   log_mean3[cnt] = m.log(mean3[cnt])
   std3 [cnt] = np.std(plot_data)
   log_std3[cnt] = m.log(std3[cnt])
   cnt += 1
#拟合直线
popt3,pcov3 = curve_fit(func,log_mean3,log_std3)
xn3 = range(21)
yn3 = range(21)
for i in xrange(21):
   xn3[i] = m.exp(log_mean3[i])
   yn3[i] = m.exp(func(log_mean3[i],float(popt3[0]),float(popt3[1])))
plt.figure(3)
#plt.title("21个城市10月用户数的期望与标准差双对数关系图")
plt.loglog(mean3,std3,'.',xn3,yn3) 
plt.text(10**(5),10**(3),'k = '+str(float(popt3[0]))[0:4],fontsize = '20')
plt.xlabel("Mean",fontsize = '30')
plt.ylabel("STD",fontsize = '30')
plt.show()
