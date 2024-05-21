import pandas as pd

csv_file_path = 'crashes-raw.csv'
df = pd.read_csv(csv_file_path)

crew_numeric = pd.to_numeric(df['Crew on board'], errors='coerce')
pax_numeric = pd.to_numeric(df['Pax on board'], errors='coerce')

df['Total on board'] = crew_numeric + pax_numeric
df['Total on board'] = df['Total on board'].fillna('NA')
df['Season'] = None

columns_to_keep = [
    'Date', 'Country', 'Region', 'Aircraft', 'Operator', 'Registration', 'Flight phase', 'Flight type',
    'Crash site', 'Schedule', 'Total on board', 'Survivors', 'Crew on board', 'Crew fatalities', 'Pax on board',
    'PAX fatalities', 'Other fatalities', 'Total fatalities', 'Circumstances', 'Crash cause', 'Crash location', 'Season'
]

df = df[columns_to_keep]

# Convert 'Date' to datetime and extract the month
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')


# Define the season function
def get_season(month):
    if month in (12, 1, 2):
        return 'Winter'
    elif month in (3, 4, 5):
        return 'Spring'
    elif month in (6, 7, 8):
        return 'Summer'
    elif month in (9, 10, 11):
        return 'Autumn'


# Apply the function to determine the season
df['Season'] = df['Date'].dt.month.apply(get_season)

# Convert other columns to numeric types
int_columns = [
    'Total on board', 'Crew on board', 'Crew fatalities', 'Pax on board',
    'PAX fatalities', 'Other fatalities'
]
for column in int_columns:
    df[column] = pd.to_numeric(df[column], errors='coerce').astype('Int64')

new_csv_file_path = 'crashes-processed.csv'
df.to_csv(new_csv_file_path, index=False)

print(f"New CSV with selected columns saved to: {new_csv_file_path}")