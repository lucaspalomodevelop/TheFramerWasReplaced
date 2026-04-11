from helperclasses.Entities import Entities
from helperclasses.Hats import Hats

pos_x = 0
pos_y = 0
size = 32


def change_hat(hat: Hats):
    print("changed hat to " + str(hat))


def gotoStart():
    pos_x = 0
    pos_y = 0


def get_pos_x():
    return pos_x


def get_pos_y():
    return pos_x


def quick_print(str: str):
    print(str)


def print_costs():
    return 1


def get_cost(e: Entities):
    return 1


def get_world_size():
    return size
