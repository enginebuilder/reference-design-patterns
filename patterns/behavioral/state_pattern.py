class PlayerState:
    def die(self):
        pass
    def play(self):
        pass
    def resurrect(self):
        pass

class DeadPlayerState(PlayerState):
    def die(self):
        raise Exception("Already dead")
    
    def play(self):
        raise Exception("Can't play in dead state")
    
    def resurrect(self):
        print("I am alive again!")
        return AlivePlayerState()

class AlivePlayerState(PlayerState):
    def die(self):
        print("Oh no, I am dead!")
        return DeadPlayerState()

    def play(self):
        print("Playing game")
        return self
    
    def resurrect(self):
        raise Exception("I am not dead")
    
class Player:

    def __init__(self) -> None:
        self.state = AlivePlayerState()

    def die(self):
        self.state = self.state.die()

    def play(self):
        self.state = self.state.play()

    def resurrect(self):
        self.state = self.state.resurrect()

if __name__ == "__main__":
    player = Player()
    player.play()
    player.die()
    player.resurrect()
