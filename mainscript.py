import pandas as pd
import requests

# Load the CSV containing the Zip codes and neighborhood names for Brooklyn
df = pd.read_csv('Brooklyn Zip Codes & Neighborhoods.csv')

# Define the base URL for Google's Geocoding API to get latitudes and longitudes
base_url_geocode = "https://maps.googleapis.com/maps/api/geocode/json?"

# User should insert their personal API Key from Google Cloud Console here
api_key = "[Your API Key]"

# Add new columns for storing latitude and longitude values
df['Latitude'] = None
df['Longitude'] = None

# Function to retrieve latitude and longitude for each Zip code
for index, row in df.iterrows():
    url = f"{base_url_geocode}address={row['Zip Code']}&key={api_key}"
    response = requests.get(url).json()
    if response['status'] == 'OK':
        lat = response['results'][0]['geometry']['location']['lat']
        lng = response['results'][0]['geometry']['location']['lng']
        df.at[index, 'Latitude'] = lat
        df.at[index, 'Longitude'] = lng

# Define the base URL for Google's Directions API to calculate distances and durations
base_url_directions = "https://maps.googleapis.com/maps/api/directions/json?"

# List to store results for each combination of origin and destination zip codes
results = []

# Function to get directions (both driving and bicycling) between each combination of Zip codes
for index, origin in df.iterrows():
    for _, destination in df.iterrows():
        for mode in ['driving', 'bicycling']:
            url = (base_url_directions +
                   "origin={},{}&destination={},{}&mode={}&key={}"
                   .format(origin['Latitude'], origin['Longitude'], 
                           destination['Latitude'], destination['Longitude'], 
                           mode, api_key))
            response = requests.get(url).json()
            if response['status'] == 'OK':
                route = response['routes'][0]['legs'][0]
                result = {
                    'Origin ZIP': origin['Zip Code'],
                    'Origin Neighborhood': origin['Neighborhood'],
                    'Destination ZIP': destination['Zip Code'],
                    'Destination Neighborhood': destination['Neighborhood'],
                    'Mode': mode,
                    'Distance': route['distance']['text'],
                    'Duration': route['duration']['text']
                }
                results.append(result)

# Convert the results list into a DataFrame
results_df = pd.DataFrame(results)

# Filter out rows where the origin and destination zip codes are the same
results_df = results_df[results_df['Origin ZIP'] != results_df['Destination ZIP']]

# Remove 'mi' from Distance column and convert to float
results_df['Distance'] = results_df['Distance'].str.replace(' mi', '').astype(float)

# Function to convert duration strings (e.g., "1 hour 4 mins") into total minutes
def convert_duration_to_minutes(duration_str):
    parts = duration_str.split()
    if "hour" in duration_str:
        hours = int(parts[0])
        minutes = int(parts[2]) if "min" in duration_str else 0
        return 60 * hours + minutes
    else:
        return int(parts[0])

results_df['Duration'] = results_df['Duration'].apply(convert_duration_to_minutes)

# Rename the Distance and Duration columns to include units for clarity
results_df.rename(columns={'Distance': 'Distance (mi)', 'Duration': 'Duration (min)'}, inplace=True)

# Save the results to a new CSV file
results_df.to_csv('Brooklyn_Bike_Drive_Trips.csv', index=False)
