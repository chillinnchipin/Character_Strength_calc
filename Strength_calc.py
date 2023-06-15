#Ronald Hardy Jr
# V0.0.1 6/10/2023
import math

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
def calcPowerLvl(offenStrn, defenStrn, speed, adgility, manaCap, maxOutput,regenRate, iq, biq, knowl):
    phsLvl = calcPhysical(offenStrn, defenStrn, speed, adgility)
    magLvl = calcMagical(manaCap, maxOutput,regenRate)
    mentlvl = calcMental(iq, biq, knowl)
    return calcPowerLvl(phsLvl, magLvl, mentlvl)
    #return calcPowerLvl(calcPhysical(offenStrn, defenStrn, speed, adgility),calcMagical(manaCap, maxOutput,regenRate),calcMental(iq, biq, knowl))
    raise NotImplementedError("calcPowerLvl (7 inputs) is to implemented at a later date")

def calcNumLvl(powerLvl):
    return 7.15 * math.log(powerLvl) - 4.3
    raise NotImplementedError("callcNumLvl (1 input) is to be implemented at a later date")
def calcNumLvl(phsLvl, magLvl, mentLvl):
    powerLvl = calcPowerLvl(phsLvl, magLvl, mentLvl)
    return calcNumLvl(powerLvl)
    #return calcNumLvl(calcPowerLvl(phsLvl, magLvl, mentLvl))
    raise NotImplementedError("callcNumLvl (3 inputs) is to be implemented at a later date")
def calcNumLvl(offenStrn, defenStrn, speed, adgility, manaCap, maxOutput,regenRate, iq, biq, knowl):
    powerLvl = calcPowerLvl(offenStrn, defenStrn, speed, adgility, manaCap, maxOutput,regenRate, iq, biq, knowl)
    return calcNumLvl(powerLvl)
    #return calcNumLvl(calcPowerLvl(offenStrn, defenStrn, speed, adgility, manaCap, maxOutput,regenRate, iq, biq, knowl))
    raise NotImplementedError("callcNumLvl (7 inputs) is to be implemented at a later date")

def readFile():
    # TODO: file read and write
    raise NotImplementedError("File read and write not implemented yet.")
def saveToFile():
    raise NotImplementedError("File read and write not implemented yet.")

#def StrenthCalc():
if __name__ == "__main__":
    # TODO: run user interface for opitions and inputing data
    print("Weolcome to Character Strength Calculator! \nUsing the CH Base Magic System's Power Level Rank!\n")
    option = -1
    menu = "0: Quit\n1: Input Character Stats\n2: View Character Stats & Levels\n3: Edit Chacter Stats\n4: Save Character Data\n5: Load data from file"
    while option != 0:
        try:
            print(menu)
            print("Please enter an option: ", end = '')
            option = int(input())
            match option:
                case 0: break
                case 1: print("Placeholder") #Temp, delete when implementing
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

    #print(option) #for debug only