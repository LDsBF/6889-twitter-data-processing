import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob

path = 'hashtag_file.csv'
all_files = glob.glob(path + "/*.csv")

# li = []

for filename in all_files:
    df = pd.read_csv(filename)
    print(df)
    print(df.describe())

    objects = df.word
    y_pos = np.arange(len(objects))
    count = df.word_count

    plt.barh(y_pos, count, align='center', alpha=0.5, color="navy")
    plt.yticks(y_pos, objects)
    plt.xlabel('Count')
    plt.title('Top Ten Hashtag Tweets')

    plt.show()

path = 'country_file.csv'
all_files = glob.glob(path + "/*.csv")

# li = []

for filename in all_files:
    df = pd.read_csv(filename)
    print(df)
    print(df.describe())

    objects = df.country_code
    y_pos = np.arange(len(objects))
    count = df.tweet_count

    plt.barh(y_pos, count, align='center', alpha=0.5, color="yellow")
    plt.yticks(y_pos, objects)
    plt.xlabel('Count')
    plt.title('Top Ten Tweets Source Country')

    plt.show()

path = 'device_file.csv'
all_files = glob.glob(path + "/*.csv")

# li = []

for filename in all_files:
    df = pd.read_csv(filename)
    print(df)
    print(df.describe())

    objects = df.device
    y_pos = np.arange(len(objects))
    count = df.device_count

    plt.barh(y_pos, count, align='center', alpha=0.5, color="green")
    plt.yticks(y_pos, objects)
    plt.xlabel('Count')
    plt.title('Top Ten Hashtag Tweets')

    plt.show()
# li.append(df)

# frame = pd.concat(li, axis=0, ignore_index=True)
# print(li)

# df = pd.read_csv('/hashtag.csv')
#
# df.describe()