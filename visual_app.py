import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas as pd
import glob
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
from wordcloud import STOPWORDS

#tag
def tag():
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
    plt.savefig('./resource/tag.jpg')

    plt.show()
    #
    text = " ".join(i for i in df.word)
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
    plt.figure(figsize=(15, 10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('./resource/wordcloud_tag.jpg')
    plt.show()

#country
def country():
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
    plt.savefig('./resource/country.jpg')

    plt.show()

    text = " ".join(i for i in df.country_code)
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
    plt.figure(figsize=(15, 10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('./resource/wordcloud_country.jpg')
    plt.show()

#device
def device():
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
    plt.savefig('./resource/device.jpg')

    plt.show()

    text = " ".join(i for i in df.device)
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
    plt.figure(figsize=(15, 10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('./resource/wordcloud_device.jpg')
    plt.show()


#折线图
def number():
    path = r'Users/liupeihan/Desktop/number_file.csv/'  # use your path
    all_files = glob.glob(path + "/*.csv")

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
    df.describe()

    objects = df.num
    y_pos = objects
    length = len(y_pos)
    count = []
    for i in range(length):
        count.append(30*i)

    # plt.barh(count, y_pos, alpha=0.5, color="r")
    plt.plot(count,y_pos, 's-', color = 'r')
    plt.xlabel('Time')
    plt.ylabel("Number")
    plt.title('number of twits per 30 seconds')
    plt.savefig('./resource/number.jpg')

    plt.show()

tag()
country()
device()
number()