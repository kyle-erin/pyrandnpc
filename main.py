import random
import os.path
from openpyxl import Workbook
import csv
from char import Char

WORKBOOK_FILENAME = 'characters.xlsx'
DATA_FOLDER = 'data'
COUNT = 100
TITLES = ['Name', 'Race', 'Appearance', 'Background', 'Bonds', 'Flaws', 'High Ability', 'Low Ability', 'Ideals', 'Interactions with Others',
          'Mannerisms', 'Talents', 'Useful Knowledge']


# Returns file data
def getfilecontents(filename):
    return open(filename).read().splitlines()

# Load trait data
# classes = getfilecontents('classes.txt')
bonds = getfilecontents(os.path.join(DATA_FOLDER, 'bonds.txt'))
appearances = getfilecontents(os.path.join(DATA_FOLDER, 'appearances.txt'))
flaws_secrets = getfilecontents(os.path.join(DATA_FOLDER, 'flaws_secrets.txt'))
high_abilities = getfilecontents(os.path.join(DATA_FOLDER, 'high_abilities.txt'))
ideals = getfilecontents(os.path.join(DATA_FOLDER, 'ideals.txt'))
interactions = getfilecontents(os.path.join(DATA_FOLDER, 'interactions.txt'))
low_abilities = getfilecontents(os.path.join(DATA_FOLDER, 'low_abilities.txt'))
mannerisms = getfilecontents(os.path.join(DATA_FOLDER, 'mannerisms.txt'))
races = getfilecontents(os.path.join(DATA_FOLDER, 'races.txt'))
talents = getfilecontents(os.path.join(DATA_FOLDER, 'talents.txt'))
useful_knowledge = getfilecontents(os.path.join(DATA_FOLDER, 'useful_knowledge.txt'))
backgrounds = getfilecontents(os.path.join(DATA_FOLDER, 'backgrounds.txt'))


def getrandabilities(high, low):
    ret = []
    index = random.randrange(len(high))
    ret.append(high[index])
    index2 = random.randrange(len(low))
    while index2 is index:
        index2 = random.randrange(len(low))
    ret.append(low[index2])
    return ret


def getrandchar():
    racedata = random.choice(races).split(',')
    if len(racedata) <= 1:
        raise ValueError('races.txt file not formatted correctly. Format: race, name_filename.txt,..')
    race = racedata[0].strip()
    appearance = random.choice(appearances)
    bond = random.choice(bonds)
    flaws = random.choice(flaws_secrets)
    abilities = getrandabilities(high_abilities, low_abilities)
    high = abilities[0]
    low = abilities[1]
    ideal = random.choice(ideals)
    interaction = random.choice(interactions)
    mannerism = random.choice(mannerisms)
    talent = random.choice(talents)
    useful = random.choice(useful_knowledge)
    firstnamedata = getfilecontents(os.path.join(DATA_FOLDER, racedata[1].strip()))
    name = random.choice(firstnamedata)
    background = random.choice(backgrounds)
    if len(racedata) == 4:
        lastnamedata = getfilecontents(os.path.join(DATA_FOLDER, racedata[3].strip()))
        middlenamedata = getfilecontents(os.path.join(DATA_FOLDER, racedata[2].strip()))
        name += ' "' + random.choice(middlenamedata) + '" ' + random.choice(lastnamedata)
    if len(racedata) == 3:
        lastnamedata = getfilecontents(os.path.join(DATA_FOLDER, racedata[2].strip()))
        name += ' ' + random.choice(lastnamedata)
    char = Char(name, race, appearance, background, bond, flaws, high, low, ideal, interaction, mannerism,
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
