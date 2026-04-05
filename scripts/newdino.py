# set_world_size(4)
set_execution_speed(999)

clear()
change_hat(Hats.Dinosaur_Hat)


def move_dino():
    direction = North
    while True:
        for x in range(0, get_world_size()):
            if x == 0 or x == get_world_size() - 1:
                size = get_world_size()
            else:
                size = get_world_size() - 2

            for y in range(0, size):
                result = move(direction)

            if direction == North:
                direction = South
                quick_print(direction)
            elif direction == South:
                direction = North
                quick_print(direction)

            if get_pos_x() == get_world_size() - 1:
                for _ in range(0, get_world_size()):
                    result = move(West)
                result = move(direction)
            else:
                result = move(East)

            if not result:
                change_hat(Hats.Straw_Hat)
                clear()
                change_hat(Hats.Dinosaur_Hat)


move_dino()
