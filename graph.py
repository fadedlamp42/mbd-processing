import seaborn as sns
import matplotlib.pyplot as matplt
import sys
import os
import pandas as pd
print("imports finished")
print()

#device folders to process
if len(sys.argv) == 1:
    devices = ("EP", "IN", "MU", "MW")
else:
    devices = sys.argv[1:]

#number of events from each folder to process
count = 10

for d in devices:
    for n in range(10):
        path = f"processed/{d}/{n}/"
        out_path = f"graphs/{d}/{n}/"

        if not os.path.exists(path):
            print(f"{path} does not exist! Continuing...")
            continue

        files = os.listdir(path)
        files = files[:count]
        for fname in files:
            if not os.path.exists(path + fname):
                print(f"{path + fname} does not exist! Continuing...")
                continue

            out_name = out_path + fname.split('.')[0] + '.png'
            if os.path.exists(out_name):
                print(f"{out_name} exists already! Continuing...")
                continue

            frame = pd.read_csv(path + fname)
            print("Opened " + path + fname)
            x_col = list(frame['ms'].values)
            y_col = []
            labels = []

            for col_name in frame.columns[1:]:
                for v in frame[col_name].values:
                    y_col.append(v)

                for i in range(len(frame[col_name].values)):
                    labels.append(col_name)

            copies = len(frame.columns[1:])
            x_col = x_col * copies

            data = {'ms':x_col, 'amplitude':y_col, 'labels':labels}
            graph_frame = pd.DataFrame.from_dict(data)
            plt = sns.relplot(x='ms', y='amplitude', data=graph_frame, col='labels', kind='line', col_wrap=4)
            plt.savefig(out_name)
            matplt.close('all')
            print(out_name + " saved")
            print()
