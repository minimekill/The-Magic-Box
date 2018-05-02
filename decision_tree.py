import json

def distance(x1, x2):
    return x2 - x1

def to_jump_or_not_to_jump(x1, x2):
    out_distance = distance(x1, x2)

    data = json.loads(open('jumpingParameter.json').read())

    number = int(data['x'])

    if number == out_distance:
        return True

    return False

def change_parameter():
    data = json.loads(open('jumpingParameter.json').read())
    x = data['x'] - 1
    jumpingParameter = open('jumpingParameter.json', 'w')
    jumpingParameter.write("{ \"x\": {} }".format(x))
    jumpingParameter.close()