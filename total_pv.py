#������ʵ�֣���31��Ĳ�ͬpv���û����ֲ��ۺϺ�洢����ͼ
import pickle 
pv = range(1,32)
total_pv = {}
for date in xrange(1,32):
    #ʹbΪ�����ļ�������
    if (date<10):
        b = '0' + str(date)
    else:
        b = str(date)
    #��ȡpv�ļ����¸��յ�pv�ֵ�
    with open('F://WSC225//ReadingOnline//processed_data//pv//pv'+b+'.pickle', 'rb') as f_pickle:
        pv[date-1] = pickle.load(f_pickle)
    f_pickle.close()
    #�����յ��ֵ�¼��total_pv�ֵ�
    for item in pv[date-1].keys():
        if item in total_pv.keys():
            total_pv[item]+=pv[date-1][item]
        else:
            total_pv[item]=pv[date-1][item]
#��total_pv�洢����
with open('F://WSC225//ReadingOnline//processed_data//pv//total_pv.pickle', 'wb') as f_pickle:
    pickle.dump(total_pv, f_pickle)
f_pickle.close()            
    