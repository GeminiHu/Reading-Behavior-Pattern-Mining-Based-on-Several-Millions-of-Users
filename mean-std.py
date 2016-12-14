############################################################������δ�޸����ƣ�����ֻ�ǰ�֮ǰ����ķ����Ϊ��׼��##############################
#������ʵ�֣��������¼�������֮��Ĺ�ϵ
#1.92������ͼ��ϲ���ȹ���21�����е������뷽��Ĺ�ϵ
#2.92������ͼ���û�������21�����е������뷽��Ĺ�ϵ
#3.��ȥ10��3�����ݺ�31���û�����������ʱ��������뷽��Ĺ�ϵ
import pickle
import matplotlib.pyplot as plt
import numpy as np
import math as m
from scipy.optimize import curve_fit

#############################################################ʵ��92������ͼ��ϲ���ȹ���21�����е������뷽��Ĺ�ϵ#####################################################
#��ȡcity�ļ����µ�norm_cityclass�ļ�
with open('F://WSC225//ReadingOnline//processed_data//city//norm_cityclass.pickle', 'rb') as f_pickle:
   norm_cityclass = pickle.load(f_pickle)
f_pickle.close()
#�洢��ֵ�뷽�������
mean1 = range(92)
std1  = range(92)
#�洢˫���������ľ�ֵ�ͷ���
log_mean1 = range(92)
log_std1  = range(92)
for clas in xrange(92):
   mean1[clas] = np.mean(norm_cityclass[clas])
   log_mean1[clas] = m.log(mean1[clas])
   std1 [clas] = np.std(norm_cityclass[clas])
   log_std1[clas] = m.log(std1[clas])
#��Ҫ�õ��ĺ���
func = lambda x,a,b: a*x+b#���Թ滮�ĺ���
f1 = lambda x,a: m.pow(x,a)
f2 = lambda x: m.sqrt(x*(1-x))
#f3 = lambda x,a: m.sqrt(x*(1+a*x))
#���ֱ��
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
#plt.title("92��ͼ������г��ݶ�ֲ����������׼��˫������ϵͼ")
plt.loglog(mean1,std1,'.',xn1,yn1)#,xn1,th2,xn1,th3)
plt.text(10**(-3),10**(-5),'k = '+str(float(popt1[0]))[0:4],fontsize = '20')
plt.xlabel("Mean",fontsize = '30')
plt.ylabel("STD",fontsize = '30')





###############################################################ʵ��92������ͼ���û�������21�����е������뷽��Ĺ�ϵ########################################################
#��ȡcity�ļ����µ�city_class�ļ�
with open('F://WSC225//ReadingOnline//processed_data//city//city_class.pickle', 'rb') as f_pickle:
   city_class = pickle.load(f_pickle)
f_pickle.close()
#�洢��ֵ�뷽�������
mean2 = range(92)
std2  = range(92)
#�洢˫���������ľ�ֵ�ͷ���
log_mean2 = range(92)
log_std2  = range(92)
for clas in xrange(92):
   mean2[clas] = np.mean(city_class[clas])
   log_mean2[clas] = m.log(mean2[clas])
   std2 [clas] = np.std(city_class[clas])
   log_std2[clas] = m.log(std2[clas])
#���ֱ��
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

#��������3������ 
#�յ�ǰ������
log_th3_sub1 = []#���ֱ���õ�������
log_xn2_sub1 = []#���ֱ���õĺ�����
th3_sub1 = []#��ͼ�õ�������
xn2_sub1 = []#��ͼ�õĺ�����
#�յ�������
log_th3_sub2 = []#���ֱ���õ�������
log_xn2_sub2 = []#���ֱ���õĺ�����
th3_sub2 = []#��ͼ�õ�������
xn2_sub2 = []#��ͼ�õĺ�����
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
#��Ϲյ�ǰ����ֵ���߲��趨��ͼ����
popt_th3_sub1,pcov_th3_sub1 = curve_fit(func,log_xn2_sub1,log_th3_sub1)
#x_th3_sub1 = [0.01,1]
#y_th3_sub1 = [func(x_th3_sub1[0],popt_th3_sub1[0],popt_th3_sub1[1]),func(x_th3_sub1[1],popt_th3_sub1[0],popt_th3_sub1[1])]
#print popt_th3_sub1,y_th3_sub1
#��Ϲյ������ֵ���߲��趨��ͼ����
popt_th3_sub2,pcov_th3_sub2 = curve_fit(func,log_xn2_sub2,log_th3_sub2)
#x_th3_sub2 = [1,10**(7)]
#y_th3_sub2 = [func(x_th3_sub2[0],popt_th3_sub2[0],popt_th3_sub2[1]),func(x_th3_sub2[1],popt_th3_sub2[0],popt_th3_sub2[1])]
#y_th3_sub2[0] = m.exp(y_th3_sub2[0])
##y_th3_sub2[1] = m.exp(y_th3_sub2[1])
#print popt_th3_sub2,y_th3_sub2

plt.figure(2)
#plt.title("92��ͼ������û����ֲ����������׼��˫������ϵͼ")
#plt.loglog(mean2,std2,'.',xn2,yn2,xn2,th3,'r*',xn2_sub1,th3_sub1,xn2_sub2,th3_sub2)
plt.loglog(mean2,std2,'.',xn2,yn2)
plt.text(10**4,10,'k1 = '+str(float(popt2[0]))[0:4],fontsize = '20')
#plt.text(0.02,1000,'k1_th3 = '+str(float(popt_th3_sub1[0]))[0:4],fontsize = '20')
#plt.text(1000,1000,'k2_th3 = '+str(float(popt_th3_sub2[0]))[0:4],fontsize = '20')
plt.xlabel("Mean",fontsize = '30')
plt.ylabel("STD",fontsize = '30')



#######################################################ʵ�ֳ�ȥ10��3�����ݺ�31���û�����������ʱ��������뷽��Ĺ�ϵ#####################################################
c3 = range(1,32)
total_citydate = {}
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
    #��31������ݴ���21��31�е�total_citydate
   for city in c3[date-1].keys():
      if (date == 1):
            total_citydate[city] = range(31)
      total_citydate[city][date-1] = c3[date-1][city][0]

#�洢��ֵ�뷽�������
mean3 = range(21)
std3  = range(21)
#�洢˫���������ľ�ֵ�ͷ���
log_mean3 = range(21)
log_std3  = range(21)
cnt = 0
for city in c3[0].keys():
    #ȥ��10��3������
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
#���ֱ��
popt3,pcov3 = curve_fit(func,log_mean3,log_std3)
xn3 = range(21)
yn3 = range(21)
for i in xrange(21):
   xn3[i] = m.exp(log_mean3[i])
   yn3[i] = m.exp(func(log_mean3[i],float(popt3[0]),float(popt3[1])))
plt.figure(3)
#plt.title("21������10���û������������׼��˫������ϵͼ")
plt.loglog(mean3,std3,'.',xn3,yn3) 
plt.text(10**(5),10**(3),'k = '+str(float(popt3[0]))[0:4],fontsize = '20')
plt.xlabel("Mean",fontsize = '30')
plt.ylabel("STD",fontsize = '30')
plt.show()
