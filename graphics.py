import tkinter as tk 
from tkinter import *
from tkinter import ttk
import random,json,math,sqlite3


class star():
    worldname = None
    
    size = 0;atm = 0;hyd = 0;pop = 0;govt = 0;lawlvl = 0;tech = 0;starport = None;naval = None;scout = None;gas = None;plane = None;lvl = 0
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
        self.data = open("tables.csv","a");self.worldname = randname();self.size = (random.randint(1,6) + random.randint(1,6) - 2);self.atm = (random.randint(1,6) + random.randint(1,6) - 7 + self.size)
        if self.size == 0:self.atm = 0
        self.hyd = (random.randint(1,6) + random.randint(1,6) - 7 + self.size)
        if self.size < 1: self.hyd = 0
        if self.atm < 1 or self.atm > 10: self.atm -=4
        if self.hyd < 0: self.hyd = 0
        if self.atm > 10: self.atm = 10
        self.pop = (random.randint(1,6) + random.randint(1,6) - 2);self.govt = (random.randint(1,6) + random.randint(1,6) - 7 + self.pop)
        if self.govt < 0: self.govt = 0
        self.lawlvl = (random.randint(1,6) + random.randint(1,6) - 7 + self.govt)
        if self.atm <= 0: self.atm = 0
        if self.lawlvl < 0: self.lawlvl = 0
        if self.lawlvl > 10: self.lawlvl = 10
        if self.pop > 9: self.pop = 9
        if self.govt > 13: self.govt = 13
        line = open("tables.csv","r").read().split("\n")   
        def info(varname):
            multi = 0;twodie = random.randint(1,6) + random.randint(1,6);tempstar = json.loads(line[twodie-2])
            if varname == 'scout':
                if tempstar == "A":multi = -3                  
                elif tempstar == "B":multi = -2
                elif tempstar == "C":multi = -1
            elif varname == 'naval':
                if tempstar == "C" or tempstar == "D" or tempstar == "E"or tempstar == "X":return False
            info = json.loads(line[twodie-2+multi])
            return info[varname]
        def techlvl():
            tech = random.randint(1,6)
            data = open("table2.csv","r").read().split("\n")
            if self.starport == "A":tech+= 6
            elif self.starport == "B":tech+= 4
            elif self.starport == "C":tech+= 2
            elif self.starport == "X":tech-= 4
            nums = [self.size,self.atm,self.hyd,self.pop,self.govt];count = 0
            list = ["size","atm","hyd","pop","govt"]
            for i in list:
                k = json.loads(data[nums[count]]);tech +=k[i];count+= 1
            return tech 
        self.starport = info('starport');self.naval = info('naval');self.scout = info('scout');self.gas = info('gas');self.plane = info('plane');self.lvl = techlvl()
        if self.lvl < 0: self.lvl
        self.forlatersql() 
data = ["Name","Size","Atmosphere","Hydration","Population","Government","Law","Technology","Starport","Naval Base exists","Scout exists","Gas giant exists","Planetoids exist"];bignum = 0;numba = 10
qdata = ["name","size","atm","hyd","pop","govt","law","tech","starport","naval","scout","gas","plane"]

def notprinting():
    global data,bignum,numba
    connection = sqlite3.connect('dbase.db')
    cursor = connection.cursor()
    if bignum == 0:       
        cursor.execute('drop table stars')
        connection.commit()  
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
    for i in range(10):star();print('pop')
    
notprinting()

def printing(thing,inp):
    connection = sqlite3.connect('dbase.db')
    cursor = connection.cursor()
    if thing != 'all':
        query = f"select * from stars where {thing} = '{inp}'"
    elif thing == 'all':
        query = f"select * from stars"
    cursor.execute(query)
    result = cursor.fetchall()
    minf = []
    
    for i in result:
        sinf = []
        for k in data:
            info = []
            temp = data.index(k)+1
            if temp%2 == 0:
                info.append( f"{k}: {i[temp]}  ")
            else: info.append(f"{k}: {i[temp]}  ")
            sinf.append(info)
        text = ''
        for i in sinf:

            text+=  (f'{i[0]}' + "\n")
        minf.append(text)

    return minf

window = tk.Tk()
stars = PhotoImage(file="stars.png")
image = tk.Label(window, image=stars)
window.geometry("700x600")
window.configure(background="#ffffff")
window.title("Star System Generator")

label1 = tk.Label(window,text="Star System Generator",background="#ffffff",font = ('Arial', 30))
label2 = tk.Button(window,text="Look",background="#ffffff",font = 15)
label3 = tk.Button(window,text="Generate",background="#ffffff",font = 15)
text = ''

inf = printing('all',None)
num = 0

databox = tk.Label(window,text=f"{inf[num]}\n Page {num+1}/{len(inf)}",background="#ffffff",width = 60,height = 22,wraplength= 200)
arrowprev = tk.Button(window,text="< Previous",relief=GROOVE,width=29,background="#ffffff")
arrownex = tk.Button(window,text="Next >",relief=GROOVE,width=29,background="#ffffff")
entry = tk.Entry(window,background="#ffffff",width=15)
entry2 = tk.Entry(window,background="#ffffff",width=15)

databox.place(x =220,y = 90)
entry.place(x=0,y=800)
entry2.place(x=20,y=60)
image.place(x=0,y=0)
label1.place(x=230,y=30)
label2.place(x=20,y=100)
label3.place(x=20,y=20)
arrownex.place(x=433,y=424)
arrowprev.place(x=220,y=424)


def entryclick(e):
    global entry,thing
    entry.destroy()
    entry = tk.Entry(window,background="#ffffff",width=15)
    entry.bind("<Return>",aclick)
    yy = window.winfo_pointery()-window.winfo_y()-40
    entry.place(x=120,y=yy)
    thing = qdata[math.floor((yy-140)/30)]

def aclick(e):
    global thing,num
    connection = sqlite3.connect('dbase.db')
    cursor = connection.cursor()
    inp = StringVar()
    inp = entry.get()

    try:
        if inp != "":

            
            global inf
            inf = printing(thing,inp)
            num = 0
            databox = tk.Label(window,text=f"{inf[num]}\n Page {num+1}/{len(inf)}",background="#ffffff",width = 60,height = 22,wraplength= 200)
            databox.place(x =220,y = 90)
    except:
        databox = tk.Label(window,text=f"No Results",background="#ffffff",width = 60,height = 22,wraplength= 200)
        databox.place(x =220,y = 90)

def click(e):
    button = []
    for i in data:
        button.append(tk.Button(window, text = f"{i}",background="#ffffff"))
        button[data.index(i)].place(x=20,y=((data.index(i))*30)+150,width = 100)
        
    button.append(tk.Button(window, text = "All",background="#ffffff"))
    button[-1].place(x=20,y=550,width = 100)
    button[-1].bind("<Button-1>",all)

    for i in range(len(button)):
        if i !=13:
            button[i].bind("<Button-1>",entryclick)

def prev(e):
    global num,inf
    if inf!= []:
        if num != 0:num-=1
        else:num = len(inf)-1
        databox = tk.Label(window,text=f"{inf[num]}\n Page {num+1}/{len(inf)}",background="#ffffff",width = 60,height = 22,wraplength= 200)
        databox.place(x =220,y = 90)

def next(e):
    global num,inf
    if inf!= []:
        num +=1
        if num >= len(inf): num =0
        databox = tk.Label(window,text=f"{inf[num]}\n Page {num+1}/{len(inf)}",background="#ffffff",width = 60,height = 22,wraplength= 200)
        databox.place(x = 220,y = 90)
    
def gen(e):
    global inf,num

    inp = IntVar()
    inp = int(entry2.get())
    for i in range(inp): star()


    inf = printing('all',None)
    databox = tk.Label(window,text=f"{inf[num]}\n Page {num+1}/{len(inf)}",background="#ffffff",width = 60,height = 22,wraplength= 200)
    databox.place(x = 220,y = 90)


def all(e):
    global inf
    inf = printing('all',None)
    databox = tk.Label(window,text=f"{inf[num]}\n Page {num+1}/{len(inf)}",background="#ffffff",width = 60,height = 22,wraplength= 200)
    databox.place(x = 220,y = 90)

label2.bind("<Button-1>",click)
arrowprev.bind("<Button-1>",prev)
arrownex.bind("<Button-1>",next)
entry2.bind("<Return>",gen)

window.mainloop()