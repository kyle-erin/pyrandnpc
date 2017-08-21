import random
from openpyxl import Workbook
from char import Char

WORKBOOK_FILENAME = 'characters.xlsx'
DATA_FOLDER = 'data'
COUNT = 100
TITLES = ['Name', 'Race', 'Appearance', 'Bonds', 'Flaws', 'High Ability', 'Low Ability', 'Ideals', 'Interactions with Others',
          'Mannerisms', 'Talents', 'Useful Knowledge']


# Returns file data
def getfilecontents(filename):
    openfile = open(filename, 'r')
    data = []
    for line in openfile:
        data.append(line.strip())

    openfile.close()
    return data


# Returns a random trait from the array
def getrandomtrait(arr):
    index = random.randint(0, len(arr) - 1)
    return arr[index]


# Load trait data
# classes = getfilecontents('classes.txt')
bonds = getfilecontents(DATA_FOLDER + '/bonds.txt')
appearances = getfilecontents(DATA_FOLDER + '/appearances.txt')
flaws_secrets = getfilecontents(DATA_FOLDER + '/flaws_secrets.txt')
high_abilities = getfilecontents(DATA_FOLDER + '/high_abilities.txt')
ideals = getfilecontents(DATA_FOLDER + '/ideals.txt')
interactions = getfilecontents(DATA_FOLDER + '/interactions.txt')
low_abilities = getfilecontents(DATA_FOLDER + '/low_abilities.txt')
mannerisms = getfilecontents(DATA_FOLDER + '/mannerisms.txt')
races = getfilecontents(DATA_FOLDER + '/races.txt')
talents = getfilecontents(DATA_FOLDER + '/talents.txt')
useful_knowledge = getfilecontents(DATA_FOLDER + '/useful_knowledge.txt')
firstnames = getfilecontents(DATA_FOLDER + '/firstnames.txt')
lastnames = getfilecontents(DATA_FOLDER + '/lastnames.txt')


def getrandabilities(high, low):
    ret = []
    index = random.randint(0, len(high) - 1)
    ret.append(high[index])
    index2 = random.randint(0, len(low) - 1)
    while index2 is index:
        index2 = random.randint(0, len(low) - 1)
    ret.append(low[index2])
    return ret


def getrandchar():
    racedata = getrandomtrait(races).split(',')
    if len(racedata) <= 1:
        raise ValueError('races.txt file not formatted correctly. Format: race, name_filename.txt,..')
    race = racedata[0].strip()
    # race = getrandomtrait(races)
    # clss = getrandomtrait(classes)
    appearance = getrandomtrait(appearances)
    bond = getrandomtrait(bonds)
    flaws = getrandomtrait(flaws_secrets)
    abilities = getrandabilities(high_abilities, low_abilities)
    high = abilities[0]
    low = abilities[1]
    ideal = getrandomtrait(ideals)
    interaction = getrandomtrait(interactions)
    mannerism = getrandomtrait(mannerisms)
    talent = getrandomtrait(talents)
    useful = getrandomtrait(useful_knowledge)
    firstnamedata = getfilecontents(DATA_FOLDER + '/' + racedata[1].strip())
    name = getrandomtrait(firstnamedata)
    if len(racedata) == 4:
        lastnamedata = getfilecontents(DATA_FOLDER + '/' + racedata[3].strip())
        middlenamedata = getfilecontents(DATA_FOLDER + '/' + racedata[2].strip())
        name += ' "' + getrandomtrait(middlenamedata) + '" ' + getrandomtrait(lastnamedata)
    if len(racedata) == 3:
        lastnamedata = getfilecontents(DATA_FOLDER + '/' + racedata[2].strip())
        name += ' ' + getrandomtrait(lastnamedata)
    # name = getrandomtrait(firstnames) + " " + getrandomtrait(lastnames)
    char = Char(name, race, appearance, bond, flaws, high, low, ideal, interaction, mannerism,
                talent, useful)
    return char


wb = Workbook()
ws = wb.active
ws.title = 'Characters'

# Create column names
ws.append(TITLES)

for i in range(0, COUNT):
    ws.append(getrandchar().getarray())

wb.save(WORKBOOK_FILENAME)
