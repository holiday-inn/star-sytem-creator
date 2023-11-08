import random
import json

class star():
    size = 0
    atmos = 0
    hydros = 0
    populus = 0
    govt = 0
    lawlvl = 0
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
        # if size<1, hydro = 0. if atmos <1
        #gotta have a bunch of technicalities
        self.pop = (random.randint(1,6) + random.randint(1,6) - 2)
        self.govt = (random.randint(1,6) + random.randint(1,6) - 7 + self.populus)
        self.lawlvl = (random.randint(1,6) + random.randint(1,6) - 7 + self.govt)
        #need tech level, gotta ask quechuns
        
        
        line = open("tables.csv","r").read().split("\n")
            
        def info(varname):
            info = json.loads(line[random.randint(1,6) + random.randint(1,6)-2])
            return info[varname]
        
        def techlvl():
            num = random.randint(0,8) + random.randint(0,8)
            info = json.loads(line[num+12])
            
            return info

        info('die'),self.size,self.hyd,self.atm
        
        if info('starport') == "A"
        self.starport 
        self.naval = info('naval')
        self.scout = info('scout')
        self.gas = info('gas')
        self.plane = info('plane')

        print(self.starport,self.naval,self.scout,self.gas,self.plane)

        tech = techlvl()
        self.size += (tech['size'])
        self.size += (tech['size'])
        self.atm += (tech['atm'])
        self.hyd += (tech['hyd'])
        self.pop += (tech['pop'])
        self.govt += (tech['govt'])
        
        
        print(self.size,self.atm,self.hyd,self.pop,self.govt)
        
        
        
        



star()




