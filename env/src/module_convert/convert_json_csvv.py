import pandas as pd
from pathlib import Path
import time
import json


new_dict = {}

temp = {
    "details": 
    {
        "id": "STU001",
        "name": "Amit Pathak",
        "age": 24,
        "results": {
            "school": 85,
            "high_school": 75,
            "graduation": 70
        },
        "education": {
            "graduation": {
                "major": "Computers",
                "minor": "Sociology"
            }
        }
    }
}


def normalize_json(data: dict|list[dict] , new_dict: dict) -> dict:
    """"Function to normalize many-nested dictionary or array to non-nested dictionary (recursive)"""
    if isinstance(data,dict):
        for key,value in data.items():
            if not isinstance(value,dict):
                new_dict[key]=value
            else:
                for key2,value2 in value.items():
                    if not isinstance(value2,dict):
                        new_dict[key +'_'+key2]=value2
                    else:
                        normalize_json(value2,new_dict) 
    else:
        for item in range(0,len(value)+1):
            normalize_json(value[item],new_dict)   
    return new_dict


    
u = 3795506
start_time = time.time()



# a = dict(pd.read_json(r'D:\code\Anlyze_github\env\src\data\7430.json'))
data = normalize_json(temp,new_dict)
print(data)



# for i in range(7430,7300 ):

#     path = Path(fr'D:\soccer_data\open-data\data\lineups\\{i}.json')
        
#     if(path.is_file()):
#         data = dict(pd.read_json(fr'D:\soccer_data\open-data\data\lineups\\{i}.json'))
#         data_normalize = normalize_json(data)
#         print(data_normalize)
#         df = pd.DataFrame(data_normalize)
#         df.to_csv(fr'D:\soccer_data\data_convert\\{i}_converted.csv',index=None)
#         print(i)

print('Converting is done')
print('time spend %s seconds'%(time.time()-start_time))
