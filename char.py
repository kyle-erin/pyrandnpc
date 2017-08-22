class Char:
    def __init__(self, name, race, appearance, background, bond, flaws, high, low, ideals, interactions, mannerisms, talents,
                 useful):
        self.race = race
        self.name = name
        # self.clss = clss
        self.appearance = appearance
        self.bond = bond
        self.flaws = flaws
        self.high = high
        self.low = low
        self.ideals = ideals
        self.interactions = interactions
        self.mannerisms = mannerisms
        self.talents = talents
        self.background = background
        self.useful = useful

    def __str__(self):
        return self.name + ' ' + self.race + ' ' + ' ' + self.appearance + ' ' + self.background + ' ' +\
               self.bond + ' ' + self.flaws + ' ' + self.high + ' ' + self.low + ' ' + self.ideals + ' ' +\
               self.interactions + ' ' + self.mannerisms + ' ' + self.talents + ' ' + self.useful

    def getarray(self):
        return [self.name, self.race, self.appearance, self.background, self.bond, self.flaws, self.high, self.low, self.ideals,
                self.interactions, self.mannerisms, self.talents, self.useful]
