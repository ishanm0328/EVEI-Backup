#!/usr/bin/env bash

sudo socat -d -d pty,raw,echo=0,link=/dev/ttyS10,mode=666\
                 pty,raw,echo=0,link=/dev/ptyS10,mode=666
