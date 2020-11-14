#!/usr/bin/env python

import yaml

# Reading Yaml

with open('fruits.yaml') as file:
    fruits_dict = yaml.load(file, Loader=yaml.FullLoader)
    print(type(fruits_dict['last']))
    # print(fruits_dict)

# Note
# yaml.load(file, Loader=yaml.FullLoader) = yaml.full_load(file)

# with open('categories.yaml') as file:
#     documents = yaml.full_load(file)
#     for item, doc in documents.items():
#         print(item, ":", doc)

# Writting Yaml
# dict_file = [
#     {'sports' : ['soccer', 'football', 'basketball', 'cricket', 'hockey', 'table tennis']},
#     {'countries' : ['Pakistan', 'USA', 'India', 'China', 'Germany', 'France', 'Spain']}
# ]

# with open("storing.yaml", 'w') as file:
#     documents = yaml.dump(dict_file, file)
