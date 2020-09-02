#!/usr/bin/env python
# coding: utf-8

# # HESA Data - UK Undergraduate Students


# Analysing student population number for UK undergraduate students 
# Data source: https://www.hesa.ac.uk/data-and-analysis/students/where-study


# import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# import data: HE student enrolments by HE provider (2018-2019)
data1819 = pd.read_csv("dt051-table-1 (20182019).csv", skiprows=17, nrows=169)

# set the UKPRN as the primary key
data1819.set_index("UKPRN",inplace=True)


# List the dataset columns
for i in data1819.columns.values:
    print (i)

# view data structure
data1819.info()


# View sample data
data1819.head()


# Convert object data to numbers, for each country in the UK
for i in data1819.columns.values[1:5]:
    data1819[i] = data1819[i].str.replace(",","")
    data1819[i] = data1819[i].astype(int)

data1819.head()


# # Basic arithmatic


# Total number of students from England?
print("Students from England (Total): ", data1819.England.sum(), "\n")


# Total number of UK undergraduate students
total = data1819.England.sum() + data1819.Scotland.sum() + data1819.Wales.sum() + data1819["Northern Ireland"].sum()
print("Total number of UK undergraduate students (2018/2019): ", total)


# # Basic Queries


# Average number of students from each UK country at university
e = int(data1819.England.mean())
s = int(data1819.Scotland.mean())
w = int(data1819.Wales.mean())
i = int(data1819["Northern Ireland"].mean())

print("Number of UK students from each country at a UK university (average)")
print("England: ", e)
print("Scotland: ", s)
print("Wales: ", w)
print("Northern Ireland: ", i)



# Number of universities with 10 or less students from England
data1819[data1819["England"] <= 10]

# Number of universities with 1,000 or more students from each UK country
data1819[(data1819["England"] >= 1000) & (data1819["Scotland"] >= 1000) & (data1819["Wales"] >= 1000) & (data1819["Northern Ireland"] >= 1000)]


# Number of universities with no students from Ireland
data1819[data1819["Northern Ireland"] == 0]


# Search for univeristy details

# Search for a university... enter the name in the 'contains' method
uni_search = "Leeds"
uni = data1819[data1819["HE provider"].str.contains(uni_search)]

# 'uni' is a two dimensional array as [row][columns] accessible using indecies
uni


# count position of univeristy row, starting at 0, e.g. 3 = The University of Leeds
uni_name  = uni.iloc[3][0] # the second array dimension is the column index, e.g. 1 = 'HE provider', 2 = 'England'
uni_eng   = uni.iloc[3][1]
uni_scot  = uni.iloc[3][2]
uni_wal   = uni.iloc[3][3]
uni_ire   = uni.iloc[3][4]
uni_total = uni_eng + uni_scot + uni_wal + uni_ire

print("Students at", uni_name)
print("England: ", uni_eng)
print("Scotland: ", uni_scot)
print("Wales: ", uni_wal)
print("Northern Ireland: ", uni_ire)
print("Total: ", uni_total)


# Visualise the data

# For these visualisations, we'll compare historical data to the most recent data available

# import and normalise data: HE student enrolments by HE provider (2014-2015)
data1415 = pd.read_csv("dt051-table-1 (20142015).csv", skiprows=17, nrows=169)
data1415.set_index("UKPRN",inplace=True)
for i in data1415.columns.values[1:5]:
    data1415[i] = data1415[i].str.replace(",","")
    data1415[i] = data1415[i].astype(int)

# import and normalise data: HE student enrolments by HE provider (2015-2016)
data1516 = pd.read_csv("dt051-table-1 (20152016).csv", skiprows=17, nrows=169)
data1516.set_index("UKPRN",inplace=True)
for i in data1516.columns.values[1:5]:
    data1516[i] = data1516[i].str.replace(",","")
    data1516[i] = data1516[i].astype(int)

# import and normalise data: HE student enrolments by HE provider (2016-2017)
data1617 = pd.read_csv("dt051-table-1 (20162017).csv", skiprows=17, nrows=169)
data1617.set_index("UKPRN",inplace=True)
for i in data1617.columns.values[1:5]:
    data1617[i] = data1617[i].str.replace(",","")
    data1617[i] = data1617[i].astype(int)

# import and normalise data: HE student enrolments by HE provider (2017-2018)
data1718 = pd.read_csv("dt051-table-1 (20172018).csv", skiprows=17, nrows=169)
data1718.set_index("UKPRN",inplace=True)
for i in data1718.columns.values[1:5]:
    data1718[i] = data1718[i].str.replace(",","")
    data1718[i] = data1718[i].astype(int)

# display data from 2014-2015
data1415.head()

# Get data for Durham University over the years (2015-2019)

dur1415 = data1415[data1415["HE provider"].str.contains("Durham")]
dur1516 = data1516[data1516["HE provider"].str.contains("Durham")]
dur1617 = data1617[data1617["HE provider"].str.contains("Durham")]
dur1718 = data1718[data1718["HE provider"].str.contains("Durham")]
dur1819 = data1819[data1819["HE provider"].str.contains("Durham")]

dur_eng = [dur1415.iloc[0][1], dur1516.iloc[0][1], dur1617.iloc[0][1], dur1718.iloc[0][1], dur1819.iloc[0][1]]
dur_sco = [dur1415.iloc[0][2], dur1516.iloc[0][2], dur1617.iloc[0][2], dur1718.iloc[0][2], dur1819.iloc[0][2]]
dur_wal = [dur1415.iloc[0][3], dur1516.iloc[0][3], dur1617.iloc[0][3], dur1718.iloc[0][3], dur1819.iloc[0][3]]
dur_ire = [dur1415.iloc[0][4], dur1516.iloc[0][4], dur1617.iloc[0][4], dur1718.iloc[0][4], dur1819.iloc[0][4]]

year = list(['2015', '2016', '2017', '2018', '2019'])

# display students at Durham University who come from England

print("Number of Undergraduate Students at Durham University from England (2015-2019)")
print("2015: ", dur_eng[0])
print("2016: ", dur_eng[1])
print("2017: ", dur_eng[2])
print("2018: ", dur_eng[3])
print("2019: ", dur_eng[4])


# To help visualise the trend over time for Durham University undergraduate students by country, 
# lets create dataframes to hold values per country

dur_eng_df = pd.DataFrame(dur_eng)
dur_sco_df = pd.DataFrame(dur_sco)
dur_wal_df = pd.DataFrame(dur_wal)
dur_ire_df = pd.DataFrame(dur_ire)

# Time to create the chart!

x = year
y1a = dur_sco_df
y1b = dur_wal_df
y1c = dur_ire_df
y2 = dur_eng_df

fig = plt.figure()
fig, ax1 = plt.subplots(figsize=[20,10])

ax2 = ax1.twinx() # share the x-axis

ax1.plot(x,y1a, color="black", label="Scotland", linewidth=2, marker="o")
ax1.plot(x,y1b, color="green", label="Wales", linewidth=2, marker="o")
ax1.plot(x,y1c, color="orange", label="N. Ireland", linewidth=2, marker="o")
ax1.grid(color="white")

ax2.plot(x,y2, label="England", color="blue", linewidth=3, marker="o")
ax2.grid(False)
plt.style.use('seaborn')
ax1.legend(fontsize=14)
ax2.legend(fontsize=14)

ax1.set_ylabel("Student Population Numbers (Scotland, Wales, and N. Ireland)", fontsize=16)
ax1.tick_params(labelsize=14)
ax2.set_ylabel("Student Population Numbers (England)", fontsize=16)
ax2.tick_params(labelsize=14)

ax1.set_xlabel("Year", fontsize=14)
plt.title("Undergraduate Student Numbers at Durham University between 2015 - 2019", fontsize=20, pad=20)
plt.plot()
plt.show()

# Whilst this is useful, it only shows student numbers; how about we seperate students by gender?

# import gender data for Durham University
gender_data1819 = pd.read_csv("dt051-table-1 gender (20182019).csv", skiprows=17, nrows=169)
gender_data1718 = pd.read_csv("dt051-table-1 gender (20172018).csv", skiprows=17, nrows=169)
gender_data1617 = pd.read_csv("dt051-table-1 gender (20162017).csv", skiprows=17, nrows=169)
gender_data1516 = pd.read_csv("dt051-table-1 gender (20152016).csv", skiprows=17, nrows=169)
gender_data1415 = pd.read_csv("dt051-table-1 gender (20142015).csv", skiprows=17, nrows=169)

# using iloc to select a row of data for the 2018/2019 academic year
gender_data1415.iloc[0]

# From the row of data, select the number of female undergraduate students
print("Number of female undergraduates at Durham (2018-2019):", gender_data1415.iloc[0][2])

# Let's combine male and female undergraduate numbers, by academic year, into a single DataFrame

combined_data = pd.DataFrame(
    {
        'Year':['2015','2016','2017','2018','2019'],
        'Male':[
            gender_data1415.iloc[0][3],
            gender_data1516.iloc[0][3],
            gender_data1617.iloc[0][3],
            gender_data1718.iloc[0][3],
            gender_data1819.iloc[0][3]
        ],
        'Female':[
            gender_data1415.iloc[0][2],
            gender_data1516.iloc[0][2],
            gender_data1617.iloc[0][2],
            gender_data1718.iloc[0][2],
            gender_data1819.iloc[0][2]
        ]
    }
)

combined_data

# We can also present it through the year horizontally...

combined_data_year = pd.DataFrame(
    {
        'Gender': ['Female', 'Male'],
        '2015': [gender_data1415.iloc[0][2], gender_data1415.iloc[0][3]],
        '2016': [gender_data1516.iloc[0][2], gender_data1516.iloc[0][3]],
        '2017': [gender_data1617.iloc[0][2], gender_data1617.iloc[0][3]],
        '2018': [gender_data1718.iloc[0][2], gender_data1718.iloc[0][3]],
        '2019': [gender_data1819.iloc[0][2], gender_data1819.iloc[0][3]]
    }
)

combined_data_year

# There is an easier way to do this... well, sort of.

transpose_data = combined_data.transpose() # can also use: combined_data.T


# ... but there's a problem, our values are not values - they're strings...

print("Female (2015): ", combined_data.iloc[0][1], "( is of type ", type(combined_data.iloc[0][1]),")") 

# Lets convert these strings to integers using the following identifiers
# iloc[row][column], e.g. combined_data.iloc[1][5] = 8,775

# Lets first try and get just one column of data

print("Female numbers at Durham (2015-2019)")
for i in range(5):
    print(year[i], ": ",combined_data.iloc[i][2])


# Now lets convert this example column of data to integers
combined_data['Male'] = combined_data['Male'].str.replace(",","")
combined_data['Female'] = combined_data['Female'].str.replace(",","")

combined_data['Male'] = combined_data['Male'].astype(int)
combined_data['Female'] = combined_data['Female'].astype(int)


# Lets check the data type...
print("Female (2015): ", combined_data.iloc[0][1], "( is of type ", type(combined_data.iloc[0][1]),")") 

# Lets put male and female values into seperates data series

male = combined_data.loc[:,"Male"].values

female = combined_data.loc[:,"Female"].values

male_list = list(male)
female_list = list(female)


male_df = pd.DataFrame(male_list,columns=["male"])
female_df = pd.DataFrame(female_list,columns=["female"])

# Step 1: Set up the chat plot area

# fig is the chart container, i.e. the plot area
fig = plt.figure()

# assigning the plot area to contain subplots, and assigning the axis variable (ax_1) to hold multiple plots
fig, ax_1 = plt.subplots(figsize=[20,10], sharex=True)
ax_2 = ax_1.twinx()

# Step 2: set up the variables to plot the chart (first y-axis)

# Get the years of data held, e.g. 2015
y = year

# create a variable to hold the male student numbers (m)
m = pd.Series(male)

# create a variable to hold the female student numbers (f)
f = pd.Series(female)

# create variable to hold total numbers for each year

t = pd.Series(
    [
        (female[0] + male[0]),
        (female[1] + male[1]),
        (female[2] + male[2]),
        (female[3] + male[3]),
        (female[4] + male[4]),
    ]
)

# Step 3: plot the chart (first y-axis)

# Charting male numbers. NB: negative width moves the bar chart to the left, making space for female numbers.
ax_1.bar(y,m, color='navy', width=-0.25, align="edge", label="Male")

# Charting female numbers. NB: positive width moves bar chart to the right, making space for make numbers.
ax_1.bar(y,f, color="green", width=0.25, align="edge", label="Female")

ax_2.plot(y,t, color="orange", label="Total", linewidth=3, marker='D', markersize=7)

# Chart formatting...
ax_1.legend(fontsize=(14))
plt.style.use('tableau-colorblind10')
plt.title("Undergraduate students at Durham University by gender (2015-2019)", fontsize=(25), pad=(20))
ax_1.set_xlabel("Academic year", fontsize=(16))
ax_1.set_ylabel("Number of students", fontsize=((16)))
ax_2.set_ylabel("Total Number of Students", fontsize=(16))
plt.xticks(fontsize=(12))
plt.yticks(fontsize=(12))

ax_2.grid(False)
ax_2.legend(fontsize=(14))
