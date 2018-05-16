import json


def distance(x1, x2):
    return x2 - x1


def to_jump_or_not_to_jump(x1, x2, enemy_height):
    out_distance = distance(x1, x2)

    data = json.loads(open('jumpingParameter.json').read())
    if str(enemy_height) in data:
        number = int(data[str(enemy_height)])

        if out_distance - 3 <= number <= out_distance + 3:
            return True

    return False


def change_parameter(enemy_height):
    data = json.loads(open('jumpingParameter.json').read())
    if str(enemy_height) in data:
        data[str(enemy_height)] = int(data[str(enemy_height)]) - 1
    else:
        data[str(enemy_height)] = 100
    
    with open('jumpingParameter.json', 'w') as outfile:
        json.dump(data, outfile)