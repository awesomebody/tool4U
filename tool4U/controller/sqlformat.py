# coding: utf-8
# author: Henry
import re
from config import envConfig
from controller import common
#from controller import dbControrller

class Sqlformat:
    def __init__(self,sql):
        self.tabletemp = ''
        self.criterias = ''
        self.order = []
        self.sql = sql
        self.finalsql = []
        self.tables = {}
        self.table_rule = ".*from(.*\..*?)*where.*"
        self.criterias_rule = ".*where (.*)"
        self.criteriastemp = ''
        self.env = ''
        self.dbs = []
        self.env_info = []

    def tableinfo_factory(self,sql):
        self.sql = sql
        self.tabletemp = re.findall(self.table_rule,self.sql)
        self.criteriastemp = re.findall(self.criterias_rule,self.sql)
        print self.criteriastemp
        tablestemp = self.tabletemp[0].split(',')
        while '' in tablestemp:
            tablestemp.remove('')
        for tabletemp in tablestemp:
            tabletemp = tabletemp.split(' ')
            while '' in tabletemp:
                tabletemp.remove('')
            dbtemp = tabletemp[0].split('.')
            if tabletemp.__len__() == 1:
                self.tables[dbtemp[0]] = {tabletemp[0]:''}
            else:
                self.tables[dbtemp[0]] = {tabletemp[0]:tabletemp[1]}
        print self.tables
        return self.tables


    def envinfo_factory(self,env):
        self.env = env
        for key in self.tables:
            if envConfig.envConfigs["env"][self.env].has_key(key):
                self.env_info.append(common.commonutil.getdbinfo(self.env,key))
        print self.env_info
        return self.env_info

    def sqlfactory(self):
        columns = []
        for db in self.env_info:
            sql = ''
            db.keys()[0]



















if __name__ == "__main__":
    sqlformat = Sqlformat("select * from seashell.b a, maspos.d b,reconcav.f where a.skrhuo = b.huetihueo and b.guirhuo = c.fuouho")
    sqlformat.tableinfo_factory(sqlformat.sql)
    sqlformat.envinfo_factory("dev")
    sqlformat.sqlfactory()
