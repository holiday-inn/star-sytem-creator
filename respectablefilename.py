import random
import json
import sqlite3

class star():
    worldname = None
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
    lvl = 0
    
    def __init__(self):

        def randname():
                letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHLMNOPQRSTUVWXZY"
                name = ''.join(random.choice(letters) for _ in range(random.randint(3,9)))
                return name

        self.data = open("tables.csv","a")
        self.worldname = randname()
        print(f"|  Planet Name:{self.worldname:<9}  |")
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
            data = open("table2.csv","r").read().split("\n")
            if self.starport == "A":tech+= 6
            elif self.starport == "B":tech+= 4
            elif self.starport == "C":tech+= 2
            elif self.starport == "X":tech-= 4
            
            nums = [self.size,self.atm,self.hyd,self.pop,self.govt]
            count = 0
            list = ["size","atm","hyd","pop","govt"]
            for i in list:
                k = json.loads(data[nums[count]])
                tech +=k[i]
                count+= 1
            return tech

        

        self.starport = info('starport')
        self.naval = info('naval')
        self.scout = info('scout')
        self.gas = info('gas')
        self.plane = info('plane')
        self.lvl = techlvl()
        
        print(f"|{self.starport},{self.naval},{self.scout},{self.gas},{self.plane:<5} |")
        print(self.lvl,self.size,self.atm,self.hyd,self.pop,self.govt) 


    def forlatersql():
        file = "dbase.db"
        conn = sqlite3.connect(file)
        curso = conn.cursor()
        query = """
        create table if not exists stars (
            id integer primary key autoincrement,
            name tinytext
            size integer,
            atm integer,
            hyd integer,
            pop integer,
            govt integer,
            law integer,
            tech integer,
            starport tinytext,
            naval bool,
            scout bool,
            gas bool,
            plane bool);"""
        curso.execute(query)
        query = query = f"""insert into customers (name,size,atm,hyd,pop,govt,law,tech,starport,naval,scout,gas,plane) values ('{pname}','{species}','{breed}','{rname}',{pnum},"{email}",{balance},"{fdate}");"""
        
        
        
        

for i in range(20):
    
    print("┌─────────────────────────┐")
    if i < 10:
        print((f"|  Planet number {i+1}:       |"))
    else:
        print(f"|  Planet number {i+1}:      |")
    star()
    print("│─────────────────────────|")



