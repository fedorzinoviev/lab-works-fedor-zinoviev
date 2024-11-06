players=["Oleg", "Fedor", "Daniel", "Messi", "Ronaldo", "Mbappe"]
all_players = len(players)
print(all_players)
mid_index= all_players // 2
first_team = players[:mid_index]
second_team = players[mid_index:]
print(first_team)
print(second_team)