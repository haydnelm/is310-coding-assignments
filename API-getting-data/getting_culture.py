import apikey
import os
import pandas as pd
from steam_web_api import Steam

# Enter your API keys here or in the terminal, I've removed mine for obvious reasons

import pyeuropeana.apis as apis
import pyeuropeana.utils as utils

user_details = steam.users.get_user_details("76561198371006443")
user_details_df = pd.DataFrame([user_details])

user_csv_file_path = r'\\wsl.localhost\Ubuntu\home\haydnelm\is310-coding-assignments\API-getting-data\steam_user_details.csv' # I've hardcoded my filepath, you'll have to change this if you want to use this code
user_details_df.to_csv(user_csv_file_path, index=False)
print(user_details_df)

result = apis.search(query="TheLasagna") # My steam profile ID is "TheLasagna"
dataframe = utils.search2df(result)

csv_file_path = r'\\wsl.localhost\Ubuntu\home\haydnelm\is310-coding-assignments\API-getting-data\europeana_search_results.csv' # Same as above
dataframe.to_csv(csv_file_path, index=False)
print(dataframe)