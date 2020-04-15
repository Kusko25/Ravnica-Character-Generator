import database as db
import numpy.random as npr

class Character:
    def __init__(self,**kwargs):
        self.miscFields = dict()

        if "guild" in kwargs:
            self.guild = kwargs["guild"]
        else:
            if npr.random()<=0.3:
                self.guild = db.Guildless
            else:
                self.guild = npr.choice(db.GUILDS)

        if "race" in kwargs:
            self.race = kwargs["race"]
        else:
            self.race = self.guild.getRace()

        if "class" in kwargs:
            self.npcClass = kwargs["class"]
        else:
            self.npcClass = self.guild.getClass()

        if self.guild == db.Gruul:
            if "clan" in kwargs:
                self.miscFields["clan"] = kwargs["clan"]
            else:
                self.miscFields["clan"] = self.guild.getClan()

        if "role" in kwargs and "guild" in kwargs:
            self.miscFields["role"] = kwargs["role"]
        else:
            if self.guild is not db.Guildless:
                self.miscFields["role"] = self.guild.getRole(self.npcClass)

        if "alignment" in kwargs:
            self.alignment = kwargs["alignment"]
        else:
            self.alignment = self.guild.getAlignment()


        if "gender" in kwargs:
            self.gender = kwargs["gender"]
        else:
            self.gender = self.race.getGender()

        if "name" in kwargs:
            self.name = kwargs["name"]
        else:
            self.name = self.race.getName(self.gender)

        if "age" in kwargs:
            self.age = kwargs["age"]
        else:
            self.age = self.race.getAge()

        if "height" in kwargs:
            self.height = kwargs["height"]
        else:
            self.height = self.race.getHeight()

        if "weight" in kwargs:
            self.weight = kwargs["weight"]
        else:
            self.weight = self.race.getWeight(self.height)

    def printChar(self):
        def myPrint(string):
            with open("newCharacters.txt","a") as out:
                print(string)
                print(string,file=out)

        myPrint(f"Name: {self.name.capitalize()}")
        myPrint("")
        myPrint(f"Race: {str(self.race()).capitalize()}")
        myPrint(f"Class: {self.npcClass.capitalize()}")
        myPrint("")
        myPrint(f"Gender: {self.gender.capitalize()}")
        myPrint(f"Age: {self.age} years (out of {self.race.maxAge} years)")
        myPrint(f"Height: {self.height//12}'{self.height%12}\" ({int(self.height*2.54)}cm)")
        myPrint(f"Weight: {self.weight}lbs ({int(self.weight*0.4535924)}kg)")
        myPrint("")
        myPrint(f"Alignment: {self.alignment.capitalize()}")
        myPrint(f"Guild: {self.guild()}")
        if "clan" in self.miscFields:
            myPrint(f"Clan: {self.miscFields['clan'].capitalize()}")
        if "role" in self.miscFields:
            myPrint(f"Role: {self.miscFields['role'].capitalize()}")

        myPrint("\n==============\n")




def scanChar():
    guildDict = {"azorius":db.Azorius,"boros":db.Boros,"dimir":db.Dimir,"golgari":db.Golgari,"gruul":db.Gruul,"izzet":db.Izzet,"orzhov":db.Orzhov,"rakdos":db.Rakdos,"selesnya":db.Selesnya,"simic":db.Simic}
    raceDict = {"human":db.Human,"wood elf":db.Wood_Elf,"high elf":db.High_Elf,"dark elf":db.Dark_Elf,"centaur":db.Centaur,"goblin":db.Goblin,"loxodon":db.Loxodon,"minotaur":db.Minotaur,"vedalken":db.Vedalken}
    genders = ["Male","Female"]

    print("Enter characteristics split by '/' or leave blank for random:")
    print("Guild, race, class and gender are automatically recognized")
    print("The remaining attributes should be entered in the form: 'attrib=value'")
    print("Available attributes are:")
    print("\t- age in years(age=12)")
    print("\t- height in inches(height=67)")
    print("\t- weight in lbs(weight=132)")
    print("\t- alignment (alignment=Lawful evil)")
    print("\t- clan (clan=Stubs)")
    print("\t- role (role=Lab Assistant)")
    print("Example: Male/Human/Rogue/Dimir/age=56")

    inString = input()
    parameters = [x.strip() for x in inString.split("/")]
    attributes = dict()

    for par in parameters:
        if "=" in par:
            key,value = par.split("=",1)
            key = key.lower();value = value.lower()
            if key in ["age","height","weight"]:
                try:
                    attributes[key]=int(value)
                except Exception as e:
                    print(f"'{par}' is malformatted and will be ignored.")
            else:
                attributes[key]=value
        else:
            if par.lower() in guildDict:
                attributes["guild"] = guildDict[par.lower()]
            elif par.lower() in raceDict:
                attributes["race"] = raceDict[par.lower()]
            elif par.lower() in db.CLASSES:
                attributes["class"] = par.lower()
            elif par.lower() in ["male","female"]:
                attributes["gender"] = par.lower()
    print("\n==============\n")

    char = Character(**attributes)
    char.printChar()



def main():
    print("Welcome to the Ravnica Char Gen!")
    while True:
        scanChar()
        if input("Press Enter to continue or type exit...").lower().strip()=="exit":
            break

if __name__ == '__main__':
    main()
