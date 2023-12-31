
import requests
import pandas as pd
from utils import *

def fuksiarz_scraper(api_url):
    datetime_list=[]
    gospodarze_name_list=[]
    gospodarze_odds_list=[]
    remis_name_list=[]
    remis_odds_list=[]
    goscie_name_list=[]
    goscie_odds_list=[]


    response = requests.get(api_url,)
    if response.status_code == 200:
        response=response.json() 
    else:
        print(f"Error: {response.status_code}")
    response=response['data']
  
    for match in response:

        
        
        competition=match['category3Name']
        data2=match['eventGames']
      
        for game in data2:
            typ=game['gameName']
            if typ!='1X2':
                continue
            else:
                datetime_list.append(match['eventStart'])
                
                data2=game['outcomes']
                for data3 in data2:
                    if data3==data2[0]:
                        gospodarze_name=data3['outcomeName']
                        gospodarze_odds=data3['outcomeOdds']
                        gospodarze_name_list.append(gospodarze_name)
                        gospodarze_odds_list.append(gospodarze_odds)
                    if data3==data2[1]:
                        remis_name='Remis'
                        remis_odds=data3['outcomeOdds']
                        remis_name_list.append(remis_name)
                        remis_odds_list.append(remis_odds)
                    if data3==data2[2]:
                        goscie_name=data3['outcomeName']
                        goscie_odds=data3['outcomeOdds']    
                        goscie_name_list.append(goscie_name)
                        goscie_odds_list.append(goscie_odds)
        
    typ='1X2'  
    df=raw_to_df(gospodarze_name_list,gospodarze_odds_list,remis_name_list,remis_odds_list,goscie_name_list,goscie_odds_list,
              typ,datetime_list,competition
              ,'fuksiarz')

    return df
