import numpy as np
from update_game_state import clean_game_state
def pretty_print(game_state):
    if game_state == {}:
        print("===LOST!===")
        return 
    grid = np.zeros((game_state["board"]["width"],game_state["board"]["height"]))
    for bp in game_state["you"]["body"]:
        grid[bp["x"]][bp["y"]] = 1
    for snake in game_state["board"]["snakes"]:
        for bp in snake["body"]:
            grid[bp["x"]][bp["y"]] = 2
    for apple in game_state["board"]["food"]:
        grid[apple["x"]][apple["y"]] = 3
    grid = np.rot90(grid)
    print(grid)
    return