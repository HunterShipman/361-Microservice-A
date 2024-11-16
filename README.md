# Microservice Communication

My unit converter service communicates via ZeroMQ and the microservice binds to port 5555. You must install ZeroMQ before using this microservice and include 'import zmq' in your main program. If you need to, you can change the port the microservice binds to incase it is already in use.

## Files
unit_converter_service.py is the microservice
converter_example.py is the test program shown in the video

## REQUESTING DATA:
First you must set up ZeroMQ context and create a request socket, and then send a request. 'activities' is an example of what the JSON will need to look like, which is a list of dictionaries with each dictionary having a key named 'distance'. If you need to change the port, change the '5555' in "tcp://localhost:5555" to your new port. You must also change the port in the microservice, '5555' in "tcp://*:5555" to your new port.

```python
import zmq

# ZeroMQ setup
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# example JSON
activities = [
        {"id": 1, "name": "Run", "distance": 5.0, "duration": "00:45:00"},
        {"id": 2, "name": "Walk", "distance": 2.0, "duration": "00:30:00"}
    ]

# example request call
socket.send_json(activities)
```

## RECEIVING DATA:
With ZeroMQ already set up to send data, receiving data is much more simple.

```python
# example recieve data call
converted_activities = socket.recv_json()
```

In this example, converted_activities will be nearly identical to the JSON
object given to the microservice, but with the 'distance' fields converted
from miles to kilometers.