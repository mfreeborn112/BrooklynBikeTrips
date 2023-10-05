# Brooklyn Travel Time Analysis: Driving vs. Biking

## Introduction
This project seeks to analyze the travel time differences between driving and bicycling across various neighborhoods in Brooklyn. By understanding these differences, we aim to determine which mode of transportation is faster in different contexts.

## Datasets
- **Brooklyn Zip Codes & Neighborhoods.csv** - This dataset contains ZIP codes from Brooklyn along with their associated neighborhood names. The list was generated using OpenAI's Chat GPT, and it serves as the foundation for our travel time analysis.

- **Brooklyn_Bike_Drive_Trips.csv** - The final output dataset, containing travel times (both driving and biking) between various Brooklyn neighborhoods.

## How to Use

### Prerequisites:
1. Ensure you have Python and the required libraries (pandas and requests) installed.
2. Acquire a Google Maps API key.

### Steps:
1. Clone this repository.
2. Download the `Brooklyn Zip Codes & Neighborhoods.csv` file from this repository.
3. Replace the placeholder `[Your API Key]` in the script with your actual Google Maps API key.
4. Run the script.
5. After execution, you'll obtain the `Brooklyn_Bike_Drive.csv` file containing the travel time data.

## Analysis
The resulting dataset can be analyzed using your preferred data analysis tools or libraries to determine which mode of transportation, driving or bicycling, is faster for various neighborhood pairs in Brooklyn.

## Acknowledgements
Special thanks to OpenAI's Chat GPT for providing the initial ZIP code and neighborhood names data.
