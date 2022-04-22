import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas as pd
import glob
#tag
path = r'Users/liupeihan/Desktop/hashtag_file.csv/' # use your path
all_files = glob.glob(path + "/*.csv")

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)

df.describe()
print(df)
import matplotlib.pyplot as plt;plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = df.word
y_pos = np.arange(len(objects))
count = df.word_count

plt.barh(y_pos, count, align='center', alpha=0.5, color="navy")
plt.yticks(y_pos, objects)
plt.xlabel('Count')
plt.title('Top Ten Hashtag Tweets')

plt.show()
#

#country
path = r'Users/liupeihan/Desktop/country_file.csv/' # use your path
all_files = glob.glob(path + "/*.csv")

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
df.describe()

objects = df.country_code
y_pos = np.arange(len(objects))
count = df.tweet_count

plt.barh(y_pos, count, align='center', alpha=0.5, color="brown")
plt.yticks(y_pos, objects)
plt.xlabel('Count')
plt.title('Tweets from Top 10 countries')

plt.show()

#device
path = r'Users/liupeihan/Desktop/device_file.csv/' # use your path
all_files = glob.glob(path + "/*.csv")

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
df.describe()

objects = df.device
y_pos = np.arange(len(objects))
count = df.device_count

plt.barh(y_pos, count, align='center', alpha=0.5, color="yellow")
plt.yticks(y_pos, objects)
plt.xlabel('Count')
plt.title('Tweets originating from devices')

plt.show()
