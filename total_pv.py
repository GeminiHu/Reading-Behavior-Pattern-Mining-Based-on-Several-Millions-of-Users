#本程序实现：将31天的不同pv的用户数分布综合后存储并绘图
import pickle 
pv = range(1,32)
total_pv = {}
for date in xrange(1,32):
    #使b为数据文件的日期
    if (date<10):
        b = '0' + str(date)
    else:
        b = str(date)
    #读取pv文件夹下各日的pv字典
    with open('F://WSC225//ReadingOnline//processed_data//pv//pv'+b+'.pickle', 'rb') as f_pickle:
        pv[date-1] = pickle.load(f_pickle)
    f_pickle.close()
    #将当日的字典录入total_pv字典
    for item in pv[date-1].keys():
        if item in total_pv.keys():
            total_pv[item]+=pv[date-1][item]
        else:
            total_pv[item]=pv[date-1][item]
#将total_pv存储下来
with open('F://WSC225//ReadingOnline//processed_data//pv//total_pv.pickle', 'wb') as f_pickle:
    pickle.dump(total_pv, f_pickle)
f_pickle.close()            
    