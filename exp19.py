import pandas as pd

# Sample dataset
data = {
    'City':['Chennai','Delhi','Mumbai','Kolkata'],
    'Day1':[32,28,30,29],
    'Day2':[33,27,31,30],
    'Day3':[31,29,32,28],
    'Day4':[34,30,30,27],
    'Day5':[32,31,29,29]
}

df = pd.DataFrame(data)

# Mean temperature
df['MeanTemp'] = df.iloc[:,1:].mean(axis=1)

# Standard deviation
df['StdTemp'] = df.iloc[:,1:-1].std(axis=1)

# Temperature range
df['Range'] = df.iloc[:,1:-2].max(axis=1) - df.iloc[:,1:-2].min(axis=1)

print(df)

# City with highest range
print("City with highest temperature range:", df.loc[df['Range'].idxmax(),'City'])

# Most consistent city
print("City with most consistent temperature:", df.loc[df['StdTemp'].idxmin(),'City'])