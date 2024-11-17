import zmq

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    activities = [
        {"id": 1, "name": "Run", "distance": 5.0, "duration": "00:45:00", 'elevation': 1000},
        {"id": 2, "name": "Walk", "distance": 2.0, "duration": "00:30:00", 'elevation': 245}
    ]

    # send activities to microservice
    print('Sending activities...')
    socket.send_json({"action": "convert", "data": activities})

    # recieve converted activites
    print('Converting units...')
    converted_activities = socket.recv_json()

    # print original data
    print('\nOriginal Data: ')
    for i, activity in enumerate(activities, start=1):
        print(f'Activity {i} distance in miles: {activity['distance']}')
        print(f'Activity {i} elevation in feet: {activity['elevation']}')

    # print converted data
    print('\nConverted Data: ')
    for i, activity in enumerate(converted_activities, start=1):
        print(f'Activity {i} distance in kilometers: {activity['distance']}')
        print(f'Activity {i} elevation in meters: {activity['elevation']}')

if __name__ == '__main__':
    main()