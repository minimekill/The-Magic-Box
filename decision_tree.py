import decision_tree_lower as dts
import decision_tree_upper as dtu
import decision_tree_middle as dtm

mode = "middle"

def to_jump_or_not_to_jump(x1, x2, enemy_height):
    if mode is "upper":
        return dtu.to_jump_or_not_to_jump(x1, x2, enemy_height)
    elif mode is "lower":
        return dts.to_jump_or_not_to_jump(x1, x2, enemy_height)
    elif mode is "middle":
        return dtm.to_jump_or_not_to_jump(x1, x2, enemy_height)

def change_parameter(enemy_height):
    if mode is "upper":
        dtu.change_parameter(enemy_height)
    elif mode is "lower":
        dts.change_parameter(enemy_height)