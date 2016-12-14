import xlwt
import time
TIME_FORM = '%Y-%m-%d %X'
print 'This statistics began at '+time.strftime(TIME_FORM,time.localtime(time.time()))
#创建excel，在第一行写入需要统计的量
wb = xlwt.Workbook()
ws  = wb.add_sheet('01')
ws.write(0,0,'RECORD_DAY')
ws.write(0,1,'Lines')
ws.write(0,2,'MSISDN')
ws.write(0,3,'ACCESS_TYPE')
ws.write(0,4,'CHARGE_TYPE')
ws.write(0,5,'BOOK_TYPE')
#数据文件地址拆分
a ='F://WSC225//ReadingOnline//ReadingData&BI//ReadingData//guangdong_pagevisit_201110' 
c = '.txt'
for k in xrange(1,32):
    #使b为数据文件的日期
    if (k<10):
        b = '0' + str(k)
    else:
        b = str(k)
    ws.write(k,0,b)
    #d为数据文件存放位置
    d = a+b+c
    f = open(d)
    #对一些统计量或辅助量赋初值
    Lines = 0    #统计行数
    pre_user = ''#前一个用户的ID初值
    User_IDs = 0 #用来统计用户个数
    #门户类型的统计量
    www = 0
    wap = 0
    g3  = 0
    cli = 0
    mm  = 0
    #图书收费类型的统计量
    whl = 0
    ch2 = 0
    ch3 = 0
    pmn = 0
    fas = 0
    fun8= 0
    #图书类型的统计量
    bok = 0
    ctn = 0
    mgz = 0
    fun9= 0
    #for i in xrange(100):
        #line = f.readline()
        #print line
    for line in f.xreadlines():
        Lines +=1
        user = line[0:11]
        if (user != pre_user):
            User_IDs+=1
        pre_user = user
        index = range(17)#存储17个字段的起始位置
        index[0] = 0
        cnt = 0
        for j in xrange(0,len(line)):
            if (line[j]== '\t'):
                cnt += 1  
                index[cnt] = j+1
            #出现四个'\t',则为门户类型数据
            if (cnt==4):
                if  (line[j+1]=='1'):
                    wap+=1
                elif(line[j+1]=='2'):
                    www+=1
                elif(line[j+1]=='3'):
                    g3 +=1 
                elif(line[j+1]=='4'):
                    cli+=1
                elif(line[j+1]=='8'):
                    mm +=1 
            #出现七个'\t',则为图书收费类型数据           
            if (cnt==7):
                if  (line[j+1]=='1'):
                        whl+=1
                elif(line[j+1]=='2'):
                        ch2+=1
                elif(line[j+1]=='3'):
                        ch3+=1 
                elif(line[j+1]=='5'):
                        pmn+=1
                elif(line[j+1]=='7'):
                        fas+=1 
                elif(line[j+1]=='$'):
                        fun8+=1 
            #出现八个'\t',则为图书类型数据
            if (cnt==8):
                if  (line[j+1]=='1'):
                    bok+=1
                elif(line[j+1]=='2'):
                    ctn+=1
                elif(line[j+1]=='3'):
                    mgz+=1 
                elif(line[j+1]=='$'):
                    fun9+=1 
    ACCESS_TYPE = '\tWAP:'+str(wap)+'    \tWWW:'+str(www)+'    \tG3_Ebook:'+str(g3)+'    \tClient:'+str(cli)+'    \tMM:'+str(mm)
    CHAREGE_TYPE = '\tWhl:'+str(whl)+'    \tCh2:'+str(ch2)+'    \tCh3:'+str(ch3)+'    \tPmn:'+str(pmn)+'    \tFas:'+str(fas)+'    \tFun8:'+str(fun8)
    BOOK_TYPE = '\tBok:'+str(bok)+'    \tCtn:'+str(ctn)+'    \tMgz:'+str(mgz)+'    \tFun9:'+str(fun9)
    f.close() 
    ws.write(k,1,Lines)
    ws.write(k,2,User_IDs)
    ws.write(k,3,ACCESS_TYPE)
    ws.write(k,4,CHAREGE_TYPE)
    ws.write(k,5,BOOK_TYPE)
    wb.save('F://WSC225//ReadingOnline//STATISTICS.xls')
    print 'The statistics of file: guangdong_pagevisit_201110'+b+c+' has been finished at '+time.strftime(TIME_FORM,time.localtime(time.time()))
