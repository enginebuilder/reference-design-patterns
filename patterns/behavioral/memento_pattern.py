class GameState:
    def __init__(self, x, y, prev = None) -> None:
        self.x = x
        self.y = y
        self.prev: GameState = prev

class Game:
    def __init__(self, coordinates) -> None:
        state = GameState(x=coordinates[0], y=coordinates[1])
        self.curr_state: GameState = state

    def move(self, coordinates):
        new_state = GameState(x=coordinates[0], y=coordinates[1])
        self.curr_state, self.curr_state.prev = new_state, self.curr_state

    def print_moves(self):
        state = self.curr_state
        result = ''
        print("Game steps:")
        while state:
            result += f"({state.x}, {state.y})"
            state = state.prev
        print(result)
    
    def save(self):
        return GameState(self.curr_state.x, self.curr_state.y, self.curr_state.prev)
    
    def rollback(self, state):
        self.curr_state = state

if __name__ == "__main__":
    game = Game((0, 0))
    game.move((1,0))
    game.move((1,1))
    some_state = game.save()
    game.move((2,1))
    game.print_moves()
    game.rollback(some_state)
    game.print_moves()
    
    