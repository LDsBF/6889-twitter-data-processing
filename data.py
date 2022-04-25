import pandas as pd
import glob

path = r'Users/liupeihan/Desktop/country_file.csv/' # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)
new = str(li[0]).split(" ")
country_name = []
country_num = []
country = {}
print(new)

for i in range(len(new)):
    if new[i][:2] == 'CC':
        country_name.append(new[i])
    if new[i] and new[i][0].isdigit():
        country_num.append(new[i])
for i in range(len(country_name)):
    if country_num[i][:-2]:
        country[country_name[i]] = country_num[i][:-2]
    else:
        country[country_name[i]] = country_num[i]
print(country)