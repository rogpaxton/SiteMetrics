import numpy as np
import pandas as pd
import io
from numpy import genfromtxt
import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')

def plots(filename):
    data = genfromtxt(filename, delimiter=',')

    df = pd.read_csv(filename)

    df_site44 = df.loc[df['SiteId'] == 44]

    df_invitations = df_site44.loc[df['EventTypeId'] == 1]
    df_invitations_sorted = df_invitations.sort('EventDateTime')
    df_invitations_sorted['EventDateTime'] = pd.to_datetime(df_invitations_sorted['EventDateTime'])
    df_invitations_sorted = df_invitations_sorted.set_index('EventDateTime')
    df_invitations_sorted['day'] = df_invitations_sorted.index.date
    counts =  df_invitations_sorted.groupby('day').size(); counts
    counts.plot()
    axes = plt.gca()
    axes.set_ylim([0,12])
    plt.ylabel('Invitations')
    plt.xlabel('Date')
    plt.title('Site 44')
    plt.xticks(rotation=30)
    #plt.setp(counts, rotation=45)
    plt.show()

    #df_registrations = df_site44.loc[df['EventTypeId'] == 2]
    #df_access = df_site44.loc[df['EventTypeId'] == 3]
    #df_referral = df_site44.loc[df['EventTypeId'] == 4]
    #df_question = df_site44.loc[df['EventTypeId'] == 5]
    #df_accessed = df_site44.loc[df['EventTypeId'] == 6]
    #df_interested = df_site44.loc[df['EventTypeId'] == 7]
    #df_not_interested = df_site44.loc[df['EventTypeId'] == 8]


#print df_invitations_sorted.head()

if __name__ == '__main__':
    plots('SiteMetrics_DatesFormatted.csv')
