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
from matplotlib.dates import MonthLocator, WeekdayLocator, DateFormatter

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
    event_type_id = {1: 'Metric 1', 2: 'Metric 2', 3: 'Metric 3', 4: 'Metric 4', 5: 'Metric 5', 6: 'Metric 6', 7: 'Metric 7', 8: 'Metric 8'}
    events = [1, 2, 3, 4, 5, 6, 7, 8]

    #calculate means by event type
    faux_event_means = {1:6, 2:2, 3:3, 4:7, 5:0, 6:4, 7:5, 8:6}

    #create plots of interest
    for i in list(site_set):
        grid_col = 0
        grid_row = 0
        count =1
        site_score = 0
        for j in events:
            plt.subplot(2,4,count)
            plt.tight_layout()
            df_site = df.loc[df['SiteId'] == i]
            df_event = df_site.loc[df['EventTypeId'] == j]
            df_sorted = df_event.sort_values(by='EventDateTime')
            df_sorted['EventDateTime'] = pd.to_datetime(df_sorted['EventDateTime'])
            df_sorted = df_sorted.set_index('EventDateTime')
            df_sorted['day'] = df_sorted.index.date

            #tabulate counts by event and day
            counts =  df_sorted.groupby('day').size(); counts
            idx = pd.date_range(date_min, date_max)
            counts.index = pd.DatetimeIndex(counts.index)
            counts = counts.reindex(idx, fill_value = 0)
            plt.tick_params(axis='both', which='major', labelsize=8, labelright='off', length = 0)
            plt.tick_params(axis='both', which='minor', labelsize=8, labelright='off', length = 0)

            #render the plot
            counts.plot()
            plt.axhline(y=faux_event_means[j], xmin=0.0, xmax=1.0, linewidth=1, color = 'k')
            if counts.max() >= 10:
                count_max = counts.max()
            else:
                count_max = 10

            #refine plot axes
            days = df_sorted['day'].tolist()
            axes = plt.gca()
            plt.setp(axes.get_xminorticklabels(), visible=False)
            axes.set_ylim([-1, count_max + 1])

            color = 'r'
            plt.title(event_type_id[j], size = 10)
            plt.locator_params(axis = 'y', nbins=4)
            count += 1

            #calculate combined site score
            if j == 1 or 3 or 6 or 7 or 8:
                site_score += sum(counts)
            elif j == 2 or 5:
                site_score += 2*sum(counts)
            elif j == 4:
                site_score += 3*sum(counts)

        #render plot title
        st = plt.suptitle("Site Score: %s" % site_score, fontsize="x-large")
        st.set_y(0.95)
        plt.subplots_adjust(top=0.85)
        filenumber = i
        plt.savefig('plot%s.png' % filenumber)
        plt.gcf().clear()



if __name__ == '__main__':
    data_conditioner('SiteMetrics_DatesFormatted.csv')
