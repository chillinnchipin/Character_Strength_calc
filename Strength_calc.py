#Ronald Hardy Jr
# V0.2.0 6/20/2023
import math
# TODO: Setup app using flask
# TODO: intergrate sql with
# TODO: create docker image & run in container

class Character:
    # TODO: Finish character class for saving characters
    def __init__(self, name, offenStrn = 50, defenStrn = 50, speed = 30, adgility = 4, manaCap = 1000, maxOutput = 500,regenRate = 10, iq = 100, biq = 50, knowl = 50):
        #instance info
        self.name = name
        self.spellList = []

        #instance states
        self.offenStrn = offenStrn
        self.defenStrn = defenStrn
        self.speed = speed
        self.adgility = adgility
        self.manaCap = manaCap
        self.maxOutput = maxOutput
        self.regenRate = regenRate
        self.iq = iq
        self.biq = biq
        self.knowl = knowl

        #declares instance levels
        self.phsLvl = calcPhysical(offenStrn, defenStrn, speed, adgility)
        self.magLvl = calcMagical(manaCap, maxOutput,regenRate)
        self.mentlvl = calcMental(iq, biq, knowl)
        self.powerLvl = calcPowerLvl(self.phsLvl, self.magLvl, self.mentlvl)
        self.numLvl = calcNumLvl(self.powerLvl)
    
    def addSpell(self, spell: str):
        self.spellList.append(spell)
    def veiwSpells(self):
        toReturn = ''
        for spell in self.spellList:
            toReturn += spell + ', '
        return toReturn
    def printSpells(self):
        for spell in self.spellList:
            print(spell, end = " ")
        print()

    def __str__ (self):
        toReturn = f"{self.name}\nRank: {self.numLvl:.2f}\nPower Level: {self.powerLvl:.0f}"
        toReturn += f"\nPhysical Level: {self.phsLvl:.0f}\tMagical Level: {self.magLvl:.0f}\tMental Level: {self.mentlvl:.0f}"
        toReturn += f"\nOffensive Strength {self.offenStrn:.1f}\tDefensive Strength {self.defenStrn:1f}\tSpeed {self.speed:.2f}\tAcceleration {self.adgility:.2f}"
        toReturn += f"\nMana Capacity {self.manaCap:.0f}\tMaximum Mana Output {self.maxOutput:.0f}\tMana Regeneration Rate {self.regenRate:.0f}"
        toReturn += f"\nIQ {self.iq:3f}\tBattle IQ {self.biq:3f}\t World Knowlege {self.knowl:3f}"
        return toReturn
    def __lt__(self, other):
        return self.powerLvl < other.powerLvl
    def __gt__(self, other):
        return self.powerLvl > other.powerLvl
    def __eq__(self, other):
        return self.name == other.name and self.powerLvl == other.powerLvl

class InvalidInput(Exception):
    pass

def calcPhysical(offenStrn, defenStrn, speed, adgility): return (0.25*offenStrn) + (0.25*defenStrn) + (0.15625*speed) + (2.5 * adgility)
def calcMental(iq, biq, knowl): return (0.25 * iq) + (0.25 * biq) + (0.25 * knowl)
def calcMagical(manaCap, maxOutput,regenRate): return (0.0004 * manaCap) + (0.0004 * maxOutput) + (0.004 * regenRate)

def calcPowerLvl(phsLvl, magLvl, mentLvl): return (0.45 * magLvl) + (0.45 * phsLvl) + (0.1 * mentLvl)
def calcPowerLvl_usingStats(offenStrn, defenStrn, speed, adgility, manaCap, maxOutput,regenRate, iq, biq, knowl):
    phsLvl = calcPhysical(offenStrn, defenStrn, speed, adgility)
    magLvl = calcMagical(manaCap, maxOutput,regenRate)
    mentlvl = calcMental(iq, biq, knowl)
    #return (0.45 * calcMagical(manaCap, maxOutput,regenRate)) + (0.45 * calcPhysical(offenStrn, defenStrn, speed, adgility)) + (0.1 * calcMental(iq, biq, knowl))
    return calcPowerLvl(phsLvl, magLvl, mentlvl)

def calcNumLvl(powerLvl):
    return 7.15 * math.log(powerLvl, 10) - 4.3
def calcNumLvl_noPwrLvl(phsLvl, magLvl, mentLvl):
    powerLvl = calcPowerLvl(phsLvl, magLvl, mentLvl)
    return calcNumLvl(powerLvl)
    #return calcNumLvl(calcPowerLvl(phsLvl, magLvl, mentLvl))
def calcNumLvl_usingStats(offenStrn, defenStrn, speed, adgility, manaCap, maxOutput,regenRate, iq, biq, knowl):
    powerLvl = calcPowerLvl(offenStrn, defenStrn, speed, adgility, manaCap, maxOutput,regenRate, iq, biq, knowl)
    return calcNumLvl(powerLvl)
    #return calcNumLvl(calcPowerLvl(offenStrn, defenStrn, speed, adgility, manaCap, maxOutput,regenRate, iq, biq, knowl))

def readFile():
    # TODO: file read and write
    raise NotImplementedError("File read and write not implemented yet.")
def saveToFile():
    raise NotImplementedError("File read and write not implemented yet.")

#def StrenthCalc():
if __name__ == "__main__":
    #Tesing

    #UI
    # TODO: run user interface for opitions and inputing data
    # TODO: add character arraylist and ability to add, remove, view, and edit characters on it
    print("Weolcome to Character Strength Calculator! \nUsing the CH Base Magic System's Power Level Rank!")
    option = -1
    menu = "\n0: Quit\n1: Input Character Stats\n2: View all saved Characters \n3: View a Character\n4: Edit Character Stats\n5: Save or Load from .txt file"
    characters = []
    while option != 0:
        try:
            print(menu)
            #print("Please enter an option: ", end = '')
            option = int(input("Please enter an option: "))
            match option:
                case 0: break
                case 1:
                    # TODO: Add inputs for character stats and use inputs to return character levels
                    offenStrn = int (input("Please enter the character's Offensive Strength (Numbers Only): "))
                    defenStrn = int(input("Please enter the character's Defensive Strength (numbers only): "))
                    speed = int(input("Please enter the character's speed in km/hr: "))
                    adgility = int(input("Please enter the character's avg running acceleration in m/s: "))
                    manaCap = int(input("Please enter the character's maximun mana capacity in mp: "))
                    maxOutput = int(input("Please enter the character's maximum mana output in mp: "))
                    regenRate = int(input("Please enter the character's mana regeneration rate in mp/hr: "))
                    iq = int(input("Please enter the character's IQ: "))
                    biq = int(input("Please enter the character's battle iq (0-100, avg 50): "))
                    knowl = int(input("Please enter the character's score on a world magic & history test (0-100, avg 50): "))
                    phsLvl = calcPhysical(offenStrn, defenStrn, speed, adgility)
                    magLvl = calcMagical(manaCap, maxOutput,regenRate)
                    mentLvl = calcMental(iq, biq, knowl)
                    powerLvl = calcPowerLvl(phsLvl, magLvl, mentLvl)
                    numRankLvl = calcNumLvl(powerLvl)
                    print(f'This Character has a Number Rank of: {numRankLvl:.2f}\nTheir Power level: {powerLvl:.0f}')
                    print(f'Other Character Stats:\nMagical Power: {magLvl:.0f}\nPhysical Level: {phsLvl:.0f}\nMental Power: {mentLvl:.0f}')
                    while option != 0:
                        print("\nWhat to do next?\n1: Return to main menu\n2: Explain Results\n3: View Character Number Rank\n4: View Character Power Level\n5: Veiw Specific Levels\n6: Save Character")
                        option = int(input("Please Selection an option:"))
                        match option:
                            case 1: break
                            case 2: print('The number rank is a simple numerical measurement of a character strength (typicall 0-10) that uses a logarthic equation to easily compare character capabilites\nThe power level is a linear measurement of a character strength that is used to determine a number rank\nThere are three power level for specific aspects: Physical, Magical, and Mental. These are put into a weighted average to determine the power level.\n')
                            case 3: print(f'Character has a Number Rank of: {numRankLvl:.2f}')
                            case 4: print(f'Character has a power level of {powerLvl:.0f}')
                            case 5: print(f'Physical Level: {phsLvl:.0f}\nMagical Level: {magLvl:.0f}\nMental Level: {mentLvl:.0f}')
                            case 6: 
                                name = input("Please enter character name: ")
                                toSave = Character(name, offenStrn, defenStrn, speed, adgility, manaCap, maxOutput,regenRate, iq, biq, knowl)
                                characters.append(toSave)
                case 2: 
                    characters.sort()
                    print()
                    for current in characters:
                        print(current)
                        print()
                case 3:
                    toFind = input("Enter name of character to view: ")
                    found = False
                    for current in characters:
                        if current.name == toFind:
                            print(current)
                            found = True
                            break
                    if not found: raise InvalidInput
                case 4:
                    toFind = input("\nEnter name of character to edit: ")
                    #toEdit = None
                    for current in characters:
                        if current.name == toFind: toEdit = current
                    #if toEdit == None: raise InvalidInput
                    while option != 0:
                        print()
                        print(toEdit)
                        print("\nWhat would you like to edit?\n1: Return to Main Menu\n2: Name\n3: Offensive Strength\n4: Defensive Strength\n5: Sprinting Speed\n6: Acceleration\n7: Mana Capacity\n8: Maximum Mana Output\n9: Mana Regeneration Rate\n10: IQ\n11: Battle IQ\n12: Magic & History Test Score")
                        option = int(input("Please enter an option:"))
                        match option:
                            case 1: break
                            case 2: toEdit.name = input("What would you like to change the name to: ")
                            case 3: toEdit.offenStrn = int(input(f"{toEdit.name}'s Offensive Strength is {toEdit.offenStrn:4f}\nWhat would you like to change the Offensive Strength to: "))
                            case 4: toEdit.defenStrn = int(input(f"{toEdit.name}'s Defensive Strength is {toEdit.defenStrn:4f}\nWhat would you like to change the Defensive Strength to: "))
                            case 5: toEdit.speed = int(input(f"{toEdit.name}'s Sprinting Speed is {toEdit.speed:.2f}\nWhat would you like to change the Sprinting Speed to: "))
                            case 6: toEdit.adgility = int(input(f"{toEdit.name}'s Acceleration is {toEdit.adgility:.0f}\nWhat would you like to change the Acceleration to: "))
                            case 7: toEdit.manaCap = int(input(f"{toEdit.name}'s Mana Capacity is {toEdit.manaCap:.0f}\nWhat would you like to change the Mana Capacity to: "))
                            case 8: toEdit.maxOutput = int(input(f"{toEdit.name}'s Maximum Mana Output is {toEdit.maxOutput:.0f}\nWhat would you like to change the Maximum Mana Output to: "))
                            case 9: toEdit.regenRate = int(input(f"{toEdit.name}'s  Mana Regeneration Rate is {toEdit.regenRate:.0f}\nWhat would you like to change the  Mana Regeneration Rate to: "))
                            case 10: toEdit.iq = int(input(f"{toEdit.name}'s IQ is {toEdit.iq:.0f}\nWhat would you like to change the IQ to: "))
                            case 11: toEdit.biq = int(input(f"{toEdit.name}'s Battle IQ is {toEdit.biq:.0f}\nWhat would you like to change the Battle IQ to: "))
                            case 12: toEdit.knowl = int(input(f"{toEdit.name}'s Magic & History Test Score is {toEdit.knowl:.0f}\nWhat would you like to change the Magic & History Test Score to: "))
                        toEdit.phsLvl = calcPhysical(toEdit.offenStrn, toEdit.defenStrn, toEdit.speed, toEdit.adgility)
                        toEdit.magLvl = calcMagical(toEdit.manaCap, toEdit.maxOutput, toEdit.regenRate)
                        toEdit.mentlvl = calcMental(toEdit.iq, toEdit.biq, toEdit.knowl)
                        toEdit.powerLvl = calcPowerLvl(toEdit.phsLvl, toEdit.magLvl, toEdit.mentlvl)
                        toEdit.numLvl = calcNumLvl(toEdit.powerLvl)
                case 5: raise NotImplementedError
                case _: raise InvalidInput
        except InvalidInput:
            print("Invalid Input. Please try again")
        except NotImplementedError:
            print("This feature has not been implemented yet. Feature is comming soon!")
        except ValueError:
            print("Input is not correct. Please input a number.")
    print("Thanks for using Character Strength Calculator! have a good day!")