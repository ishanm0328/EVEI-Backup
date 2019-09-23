# RF Serial Transmission Spec

Currently, the RF transmission is done as a simple 2 wire serial connection. It uses a 9600 baud rate, no parity, 8 data bits, and 1 stop bit.

The RF transmitter simply reads the data being sent to the Physics Box's display and transmits the characters over serial. The format looks something like this:

```
RM0    A0.0B0.0D
E0     +1 -11+10
```
