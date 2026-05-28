import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd

data = {
    'creater': ['carryMinati', 'Mrbeast', 'RoundToHell', 'Technical Gruji', "RoundToWorld"],
    'category': ['comedy', 'influencer', 'comedy', 'Tech', 'comedy'],
    'subscriber_M': [34, 50, 40, 30, 20],
    'Daily_views_lakh': [44, 55, 34, 66, 33]
}

df = pd.DataFrame(data)

# plt.figure(figsize=(9, 6))
# sns.barplot(x = 'creater', y = 'Daily_views_lakh', data = df, palette = 'viridis')

# plt.title('Creater vs Daily views (lakh)' , fontsize = 14)
# plt.xlabel('YouTube Creater', fontsize = 22)
# plt.ylabel('Daily Views (in lakh)', fontsize = 22)

# plt.show(

plt.figure(figsize = (7, 7))
plt.pie(df['subscriber_M'],   
        labels=df['creater'], 
        autopct='%1.1f%%', 
        startangle=140, 
        colors=sns.color_palette('pastel'))
plt.title('Subscriber Share Percentage' , fontsize = 14)
plt.show()
