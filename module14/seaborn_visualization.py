import seaborn asa sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('avgIQpercountry.csv')
print(df.info())

plt.figure(figsize=(10,6))
sns.histplot(df['Average IQ'])
plt.title('histogram of average IQ')
plt.xlabel('Average IQ')
plt.ylabel('frequency')
plt.tight_layout()
plt.show