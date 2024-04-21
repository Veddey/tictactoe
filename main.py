#Игра крестики-нолики.
#Строки 4-96.

from random import choice
import sys

cells = {1 : ".", 2 : ".", 3 : ".", 4 : ".", 5 : ".", 6 : ".", 7 : ".", 8 : ".", 9 : "."}
coord = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

exit = ["exit", ""]
var_x = ["X", "x", "Х", "х"]
var_0 = ["0", "O", "o", "О", "о"]


def draw_game_field():
    for i in range(1, 10, 3):
        print("")
        for i in range(i, i + 3):
            print(f"{cells[i]} ", end='')
    print("\n")

def victory_test(player_move):
    if cells[1]+cells[2]+cells[3] == var_x[0]*3 or cells[4]+cells[5]+cells[6] == var_x[0]*3 or cells[7]+cells[8]+cells[9] == var_x[0]*3 \
            or cells[1]+cells[4]+cells[7] == var_x[0]*3 or cells[2]+cells[5]+cells[8] == var_x[0]*3 or cells[3]+cells[6]+cells[9] == var_x[0]*3 \
            or cells[1]+cells[5]+cells[9] == var_x[0]*3 or cells[3]+cells[5]+cells[7] == var_x[0]*3:
        draw_game_field()
        if player_move in var_x:
            print("Поздравляю! Вы победили.")
        else:
            print("Победил искусственный интеллект.")
        sys.exit()
    elif cells[1]+cells[2]+cells[3] == var_0[0]*3 or cells[4]+cells[5]+cells[6] == var_0[0]*3 or cells[7]+cells[8]+cells[9] == var_0[0]*3 \
            or cells[1]+cells[4]+cells[7] == var_0[0]*3 or cells[2]+cells[5]+cells[8] == var_0[0]*3 or cells[3]+cells[6]+cells[9] == var_0[0]*3 \
            or cells[1]+cells[5]+cells[9] == var_0[0]*3 or cells[3]+cells[5]+cells[7] == var_0[0]*3:
        draw_game_field()
        if player_move in var_0:
            print("Поздравляю! Вы победили.")
        else:
            print("Победил искусственный интеллект.")
        sys.exit()

def turn_order():
    player_move = input("Выберите X или 0: ")

    while player_move not in var_x and player_move not in var_0 and player_move not in exit:
        print("Не удалось распознать выбор.")
        player_move = input("Выберите X или 0: ")

    if player_move in var_x:
        player_move = var_x[0]
        ii_move = var_0[0]
    elif player_move in var_0:
        player_move = var_0[0]
        ii_move = var_x[0]

    return player_move, ii_move

def player_moves(player_move):
    move_coord = input("Введите координаты поля (от 1 до 9): ")

    while move_coord not in coord and player_move not in exit:
        print("Неверный ввод поля.")
        move_coord = input("Введите координаты поля (от 1 до 9): ")

    coord.remove(move_coord)
    cells[int(move_coord)] = player_move

def ii_moves(ii_move):
    move_coord = choice(coord)
    coord.remove(move_coord)
    cells[int(move_coord)] = ii_move
    print(f"Выбор ИИ: {move_coord}.")

def main():
    player_move, ii_move = turn_order()

    match player_move:
        case "X":
            while True:
                player_moves(player_move)
                victory_test(player_move)
                ii_moves(ii_move)
                victory_test(player_move)
                draw_game_field()

        case "0":
            while True:
                ii_moves(ii_move)
                victory_test(player_move)
                draw_game_field()
                player_moves(player_move)
                victory_test(player_move)
                draw_game_field()

if __name__ == "__main__":
    main()