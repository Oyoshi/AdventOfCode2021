#!/usr/bin/python3
import functools as ft

STARTING_POS_PLAYER_1 = 8
STARTING_POS_PLAYER_2 = 1
WINNING_SCORE_PART1 = 1000

def simulate_game(players):
    turn = 0
    while True:
        turn += 1
        move_p1 = sum(get_dirac_dice_rolls(turn))
        upd_pos_p1 = get_updated_position(players[0]['position'], move_p1)
        players[0]['position'] = upd_pos_p1
        players[0]['score'] += upd_pos_p1
        players[0]['rolls'] += 3
        if players[0]['score'] >= WINNING_SCORE_PART1:
            break
        turn += 1
        move_p2 = sum(get_dirac_dice_rolls(turn))
        upd_pos_p2 = get_updated_position(players[1]['position'], move_p2)
        players[1]['position'] = upd_pos_p2
        players[1]['score'] += upd_pos_p2
        players[1]['rolls'] += 3
        if players[1]['score'] >= WINNING_SCORE_PART1:
            break
    total_rolls = players[0]['rolls'] + players[1]['rolls']
    loser_score = players[0]['score'] if players[0]['score'] < WINNING_SCORE_PART1 else players[1]['score']
    return total_rolls * loser_score

def get_dirac_dice_rolls(n):
    return [3*n-2, 3*n-1, 3*n]

def get_updated_position(pos, move):
    acc_pos = (pos + move) % 10
    return 10 if acc_pos == 0 else acc_pos

def main():
    players = [{'score': 0, 'position': STARTING_POS_PLAYER_1, 'rolls': 0}, {'score': 0, 'position': STARTING_POS_PLAYER_2, 'rolls': 0}]
    # PART 1
    result_part1 = simulate_game(players)
    print(f'PART 1: {result_part1}')
    # PART 2

if __name__ == '__main__':
    main()
