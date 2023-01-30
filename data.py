database = [
    {
    "name":"Hector Liguori", 
    "human": True,
    "parte del hub": True,
    "youtuber": False,
    "level +10": True,
    "iD 0303456": False,
    "tiene Anteojos": False,
    "pelo corto": True,
    "parte de Innovation": True,
    "argentin@":True,

    },
    {
    "name":"Diego Martins", 
    "human": True,
    "parte del hub": False,
    "youtuber": False,
    "level +10": True,
    "iD 0303456": False,
    "tiene Anteojos": False,
    "pelo corto": True,
    "parte de Innovation": True,
    "argentin@":True,

    },
    {
    "name":"hola hola", 
    "human": True,
    "parte del hub": True,
    "youtuber": False,
    "level +10": True,
    "iD 0303456": False,
    "tiene Anteojos": False,
    "pelo corto": False,
    "parte de Innovation": False,
    "argentin@":True,

    },
    {
    "name":"chau chau", 
    "human": True,
    "parte del hub": True,
    "youtuber": False,
    "level +10": True,
    "iD 0303456": False,
    "tiene Anteojos": False,
    "pelo corto": True,
    "parte de Innovation": True,
    "argentin@":True,

    },
    {
    "name":"pitufa gandolfo",
    "human": True,
    "parte del hub": True,
    "youtuber": False,
    "level +10": True,
    "iD 0303456": True,
    "tiene Anteojos": True,
    "pelo corto": True,
    "parte de Innovation": True,
    "argentin@":True,

    }
]


def take_chance(answer, property):
    if answer == "y":
        ans = True
    else: 
        ans = False 
    
    to_remove=[]
    for d in database:
        if d[property] != ans:
            to_remove.append(d)

    for i in to_remove:
        database.remove(i)
    
    if len(database) == 1:
        print("your character is "+database[0]["name"])
        quit ()

ans = input( "Is your character human(y,n)")
take_chance(ans, "human" )

ans = input("Is your character part of the hub(y,n)")
take_chance(ans, "parte del hub")

ans = input("Is your character youtuber(y,n)")
take_chance(ans, "youtuber" )

ans = input("Is your character level up +10(y,n)")
take_chance(ans, "level +10" )

ans = input("Is your character iD:0303456?")
take_chance(ans,"iD 0303456")

ans = input("Does your character regularly wear glasses(y,n)")
take_chance(ans, "glasses" )

ans = input("Does your character have short hair(y,n)")
take_chance(ans, "short hair" )

ans = input( "Is your character part of Innovation(y,n)")
take_chance(ans, "innovation" )

ans = input("Your character is of Argentine nationality(y,n)")
take_chance(ans, "nationality" )
