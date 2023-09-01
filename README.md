# Python code for LSLiDAR N10
I put together this really simple code for reading the LSLiDAR N10 through python and pure serial.

## Dependencies
- [`pyserial`](https://pypi.org/project/pyserial/)

## Usage
```python3
from n10 import N10
n10 = N10('COM7') # Initialize the N10
n10.scan(lambda x:print(f'Angle: {x[0]}, Distance: {x[1]}')) # Start scanning
```

## Reference
- ### `N10.start()`

Start the scanning in the LiDAR


- ### `N10.stop()`

Stop the scanning in the LiDAR


- ### `N10.scan(update: Callable)`

Scan the data received. All the received data will be passed as a parameter to a function provided.<br>
The data is passed as a list of tuples, containing the angle and distance (in milimeters).<br>
Example: `[(1, 300), (2, 300), (3, 401)]`
