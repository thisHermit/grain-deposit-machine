#!/bin/bash
python3 label_image.py --graph=./output_graph.pb --labels=./output_labels.txt --input_layer=Placeholder --output_layer=final_result --input_height=224 --input_width=224 --image=/home/pi/image.png
