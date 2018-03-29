import pandas as pd
import numpy as np
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


def read_large_file(file_object):
    """A generator function to lazily read a large file"""

    # Loop indefinitely until the end of the file
    while True:
        # Read a line from the file: data
        data = file_object.readline()

        # Break if it is the end of the file
        if not data:
            break

        # Yield the line of data
        yield data



recipe_file_path = "/Users/robingoh/Documents/161Project/CulinaryMaster/server/dp/epi.csv"

# Create a context manager to read and close file.
with open(recipe_file_path) as file:

    generator = read_large_file(file)
    labels = next(read_large_file(file))

    # Iterate over the generator from read_large_file
    for line in generator:
        row = line.split(',')


# Read recipes information from epi.csv
# Need help fixing the path
recipes_df = pd.read_csv("/Users/robingoh/Documents/161Project/CulinaryMaster/server/dp/epi.csv")

def get_sorted_popular_property(recipe_data):
    """Get most popular property
    Args:
        recipe_data: A DataFrame containing recipes raw information.
    Returns:
        label_count: A 'list' of sorted property found in the DataFrame in descending order.
    """
    labels = list(recipe_data)

    label_count = pd.DataFrame()

    for label in labels:
        column = recipe_data[label]
        column_sum = column.sum()

        # Add column sum to label_count only if the property is one-hot encoding
        if type(column_sum) == np.float64:
            if column_sum <= recipe_data.shape[0]:
                label_count[label] = [column_sum]

    label_count = label_count.transpose()
    label_count.columns = ['property']
    label_count = label_count.sort_values('property', ascending=False)

    return label_count
# Test for get_sorted popular_property
# print(get_sorted_popular_property(recipes_df))








def find_matching_recipes(keywords, recipes_data):
    """
    Given a list of keywords find recipes that match the ingredients and return all the recipes
    and their matching percentage.
    Args:
        keywords: A 'list' containing all the ingredients in user's inventory and other keywords such as allergy info.
    Returns:
        (matched_recipes, match_percentage): A tuple containing two lists.
            matched_recipes: A 'list' containing the name of recipes with at least one ingredient match.
            match_percentage: A 'list' with the matching percentage for each recipe
                              with regards to the inventorial ingredients.
    """


recipe_json_file_path = "/Users/robingoh/Documents/161Project/CulinaryMaster/server/dp/full_format_recipes.json"
recipes_df_json_m = pd.read_json(recipe_json_file_path)

with open(recipe_json_file_path) as json_data:
    recipes_df_json = json.load(json_data)

# Keep first 10 data
temp_data = recipes_df_json[0:1]

# Get only ingredient col
temp_data = list(map(lambda x: x['ingredients'], temp_data))


keywords = ["chicken", "avocado"]
# print if "chicken" is in the ingredient list
# for x in temp_data:
#     print(x)
#     for y in x:
#         if "chicken" in y:
#             print(y)
# print()

values = sorted(recipes_df_json_m[0:1]['categories'])
for value in values:
    print(value)

is_one_hot_true = map(lambda x: x == np.float(1), recipes_df.iloc[0])
keywords_in_1st_recipe = (recipes_df.iloc[0][is_one_hot_true])
print(keywords_in_1st_recipe)
if keywords[0] in keywords_in_1st_recipe:
    print("found")
else:
    print("none"









"""
Sort recipes based on criteria such as rating, calories, protein, fat, sodium etc.
Args:
    presorted_recipes: A list of recipes to be sorted.
    criteria: The desired criteria to sort the recipes such as rating, calories, protein, fat, sodium etc.
    order: A 'boolean' value of the order of the sort, ascending: True, descending: False.
"""









