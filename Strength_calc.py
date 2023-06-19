#Ronald Hardy Jr
# V0.0.2 6/18/2023
import math
# TODO: Setup app using flask
# TODO: intergrate sql with
# TODO: create docker image & run in container

"""class character:
    # TODO: Finish character class for saving characters
    def __init__(self):
        #declares instance stats
        self.offenStrn = 50
        self.defenStrn = 50
        self.speed = 30
        self.adgility = 4
        self.manaCap = 1000
        self.maxOutput = 500
        self.regenRate = 10
        self.iq = 100
        self.biq = 50
        self.knowl = 50

        #declares instance levels
        self.phsLvl
        self.magLvl
        self.mentlvl
        self.numLvl

        self.name = 'null'
        self.spellList = []
    
    def __init__(self, offenStrn, defenStrn, speed, adgility, manaCap, maxOutput,regenRate, iq, biq, knowl):
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
        self.numLvl = calcPowerLvl(self.phsLvl, self.magLvl, self.mentLvl)

        self.name = 'null'
        self.spellList = []"""


class InvalidInput(Exception):
    pass

def calcPhysical(offenStrn, defenStrn, speed, adgility): return (0.25*offenStrn)+(0.25*defenStrn) + (0.15625*speed) + (2.5 * adgility)
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
    # TODO: add character arraylist and ability to add, remove, view, and edit chacters on it
    print("Weolcome to Character Strength Calculator! \nUsing the CH Base Magic System's Power Level Rank!")
    option = -1
    menu = "\n0: Quit\n1: Input Character Stats\n2: View Character Stats & Levels\n3: Edit Chacter Stats\n4: Save Character Data\n5: Load data from file"
    while option != 0:
        try:
            print(menu)
            print("Please enter an option: ", end = '')
            option = int(input())
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
                case 2: raise NotImplementedError
                case 3: raise NotImplementedError
                case 4: raise NotImplementedError
                case 5: raise NotImplementedError
                case _: raise InvalidInput
        except InvalidInput:
            print("Invalid Input. Please try again")
        except NotImplementedError:
            print("This feature has not been implemented yet. Feature is comming soon!")
        except ValueError:
            print("Input is not correct. Please input a number.")
    print("Thanks for using Character Strength Calculator! have a good day!")