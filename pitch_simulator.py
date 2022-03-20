import json

import matplotlib.pyplot as plt
import zmq
import rtls_pb2 as rt
from matplotlib.animation import FuncAnimation

class PitchSimulator:

    PITCH_LENGTH = 40.0
    PITCH_WIDTH = 24.0
    NUMBER_OF_PLAYERS = 10

    def __init__(self, game_time):
        self.__ani = None
        self.__game_time = game_time
        self.__fig,self.__ax = plt.subplots()
        self.__context = zmq.Context()
        self.__socket = self.__context.socket(zmq.REP)
        self.__game_time = 100
        self.__points = []
        self.__annotations = []
        self.__position_history = []
        self.__socket.bind("tcp://*:5555")
        #  Socket to talk to server
        print("Connecting to rtls server…")
        self.simulate()

    def simulate(self):
        # set the axes limits - Futsal pitch size
        self.__ax.axis([-self.PITCH_LENGTH/2, self.PITCH_LENGTH/2, -self.PITCH_WIDTH/2, self.PITCH_WIDTH/2])
        for n in range (1,11):
            color='green' if n<6 else 'blue'
            newP, = self.__ax.plot(0,n,marker="o",color=color)
            self.__points.append(newP)
            self.__annotations.append(self.__ax.annotate(str(n), xy=(0,n)))
        self.__ani = FuncAnimation(self.__fig, self.update_pitch, save_count=10)
        self.__fig.set_size_inches(10, 6)
        plt.show()

    # Updating players position from server on the pitch, to be repeatedly called by the animation
    def update_pitch(self,t):
        message = self.__socket.recv()
        if message == b'Finish':
            self.__socket.close()
            self.__ani.event_source.stop()
            return self.__points[0], self.__annotations[0]
        position_message = rt.Position()
        position_message.ParseFromString(message)
        id = position_message.sensorId
        if id<1 or id>10 :
            return
        x = position_message.position.x
        y = position_message.position.y
        z = position_message.position.z
        self.__points[id-1].set_data([x],[y])
        self.__annotations[id-1].set_position((x,y))
        self.__annotations[id-1].xy = (x, y)
        self.__position_history.append(
            {"id": id, "usec": position_message.timestamp_usec, "x": round(x,4), "y": round(y,4), "z": round(z,4)})
        self.__socket.send(b"message received")
        return self.__points[id-1], self.__annotations[id-1]

    def write_input_history(self):
        json_input = json.dumps(self.__position_history)
        with open("pitch_input.json", "w") as outfile:
            outfile.write(json_input)
