from game_tree import is_bad_move, update_game_state
from update_game_state import clean_game_state
import heapq as q 
from utils import pretty_print
import copy
import time


counter = 10000
#berechnet die länge des Weges von einem Punkt zu einm anderen auf einem freien board
def heuristik(pos, goal):
    return abs(pos["x"]-goal["x"])+abs(pos["y"]-goal["y"])

#diese funtion wird gebraucht weil sonst heappush wenn ein element mit gleichen key schon in der queue ist dictionries versucht werden zu vergleichen 
def heappush_with_unique_id(queue, key, dictionary):
    global counter
    q.heappush(queue, (key, counter, dictionary))
    counter -= 1

def a_star(gamestate, food,max_step):
    moves = ["right", "up", "down", "left"]
    queue = []
    #gamestate_memory = [gamestate["board"]]
    min_abstand = heuristik(gamestate["you"]["body"][0], food)
    heappush_with_unique_id(queue, min_abstand, gamestate) #erstellt prioty queue
    min_gamestate = queue[0]

    while min_gamestate[0] - min_abstand < max_step and queue:

        min_gamestate = q.heappop(queue) #nimmt element mit dem kleinsten kosten
        #checkt ob das Ziel erreicht wurde
        if min_gamestate[2]["you"]["body"][0] == food: # noch schauen ob das mit vergleich dictionary functioniert

            return min_gamestate[0]
        
        #expandet den Punkt
        for move in moves:

            if not is_bad_move(gamestate, move, min_gamestate[2]["you"]["body"]):

                new_gamestate = update_game_state(copy.deepcopy(min_gamestate[2]),move, True)


                min_abstand = heuristik(min_gamestate[2]["you"]["body"][0], food)
                NeuAbstandh = heuristik(new_gamestate["you"]["body"][0], food)
            
                heappush_with_unique_id(queue, min_gamestate[0]-min_abstand + NeuAbstandh +1,new_gamestate)

        
    return max_step
                   
            


state = {
    'game': {'id': '90aa8919-aa32-44c0-a3ea-f2b76dbff1f1', 'ruleset': {'name': 'standard', 'version': 'cli', 'settings': {'foodSpawnChance': 15, 'minimumFood': 1, 'hazardDamagePerTurn': 14, 'hazardMap': '', 'hazardMapAuthor': '', 'royale': {'shrinkEveryNTurns': 25}, 'squad': {'allowBodyCollisions': False, 'sharedElimination': False, 'sharedHealth': False, 'sharedLength': False}}}, 'map': 'standard', 'timeout': 500, 'source': ''}, 'turn': 1, 
    
    'board': {'height': 11, 'width': 11, 'snakes': [{'id': 'eacfa58f-5356-47e6-94aa-833295c6b96c', 'name': 'snek', 'latency': '4', 'health': 95, 'body': [{'x': 1, 'y': 0}, {'x': 1, 'y': 1}, {'x': 1, 'y': 2}], 'head': {'x': 1, 'y': 0}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#FFFF00', 'head': 'fang', 'tail': 'block-bum'}}, {'id': '3d6b6171-8a95-41d9-86a5-db01fa72e0aa', 'name': 'snek2', 'latency': '5', 'health': 95, 'body': [{'x': 9, 'y': 0}, {'x': 9, 'y': 1}, {'x': 9, 'y': 2}], 'head': {'x': 9, 'y': 0}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#FFFF00', 'head': 'fang', 'tail': 'block-bum'}}, {'id': 'fc917519-276a-4d76-b553-166cc4b4340b', 'name': 'snek3', 'latency': '3', 'health': 99, 'body': [{'x': 5, 'y': 4}, {'x': 5, 'y': 5}, {'x': 5, 'y': 6}, {'x': 5, 'y': 7}], 'head': {'x': 5, 'y': 4}, 'length': 4, 'shout': '', 'squad': '', 'customizations': {'color': '#FFFF00', 'head': 'fang', 'tail': 'block-bum'}}], 
    
    'food': [{'x': 0, 'y': 6}, {'x': 10, 'y': 4}, {'x': 6, 'y': 10}, {'x': 8, 'y': 6}, {'x': 0, 'y': 4}], 'hazards': []}, 
    
    'you': {'id': '3d6b6171-8a95-41d9-86a5-db01fa72e0aa', 'name': 'snek2', 'latency': '0', 'health': 95, 'body': [{'x': 9, 'y': 0}, {'x': 9, 'y': 1}, {'x': 9, 'y': 2}], 'head': {'x': 9, 'y': 0}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#FFFF00', 'head': 'fang', 'tail': 'block-bum'}}}


clean_game_state(state) 
pretty_print(state)
start_time = time.time()
print(a_star(state, state["board"]["food"][1], 5))
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Function execution time: {elapsed_time} seconds")

