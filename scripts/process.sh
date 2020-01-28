#!/bin/bash
#mkdir processed 
for d in EP MU IN MW
do
    for n in 0 1 2 3 4 5 6 7 8 9
    do
        mkdir test/$d/$n -p
    done
done

echo "Done creating processing directories"

echo "Starting mega-processing..."
#python3 process.py
echo "DONE!"
