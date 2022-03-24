from itertools import count
import pandas as pd
import json

from zmq import NULL

def list_normalize (nest_list: list) -> list:
    """Final method to convert json list
        [
            {},{},{},.....,{}
        ]    
    """
    normalized_list = []
    for i in range(0,len(nest_list)):
        list = dict_normalize(nest_list[i])
        for k in range(0,len(list)):
            normalized_list.append(list[k])
    return normalized_list



empty_count = []



def count_row(nest_dict: dict|list, count: list) -> list:
    """When value of dictionary is a list with n item, if we convert it to csv or dataframe ( tabualar data), 
    it will have n rows to describe data
    This method use to calculate how many rows will be in table after converting data"""
    if isinstance(nest_dict,dict):
        for key,value in nest_dict.items():
            if isinstance(value,dict):
                count_row(value,empty_count)
            elif isinstance(value,list):
                count.append(len(value))
                for i in range(0,len(value)):
                    if isinstance(value[i],dict) or isinstance(value[i],list):
                        count_row(value[i],empty_count)
    else:
        count.append(len(nest_dict))
        for k in range(0,len(nest_dict)):
            if isinstance(nest_dict[k],dict) or isinstance(nest_dict[i],list):
                count_row(nest_dict[k],empty_count)                
    return count

def assumpt_row(count_list: list)->int:
    empty_list = []
    result = 1
    for i in range(0,len(count_list)):
        if(count_list[i]!= 0 and count_list[i]!=1):
            result = result * empty_list[i]
    return result

def dict_normalize(nest_dict: dict) -> list:
    normalized_list = []
    temp_dict = {}
    count_list_item_Array = []
    for key,value in nest_dict.items():
        print("temp")
    return normalized_list



temp_data = [{
  "team_id" : 759,
  "team_name" : "Washington Spirit",
  "lineup" : [ {
    "player_id" : 4940,
    "player_name" : "Andi Sullivan",
    "player_nickname" : NULL,
    "jersey_number" : 6,
    "country" : {
      "id" : 241,
      "name" : "United States of America"
    },
    "cards" : [ ],
    "positions" : [ {
      "position_id" : 10,
      "position" : "Center Defensive Midfield",
      "from" : "00:00",
      "to" : NULL,
      "from_period" : 1,
      "to_period" : NULL,
      "start_reason" : "Starting XI",
      "end_reason" : "Final Whistle"
    },{
      "position_id" : 10,
      "position" : "Center Defensive Midfield",
      "from" : "00:00",
      "to" : NULL,
      "from_period" : 1,
      "to_period" : NULL,
      "start_reason" : "Starting XI",
      "end_reason" : "Final Whistle"
    },{
      "position_id" : 10,
      "position" : "Center Defensive Midfield",
      "from" : "00:00",
      "to" : NULL,
      "from_period" : 1,
      "to_period" : NULL,
      "start_reason" : "Starting XI",
      "end_reason" : "Final Whistle"
    } ]
  }, {
    "player_id" : 4941,
    "player_name" : "Taylor Smith",
    "player_nickname" : NULL,
    "jersey_number" : 7,
    "country" : {
      "id" : 241,
      "name" : "United States of America"
    },
    "cards" : [ ],
    "positions" : [ {
      "position_id" : 2,
      "position" : "Right Back",
      "from" : "00:00",
      "to" : NULL,
      "from_period" : 1,
      "to_period" : NULL,
      "start_reason" : "Starting XI",
      "end_reason" : "Final Whistle"
    } ]
  }, {
    "player_id" : 4943,
    "player_name" : "Estelle Johnson",
    "player_nickname" : NULL,
    "jersey_number" : 24,
    "country" : {
      "id" : 39,
      "name" : "Cameroon"
    },
    "cards" : [ {
      "time" : "83:15",
      "card_type" : "Yellow Card",
      "reason" : "Foul Committed",
      "period" : 2
    } ],
    "positions" : [ {
      "position_id" : 5,
      "position" : "Left Center Back",
      "from" : "00:00",
      "to" : NULL,
      "from_period" : 1,
      "to_period" : NULL,
      "start_reason" : "Starting XI",
      "end_reason" : "Final Whistle"
    } ]
  }, {
    "player_id" : 4945,
    "player_name" : "Havana Solaun",
    "player_nickname" : NULL,
    "jersey_number" : 9,
    "country" : {
      "id" : 113,
      "name" : "Jamaica"
    },
    "cards" : [ ],
    "positions" : [ {
      "position_id" : 13,
      "position" : "Right Center Midfield",
      "from" : "53:51",
      "to" : NULL,
      "from_period" : 2,
      "to_period" : NULL,
      "start_reason" : "Substitution - On (Tactical)",
      "end_reason" : "Final Whistle"
    } ]
  }, {
    "player_id" : 4946,
    "player_name" : "Joanna Lohman",
    "player_nickname" : NULL,
    "jersey_number" : 15,
    "country" : {
      "id" : 241,
      "name" : "United States of America"
    },
    "cards" : [ ],
    "positions" : [ {
      "position_id" : 13,
      "position" : "Right Center Midfield",
      "from" : "00:00",
      "to" : "53:51",
      "from_period" : 1,
      "to_period" : 2,
      "start_reason" : "Starting XI",
      "end_reason" : "Substitution - Off (Tactical)"
    } ]
  }, {
    "player_id" : 4950,
    "player_name" : "Whitney Church",
    "player_nickname" : NULL,
    "jersey_number" : 5,
    "country" : {
      "id" : 241,
      "name" : "United States of America"
    },
    "cards" : [ ],
    "positions" : [ {
      "position_id" : 3,
      "position" : "Right Center Back",
      "from" : "00:00",
      "to" : NULL,
      "from_period" : 1,
      "to_period" : NULL,
      "start_reason" : "Starting XI",
      "end_reason" : "Final Whistle"
    } ]
  }, {
    "player_id" : 4956,
    "player_name" : "Mallory Eubanks",
    "player_nickname" : NULL,
    "jersey_number" : 22,
    "country" : {
      "id" : 241,
      "name" : "United States of America"
    },
    "cards" : [ ],
    "positions" : [ {
      "position_id" : 21,
      "position" : "Left Wing",
      "from" : "00:00",
      "to" : "66:30",
      "from_period" : 1,
      "to_period" : 2,
      "start_reason" : "Starting XI",
      "end_reason" : "Substitution - Off (Tactical)"
    } ]
  }, {
    "player_id" : 4962,
    "player_name" : "Caprice Dydasco",
    "player_nickname" : NULL,
    "jersey_number" : 3,
    "country" : {
      "id" : 241,
      "name" : "United States of America"
    },
    "cards" : [ ],
    "positions" : [ {
      "position_id" : 6,
      "position" : "Left Back",
      "from" : "00:00",
      "to" : NULL,
      "from_period" : 1,
      "to_period" : NULL,
      "start_reason" : "Starting XI",
      "end_reason" : "Final Whistle"
    } ]
  }, {
    "player_id" : 4964,
    "player_name" : "Ashley Hatch",
    "player_nickname" : NULL,
    "jersey_number" : 33,
    "country" : {
      "id" : 241,
      "name" : "United States of America"
    },
    "cards" : [ ],
    "positions" : [ {
      "position_id" : 23,
      "position" : "Center Forward",
      "from" : "00:00",
      "to" : NULL,
      "from_period" : 1,
      "to_period" : NULL,
      "start_reason" : "Starting XI",
      "end_reason" : "Final Whistle"
    } ]
  }, {
    "player_id" : 5022,
    "player_name" : "Francisca Ordega",
    "player_nickname" : NULL,
    "jersey_number" : 14,
    "country" : {
      "id" : 166,
      "name" : "Nigeria"
    },
    "cards" : [ ],
    "positions" : [ {
      "position_id" : 17,
      "position" : "Right Wing",
      "from" : "00:00",
      "to" : NULL,
      "from_period" : 1,
      "to_period" : NULL,
      "start_reason" : "Starting XI",
      "end_reason" : "Final Whistle"
    } ]
  }, {
    "player_id" : 5023,
    "player_name" : "Mallory Pugh",
    "player_nickname" : NULL,
    "jersey_number" : 11,
    "country" : {
      "id" : 241,
      "name" : "United States of America"
    },
    "cards" : [ ],
    "positions" : [ {
      "position_id" : 15,
      "position" : "Left Center Midfield",
      "from" : "00:00",
      "to" : "74:40",
      "from_period" : 1,
      "to_period" : 2,
      "start_reason" : "Starting XI",
      "end_reason" : "Substitution - Off (Tactical)"
    } ]
  }, {
    "player_id" : 5025,
    "player_name" : "Aubrey Bledsoe",
    "player_nickname" : NULL,
    "jersey_number" : 1,
    "country" : {
      "id" : 241,
      "name" : "United States of America"
    },
    "cards" : [ ],
    "positions" : [ {
      "position_id" : 1,
      "position" : "Goalkeeper",
      "from" : "00:00",
      "to" : NULL,
      "from_period" : 1,
      "to_period" : NULL,
      "start_reason" : "Starting XI",
      "end_reason" : "Final Whistle"
    } ]
  }, {
    "player_id" : 5026,
    "player_name" : "Meggie Dougherty Howard",
    "player_nickname" : NULL,
    "jersey_number" : 8,
    "country" : {
      "id" : 241,
      "name" : "United States of America"
    },
    "cards" : [ ],
    "positions" : [ {
      "position_id" : 21,
      "position" : "Left Wing",
      "from" : "66:30",
      "to" : NULL,
      "from_period" : 2,
      "to_period" : NULL,
      "start_reason" : "Substitution - On (Tactical)",
      "end_reason" : "Final Whistle"
    } ]
  }, {
    "player_id" : 5029,
    "player_name" : "Tori Huster",
    "player_nickname" : NULL,
    "jersey_number" : 23,
    "country" : {
      "id" : 241,
      "name" : "United States of America"
    },
    "cards" : [ ],
    "positions" : [ {
      "position_id" : 15,
      "position" : "Left Center Midfield",
      "from" : "74:40",
      "to" : NULL,
      "from_period" : 2,
      "to_period" : NULL,
      "start_reason" : "Substitution - On (Tactical)",
      "end_reason" : "Final Whistle"
    } ]
  } ]
}
]


a = count_row(temp_data,count=empty_count)
print(assumpt_row(a))
print(a)