####### importing needed functions
import pandas as pd
import numpy as np

####### pulling in the df and tweaking

## pulling in
happy_and_COVID = pd.read_csv('happy_and_COVID.csv')
countries=list(happy_and_COVID['Country name'])
happy_and_COVID.set_index('Country name', inplace = True)

## make sub-df of points of interest
sub_happy_and_COVID = happy_and_COVID[['Regional indicator',
                                    '21_Ladder score',
                                    '20_Ladder score',
                                    'Ladder score_diff',
                                    '21_Logged GDP per capita',
                                    '20_Logged GDP per capita',
                                    'Logged GDP per capita_diff',
                                    'Median age',
                                    'COVID-19 deaths per 100,000 population in 2020']]
my_medians = sub_happy_and_COVID.median()
my_means = sub_happy_and_COVID.mean()
###### defining class Country

class Country:
    def __init__(self, ladder_score_21,ladder_score_20,ladder_score_dif,GPD_21,GDP_20,GDP_dif,median_age,COVID_deaths):
        self.ladder_score_21 = ladder_score_21
        self.ladder_score_20 = ladder_score_20
        self.ladder_score_dif = ladder_score_dif
        self.GPD_21 = GPD_21
        self.GDP_20 = GDP_20
        self.GDP_dif = GDP_dif
        self.median_age = median_age
        self.COVID_deaths = COVID_deaths


###### interactive piece of code

## inital prompt
print('#'*10)
input_string_1 = input('Please enter the name of a country: ')
# input_string_1 ='Switzerland'

## small overview of country
if input_string_1 in countries:
    print('')
    print('Great choice! I have data on',input_string_1)
    print('Here is some information about',input_string_1,':')
    print('')
    country_data = sub_happy_and_COVID.loc[input_string_1]
    print('')
    joined = pd.DataFrame({input_string_1:country_data,
                            'Global median':my_medians,
                            'Global average':my_means})
    print(joined)

else:
    print('sorry I don\'t have that country. Please try again with a different country')
