#setting up a exit() funktion which stops cell execution but 
#dosent kill the Kernal. (Also prints errors like in CPython)
#mostly copyid from: https://stackoverflow.com/questions/24005221/ipython-notebook-early-exit-from-cell
class StopExecution(Exception):
    def _render_traceback_(self):
        return []
def exit(kill_reason): raise StopExecution(kill_reason)