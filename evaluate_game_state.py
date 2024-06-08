from constants import *
from a_star import a_star, heuristik
def evaluate_game_state(game_state, snake_id):
    if game_state == {}:
        return death_score
    else: 
        x = game_state["you"]["body"][0]["x"]
        y = game_state["you"]["body"][0]["y"]
        width = game_state["board"]["width"]
        height = width + game_state["board"]["height"]
        too_far = 4 #obere Schranke damit nicht aufwendig mit a* reeler Abstand zu weit entfernten Apfel berechnet wird. Muss noch sinnvolo gewählt werden
        max_distance_to_food = too_far #hier muss vlt auch noch was gemacht werden
        min_distance_to_food = max_distance_to_food
        max_steps = width/2
        
        for apple in game_state["board"]["food"]:

            naive_distance = heuristik(game_state["you"]["body"][0], apple)
            for snake in game_state["board"]["snakes"]: #vlt noch "you" ausschliesen
                              
                if heuristik(snake["body"][0], apple)> naive_distance and naive_distance< too_far and naive_distance < min_distance_to_food: #versucht aufrufe der a_star funktion zu minimieren

                    distance_to_food = a_star(game_state,apple, snake_id, too_far) # schaut ob apfel wirklich erreichbar ist
                    if distance_to_food < min_distance_to_food:
                        min_distance_to_food = distance_to_food

        
        return -min_distance_to_food/max_distance_to_food+game_state["you"]["length"] # muss noch angepasst werden