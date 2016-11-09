import numpy as np
import pandas as pd
import io
from numpy import genfromtxt
import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')

df = pd.read_csv('ClinTrialLog_DatesFormatted.csv')
df['EventDateTime'] = pd.to_datetime(df['EventDateTime'])
events = (1, 2, 3, 4, 5, 6, 7, 8)
events_dict = {1: 'Invitation', 2: 'Registration', 3: 'Access Site', 4: 'Referral', 5: 'Question', 6: 'Accessed Document', 7: 'Interested', 8: 'Not Interested'}

sites = set(list(df['SiteId']))
sites = list({x for x in sites if x==x})
min_date = df['EventDateTime'].min()
max_date = df['EventDateTime'].max()
print min_date
print max_date

figures = []

for i in sites:
    df_site = df.loc[df['SiteId'] == i]
    for j in events:
#       will need to make date range consistent
#       y axis will need to adapt to data
        df_invitations = df_site.loc[df['EventTypeId'] == j]
        df_invitations_sorted = df_invitations.sort('EventDateTime')
        df_invitations_sorted['EventDateTime'] = pd.to_datetime(df_invitations_sorted['EventDateTime'])
        df_invitations_sorted = df_invitations_sorted.set_index('EventDateTime')
        df_invitations_sorted['day'] = df_invitations_sorted.index.date
        counts =  df_invitations_sorted.groupby('day').size(); counts
        print counts
#       if counts.empty == True:
#       counts = pd.DataFrame(0, index=np.arange(5, columns=2)
        counts.plot()
        axes = plt.gca()
        axes.set_ylim([0,12])
        plt.ylabel('Count')
        plt.xlabel('Date')
        plt.title(events_dict[j])
        plt.xticks(rotation=30)
        plt.show()

    #Four panel figure
#        f, axarr = plt.subplots(2, 4)
#        axarr[0, 0].plot(x, y)
#        axarr[0, 0].set_title('Axis [0,0]')
#        axarr[0, 1].scatter(x, y)
#        axarr[0, 1].set_title('Axis [0,1]')
#        axarr[1, 0].plot(x, y ** 2)
#        axarr[1, 0].set_title('Axis [1,0]')
#        axarr[1, 1].scatter(x, y ** 2)
#        axarr[1, 1].set_title('Axis [1,1]')

#df_registrations = df_site44.loc[df['EventTypeId'] == 2]
#df_access = df_site44.loc[df['EventTypeId'] == 3]
#df_referral = df_site44.loc[df['EventTypeId'] == 4]
#df_question = df_site44.loc[df['EventTypeId'] == 5]
#df_accessed = df_site44.loc[df['EventTypeId'] == 6]
#df_interested = df_site44.loc[df['EventTypeId'] == 7]
#df_not_interested = df_site44.loc[df['EventTypeId'] == 8]


#print df_invitations_sorted.head()

if __name__ == '__main__':
    pass
