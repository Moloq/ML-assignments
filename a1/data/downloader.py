import requests
import numpy as np
def getFIPSforLocation(latitude, longitude):
    try:
        FTC_API_format = "http://data.fcc.gov/api/block/find?format=json&latitude={latitude}&longitude={longitude}"
        return requests.get(FTC_API_format.format(longitude=longitude, latitude=latitude)).json()['Block']['FIPS'][:12]
    except:
        return np.nan

buildings_df.dropna(subset=['latitude'], inplace=True)
buildings_df.dropna(subset=['longitude'], inplace=True)
buildings_df['FIPS']=buildings_df.apply(lambda row: getFIPSforLocation(row['latitude'],row['longitude']), axis=1)
buildings_df.to_json("data/sanitation_df_with_fips.json")

sanitation_df.dropna(subset=['latitude'], inplace=True)
sanitation_df.dropna(subset=['longitude'], inplace=True)
sanitation_df['FIPS']=sanitation_df.apply(lambda row: getFIPSforLocation(row['latitude'],row['longitude']), axis=1)
sanitation_df.to_json("data/sanitation_df_with_fips.json")