class GameStateManager:
    def __init__(self, state):
        self._currentState = state
        self._previousState = None
    
    
    def set_state(self, state):
        self._previousState = self._currentState
        self._currentState = state


    def get_previous_state(self):
        return self._previousState

    def get_state(self):
        return self._currentState
