# Microservice Communication

My unit converter service communicates via ZeroMQ and the microservice binds to port 5555. You must install ZeroMQ before using this microservice and include 'import zmq' in your main program. If you need to, you can change the port the microservice binds to incase it is already in use.

## Files
unit_converter_service.py is the microservice  
converter_example.py is the test program shown in the video

## REQUESTING DATA:
First you must set up ZeroMQ context and create a request socket, and then send a request. The variable 'activities' is an example of what the JSON will need to look like, which is a list of dictionaries with each dictionary having a key named 'distance'. The request must be in the form of a dictionary with an 'action' key that has a 'convert' value and a 'data' key with its corresponding value being the JSON you want to convert. If you need to change the port, change the '5555' in "tcp://localhost:5555" to your new port. You must also change the port in the microservice, '5555' in "tcp://*:5555" to your new port.

```python
import zmq

# ZeroMQ setup
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# example JSON
activities = [
        {"id": 1, "name": "Run", "distance": 5.0, "duration": "00:45:00", 'elevation': 1000},
        {"id": 2, "name": "Walk", "distance": 2.0, "duration": "00:30:00", 'elevation': 245}
    ]

# example request call, 'action' is set to 'covert'.
socket.send_json({"action": "convert", "data": activities})
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

## UML DIAGRAM
![UML Diagram](https://github.com/HunterShipman/361-Microservice-A/blob/07a9d65607575afc5cbb540359f79bcb7970d36f/Diagram.png)