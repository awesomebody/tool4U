import re
from config import envConfig



class commonutil:
    def __init__(self):
        pass

    @staticmethod
    def getdbinfo(env,db):
        dbinfos = {}
        dbinfos[db] = envConfig.envConfigs["env"][env][db]

        return dbinfos



if __name__ == "__main__":
    Commonutil = commonutil()
    Commonutil.getdbinfo('dev','seashell')