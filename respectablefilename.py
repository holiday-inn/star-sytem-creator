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

    def forlatersql(self):
        connection = sqlite3.connect('dbase.db')
        cursor = connection.cursor()
        
        query = f"""insert into stars (name,size,atm,hyd,pop,govt,law,tech,starport,naval,scout,gas,plane) values ('{self.worldname}','{self.size}','{self.atm}','{self.atm}',{self.pop},"{self.govt}",{self.lawlvl},"{self.lvl}","{self.starport}","{self.naval}","{self.scout}","{self.gas}","{self.plane}");"""
        cursor.execute(query)
        cursor.connection.commit()
        query = "select * from stars"
        cursor.execute(query)


        

    def __init__(self):

        
        def randname():
                letters = ["bdfghjklmnprstvwyz","aeiou"]
                name = ''.join(random.choice(letters[random.randint(0,1)]) for _ in range(random.randint(3,8))).capitalize()

                return name

        self.data = open("tables.csv","a")
        self.worldname = randname()
        
        self.size = (random.randint(1,6) + random.randint(1,6) - 2)
        self.atm = (random.randint(1,6) + random.randint(1,6) - 7 + self.size)
        if self.size == 0:self.atm = 0
        
        self.hyd = (random.randint(1,6) + random.randint(1,6) - 7 + self.size)
        if self.size < 1: self.hyd = 0
        if self.atm < 1 or self.atm > 10: self.atm -=4
        if self.hyd < 0: self.hyd = 0
        if self.atm > 10: self.atm = 10
        self.pop = (random.randint(1,6) + random.randint(1,6) - 2)
        self.govt = (random.randint(1,6) + random.randint(1,6) - 7 + self.pop)
        if self.govt < 0: self.govt = 0
        self.lawlvl = (random.randint(1,6) + random.randint(1,6) - 7 + self.govt)
        if self.atm <= 0: self.atm = 0
        
        
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
        if self.lvl < 0: self.lvl
        
        self.forlatersql()

        
def main():   
    data = ["Name","Size","Atmosphere","Hydration","Population","Government","Law","Technology","Starport","Naval Base exists","Scout exists","Gas giant exists","Planetoids exist"]   
    connection = sqlite3.connect('dbase.db')
    cursor = connection.cursor()
    cursor.execute('drop table stars')
    connection.commit()
    
    query = """
        create table if not exists stars (
            id integer primary key autoincrement,
            name tinytext,
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
    cursor.execute(query)
    

    for i in range(10):
        star()
    
    connection = sqlite3.connect('dbase.db')
    cursor = connection.cursor()
    query = "select * from stars"
    cursor.execute(query)
    res = cursor.fetchall()
    for i in res:
        print(i)
    while True:
        inp = input("what do you want to look for?: ").strip()
        inp2 = input("Enter value: ").strip()
        try:
            query = f"select * from stars where {inp} = '{inp2}'"
            cursor.execute(query)
            result = cursor.fetchall()
            if len(result) == 0:
                print("No data with that value")
                continue
            break
        except:
            print("invalid input")
            print("Valid inputs: name, size, atm, hyd, pop, govt, law, tech, starport, naval, scout, gas, plane")

    
    
    
    for i in result:
        for k in data:
            print(f"\033[1m{k}\033[0m: {i[data.index(k)+1]}")
        print("\n")
    
    

main()





