import json


def distance(x1, x2):
    return x2 - x1


def to_jump_or_not_to_jump(x1, x2, enemy_height):
    out_distance = distance(x1, x2)

    data = json.loads(open('jumpingParameter.json').read())
    if data[enemy_height]:
        number = int(data[enemy_height])

        if number >= out_distance - 3 and number <= out_distance + 3:
            return True

    return False


def change_parameter(enemy_height):
    data = json.loads(open('jumpingParameter.json').read())
    data[enemy_height] = int(data[enemy_height]) - 1
    with open('jumpingParameter.json', 'w') as outfile:
        json.dump(data, outfile)