'''
    The CRUD Operations of Database
'''
import pymysql
from datetime import date
import json

def get(audioFile,ID):
    try:  
        con = pymysql.connect(host='localhost',user='root',password='root',db='audio_files',charset='utf8mb4')
        sql="select * from {0} where ID= {1}".format(audioFile,ID)
        with con.cursor() as cur:
            cur.execute(sql)
            result = cur.fetchone()
        if result:
            response= { 'Successful': '200 OK'}
        else: 
            response= {'Invalid':'400 bad request'}
    except:
        response= {'error':'500 internal server error'}
    finally:
        cur.close()
        con.close()
    return json.dumps(response)
    

def insert(audioFile,data):
    try:
        con = pymysql.connect(host='localhost',user='root',password='root',db='audio_files',charset='utf8mb4')
        sql="insert into {0}(".format(audioFile)
        sql2=" ) values("
        datalist=[]
        for key,value in data.items():
            sql=sql+key+","
            sql2=sql2+'%s'+","
            datalist.append(value)
        sql=sql[:len(sql)-1] +",Uploaded_Time"+sql2[:len(sql2)-1] + ",%s)"
        cur=con.cursor()
        datalist.append(date.today())
        result=cur.execute(sql,datalist)
        con.commit()
        if result:
            response= { 'Successful': '200 OK'}
        else: 
            response= {'Invalid':'400 bad request'}
    except Exception as e:
        response= {'error':'500 internal server error'}
    finally:
        cur.close()
        con.close()
    return json.dumps(response)
    
def delete(type,ID):
    try:
        con = pymysql.connect(host='localhost',user='root',password='root',db='audio_files',charset='utf8mb4')
        sql="DELETE FROM {0} WHERE ID={1}".format(type,ID)
        cur=con.cursor()
        result=cur.execute(sql)
        con.commit()
        if result:
            response= { 'Successful': '200 OK'}
        else: 
            response= {'Invalid':'400 bad request'}
    except:
        response= {'error':'500 internal server error'}
    finally:
        con.close()
    return json.dumps(response)
    
def update(type,ID,data):
    try:
        con = pymysql.connect(host='localhost',user='root',password='root',db='audio_files',charset='utf8mb4')
        sql="Update {0} SET ".format(type) 
        sql2=" WHERE ID={0}".format(ID)
        setdata=[]
        for key,value in data.items():
            sql= sql+ key+"="+"%s,"
            setdata.append(value)
        sql=sql[:len(sql)-1]+ sql2
        cur=con.cursor()
        result=cur.execute(sql,setdata)
        con.commit()
        if result:
            response= { 'Successful': '200 OK'}
        else: 
            response= {'Invalid':'400 bad request'}
    except:
        response= {'error':'500 internal server error'}
    finally:
        con.close()
    return json.dumps(response)
    