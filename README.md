# evei

Purdue EPICS EVEI Data Acquisition Team Code

## Documentation

See the `spring2019` branch for the old python script.

See `example.csv` for an example Physics Box log file.

See `MANUAL.md` for the user's manual.

### Program Design Details

The main program, located in `main.py`, is primarily responsible for initializing components of the program and then continuously updating them throughout the program's runtime. 

`graph.py` handles all of the plotting of the data - the init method sets up the graph displays, and the update method redraws the graph lines when data is updated.

`serial.py` is responsible for handling serial connections. The connect method connects to the selected serial port, and the update method polls for more data and parses the strings for data. The parse method does the heavy lifting of this, primarily through a regular expression.

`window.py` handles the other UI elements, such as the serial port selection dialog popup.

### RF Serial Transmission Spec

Currently, the RF transmission is done as a simple 2 wire serial connection. It uses a 9600 baud rate, no parity, 8 data bits, and 1 stop bit.

The RF transmitter simply reads the data being sent to the Physics Box's display and transmits the characters over serial. The format looks something like this:

```
RM0    A0.0B0.0D
E0     +1 -11+10
```

## Design Roadmap

- [x] Display graphs of RPM, Gyros, Throttle, and Steering
- [x] Use actual serial data instead of random data
- [x] Add serial port selection dialog
- [x] Overlay Gyro Graphs
- [ ] Add start/stop display button
- [ ] Add option to flip analog port assignments
- [ ] Add options to change serial port configs
- [ ] Add ability to calibrate steering & throttle; display as % or angle instead of voltage
- [ ] Add digital event/lap count

## Serial Simulation

Serial simulation currently only works on Linux. First, you must run the `virtual_serial.sh` shell script to create a virtual serial port device. Then, run `simulate_serial.py FILE` to write a CSV log file to the virtual serial port. Then, you can run the program - be sure to connect to `/dev/ttyS10` to see this simulated serial data.
