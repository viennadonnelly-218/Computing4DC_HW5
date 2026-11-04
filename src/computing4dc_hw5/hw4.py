import datetime
import pandas as pd
from functools import reduce
import geopy.distance

##### Try to use map and reduce in the next 3 exercises
# 1)
# Create a function called "count_simba" that counts and returns
# the number of times that Simba appears in a list of
# strings. Example:
# Answer:

def count_simba(string_list):
    counts_per_strings = map(lambda s: s.lower().count("simba"), string_list)
    return reduce (lambda x,y: x + y, counts_per_strings, 0)


# 2) Create a function called "get_day_month_year" that takes
# a list of datetimes.date and returns a pandas dataframe
# with 3 columns (day, month, year) in which each of the rows
# is an element of the input list and has as value its day, month, and year.

# Answer:

def get_day_month_year(date_list):
    rows = list(map(lambda d: (d.day, d.month, d.year), date_list))
    return pd.DataFrame(rows, columns=["day", "month", "year"])


# 3)
# Create a function called "compute_distance" that takes
# a list of tuple pairs with latitude and longitude coordinates and
# returns a list with the distance between the two pairs
# example input: [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
# HINT: You can use geopy.distance in order to compute the distance
#

#Answer:

def compute_distance(coordinate_pairs):
    return list(map(lambda pair: geopy.distance.geodesic(pair[0], pair[1]).km, coordinate_pairs))


#################################################
# 4)
# Consider a list that each element can be an integer or
# a list that contains integers or more lists with integers
# example: [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1].
# create a recursive function called "sum_general_int_list"
# that takes as input this type of list
# and returns the sum of all the integers within the lists
# for instance for list_1=[[2], 3, [[1,2],5]]
# the result should be 13
#
def sum_general_int_list(lista):
    total = 0

    for elemento in lista:
        if isinstance(elemento, int):
            total = total + elemento
        elif isinstance(elemento, list):
            total = total + sum_general_int_list(elemento)
        else:
            raise TypeError(f"Elemento no válido:{elemento}")
    return total
