import pandas as pd
import json


def read_json(filename: str) -> dict:
  
    try:
        with open(filename, "r") as f:
            data = json.loads(f.read())
    except:
        raise Exception(f"Reading {filename} file encountered an error")
  
    return data
  
  
def normalize_json(data: dict) -> dict:
  
    new_data = dict()
    for key, value in data.items():
        if not isinstance(value, dict):
            new_data[key] = value
        else:
            for k, v in value.items():
                new_data[key + "_" + k] = v
      
    return new_data

def create_dataframe(data: list) -> pd.DataFrame:
  
    # Declare an empty dataframe to append records
    dataframe = pd.DataFrame()
  
    # Looping through each record
    for d in data:
          
        # Normalize the column levels
        record = pd.json_normalize(d)
          
        # Append it to the dataframe 
        dataframe = dataframe.append(record, ignore_index=True)
  
    return dataframe


data = read_json(filename=fr'D:\soccer_data\open-data\data\lineups\\7298.json')
dataframe = create_dataframe(data)
dataframe.to_csv("details.csv", index=False)