import json


def distance(x1, x2):
    return x2 - x1


def to_jump_or_not_to_jump(x1, x2, enemy_height):
    out_distance = distance(x1, x2)

    data = json.loads(open('jumpingParameter2.json').read())
    enemy_height = str(enemy_height)
    if enemy_height in data:
        number = int(data[enemy_height])

        if out_distance - 3 <= number <= out_distance + 3:
            return True

    return False


def change_parameter(enemy_height):
    data = json.loads(open('jumpingParameter2.json').read())
    enemy_height = str(enemy_height)
    if enemy_height in data:
        data[enemy_height] = int(data[enemy_height]) + 1
    else:
        data[enemy_height] = 0
    
    with open('jumpingParameter2.json', 'w') as outfile:
        json.dump(data, outfile)