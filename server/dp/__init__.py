from pprint import pprint

import pandas as pd
import numpy as np
import json

recipe_file_path = './server/dp/datasets/epi_r.csv'
recipe_json_file_path = "./server/dp/datasets/full_format_recipes.json"


# Since the dataset is large, reading data in with generator might save memory utilization.
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


# This sort function might not be necessary since it can be achieved by directly calling df.sort_values().
def find_matching_recipes(keywords, result_count=15):
    """
    Given a list of keywords find recipes that match the keywords and return all the matched recipes
    and their matching percentage.
    Args:
        keywords: A 'list' containing all the ingredients and other keywords in user's inventory and
         other keywords such as allergy info.
    Returns:
        partial_result_json: A list of dictionary containing result json objects.
        partial_result_df: A Pandas DataFrame containing:
            Title: The name of the recipe with at least one keyword found in it.
            Match Found: The number of keywords found in the recipe given a querying list of keywords.
            Match Percentage: The percentage of matching, defined as match found divided by item count in each recipe.
            Match Items: A list of matched keywords found in each recipe.
    """
    # Read recipes information from epi.csv
    recipes_df = pd.read_csv(recipe_file_path)

    result_list = []
    for index, recipe in recipes_df.iterrows():
        # The recipe title to be used as a key in found_count for storing recipe result name.
        recipe_name = recipe["title"]

        is_one_hot_true = map(lambda x: x == np.float(1), recipe)

        # Recipe with only one-hot encoding column.
        one_hot_recipe = recipe[is_one_hot_true]

        found = 0
        found_keywords = []
        # Loop and count matching keywords in a recipe.
        for keyword in keywords:
            if keyword in one_hot_recipe:
                found += 1
                found_keywords.append(keyword)
        if found != 0:
            # matching_percentage = found_count[recipe_name] / one_hot_recipe.count() * 100
            matching_percentage = found / one_hot_recipe.count() * 100.00

            # Add results to DataFrame.
            result_list.append({'Title': recipe_name,
                                'Match Found': found,
                                'Match Percentage': matching_percentage,
                                'Match Items': found_keywords})

    # Convert list of dicts to DataFrame.
    result_df = pd.DataFrame(result_list)

    # Specify DataFrame desired column order.
    desired_order = ['Title', 'Match Found', 'Match Percentage', 'Match Items']
    result_df = result_df[desired_order]

    # Sort the result DataFrame based on the number of item found in descending order.
    result_df = result_df.sort_values('Match Found', ascending=False)

    # Dataframe containing only the number of result desired.
    partial_result_df = result_df[0:result_count]

    # Get the index number of the matched recipe from the partial result.
    result_indexes = partial_result_df.index.values.tolist()

    # Read recipe.json file
    recipes_json_df = pd.read_json(recipe_json_file_path)

    # Get the partial recipe.json, all row in the indexes, and all col in the dataframe.
    partial_recipes_json_df = recipes_json_df.iloc[result_indexes, :]

    # Convert Dataframe to JSON
    partial_result_json = partial_recipes_json_df.to_json(orient='index')
    partial_result_json = json.JSONDecoder().decode(partial_result_json)

    return partial_result_json, partial_result_df


# Test for find_matching_recipes
# keywords_from_inventory = ["lettuce", "chicken", "apple", "tomato", "turkey", "bean"]
# result, result_details = find_matching_recipes(keywords_from_inventory)
# 
# print(type(result))
# pprint(result)
# 
# print("Result details: " + str(type(result_details)))
# print(result_details)




