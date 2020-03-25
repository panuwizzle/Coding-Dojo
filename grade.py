#rules = [
#    ['A', 91, 100],
#    ['B', 81, 90],
#    ['C', 71, 80],
#    ['D', 61, 70],
#    ['F', 0, 60]
#]

def grade(point: int):
    if point <= 100 and point >= 91:
        return 'A'
    
    if point <= 90 and point >= 81:
        return 'B'

    if point <= 80 and point >= 71:
        return 'C'

    if point <= 70 and point >= 61:
        return 'D'

    if point <= 60 and point >= 0:
        return 'F'

