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
        if self.lawlvl > 10: self.lawlvl = 10
        if self.pop > 9: self.pop = 9
        if self.govt > 13: self.govt = 13
        
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
        
        
    
        choice = input('\n\033[1mWhat would you like to do? (help for options): \033[0m ')
        if choice == 'help':print("\nYou can: \nlook: To look at star systems or search systems for values\ngenerate: To create new star systems");continue
        
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
                for i in (result):
                    for k in data:
                        temp = data.index(k)+1
                        if temp%2 == 0:
                            print(f"\033[1m{k}\033[0m: {i[data.index(k)+1]}")
                        else: print(f"\033[1m{k:<20}\033[0m: {i[data.index(k)+1]:<20}",end="")
                    print("\n")
                
            except:
                print("\033[1minvalid input\033[0m ")
            

            
        
        elif choice == 'generate':
            numba = int(input("\033[1mHow many stars would you like to create?: \033[0m "))
            for i in range(numba):
                star()
            query = "select * from stars"
            cursor.execute(query)
            result = cursor.fetchall()
            
            linedata = [["Asteroid Belt","1000 miles","2000 miles","3000 miles","4000 miles","5000 miles","6000 miles","7000 miles","8000 miles","9000 miles","10000 miles"],
["No atmosphere","Trace","Very thin, tainted","Very thin","Thin, tainted","Thin","Standard","Standard, tainted","Dense","Dense, tainted","Exotic","Corrosive","Insidious","Dense, high","Ellippsoid","Thin, low"],
["No free standing water","10% water","20% water","30% water","40% water","50% water", "60% water","70% water","80% water","90% water", "No land masses"],
["No inhabitants", "Tens of inhabitants", "Hundreds of inhabitants", "Thousands of inhabitants", "Hundreds of thousands of inhabitants", "Millions of inhabitants","Tens of millions of inhabitants","Hundreds of millions of inhabitants","Billions of inhabitants","Tens of billions of inhabitants"],
['No government structure','Company/Corporation','Participating Democracy','Self-Perpetuating Oligarchy','Representative Democracy','Feudal Technocracy','Captive Government','Balkanization','Civil Service Bureaucracy','Impersonal Bureaucracy','Charismatic Dictator','Non-Charismatic Leader','Charismatic Oligarchy','Religious Dictatorship'],
["No prohibitions", "Body pistols are undetectable by standard detectors, explosives and poison are prohibited", "Portable enrgy weapons are prohibited","Weapons of a strict military nature prohibited","Light assault weapons prohibited","Personal concealable firearms are prohibited", "Most firearms prohibited","Shotguns are prohibited", "Long bladed weapons are controlled, and open possesion is prohibited", "Posession of any weapon outside of one's resident is prohibited", "Weapon Possesion is prohibited"],
['Stone Age. Primitive','Bronze to Middle Ages','1400-1700','1700-1860','1860-1900','1900-1939','1940-1969','1970-1979','1980-1989','1990-2000','Interstellar community','Average Imperial','Average Imperial','Above Average Imperial','Above Average Imperial','Technical maximum Imperial','Occasional non-Imperial'],
["Excellent quality","Good quality","Routine quality","Poor quality","Frontier installation","No starport"]]

            for i in (result):
                for k in data:
                    temp = data.index(k)+1
                    if temp < 10:
                        if temp%2 == 0:
                            if temp == 2:
                                print(f"\033[1m{k:>55}\033[0m: {i[data.index(k)+1]}, {linedata[data.index(k)-1][i[data.index(k)+1]]}")
                            else:
                                print(f"\033[1m{k}\033[0m: {i[data.index(k)+1]}, {linedata[data.index(k)-1][i[data.index(k)+1]]}")
                        else: 
                            if temp !=1:
                                if temp ==9:
                                    dic = {"A":0,"B":1,"C":2,"D":3,"E":4,"X":5}
                                    print(f"\033[1m{k:<20}\033[0m: {i[data.index(k)+1]:<100}",f"{linedata[7][dic[i[9]]]:<50}", end="")
                                    
                                else:
                                    print(f"\033[1m{k:<20}\033[0m: {i[data.index(k)+1]:<20}",f"{linedata[data.index(k)-1][i[data.index(k)+1]]:<50}", end="")

                            else:
                                print(f"\033[1m{k:<20}\033[0m: {i[data.index(k)+1]:<20}", end="")
                                
                print("\n")

main()