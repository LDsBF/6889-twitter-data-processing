from n import WordCloud
from n import ImageColorGenerator
from n import STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
import glob
path = r'Users/liupeihan/Desktop/hashtag_file.csv_file.csv/' # use your path
all_files = glob.glob(path + "/*.csv")

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)

text = " ".join(i for i in df.text)
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
plt.figure( figsize=(15,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

