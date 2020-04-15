import random

def diceRoll(num,dice):
    res = 0
    for i in range(num):
        res+=random.randint(1,dice)
    return res

class Race:
    def __init__(self):
        pass

    def getGender():
        pass

    def getAge():
        pass

    def getName(gender):
        pass

    def getHeight():
        pass

    def getWeight():
        pass

    def getAlignment():
        return random.choice(ALLIGNMENTS)

class Minotaur(Race):
    maxAge = 150
    def getGender():
        return random.choice(["Male","Female"])

    def getAge():
        return diceRoll(3,Minotaur.maxAge//3)

    def getName(gender):
        if gender.lower()=="male":
            return random.choice(['Alovnek','Brogmir','Brozhdar','Dornik','Drakmir','Drazhan','Grozdan','Kalazmir','Klattic','Melislek','Nirikov','Prezhlek','Radolak','Rugilar','Sarovnek','Svarakov','Trovik','Vraslak','Yarvem'])
        if gender.lower()=="female":
            return random.choice(['Akra','Bolsa','Cica','Dakka','Drakisla','Eleska','Enka','Irnaya','Jaska','Kalka','Makla','Noraka','Pesha','Raisha','Sokali','Takyat','Vrokya','Veska','Yelka','Zarka','Zoka'])

    def getHeight():
        return 5*12+4+diceRoll(2,8)

    def getWeight(height):
        return 175+((height-(5*12+4))*diceRoll(2,6))

    def getAlignment():
        return random.choice(["Lawful good","Neutral good","Chaotic good","Lawful neutral","Neutral neutral","Chaotic neutral"])

    def __repr__(self):
        return "Minotaur"

class Centaur(Race):
    maxAge = 100
    def getGender():
        return random.choice(["Male","Female"])

    def getAge():
        return diceRoll(3,Centaur.maxAge//3)

    def getName(gender):
        candidates = ""
        if gender.lower()=="male":
            candidates = "Bonmod, Boruvo, Chodi, Drozan, Kozim,Milosh, Ninos, Oleksi, Orval, Radovas, Radom, Rostis,Svetyos, Tomis, Trijiro, Volim, Vlodim, Yarog".replace(" ","")
        if gender.lower()=="female":
            candidates = "Daiva, Dunja, Elnaya, Galisnya, Irinya,Kotyali, Lalya, Litisia, Madya, Mira, Nedja, Nikya,Ostani, Pinya, Rada, Raisya, Stasolya, Tatna, Zhendoya,Zoria".replace(" ","")
        return random.choice(candidates.split(","))

    def getHeight():
        return 6*12+random.randint(1,10)

    def getWeight(height):
        return 600+((height-(6*12))*diceRoll(2,10))

    def getAlignment():
        return random.choice(["Neutral good","Chaotic good","Lawful neutral","Neutral neutral","Chaotic neutral","Neutral evil"])

    def __repr__(self):
        return "Centaur"

class Human(Race):
    maxAge = 100
    def getGender():
        return random.choice(["Male","Female"])

    def getAge():
        return diceRoll(3,Human.maxAge//3)

    def getName(gender):
        candidates = ""
        if gender.lower()=="male":
            candidates = "Agmand, Agosto, Bell, Brev,Dars, Dobromir, Dravin, Evern, Gorey, vos, Janik,Juri, Lannos, Lucian, Micas, Nikos, Obez, Olrik,Osidar, Rogad, Sergiu, Sirislav, Tibor, Trigori, Tzaric,Uzric, Valen, Vennick, Vict, Vorimir, Vuliev, Zunak".replace(" ","")
        if gender.lower()=="female":
            candidates = "Anksa, Aszala, Berta, Bori,Briska, Dahlya, Geetra, Izolda, Jozica, Lavinia, Luda,Lyzolda, Milana, Miotri, Nefara, Palla, Pel, Ruba,Strava, Sulli, Vina, Voka, Zija".replace(" ","")
        return random.choice(candidates.split(","))

    def getHeight():
        return 4*12+8+diceRoll(2,10)

    def getWeight(height):
        return 110+((height-(4*12+8))*diceRoll(2,4))

    def getAlignment():
        return random.choice(ALLIGNMENTS)

    def __repr__(self):
        return "Human"

class Half_Elf(Race):
    maxAge = 180
    def getGender():
        return random.choice(["Male","Female"])

    def getAge():
        return diceRoll(3,Half_Elf.maxAge//3)

    def getName(gender):
        candidates = ""
        if gender.lower()=="male":
            candidates = "Agmand, Agosto, Bell, Brev,Dars, Dobromir, Dravin, Evern, Gorey, vos, Janik,Juri, Lannos, Lucian, Micas, Nikos, Obez, Olrik,Osidar, Rogad, Sergiu, Sirislav, Tibor, Trigori, Tzaric,Uzric, Valen, Vennick, Vict, Vorimir, Vuliev, Zunak".replace(" ","")
            candidates += ",Alcarus, Aramin, Beryan, Carric, Ezoc,Gurras, Immeral, Jarad, Laucian, Mihas, Mandor, Molander,Peren, Suniel, Theren, Varis".replace(" ","")
        if gender.lower()=="female":
            candidates = "Anksa, Aszala, Berta, Bori,Briska, Dahlya, Geetra, Izolda, Jozica, Lavinia, Luda,Lyzolda, Milana, Miotri, Nefara, Palla, Pel, Ruba,Strava, Sulli, Vina, Voka, Zija".replace(" ","")
            candidates += ",Arin, Bethrynna, Cevraya, Dainya,Drusilia,Elga, Emmara, Fonn, Ielenya, Iveta, Karissa,Kirce, Meriele, Nayine, Niszka, Svania, Veszka, Yeva".replace(" ","")
        return random.choice(candidates.split(","))

    def getHeight():
        return 4*12+9+diceRoll(2,8)

    def getWeight(height):
        return 110+((height-(4*12+9))*diceRoll(2,4))

    def getAlignment():
        return random.choice(["Neutral good","Chaotic good","Neutral neutral","Chaotic neutral","Neutral evil","Chaotic evil"])

    def __repr__(self):
        return "Half-Elf"

class Elf(Race):
    maxAge = 750
    def getGender():
        return random.choice(["Male","Female"])

    def getAge():
        return diceRoll(3,Elf.maxAge//3)

    def getName(gender):
        candidates = ""
        if gender.lower()=="male":
            candidates = "Alcarus, Aramin, Beryan, Carric, Ezoc,Gurras, Immeral, Jarad, Laucian, Mihas, Mandor, Molander,Peren, Suniel, Theren, Varis".replace(" ","")
        if gender.lower()=="female":
            candidates = "Arin, Bethrynna, Cevraya, Dainya,Drusilia,Elga, Emmara, Fonn, Ielenya, Iveta, Karissa,Kirce, Meriele, Nayine, Niszka, Svania, Veszka, Yeva".replace(" ","")
        return random.choice(candidates.split(","))

    def getHeight():
        return 4*12+6+diceRoll(2,10)

    def getWeight(height):
        return 100+((height-(4*12+6))*(random.randint(1,4)))

    def getAlignment():
        return random.choice(ALLIGNMENTS)

    def __repr__(self):
        return "Elf"

class High_Elf(Elf):
    def getHeight():
        return 4*12+6+diceRoll(2,10)

    def getWeight(height):
        return 90+((height-(4*12+6))*(random.randint(1,4)))

    def __repr__(self):
        return "High Elf"

class Wood_Elf(Elf):
    def getHeight():
        return 4*12+6+diceRoll(2,10)

    def getWeight(height):
        return 100+((height-(4*12+6))*(random.randint(1,4)))

    def __repr__(self):
        return "Wood Elf"

class Dark_Elf(Elf):
    def getHeight():
        return 4*12+5+diceRoll(2,6)

    def getWeight(height):
        return 75+((height-(4*12+5))*(random.randint(1,6)))

    def __repr__(self):
        return "Dark Elf"

class Goblin(Race):
    maxAge = 60
    def getGender():
        return random.choice(["Male","Female"])

    def getAge():
        return diceRoll(3,Goblin.maxAge//3)

    def getName(gender="Default"):
        candidates = "Azzinax, Babolax, Blixanix, Crixizi,Dazzaz, Estrix, Finizix, Juzba, Kaluzax, Lyzaxa,Mizzix, Myznar, Nixispix, Paxizaz, Ravixiz, Stixil,Sunnix, Tozinox, Uxivozi, Vazozav, Wexiny, Zizzix".replace(" ","")
        return random.choice(candidates.split(","))

    def getHeight():
        return 3*12+5+diceRoll(2,4)

    def getWeight(height):
        return 35+height-(3*12+5)

    def getAlignment():
        return random.choice(["Chaotic good","Chaotic neutral","Chaotic evil"])

    def __repr__(self):
        return "Goblin"

class Loxodon(Race):
    maxAge = 450
    def getGender():
        return random.choice(["Male","Female"])

    def getAge():
        return diceRoll(3,Loxodon.maxAge//3)

    def getName(gender):
        candidates = ""
        if gender.lower()=="male":
            candidates = "Bayul, Berov, Brooj, Chedumov, Dobrun,Droozh, Golomov, Heruj, Ilromov, Kel, Nikoom, Ondros,Radomov, Svetel, Tamuj, Throom, Vasool".replace(" ","")
        if gender.lower()=="female":
            candidates = "Ajj, Boja, Dancu, Dooja, Elyuja, Fanoor,Irij, Jasoo, Katrun, Lyooda, Mayja, Radu, Shuja,Soofya, Totoor, Verij, Vesmova, Yoolna, Zarij, Zoorja".replace(" ","")
        return random.choice(candidates.split(","))

    def getHeight():
        return 6*12+7+diceRoll(2,10)

    def getWeight(height):
        return 295+((height-(6*12+7))*diceRoll(2,4))

    def getAlignment():
        return random.choice(["Lawful good","Lawful good","Lawful neutral","Lawful evil"])

    def __repr__(self):
        return "Loxodon"

class Vedalken(Race):
    maxAge = 350
    def getGender():
        return random.choice(["Male","Female"])

    def getAge():
        return diceRoll(3,Vedalken.maxAge//3)

    def getName(gender):
        candidates = ""
        if gender.lower()=="male":
            candidates = "Aglar, Bellin, Dallid, Firellan, Kavin,Koplony, Lomar, Mathvan, Modar, Nebun, Nhillosh,Nitt, Otrovac, Ovlan, Pelener, Rill, Trivaz, Uldin,Yolov, Zataz".replace(" ","")
        if gender.lower()=="female":
            candidates = "Azi, Barvisa, Brazia, Direll, Fainn,Griya, Hallia, Katrille, Kovel, Lilla, Mirela, Morai,Nedress, Ossya, Pierenn, Roya, Sestri, Triel, Uzana,Yaraghiya, Zlovol".replace(" ","")
        return random.choice(candidates.split(","))

    def getHeight():
        return 5*12+4+diceRoll(2,10)

    def getWeight(height):
        return 110+((height-(5*12+4))*diceRoll(2,4))

    def getAlignment():
        return random.choice("Lawful good","Lawful neutral")

    def __repr__(self):
        return "Vedalken"

class Guild:
    def __init__(self):
        pass

    def getAlignment():
        pass

    def getRace():
        pass

    def getClass():
        pass

    def getRole(npcClass):
        pass

    def __repr__(self):
        return "Guild"

class Azorius(Guild):
    def getAlignment():
        return random.choice(["Lawful good","Lawful neutral","Lawful neutral","Lawful evil"])

    def getRace():
        return random.choice([Human,Vedalken])

    def getClass():
        return random.choice("bard, cleric, fighter, paladin, wizard".replace(" ","").split((",")))

    def getRole(npcClass):
        candidates = set()
        if npcClass.lower() in ["wizard","cleric","bard"]:
            candidates.add("lawmage")
        if npcClass.lower() in ["wizard","cleric"]:
            candidates.add("precognitive mage")
        if npcClass.lower() in ["cleric","fighter","paladin"]:
            candidates.add("arrester")
        if npcClass.lower() in ["cleric","bard","paladin","wizard"]:
            candidates.add("elocutor")

        return random.choice(list(candidates))

    def __repr__(self):
        return "Azorius Senate"

class Boros(Guild):
    def getAlignment():
        return random.choice(["Lawful good","Lawful good","Neutral good","Chaotic good","Lawful neutral","Lawful neutral"])

    def getRace():
        return random.choice([Human,Goblin,Minotaur,Centaur])

    def getClass():
        return random.choice("cleric, fighter, paladin,ranger, wizard".replace(" ","").split((",")))

    def getRole(npcClass):
        candidates = set()
        if npcClass.lower() in ["fighter","ranger","paladin","cleric"]:
            candidates.add("soldier")
            candidates.add("swiftblade")
        if npcClass.lower() in ["wizard","cleric"]:
            candidates.add("embermage")
            candidates.add("medic")
        if npcClass.lower() in ["cleric","fighter","paladin"]:
            candidates.add("firefist")

        return random.choice(list(candidates))

    def __repr__(self):
        return "Boros Legion"

class Dimir(Guild):
    def getAlignment():
        return random.choice(["Lawful neutral","Neutral neutral","Chaotic neutral","Lawful evil"])

    def getRace():
        return random.choice([Human,Half_Elf])

    def getClass():
        return random.choice("monk,rogue, wizard".replace(" ","").split((",")))

    def getRole(npcClass):
        return "Agent"

    def __repr__(self):
        return "House Dimir"

class Golgari(Guild):
    def getAlignment():
        return random.choice(["Lawful neutral","Neutral neutral","Chaotic neutral","Lawful evil","Neutral evil","Chaotic evil"])

    def getRace():
        return random.choice([Human,Dark_Elf])

    def getClass():
        return random.choice("druid,fighter,ranger,rogue, wizard".replace(" ","").split((",")))

    def getRole(npcClass):
        candidates = set()
        if npcClass.lower() in ["druid","wizard"]:
            candidates.add("shaman")
        if npcClass.lower() in ["fighter","ranger","rogue"]:
            candidates.add("shock trooper")
        if npcClass.lower() in ["ranger","rogue"]:
            candidates.add("skirmisher")

        return random.choice(list(candidates))

    def __repr__(self):
        return "Golgari Swarm"

class Gruul(Guild):
    def getAlignment():
        return random.choice(["Lawful neutral","Neutral neutral","Chaotic neutral","Lawful evil","Neutral evil","Chaotic evil"])

    def getRace():
        return random.choice([Human,Dark_Elf])

    def getClass():
        return random.choice(['barbarian', 'cleric', 'druid', 'fighter', 'ranger'])

    def getRole(npcClass):
        candidates = set()
        if npcClass.lower() in ["druid","cleric"]:
            candidates.add("follower of the old way")
        if npcClass.lower() in ['barbarian','fighter', 'ranger']:
            candidates.add("gruul warrior")

        return random.choice(list(candidates))

    def getClan():
        candidates = ['Burning Tree Clan', 'Ghor Clan', 'Scab Clan', 'Slizt Clan', 'Gravel Hide Clan', 'Zhur-Taa Clan', 'Bolrac Clan', 'Trogs']
        return random.choice(list(candidates))

    def __repr__(self):
        return "Gruul Clans"

class Izzet(Guild):
    def getAlignment():
        return random.choice(["Lawful neutral","Neutral neutral","Chaotic neutral","Chaotic neutral","Chaotic good","Chaotic evil"])

    def getRace():
        return random.choice([Human,Goblin,Vedalken])

    def getClass():
        return random.choice(['wizard', 'fighter', 'sorcerer'])

    def getRole(npcClass):
        candidates = {"attendant","researcher","wizard","guard","scorchbringer"}

        return random.choice(list(candidates))

    def __repr__(self):
        return "Izzet League"

class Orzhov(Guild):
    def getAlignment():
        return random.choice(["Lawful neutral","Lawful good","Lawful evil","Neutral evil"])

    def getRace():
        return random.choice([Human])

    def getClass():
        return random.choice(['cleric', 'fighter', 'rogue', 'wizard'])

    def getRole(npcClass):
        candidates = set()
        if npcClass.lower() in ["wizard","cleric"]:
            candidates.add("advokist")
        if npcClass.lower() in ['fighter','rogue', 'cleric']:
            candidates.add("enforcer")
        if npcClass.lower() in ['cleric']:
            candidates.add("priest")


        return random.choice(list(candidates))

    def __repr__(self):
        return "Orzhov Syndicate"

class Rakdos(Guild):
    def getAlignment():
        return random.choice(["Chaotic neutral","Chaotic good","Lawful evil","Neutral evil","Chaotic evil"])

    def getRace():
        return random.choice([Human,Goblin])

    def getClass():
        return random.choice(['barbarian', 'bard', 'fighter', 'warlock'])

    def getRole(npcClass):
        candidates = set()
        candidates.add("performer")

        return random.choice(list(candidates))

    def __repr__(self):
        return "Cult of Rakdos"

class Selesnya(Guild):
    def getAlignment():
        return random.choice(["Lawful good","Neutral good","Chaotic good","Lawful good","Neutral good","Chaotic good","Lawful neutral","Neutral neutral","Chaotic neutral","Chaotic evil"])

    def getRace():
        return random.choice([Human,Centaur,Wood_Elf,Half_Elf,Loxodon])

    def getClass():
        return random.choice(['bard', 'cleric', 'druid', 'fighter', 'monk', 'paladin', 'ranger', 'warlock'])

    def getRole(npcClass):
        candidates = set()
        if npcClass.lower() in ['bard','fighter', 'paladin', 'ranger']:
            candidates.add("soldier")
        if npcClass.lower() in ['cleric', 'druid', 'monk', 'warlock']:
            candidates.add("priest")


        return random.choice(list(candidates))

    def __repr__(self):
        return "Selesnya Conclave"

class Simic(Guild):
    def getAlignment():
        return random.choice(["Lawful neutral","Neutral neutral","Chaotic neutral"])

    def getRace():
        return random.choice([Human,High_Elf,Vedalken])

    def getClass():
        return random.choice(['druid', 'fighter', 'monk', 'wizard'])

    def getRole(npcClass):
        candidates = set()
        if npcClass.lower() in ['druid', 'wizard']:
            candidates.add("scientist")
        if npcClass.lower() in ['druid', 'fighter', 'monk']:
            candidates.add("guardian")
        if npcClass.lower() in ['monk', 'wizard']:
            candidates.add("deepsage")

        return random.choice(list(candidates))

    def __repr__(self):
        return "Simic Combine"

class Guildless(Guild):
    def getAlignment():
        return random.choice(ALLIGNMENTS)

    def getRace():
        res = random.choice(RACES)
        if res == Elf:
            return random.choice([Wood_Elf,High_Elf,Dark_Elf])
        else:
            return res

    def getClass():
        return random.choice(CLASSES)

    def getRole(npcClass):
        return ""

    def __repr__(self):
        return "Guildless"


ALLIGNMENTS = ["Lawful good","Neutral good","Chaotic good","Lawful neutral","Neutral neutral","Chaotic neutral","Lawful evil","Neutral evil","Chaotic evil"]
GUILDS = [Azorius,Boros,Dimir,Golgari,Gruul,Izzet,Orzhov,Rakdos,Selesnya,Simic]
RACES = [Human,Elf,Centaur,Goblin,Loxodon,Minotaur,Vedalken]
CLASSES = ['barbarian','bard', 'cleric', 'druid', 'fighter', 'monk', 'paladin', 'ranger','rogue','sorcerer', 'warlock','wizard']
