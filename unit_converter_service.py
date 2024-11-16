import zmq

def convert_distance(activities):
    '''
    Converts each activites 'distance' key from miles to kilometers. Does not alter original 'activites' list.
    The conversion is approximate, to make it more or less precise edit the 'conversion' variable.

    Args:
        activites (list): A list of activity objects, each activity must be a dictionary with a 'distance' key.
    '''
    conversion = 1.609
    for activity in activities:
        activity['distance'] = activity['distance'] * conversion
    
    return activities

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    print('Listening for requests...')
    while True:
        # recieve request
        activities = socket.recv_json()
        
        # convert miles to kilometers
        converted_activities = convert_distance(list(activities))

        # send response
        socket.send_json(converted_activities)
    

if __name__ == '__main__':
    main()