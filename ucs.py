class Person:
    def __init__(self, name=None, parent=None, summedComfortVal=None):
        self.name = name
        self.parent = parent
        self.summedComfortVal = summedComfortVal


def getChildren(pairComfort, currentPerson):
    children = []
    for [m, n, c] in pairComfort:
        if m == currentPerson.name:
            children.append(
                Person(n, currentPerson.name, currentPerson.summedComfortVal + c)
            )
        elif n == currentPerson.name:
            children.append(
                Person(m, currentPerson.name, currentPerson.summedComfortVal + c)
            )
    return children


def getCost(pairComfort, name0, name1):
    for [m, n, c] in pairComfort:
        if [name0, name1] == [m, n] or [name1, name0] == [m, n]:
            return c


def getPersons(pairComfort):
    persons = []
    for [name0, name1, c] in pairComfort:
        if name0 not in persons:
            persons.append(name0)
        elif name1 not in persons:
            persons.append(name1)
        else:
            continue

    return persons

def findSeatingArrangement(pairComfort):
    possibleSeating = []
    persons = getPersons(pairComfort)

    for personName in persons:
        seatedNames, overallComfortValue = ucs(pairComfort, personName, len(persons))
        possibleSeating.append([seatedNames, overallComfortValue])

    possibleSeating.sort(key=lambda x: x[1], reverse=True)

    optimalArrangement = possibleSeating[0][0]
    optimalOverallComfortVal = possibleSeating[0][1]

    return optimalArrangement, optimalOverallComfortVal


def ucs(pairComfort, initialPerson, numOfPersons):
    frontier = []
    seated = []
    frontier.append(Person(initialPerson, None, 0))

    while True:
        if len(seated) == numOfPersons:
            break
        frontier.sort(key=lambda x: x.summedComfortVal, reverse=True)

        children = getChildren(pairComfort, frontier[0])

        seated.append(frontier[0])
        frontier = []

        for child in children:
            if child.name in [s.name for s in seated]:
                continue
            else:
                frontier.append(child)

        print("Seated:", [e.name for e in seated])
        print("Frontier:", [f.name for f in frontier])
        print("Children:", [c.name for c in children])
        print("")

    overallComfortValue = seated[-1].summedComfortVal + getCost(
        pairComfort, initialPerson, seated[-1].name
    )

    seatedNames = [x.name for x in seated]

    return seatedNames, overallComfortValue


if __name__ == "__main__":
    pairComfort = [
        ["a", "b", -5],
        ["a", "c", -4],
        ["a", "d", -3],
        ["a", "e", -2],
        ["b", "c", -1],
        ["b", "d", 1],
        ["b", "e", 2],
        ["c", "d", 3],
        ["c", "e", 4],
        ["d", "e", 5],
    ]

    optimalArrangement, optimalOverallComfortVal = findSeatingArrangement(pairComfort)

    print(f'Optimal Arrangement: {optimalArrangement}')
    print(f'Overall Comfort Value: {optimalOverallComfortVal}')
