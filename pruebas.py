import os
import readchar
import random
from random import randint

POS_X = 0
POS_Y = 1

NUM_POKEMON_TRAINERS = 1
HP_START_PIKACHU = 80
HP_START_SQUIRTLE = 8
HP_START_BULBASAUR = 8
HP_START_CHARMANDER = 9

HP_BAR_SIZE = 20



obstacle_definition = """\
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓      ▓▓▓▓▓▓▓▓▓▓           ▓▓    ▓▓
▓▓                                  ▓▓▓▓
▓▓▓▓▓    ▓▓▓▓▓       ▓▓▓▓▓▓  ▓▓▓▓▓     ▓
▓▓▓               ▓▓▓▓▓▓▓▓           ▓▓▓
▓        ▓▓▓▓▓                ▓▓     ▓▓▓
▓▓▓▓▓       ▓▓▓▓▓▓▓▓       ▓▓▓▓▓▓▓▓▓▓▓▓▓
▓              ▓▓▓                     ▓
▓▓  ▓▓                       ▓▓▓▓▓▓▓▓▓▓▓
▓  ▓     ▓▓▓     ▓▓▓▓▓              ▓▓▓▓
▓        ▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓▓          ▓
▓▓▓▓       ▓▓▓▓▓▓▓      ▓▓        ▓▓▓▓▓▓
▓▓▓▓▓▓▓           ▓▓▓   ▓▓▓▓▓       ▓▓▓▓
▓▓▓▓▓     ▓▓▓▓       ▓  ▓       ▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\
"""

my_position = [6,6]
map_objects = []
endgame = False
died = False

hp_pikachu = HP_START_PIKACHU
hp_squirtle = HP_START_SQUIRTLE
hp_bulbasaur = HP_START_BULBASAUR
hp_charmander = HP_START_CHARMANDER
pokemon_name = None
attack_enemy_1 = None
attack_enemy_2 = None
attack_charmander_1 = 10
attack_charmander_1_name = "arañazo"
attack_charmander_2 = 12
attack_charmander_2_name = "ascuas"
attack_squirtle_1 = 9
attack_squirtle_1_name = "placaje"
attack_squirtle_2 = 13
attack_squirtle_2_name = "burbujas"
attack_bulbasaur_1 = 9
attack_bulbasaur_1_name = "derribo"
attack_bulbasaur_2 = 13
attack_bulbasaur_2_name = "latigo cepa"
#Enemy selector random
pokemon_enemy = randint(1,3)
if pokemon_enemy == 1:
    pokemon_name = "Charmander"
    hp_start_enemy = HP_START_CHARMANDER
    hp_pokemon = hp_charmander
    attack_enemy_1 = attack_charmander_1
    attack_enemy_1_name = attack_charmander_1_name
    attack_enemy_2 = attack_charmander_2
    attack_enemy_2_name = attack_charmander_2_name
    pokemon_draw = charmander_draw
elif pokemon_enemy == 2:
    pokemon_name = "Squirtle"
    hp_start_enemy = HP_START_SQUIRTLE
    hp_pokemon = hp_squirtle
    attack_enemy_1 = attack_squirtle_1
    attack_enemy_1_name = attack_squirtle_1_name
    attack_enemy_2 = attack_squirtle_2
    attack_enemy_2_name = attack_squirtle_2_name
    pokemon_draw = squirtle_draw
else:
    pokemon_name = "Bulbasaur"
    hp_start_enemy = HP_START_BULBASAUR
    hp_pokemon = hp_bulbasaur
    attack_enemy_1 = attack_bulbasaur_1
    attack_enemy_1_name = attack_bulbasaur_1_name
    attack_enemy_2 = attack_bulbasaur_2
    attack_enemy_2_name = attack_bulbasaur_2_name
    pokemon_draw = bulbasaur_draw


obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

MAP_WIDTH = 40
MAP_HEIGHT = 15

while len(map_objects) < NUM_POKEMON_TRAINERS:
    new_position = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]

    if new_position not in map_objects and new_position != my_position and \
            obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "▓":
            map_objects.append(new_position)


while not died == True or endgame == True:

    os.system("cls")



    print("╔" + "═" * MAP_WIDTH * 2 + "╗")

    for coordinate_y in range(MAP_HEIGHT):
        print("║", end="")

        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = "░░"
            object_in_cell = None

            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = "░×"
                    object_in_cell = map_object

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw ="░@"

                if object_in_cell:

                    while hp_pokemon > 0 and hp_pikachu > 0:
                        os.system("cls")
                        os.system("cls")
                        print("Turno de {}".format(pokemon_name))
                        print(pokemon_draw)
                        attack_enemy = randint(1, 3)
                        if attack_enemy == 1:
                            print("{} ataca con {}".format(pokemon_name, attack_enemy_1_name))
                            hp_pikachu -= int(attack_enemy_1)
                        elif attack_enemy == 2:
                            print("{} ataca con {}".format(pokemon_name, attack_enemy_2_name))
                            hp_pikachu -= int(attack_enemy_2)
                        else:
                            print("{} no hace nada".format(pokemon_name))

                        if hp_pokemon < 0:
                            hp_pokemon = 0
                        if hp_pikachu < 0:
                            hp_pikachu = 0

                        hp_bars_enemy = int(hp_pokemon * HP_BAR_SIZE / hp_start_enemy)
                        print("{}: [{}{}] ({}/{})".format(pokemon_name, "▓" * hp_bars_enemy,
                                                          "░" * (HP_BAR_SIZE - hp_bars_enemy), hp_pokemon,
                                                          hp_start_enemy))

                        hp_bars_pikachu = int(hp_pikachu * HP_BAR_SIZE / HP_START_PIKACHU)
                        print("Pikachu: [{}{}] ({}/{})".format("▓" * hp_bars_pikachu,
                                                               "░" * (HP_BAR_SIZE - hp_bars_pikachu), hp_pikachu,
                                                               HP_START_PIKACHU))

                        input("Pulsa enter para continuar...\n\n")
                        os.system("cls")

                        attack_pikachu = None
                        while attack_pikachu not in ["I", "L", "A", "N"]:
                            print(pikachu_draw)
                            attack_pikachu = input(
                                "¿Qué ataque deseas realizar? [I]mpactrueno, [L]átigo, [A]taque rapido, [N]ada: ")

                        if attack_pikachu == "I":
                            print("Pikachu usa Impactrueno")
                            hp_pokemon -= 10
                        elif attack_pikachu == "L":
                            print("Pikachu usa Látigo")
                            hp_pokemon -= 13
                        elif attack_pikachu == "A":
                            print("Pikachu usa Ataque rápido")
                            hp_pokemon -= 15
                        elif attack_pikachu == "N":
                            print("Pikachu no hace nada")

                        if hp_pokemon < 0:
                            hp_pokemon = 0
                        if hp_pikachu < 0:
                            hp_pikachu = 0

                        hp_bars_enemy = int(hp_pokemon * HP_BAR_SIZE / hp_start_enemy)
                        print("{}: [{}{}] ({}/{})".format(pokemon_name, "▓" * hp_bars_enemy,
                                                          "░" * (HP_BAR_SIZE - hp_bars_enemy), hp_pokemon,
                                                          hp_start_enemy))

                        hp_bars_pikachu = int(hp_pikachu * HP_BAR_SIZE / HP_START_PIKACHU)
                        print("Pikachu: [{}{}] ({}/{})".format("▓" * hp_bars_pikachu,
                                                               "░" * (HP_BAR_SIZE - hp_bars_pikachu), hp_pikachu,
                                                               HP_START_PIKACHU))

                        input("Pulsa enter para continuar...\n\n")
                        os.system("cls")

                    if hp_pokemon > hp_pikachu:
                        died = True
                    elif NUM_POKEMON_TRAINERS == 0:
                        endgame = True
                    else:
                        print("Pikachu gana")
                        print(pikachu_draw)
                        map_objects.remove(object_in_cell)


            if obstacle_definition[coordinate_y][coordinate_x] == "▓":
                char_to_draw = "▓▓"

            print("{}".format(char_to_draw), end="")

        print("║")

    print("╚" + "═" * MAP_WIDTH * 2 + "╝")

    direction = readchar.readchar()
    new_position = None

    if direction == "w":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_WIDTH]
    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_WIDTH]
    elif direction == "a":
        new_position = [(my_position[POS_X] -1) % MAP_WIDTH, my_position[POS_Y]]
    elif direction == "d":
        new_position = [(my_position[POS_X] +1) % MAP_WIDTH, my_position[POS_Y]]
    elif direction == "q":
        break
    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "▓":
            my_position = new_position


    os.system("cls")

if died == True:
    os.system("cls")
    print("Has sido derrotado, fin del juego")
    print(pokemon_draw)