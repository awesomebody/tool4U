# -*- coding: utf-8 -*-
import  xdrlib ,sys
import xlrd
import datetime
def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)


def excel_table_byname(file= '../temp/query1501813150676.xls',colnameindex=0,by_name='list'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows
    colnames =  table.row_values(colnameindex)
    list =[]
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i]
             list.append(app)
    return list

def main():

    tables = excel_table_byname()
    list = []
    for row in tables:
        keys = ''
        values = ''
        for key in row:

            # str =  key+':'+row[key]
            keys+=key+','
            values+=row[key]+','

        insert = 'insert into xxx.xxx ('+keys+') values ('+values+')'
        select = 'select '+keys+' from xxx.xxx'
        print insert
        print select
        list.append(insert)
    print len(list)



if __name__=="__main__":
    main()