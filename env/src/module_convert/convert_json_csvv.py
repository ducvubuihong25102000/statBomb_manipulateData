import pandas as pd
from pathlib import Path
import time
import json


u = 3795506
start_time = time.time()

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
