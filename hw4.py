#assignment 4
#CSCE 4430 Programming Languages



#person class

class person :
    def __init__(self,name,gender,father,mother):
        self.name = name
        self.gender = gender
        self.father = father
        self.mother = mother


people=[]

#initialize men

people.append(person('King Gorge VI','male',None,None))
people.append(person('Charles Prince of Wales','male',None,'Queen Elizabeth II'))
people.append(person('Andrew Duke of York','male',None,'Queen Elizabeth II'))
people.append(person('Edward Earl of Wessex','male',None,'Queen Elizabeth II'))
people.append(person('David Viscount Linley','male',None,'Princess Magaret'))
people.append(person('Prince William of Wales','male','Charles Prince of Wales',None))
people.append(person('Prince Harry of Wales','male','Charles Prince of Wales',None))
people.append(person('Peter Phillips','male',None,'Princess Anne'))
people.append(person('James Viscount Severn','male','Edward Earl of Wessex',None))
people.append(person('Charles Armstrong Jones','male','David Viscount Linley',None))
people.append(person('Samuel Chatto','male',None,'Lady Sara Chatto'))
people.append(person('Arthur Chatto','male',None,'Lady Sara Chatto'))

#initialize woman

people.append(person('Queen Elizabeth II','female','King Gorge VI',None))
people.append(person('Princess Magaret','female','King Gorge VI',None))
people.append(person('Princess Anne','female',None,'Queen Elizabeth II'))
people.append(person('Lady Sara Chatto','female',None,'Princess Magaret'))
people.append(person('Zara Tindall','female',None,'Princess Anne'))
people.append(person('Princess Beatrice of York','female','Andrew Duke of York',None))
people.append(person('Princess Eugenle of York','female','Andrew Duke of York',None))
people.append(person('Savannah Phillips','female','Peter Phillips',None))
people.append(person('Isla Phillips','female','Peter Phillips',None))
people.append(person('Lady Louise Windsor','female','Edward Earl of Wessex',None))
people.append(person('Magarita Armstrong Jones','female','David Viscount Linley',None))


#sibling of individual
def sibling_of(individual):
    for i in people:
        if(i.name==individual):
            for z in people:
                if(i.mother != None and i.mother == z.mother and i.name != z.name):
                    yield z.name
                if(i.father != None and i.father == z.father and i.name != z.name):
                    yield z.name


def brother_of(individual):
    siblings = list(sibling_of(individual))

    for i in siblings:
        for z in people:
            if(i == z.name and z.gender == 'male'):
                yield i


def sister_of(individual):
    siblings = list(sibling_of(individual))

    for i in siblings:
        for z in people:
            if(i == z.name and z.gender == 'female'):
                yield i


def mother_of(individual):
    for i in people:
        if(i.name == individual and i.mother != None):
            return i.mother


def father_of(individual):
    for i in people:
        if(i.name == individual and i.father != None):
            return i.father


def gp_of(individual):
    for i in people:
        if (i.name == individual and i.mother != None):
            for z in people:
                if(i.mother == z.name):
                    if(z.mother != None):
                        yield z.mother
                    if(z.father != None):
                        yield z.father
        if(i.name == individual and i.father!= None):    #grandparents on father side if applicable
            for z in people:
                if(i.father == z.name):
                    if(z.mother != None):
                        yield z.mother
                    if(z.father != None):
                        yield z.father


def uncle_of(individual):
    momSide =mother_of(individual)
    dadSide = father_of(individual)


    for i in people:
        if(momSide == i.name):
            yield(list(brother_of(i.name)))
        if(dadSide == i.name):
            yield(list(brother_of(i.name)))



def aunt_of(individual):
    momSide = mother_of(individual)
    dadSide = father_of(individual)

    for i in people:
        if (momSide == i.name):
            yield(list(sister_of(i.name)))
        if (dadSide == i.name):
            yield(list(sister_of(i.name)))




def cousin_of(individual):
    momSide = mother_of(individual)
    dadSide = father_of(individual)


    for i in people:
        if (momSide == i.name):
            #find sisters
            aunts = list(sister_of(i.name))
            #find brothers
            uncles = list(brother_of(i.name))
            for x in aunts:
                for y in people:
                    if x == y.mother:
                        yield y.name

            for x in uncles:
                for y in people:
                    if x == y.father:
                        yield y.name



        if (dadSide == i.name):
            # find sisters
            aunts = list(sister_of(i.name))
            # find brothers
            uncles = list(brother_of(i.name))
            for x in aunts:
                for y in people:
                    if x == y.mother:
                        yield y.name


            for x in uncles:
                for y in people:
                    if x == y.father:
                        yield y.name



def ancestor_of(individual):
    for i in people:
        if i.name == individual:
            if(i.mother== None and i.father== None):
                return i.name
            if(i.mother!= None):
                return ancestor_of(i.mother)
            if(i.father!= None):
                return ancestor_of(i.father)





