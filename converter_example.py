import zmq

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    activities = [
        {"id": 1, "name": "Run", "distance": 5.0, "duration": "00:45:00"},
        {"id": 2, "name": "Walk", "distance": 2.0, "duration": "00:30:00"}
    ]

    print('Sending activities...')

    # send activities to microservice
    socket.send_json({"action": "convert", "data": activities})

    print('Converting units...')

    # recieve converted activites
    converted_activities = socket.recv_json()

    print('Activity distances in miles: ')

    # print original data
    for activity in activities:
        print(activity['distance'])

    # print converted data
    print('Activity distances in kilometers: ')
    for activity in converted_activities:
        print(activity['distance'])

if __name__ == '__main__':
    main()