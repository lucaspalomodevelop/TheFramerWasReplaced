
# ground 
soild_ground = [Entities.Carrot, Entities.Pumpkin, Entities.Sunflower, Entities.Cactus]
grass_ground = [Entities.Grass, Entities.Tree]

#plants 
plants = [
Entities.Cactus, 
Entities.Cactus, 
Entities.Cactus, 
Entities.Cactus, 
Entities.Cactus, 
Entities.Cactus, 
Entities.Cactus, 
Entities.Cactus, 
Entities.Cactus, 
Entities.Cactus,
Entities.Cactus,
Entities.Cactus,
Entities.Cactus,
Entities.Cactus,
Entities.Cactus,
Entities.Cactus,
Entities.Cactus,
Entities.Cactus,
Entities.Cactus,
Entities.Cactus, 
Entities.Cactus, 
Entities.Cactus, 
Entities.Cactus,
Entities.Cactus,
Entities.Cactus,
Entities.Cactus,
Entities.Cactus,
Entities.Cactus,
Entities.Cactus,
Entities.Cactus,
Entities.Cactus, 
Entities.Cactus, 
Entities.Cactus, 

]
#plants = Entities

# actions
#watering = [Entities.Tree, Entities.Pumpkin,Entities.Sunflower]
watering = [Entities.Tree,Entities.Pumpkin,Entities.Sunflower]
fertelize = [Entities.Tree]


#unwichtig 
itemset = [

]


			

#setItem(Entities.Pumpkin, 1 , 1 )

# functions

def goToStart():
	x, y = get_pos_x(), get_pos_y()
	for i in range(x):
		move(West)
	for i in range(y):
		move(South)
		

def isInList(item, list):
	for i in list: 
		if i == item:
			return True
	return False

def getPlant(x,y):
	current_plant = plants[y]
	for i in itemset:
		if i[1] == x and i[2] == y:
			current_plant = i[0]
	return current_plant

def plant_fn(x,y):
	
	current_plant = getPlant(x,y)
	
	
	if(isInList(current_plant, soild_ground)):
		if get_ground_type() != Grounds.Soil:
			till()
	if(isInList(current_plant, grass_ground)):
		if get_ground_type() != Grounds.Grassland:
			till()
				
		plant(current_plant)

	if(isInList(current_plant, watering)):
		use_item(Items.Water)
		quick_print(str(current_plant) + " wurde gewässter")

	if isInList(current_plant, fertelize):
		use_item(Items.Fertilizer)

def print_costs(): 
	for i in Entities: 
		quick_print(str(i) + ": " +  str(get_cost(i)))

col = 0

# main loop
change_hat(Hats.Straw_Hat)
goToStart()
print_costs()

#change_hat(Hats.Dinosaur_Hat)

	
def action():
	x = col
	while True:
		for y in range(get_world_size()):
			if can_harvest():
				harvest()
				
				plant_fn(x ,y)
			elif get_entity_type() == Entities.Dead_Pumpkin:
				plant(Entities.Carrot)       

			
			if ( get_entity_type() == None):	
				plant(getPlant(x,y))
			
			move(North)
			
for i in range(0,22):
	spawn_drone(action)
	move(East)
	col = i
		