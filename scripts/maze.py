clear()
plant(Entities.Bush)
substance = get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
quick_print(substance)
use_item(Items.Weird_Substance, substance)

compass = [West, North, East, South]


def update_direction(value):
    if value == 1:
        compass.append(compass.pop(0))
        quick_print("RIGHT turn")
        quick_print(str(compass[1]))
    elif value == 0:
        quick_print("NO turn")
        return
    elif value == -1:
        compass.insert(0, compass.pop(len(compass) - 1))
        quick_print("LEFT turn")
        quick_print(str(compass[1]))


go = True
while go:
    if get_entity_type() == Entities.Treasure:
        # harvest()
        # plant(Entities.Bush)
        use_item(Items.Weird_Substance, substance)
    if can_move(compass[1]):
        if can_move(compass[0]):
            move(compass[0])
            quick_print("Move to " + str(compass[0]))
            update_direction(-1)
        else:
            quick_print("Move to " + str(compass[1]))
            move(compass[1])

    elif can_move(compass[0]):
        move(compass[0])
        quick_print("Move to " + str(compass[0]))
        update_direction(-1)
    else:
        update_direction(1)
