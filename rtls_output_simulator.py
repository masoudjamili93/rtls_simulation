import json
import math
import time
import zmq
import random
import rtls_pb2 as pb

class RtlsSimulator:
    # pitch size; a common Futsal 40m * 24m pitch
    PITCH_MAX_X = 20.0
    PITCH_MIN_X = -20.0
    PITCH_MAX_Y = 12.0
    PITCH_MIN_Y = -12.0
    UPDATE_SPEED = 1.0     # update speed in HZ
    NUMBER_OF_PLAYERS = 10  # should be even
    __game_time = 100
    __players_position = []     # position messages will be store here
    __position_history = []

    def __init__(self, game_time):
        # generating player's start position
        self.game_time = game_time
        n = self.NUMBER_OF_PLAYERS
        for i in range(0, int(n/2)+1):   # generating home team, i+1 is the player number
            data = pb.Data3d()
            data.x = -4
            data.y = pow(-1, i) * i
            data.z = 0
            self.__players_position.append(data)

        for i in range(int(n/2)+1, n):  # generating away team
            data = pb.Data3d()
            data.x = 4
            data.y = pow(-1, i) * (i - 5)
            data.z = 0
            self.__players_position.append(data)

        self.send_position_update()

    def get_random_velocity(self):
        vel_length = random.randint(20, 400)*self.UPDATE_SPEED    # random length in cm
        vel_degree = random.randint(0, 360)*self.UPDATE_SPEED     # random movement degree
        # random Z parameter in cm - 10% possibility of jumping
        vel_z = random.randint(1, 100) if random.randint(1, 10) == 2 else 0
        # calculate x,y from polar velocity
        vel_x = vel_length * math.cos(math.radians(vel_degree))/100
        vel_y = vel_length * math.sin(math.radians(vel_degree))/100
        output = pb.Data3d()
        output.x = vel_x
        output.y = vel_y
        output.z = vel_z/100    # M to CM
        return output

    def send_position_update(self):
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:5555")
        for usec in range(self.game_time):
            time.sleep(self.UPDATE_SPEED)           # position update in Hz
            for n in range(0, self.NUMBER_OF_PLAYERS):
                random_movement = self.get_random_velocity()
                # check that players not leaving the pitch
                x = self.__players_position[n].x + random_movement.x
                y = self.__players_position[n].y + random_movement.y
                if x > self.PITCH_MAX_X:
                    x -= random_movement.x*2
                if x < self.PITCH_MIN_X:
                    x -= random_movement.x*2
                if y > self.PITCH_MAX_Y:
                    y -= random_movement.y*2
                if y < self.PITCH_MIN_Y:
                    y -= random_movement.y*2
                self.__players_position[n].x = x
                self.__players_position[n].y = y
                self.__players_position[n].z += random_movement.z
                # generating ZMQ message
                message = pb.Position()
                message.sensorId = n+1
                message.timestamp_usec = usec
                message.position.x = self.__players_position[n].x
                message.position.y = self.__players_position[n].y
                message.position.z = self.__players_position[n].z
                # for unit test
                self.__position_history.append(
                    {"id": n+1, "usec": usec, "x": round(x, 4), "y": round(y, 4), "z": round(message.position.z, 4)})
                socket.send(message.SerializeToString())
                socket.recv()

        # for unit test; need to be compared with the client input (pitch_simulator)
        socket.send(b"Finish")
        json_output = json.dumps(self.__position_history)
        with open("rtls_output.json", "w") as outfile:
            outfile.write(json_output)
