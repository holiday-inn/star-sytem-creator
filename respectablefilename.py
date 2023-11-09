import random
import json
import sqlite3

class star():
    size = 0
    atm = 0
    hyd = 0
    pop = 0
    govt = 0
    lawlvl = 0
    tech = 0
    starport = None
    naval = None
    scout = None
    gas = None
    plane = None
    
    def __init__(self):

        self.data = open("tables.csv","a")

        self.size = (random.randint(1,6) + random.randint(1,6) - 2)
        self.atm = (random.randint(1,6) + random.randint(1,6) - 7 + self.size)
        if self.size == 0:self.atmos = 0
        self.hyd = (random.randint(1,6) + random.randint(1,6) - 7 + self.size)
        if self.size < 1: self.hyd = 0
        if self.atm < 1 or self.atm > 10: pass
        # if size<1, hydro = 0. if atmos <1
        #gotta have a bunch of technicalities
        self.pop = (random.randint(1,6) + random.randint(1,6) - 2)
        self.govt = (random.randint(1,6) + random.randint(1,6) - 7 + self.pop)
        self.lawlvl = (random.randint(1,6) + random.randint(1,6) - 7 + self.govt)
        #need tech level, gotta ask quechuns
        
        
        line = open("tables.csv","r").read().split("\n")
            
        def info(varname):
            multi = 0
            twodie = random.randint(1,6) + random.randint(1,6)
            tempstar = json.loads(line[twodie-2])

            if varname == 'scout':
                if tempstar == "A":
                    multi = -3
                                
                elif tempstar == "B":
                    multi = -2

                elif tempstar == "C":
                    multi = -1
            
            elif varname == 'naval':
                if tempstar == "C" or tempstar == "D" or tempstar == "E"or tempstar == "X":
                    return False


            info = json.loads(line[twodie-2+multi])
            
            return info[varname]

        
        def techlvl():
            tech = random.randint(1,6)
            data = open("tables.csv","r").read().split("\n")
            #find line with needed number
            #
            list1 = [self.size,self.atm,self.hyd,self.pop,self.govt]
            list2 = ["size","atm","hyd","pop","govt"]
            for i in range(len(data)):
                for j in list2:
                    print(data[i][j])
    
            return info

        info('die'),self.size,self.hyd,self.atm
        

        self.starport = info('starport')
        self.naval = info('naval')
        self.scout = info('scout')
        self.gas = info('gas')
        self.plane = info('plane')

        print(self.starport,self.naval,self.scout,self.gas,self.plane)
    
        
        lvl = techlvl()



    def forlatersql():
        file = "dbase.db"
        conn = sqlite3.connect(file)
        curso = conn.cursor()
        query = """
        create table if not exists stars (
            id integer primary key autoincrement,
            size integer,
            atm integer,
            hyd integer,
            pop integer,
            govt integer,
            law integer,
            tech integer,
            head integer,
            starport integer,
            naval integer,
            scout integer,
            gas integer,
            plane integer);"""
        
        
        
        


for i in range(10):
    star()
    print(i+1)




