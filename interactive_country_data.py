####### importing needed functions
import pandas as pd
import numpy as np
import unittest

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

###### interactive piece of code

## inital prompt
print('#'*10)
input_string_1 = input('Please enter the name of a country: ')
# input_string_1 ='United States'

def country_overview(country_x):

    '''Gives a df of key variables for that country'''

    if country_x in countries:
        print('')
        print('Great choice! I have data on',country_x)
        print('Here is some information about',country_x,':')
        # print('')
        country_data = sub_happy_and_COVID.loc[country_x]
        # print('')
        joined = pd.DataFrame({country_x:country_data,
                                'Global median':my_medians,
                                'Global average':my_means})
        print(joined)
        return joined
    else:
        return 'sorry I don\'t have that country. Please try again with a different country'

#### final output
country_overview(input_string_1)






##### unit testing
#
# tc = unittest.TestCase()
#
# class CountryTestSuite(unittest.TestCase):
#     ## create example countries
#     ex_country = 'Switzerland'
#     ex_country2 = 'Westeros'
#     test_df = country_overview(ex_country)
#     test_df2 = country_overview(ex_country2)
#
#     def test_1_correct_country_data(self):
#         data_lader_21 = self.test_df[self.ex_country]['21_Ladder score']
#         data_region = self.test_df[self.ex_country]['Regional indicator']
#         data_age = self.test_df[self.ex_country]['Median age']
#         data_list = [data_lader_21,data_region,data_age]
#
#         ## test
#         expected_lader_21 = 7.571
#         expected_region = 'Western Europe'
#         expected_age = 43.09999847412109
#         expected_list=[expected_lader_21,expected_region,expected_age]
#         self.assertEqual(expected_list, data_list)
#
#     def test_2_country_not_in_data(self):
#         ##test
#         expected_return = 'sorry I don\'t have that country. Please try again with a different country'
#         self.assertEqual(expected_return, self.test_df2)
#
#     def test_3_correct_global_data(self):
#         data_global_lader_21 = self.test_df['Global median'][2]
#         #test
#         expected_global_lader_21 = 5.534000
#         self.assertEqual(data_global_lader_21, expected_global_lader_21)
#
# if __name__ == '__main__':
#     unittest.main()
