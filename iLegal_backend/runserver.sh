#!/bin/bash
source activate hackzurich
git pull
killall python
nohup python main.py &
