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
                letters = ["bdfgjklmnprstvwyz","aeiou"]
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
        if self.lawlvl < 0: self.lawlvl = 0
        
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
bignum = 0
numba = 10        
def main(): 
    global bignum
    global numba
    data = ["Name","Size","Atmosphere","Hydration","Population","Government","Law","Technology","Starport","Naval Base exists","Scout exists","Gas giant exists","Planetoids exist"]   
    connection = sqlite3.connect('dbase.db')
    cursor = connection.cursor()
    if bignum == 0:       
        cursor.execute('drop table stars')
        connection.commit()
    else:pass   
    bignum+=1
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
    for i in range(numba):star()
    while True:
        connection = sqlite3.connect('dbase.db')
        cursor = connection.cursor()
        query = "select * from stars"
        cursor.execute(query)
        result = cursor.fetchall()
        
        for i in (result):
            for k in data:
                temp = data.index(k)+1
                if temp%2 == 0:
                    print(f"\033[1m{k}\033[0m: {i[data.index(k)+1]}")
                else: print(f"\033[1m{k:<20}\033[0m: {i[data.index(k)+1]:<20}",end="")
            print("\n")
    
        choice = input('\n\033[1mWhat would you like to do? (help for options): \033[0m ')
        if choice == 'help':print("\nYou can: \nlook: To look at star systems\ngenerate: To create new star systems")
        
        elif choice == 'look':
            inp = input("\n\033[1mWould you like to look for name, size, atm, hyd, pop, \ngovt, law, tech, starport, naval, scout, gas, plane or all?: \033[0m").strip()
            if inp == 'all':
                inp2 = None
                pass
                
            else: inp2 = input("\n\033[1mEnter value:\033[0m ").strip()
            try:
                
                query = f"select * from stars where {inp} = '{inp2}'"
                if inp == 'all': query = "select * from stars"
                cursor.execute(query)
                result = cursor.fetchall()
                if len(result) == 0:
                    print("\033[1mNo data with that value\033[0m ")
                    continue
                
            except:
                print("\033[1minvalid input\033[0m ")

            for i in (result):
                
                for k in data:
                    temp = data.index(k)+1
                    if temp%2 == 0:
                        print(f"\033[1m{k}\033[0m: {i[data.index(k)+1]}")
                    else: print(f"\033[1m{k:<20}\033[0m: {i[data.index(k)+1]:<20}",end="")
                print("\n")
        
        elif choice == 'generate':
            numba = int(input("\033[1mHow many stars would you like to create?: \033[0m "))
            for i in range(numba):
                star()

main()