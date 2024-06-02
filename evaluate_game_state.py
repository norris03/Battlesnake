from constants import *
def evaluate_game_state(game_state):
    if game_state == {}:
        return death_score
    else: 
        x = game_state["you"]["body"][0]["x"]
        y = game_state["you"]["body"][0]["y"]
        width = game_state["board"]["width"]
        height = width + game_state["board"]["height"]
        max_distance_to_food = height
        min_distance_to_food = max_distance_to_food
        for apple in game_state["board"]["food"]:
            distance_to_food = abs(x-apple["x"])+abs(y-apple["y"])
            if distance_to_food < min_distance_to_food:
                min_distance_to_food = distance_to_food
        return -min_distance_to_food/max_distance_to_food+game_state["you"]["length"]