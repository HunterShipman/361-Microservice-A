import zmq
import time

def convert_distance(activities):
    '''
    Converts each activites 'distance' key from miles to kilometers. Does not alter original 'activites' list.
    The conversion is approximate, to make it more or less precise edit the 'km_conversion' variable. You can
    also edit or remove the round() function.
    Also converts the 'elevation' key value from feet to meters using the 'meter_conversoin' variable and rounds
    to the 3rd decimal point.

    Args:
        activites (list): A list of activity objects, each activity must be a dictionary with a 'distance' key.
    '''
    km_conversion = 1.609
    meter_conversion = 3.281
    for activity in activities:
        activity['distance'] = round(activity['distance'] * km_conversion, 3)
        activity['elevation'] = round(activity['elevation'] / meter_conversion, 3)
    
    return activities

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    print('Listening for requests...')
    while True:
        # recieve request
        request = socket.recv_json()

        # check if the action is "convert"
        if request.get('action') == 'convert':
            activities = request.get('data', [])
        
            # convert miles to kilometers and feet to meters
            converted_activities = convert_distance(list(activities))

            # artificial processing time
            print('Starting unit conversion...')
            time.sleep(2)

            # send response
            socket.send_json(converted_activities)
    

if __name__ == '__main__':
    main()