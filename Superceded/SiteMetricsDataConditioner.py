import pandas as pd
import numpy as np
import io
from numpy import genfromtxt
from datetime import datetime
from dateutil import rrule, parser
from datetime import date, datetime, timedelta
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
matplotlib.style.use('ggplot')

def data_conditioner(filename):

    df = pd.read_csv(filename)

    #Find min and max dates
    date_list = [datetime.strptime(i, '%m/%d/%y') for i in df['EventDateTime']]
    date_min = min(date_list)
    date_max = max(date_list)

    #Fill in full date range
    full_date_list =[]
    curr = date_min
    while curr <= date_max:
        full_date_list.append(curr)
        curr += timedelta(days=1)

    #Create dictionary of sites and geocoordinates
    site_set = set(i for i in df['SiteId'] if i == i)
    site_lat = dict.fromkeys(site_set)
    for i in site_set:
        site_lat[i] = df.ix[df.SiteId[df.SiteId == i].index.tolist()[0], 'SiteAddressLatitude']
    site_long = dict.fromkeys(site_set)
    for i in site_set:
        site_long[i] = df.ix[df.SiteId[df.SiteId == i].index.tolist()[0], 'SiteAddressLongitude']

    #Tabulate occurences of each event, in each category, for each day for each site
    event_type_id = {'1': 'Invitation Sent', '2': 'Registration', '3': 'Access Site', '4': 'Referral', '5': 'Question', '6': 'Accessed Document', '7': 'Interested', '8': 'Not Interested'}
    events = [1, 2, 3, 4, 5, 6, 7, 8]
    for i in list(site_set):
#        figure = gridspec.GridSpec(2, 4)
        grid_col = 0
        grid_row = 0
        count =1
        for j in events:
#            for k in full_date_list:
#            count = 0
#                df_filtered_site = df[df['SiteId'] == i]
#                df_filtered_event = df_filtered_site[df['EventTypeId'] = j]
#                df_filtered_date = df_filtered_date[df['EventDateTime'] = k]
#                count = len(df.index)
            df_site = df.loc[df['SiteId'] == i]
            df_event = df_site.loc[df['EventTypeId'] == j]
            df_sorted = df_event.sort('EventDateTime')
            df_sorted['EventDateTime'] = pd.to_datetime(df_sorted['EventDateTime'])
            df_sorted = df_sorted.set_index('EventDateTime')
            df_sorted['day'] = df_sorted.index.date
            counts =  df_sorted.groupby('day').size(); counts
            idx = pd.date_range(date_min, date_max)
            counts.index = pd.DatetimeIndex(counts.index)
            counts = counts.reindex(idx, fill_value = 0)
            counts.plot()
            axes = plt.gca()
            axes.set_ylim([0,12])
#            plt.ylabel(event_type_id(j))
            plt.xlabel('Date')
            plt.title(j)
            plt.xticks(rotation=30)
#            plt.show()
#            plt.subplot(gs[grid_col, grid_row])

#            plot = plt.subplot2grid((4, 2), [grid_row, grid_col])
#            if count % 2 == 0 or count == 0:
#                grid_col += 1
#            else:
#                grid_row += 1
#            count += 1
            plt.subplot(2,4,count)
            count += 1
        filenumber = i
        plt.savefig('plot%s.png' % filenumber)
        plt.gcf().clear()
#        plt.show()
#        Image.open('testplot.png').save('plot.jpg', 'JPEG')



if __name__ == '__main__':
    data_conditioner('SiteMetrics_DatesFormatted.csv')
