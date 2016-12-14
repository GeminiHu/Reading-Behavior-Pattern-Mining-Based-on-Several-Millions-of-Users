#-*- coding: UTF-8 -*- 
import pymssql
import CEasyMatching_sp as CEM
import time


for i in xrange(6,7):
    n=0
    #查询操作
    gps_slct = pymssql.connect(host='.',user='sa',password='123456',database='GpsData',as_dict=True)
    gps_updt = pymssql.connect(host='.',user='sa',password='123456',database='GpsData',as_dict=True)
    st = time.time()
    cur1 = gps_slct.cursor()
    #SELECT 长连接查询操作（逐条方式获取数据）
    sql1 = "select * from gps"+str(i)+" where ID is null order by gpsid"
    cur1.execute(sql1)
    print 'ok'
    r_slct = cur1.fetchone()
    print r_slct
    cur2 = gps_updt.cursor()
    #SELECT 长连接查询操作（逐条方式获取数据）
    #sql2 = "update gps"+str(i)+" set WayId=%d,SegId=%d,ID=%d,DeltaDis=%s,DeltaAng=%s where gpsid=%d"
    sql2 = "update gps6 set WayId=%d,SegId=%d,ID=%d,DeltaDis=%s,DeltaAng=%s where gpsid=%d"
    while r_slct:
        if r_slct['Longitude']!=0 and r_slct['Latitude']!=0:
            if r_slct['GpsSpeed']!= 0:
                r_EM = CEM.EasyMatching(float(r_slct['Longitude']), float(r_slct['Latitude']), r_slct['Angle'], 100, 5)
            else:
                r_EM = CEM.EasyMatching(float(r_slct['Longitude']), float(r_slct['Latitude']), 1000, 100, 5)
        else:
            r_EM = [0,0,0,100,181]  
        print r_EM
        cur2.execute(sql2,(r_EM[0],r_EM[1],r_EM[2],r_EM[3],r_EM[4],r_slct['GpsId']))
        print n
        n+=1
        r_slct = cur1.fetchone()
    gps_updt.commit()    
    gps_slct.close()
    gps_updt.close()


