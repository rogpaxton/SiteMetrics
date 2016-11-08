import folium
from folium.element import IFrame
import pandas as pd
import numpy as np
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

def mapper(data):
#    df = pd.read_csv(data)

    #draft map an location pins
#    m = folium.Map()

#    for each in df.iterrows():
#        m.circle_marker(location = [each[1]['Lat'], each[1]['Lon']], popup=each[1]['City'])

#    m.create_map(path='map.html')

    m = folium.Map([43,-100], zoom_start=4)

    f = open('html_test.html','w')

    html="""
        <!DOCTYPE html>
        <html>
            <h1> Popup for site location</h1>
            <br>
            <div>
                <img id="RC51" src="plot44.0.png" alt="RVT" style="width:400px;height:200px;">
            </div>
        </html>
        """

#src="file:///Users/rogpaxton/Galvanize/SiteMetrics/RC51.jpg"
#                    <img id="RC51" src="RC51.jpg" alt="RVT" style="width:48px;height:49px;">

    f.write(html)
    f.close()

    iframe = folium.element.IFrame(html=html, width=800, height=400)
#    figure = folium.element.Figure(figure=plot44.0.png, width=800, height=400)
#    h = folium.element.Html(data=html, width='100%', height='100%')

    #render figure
    fig = folium.element.Figure(width='100%', height=None, ratio='60%', figsize=None)
    df = pd.read_csv('SiteMetrics_DatesFormatted.csv')
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
    event_type_id = {1: 'Invitation Sent', 2: 'Registration', 3: 'Access Site', 4: 'Referral', 5: 'Question', 6: 'Accessed Document', 7: 'Interested', 8: 'Not Interested'}
    events = [1, 2, 3, 4, 5, 6, 7, 8]
    for i in list(site_set):
#        figure = gridspec.GridSpec(2, 4)
        grid_col = 0
        grid_row = 0
        count =1
        for j in events:

            plt.subplot(2,4,count)
            df_site = df.loc[df['SiteId'] == i]
            df_event = df_site.loc[df['EventTypeId'] == j]
            df_sorted = df_event.sort_values(by='EventDateTime')
            df_sorted['EventDateTime'] = pd.to_datetime(df_sorted['EventDateTime'])
            df_sorted = df_sorted.set_index('EventDateTime')
            df_sorted['day'] = df_sorted.index.date
            counts =  df_sorted.groupby('day').size(); counts
            idx = pd.date_range(date_min, date_max)
            counts.index = pd.DatetimeIndex(counts.index)
            counts = counts.reindex(idx, fill_value = 0)
            counts.plot()
            if counts.max() > 10:
                count_max = counts.max()
            else:
                count_max = 10
            days = df_sorted['day'].tolist()
#            axes.set_ylim([-1, count_max + 1])
#            plt.xlabel('Date')
            plt.title(event_type_id[j])
            plt.locator_params(axis = 'y', nbins=4)
            fig.add_subplot(2, 4, count, margin=0.05)
            count += 1

        filenumber = i
        plt.savefig('plot%s.png' % filenumber)
        plt.gcf().clear()

    show = fig.render()
    print show

    iframe = folium.element.IFrame(show, width=800, height=400)

    popup = folium.Popup(iframe, max_width=2650)

    folium.Marker([30,-100], popup=popup).add_to(m)

    m.create_map(path='map.html')

if __name__ == '__main__':
    map1 = mapper('data/example.csv')
