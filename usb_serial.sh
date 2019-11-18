#!/usr/bin/env bash

id=$(lsusb | grep "FT232" | awk '{ print $6 }')
vendor=$(echo $id | awk -F ':' '{ print $1 }')
product=$(echo $id | awk -F ':' '{ print $1 }')
sudo modprobe usbserial vendor=0x$vendor product=0x$product
