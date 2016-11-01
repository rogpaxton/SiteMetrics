import pandas as pd

def data_conditioner(filename):
    df = pd.read_csv(filename)

    #Find min and max dates
    #Fill in full date range for each site
    #    

if __name__ == '__main__':
    data_conditioner('SiteMetrics_DatesFormatted.csv')
