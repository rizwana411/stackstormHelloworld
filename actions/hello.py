import sys

from st2common.runners.base_action import Action

class MyEchoAction(Action):
    def run(self, message):
        print(message)

        if message == 'Rizwana':
            return (True, "Hello" + message)
        return (False, "Bye" + message)