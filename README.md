# evei

Purdue EPICS EVEI Data Acquisition Team Code

## Documentation

See the `spring2019` branch for the old python script.

See `SPEC.md` for details on the serial communication protocol used between the Physics Box and the radio receiver.

See `example.csv` for an example Physics Box log file.

See `MANUAL.md` for the user's manual.

## Design Roadmap

- [x] Display graphs of RPM, Gyros, Throttle, and Steering
- [x+0 +0 +9 
] Use actual serial data instead of random data
- [ ] Add start/stop display button
- [ ] Add serial port selection dialog
- [ ] Add option to flip analog port assignments
- [ ] Add options to change serial port configs
- [ ] Add ability to calibrate steering & throttle; display as % or angle instead of voltage
- [ ] Add digital event/lap count

## Serial Simulation

Serial simulation currently only works on Linux. First, you must run the `virtual_serial.sh` shell script to create a virtual serial port device. Then, run `simulate_serial.py FILE` to write a CSV log file to the virtual serial port. Then, you can run the program - be sure to connect to `/dev/ttyS10` to see this simulated serial data.
