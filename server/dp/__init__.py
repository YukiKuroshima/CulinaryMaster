import pandas as pd
import json
# import numpy as np


def data_processing():

    recipe_csv = pd.read_csv('./server/dp/datasets/epi_r.csv')

    with open('./server/dp/datasets/full_format_recipes.json') as json_data:
        recipe_json = json.load(json_data)

    # Keep first 10 data
    temp_data = recipe_json[0:10]

    # Get only ingredient col
    temp_data = list(map(lambda x: x['ingredients'], temp_data))

    # print if "chicken" is in the ingredient list
    for x in temp_data:
        print(x)
        for y in x:
            if "chicken" in y:
                print(y)

    return temp_data
