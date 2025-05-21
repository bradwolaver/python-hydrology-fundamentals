###########################################################
# Session 5, Step 2. Preparing DataFrame df2 for Session 5
###########################################################

# Prepared by Brad Wolaver
# New Mexico Office of the State Engineer, Hydrology Bureau, Santa Fe, NM
# November 14, 2024
# 
# See Session 4 for details of downloading USGS stream gage data, 
# preparing data, and saving data as DataFrame df2.
# 
# This script starts at Session 4, Step 1.
# Even though libaries have already been imported in Jupyter Notebook,
# you need to import the libraries the script uses in the script.


##################################################
# Session 4, Step 1: Importing Necessary Libraries
##################################################

# Data Download
import hydrofunctions as hf  # hydrofunctions is used to download USGS gage data from the web

# Data Manipulation
import pandas as pd  # pandas is used for data manipulation and analysis
from datetime import date, timedelta  # datetime is used to work with dates

# Plotting
import matplotlib.pyplot as plt  # matplotlib is a library for plotting data
import matplotlib.dates as mdates  # mdates is a module for handling date and time data in plots


################################################
# Session 4, Step 2: Setting Up Gage Information
################################################
 
# USGS gage IDs we are interested in:
# USGS:08279500: RIO GRANDE AT EMBUDO, NM
#    Discharge, cubic feet per second from 1889-01-01 to 2024-10-21
# USGS:08313000: RIO GRANDE AT OTOWI BRIDGE, NM
#    Discharge, cubic feet per second from 1895-02-01 to 2024-10-21
            
sites = ['08279500', '08313000']  # These are unique IDs for two USGS stream gages (Embudo and Otowi)

start_date = '1889-01-01'  # The first day of data for the Embudo gage (see: https://waterdata.usgs.gov/nwis/inventory?site_no=08279500&agency_cd=USGS)

today = date.today()  # Get today's date dynamically and convert to yesterday's data to deal with USGS reporting lag (so you retrieve the latest data)
yesterday = today - timedelta(days=1)  # Calculate yesterday's date
end_date = yesterday

print(f"Start date is set to: {start_date}")  
print(f"End date is set to: {end_date}")

pcode = '00060'  # USGS Parameter Code 00060 is discharge in cubic feet per second

data = hf.NWIS(sites, 'dv', start_date, end_date, parameterCd=pcode)  # NWIS can deliver data as daily mean values (‘dv’) or as instantaneous values (‘iv’)

# Check if the data download was successful
print(f"\nData download status: {data.ok}\n'True' indicates download successful\n")   # Another use of f-string

# Display a summary of the data retrieved for each gage, including gage ID, gage name, parameter (discharge), and date range
print(data)

# Convert the downloaded USGS data into a pandas DataFrame and display it
df = data.df()  # hydrofunctions includes the function .df() which converts hydrofunctions object to pandas DataFrame.  The DataFrame here is called df. 


##################################################
# Session 4, Step 3: Rename DataFrame Column Names
##################################################

# Assuming 'df' is your original DataFrame
df2 = df.copy()

# Renaming the columns in the new DataFrame
df2 = df2.rename(columns={
    'USGS:08279500:00060:00003': 'Embudo_cfs',
    'USGS:08279500:00060:00003_qualifiers': 'Embudo_qual',
    'USGS:08313000:00060:00003': 'Otowi_cfs',
    'USGS:08313000:00060:00003_qualifiers': 'Otowi_qual'
})

print(f"\nThe head of the DataFrame is:\n")
print(df2.head())

print(f"\nThe tail of the DataFrame is:\n")
print(df2.tail())


######################################################
## Session 4, Step 4. Create Hydrographs of Both Gages
######################################################

print(f"\nHere is a plot the DataFrame:\n")

# Create subplots
fig, ax = plt.subplots(2, 1, figsize=(12, 5))

# Top subplot: Embudo Streamflow
ax[0].plot(df2.index, df2['Embudo_cfs'], label='Embudo Streamflow (cfs)', color='blue')
ax[0].set_title('Rio Grande at Embudo, NM - 08279500')
ax[0].set_xlabel('Date')

# Bottom subplot: Otowi Streamflow
ax[1].plot(df2.index, df2['Otowi_cfs'], label='Otowi Streamflow (cfs)', color='blue')
ax[1].set_title('Rio Grande at Otowi, NM - 08313000')
ax[1].set_xlabel('Date')

# Common y-axis label
fig.text(-0.02, 0.5, 'Mean Daily Streamflow (cfs)', va='center', rotation='vertical')

# Adjust layout and display the plot
plt.tight_layout()
