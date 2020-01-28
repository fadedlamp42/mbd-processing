# Graphical Exploration of the [MindBigData Dataset](http://mindbigdata.com/opendb/index.html)
![Graph of contemplating the number 6](https://i.imgur.com/KQ3BkU4.png)
### Purpose
This was a project I completed largely over the winter break of 2019. My motivation was to learn more about Pandas, Numpy, and Seaborn for data manipulation, processing, and visualization. 

### Usage
For basic usage, run `make` or `make all` to download, process, and graph the dataset. Produces `raw/`, `processed/` and `graphs/` directories.

To download, run `make download`. Creates `raw/` then downloads and extracts raw data to text files.

To run processing on the data, run `make process`. Creates processed/ directory and appropriate subdirectories following the following structure: `processed/[DEVICE]/[DIGIT]/*.csv`

To graph, run `make graph`. Creates `graphs/` then graphs 10 of each number recorded by each device. Follows similar structure to `processed`: `graphs/[DEVICE]/[DIGIT]/*.png`

To clean up, run `make clean`. Removes `graphs/` and `processed/`. Keeps `raw/` in tact for convenience.

### Data
This dataset contains ~1.2 million signals corresponding to brain activity when viewing numbers (digits) 0-9. The data is divided by device, broken down to rows which represent readings of just one channel over one signal, and grouped by id to form complete tables of channels and their corresponding readings. 

The data refers to "channels" by letter and number regularly. These channel names can be cross-referenced with the following image to develop a more natural intuition of this set and its physical interpretation.
![Mapping of brain regions to channel names](http://mindbigdata.com/images/DavidVivancosBrainAreas10-20.png)

[More technical details](http://mindbigdata.com/opendb/index.html) are provided by the authors of the dataset
### Conclusion
I found this dataset fun and intuitive to work with. It taught me much about using Pandas DataFrames and avoiding memory leaks with Seaborn. In the future I would like to complete a more analytical task with EEG data, but one step at a time!
