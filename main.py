import pandas as pd
import matplotlib.pyplot as plt

sheet_id = '1tjUxedFcVGH40YegcuhqhDsJFoLzl_XaNJNfA6Kb5-U'

df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv", nrows= 1000)

xs = df.plot(x = 'time_tag', y = 'xs')
plt.savefig('xs.png')

xl = df.plot(x= 'time_tag', y = 'xl')
plt.savefig('xl.png')

time = df['time_tag']
##Max Value
max_xs = df['xs'].max()
print(max_xs)

time_txs = df.assign(time = max_xs)
print(time_txs)

##Min Value
min_xl = df['xl'].max()
print(min_xl)

time_txl = df.assign(time = min_xl)
print(time_txl)








































