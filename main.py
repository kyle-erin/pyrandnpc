import random
from openpyxl import Workbook
from char import Char

WORKBOOK_FILENAME = 'characters.xlsx'
COUNT = 10
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
bonds = getfilecontents('bonds.txt')
appearances = getfilecontents('appearances.txt')
flaws_secrets = getfilecontents('flaws_secrets.txt')
high_abilities = getfilecontents('high_abilities.txt')
ideals = getfilecontents('ideals.txt')
interactions = getfilecontents('interactions.txt')
low_abilities = getfilecontents('low_abilities.txt')
mannerisms = getfilecontents('mannerisms.txt')
races = getfilecontents('races.txt')
talents = getfilecontents('talents.txt')
useful_knowledge = getfilecontents('useful_knowledge.txt')
firstnames = getfilecontents('firstnames.txt')
lastnames = getfilecontents('lastnames.txt')


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
    race = getrandomtrait(races)
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
    name = getrandomtrait(firstnames) + " " + getrandomtrait(lastnames)
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
