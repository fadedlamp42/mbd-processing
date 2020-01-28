import pandas as pd
import time
import sys
import os
print("imports finished")
print()

if len(sys.argv) == 1:
    devices = ("EP", "IN", "MU", "MW")
else:
    devices = sys.argv[1:]

for d in devices:
    name = "raw/" + d + ".txt"
    if not os.path.exists(name):
        print(f"{name} does not exist! Continuing...")
        continue

    print(f"Opening {name}")

    start = time.process_time()
    df = pd.read_csv(name, delimiter='\t', names=['id','event','device','channel','code','size','data'])
    end = time.process_time()

    print(f"Opened {name} in {round(end-start, 2)} seconds\n")

    event_groups = df.groupby(df['event'])
    for event in event_groups: #event[0] is group, event[1] is dataFrame of event data
        output = pd.DataFrame()
        code = None

        ms_added = False
        for index, row in event[1].iterrows():
            if not ms_added:
                code = int(row['code'])
                size = int(row['size'])

                ms_added = True
                step = 1000/(size/2)
                ms = [step]
                for i in range(1, size):
                    ms.append(ms[i-1] + step)

                output = output.assign(ms=ms)

            readings = row['data'].split(',')
            channel = row['channel']
            new_col = pd.DataFrame(readings, columns=[channel])
            output = pd.concat([output, new_col], axis=1)

        path = f"processed/{d}/{code}/{event[0]}.csv"
        if code != -1:
            output.to_csv(path_or_buf=path, index=False)
            print(f"Saved to {path}")
        else:
            print("Noise event skipped")

    print(f"finished processing {d}")
