# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

n = get_number()
values = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
output = []

for i in range(n):
    player_1_cards = input().split(' ')
    player_2_cards = input().split(' ')
    
    while True:
        draw = False
        
        set1 = set(player_1_cards)
        set2 = set(player_2_cards)
        
        if set1 == set2:
            output.append('draw')
            break
        
        if len(player_1_cards) == 0:
            output.append('player 2')
            break
        
        if len(player_2_cards) == 0:
            output.append('player 1')
            break
        
        player_1_card = player_1_cards.pop(0)
        player_2_card = player_2_cards.pop(0)
        if values.index(player_1_card) > values.index(player_2_card):
            player_1_cards.append(player_2_card)
        elif values.index(player_1_card) < values.index(player_2_card):
            player_2_cards.append(player_1_card)
        else:
            player_1_cards.append(player_1_card)
            player_2_cards.append(player_2_card)

for i in output:
    print(i)