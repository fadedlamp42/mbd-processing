#!/bin/bash
mkdir graphs
for d in EP MU IN MW
do
    for n in 0 1 2 3 4 5 6 7 8 9
    do
        mkdir graphs/$d/$n -p
    done
done

echo "Done creating graphing directories"

echo "Starting graphing..."
python3 graph.py
echo "Done!
