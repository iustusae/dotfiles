#!/usr/bin/env bash

DSP=$(xrandr | awk '/1920x1080/ {print $1}' | head -n 1)

xrandr --output $DSP --primary
echo "Xwayland: Primary monitor set"
