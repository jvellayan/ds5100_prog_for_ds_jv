#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 09:19:48 2021

@author: rpindale
"""

import numpy as np
import pandas as pd
import os
import sys
import matplotlib.pyplot as plt
path = '/Users/rpindale/Documents/DS5100/ds5100_prog_for_ds_jv/'





os.chdir(path)




h15 = pd.read_csv('2015.csv').dropna()
h16 = pd.read_csv('2016.csv').dropna()
h17 = pd.read_csv('2017.csv').dropna()
h18 = pd.read_csv('2018.csv').dropna()
h19 = pd.read_csv('2019.csv').dropna()
h20 = pd.read_csv('WHR2020.csv').dropna()
h21 = pd.read_csv('world-happiness-report-2021.csv').dropna()




uniform_cols = ['Year',
                'Country',
                'Score',
                'GDP',
                'Social support',
                'Healthy life expectancy',
                'Freedom to make life choices',
                'Generosity',
                'Perceptions of corruption',
                'Score in Dystopia']










keep15_cols = ['Country', 'Happiness Score','Economy (GDP per Capita)', 'Family',
       'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)',
       'Generosity']

h15 = h15[keep15_cols]

h15['Year'] = 2015


h_15 = h15.rename(columns = {"Happiness Score":uniform_cols[2], 
                             "Economy (GDP per Capita)":uniform_cols[3],
                             "Family":uniform_cols[4], 
                             "Health (Life Expectancy)":uniform_cols[5], 
                             "Freedom": uniform_cols[6],
                             "Trust (Government Corruption)":uniform_cols[8]})


keep16_cols = ['Country', 'Happiness Score',
       'Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)',
       'Freedom', 'Trust (Government Corruption)', 'Generosity']

h16 = h16[keep16_cols]

h16['Year'] = 2016

h_16 = h16.rename(columns = {"Happiness Score":uniform_cols[2], 
                             "Economy (GDP per Capita)":uniform_cols[3],
                             "Family":uniform_cols[4], 
                             "Health (Life Expectancy)":uniform_cols[5], 
                             "Freedom": uniform_cols[6],
                             "Trust (Government Corruption)":uniform_cols[8]})
#h_16



keep17_cols = ['Country', 'Happiness.Score','Economy..GDP.per.Capita.', 'Family',
       'Health..Life.Expectancy.', 'Freedom', 'Generosity',
       'Trust..Government.Corruption.']



h17 = h17[keep17_cols]

h17['Year'] = 2017

h_17 = h17.rename(columns = {"Happiness.Score":uniform_cols[2], 
                             "Economy..GDP.per.Capita.":uniform_cols[3],
                             "Family":uniform_cols[4], 
                             "Health..Life.Expectancy.":uniform_cols[5], 
                             "Freedom": uniform_cols[6],
                             "Trust..Government.Corruption.":uniform_cols[8]})


#h_17



keep18_cols = ['Country or region', 'Score', 'GDP per capita',
       'Social support', 'Healthy life expectancy',
       'Freedom to make life choices', 'Generosity',
       'Perceptions of corruption']



h18 = h18[keep18_cols]

h18['Year'] = 2018

h_18 = h18.rename(columns = {"Country or region":uniform_cols[1], 
                             "GDP per capita":uniform_cols[3]})

#h_18


keep19_cols = ['Country or region', 'Score', 'GDP per capita',
       'Social support', 'Healthy life expectancy',
       'Freedom to make life choices', 'Generosity',
       'Perceptions of corruption']

h19 = h19[keep19_cols]

h19['Year'] = 2019

h_19 = h19.rename(columns = {"Country or region":uniform_cols[1],
                            "GDP per capita":uniform_cols[3]})
#h_19




keep20_cols = ['Country name','Ladder score',
       'Logged GDP per capita', 'Social support', 'Healthy life expectancy',
       'Freedom to make life choices', 'Generosity',
       'Perceptions of corruption']

h20 = h20[keep20_cols]

h20['Year'] = 2020

h_20 = h20.rename(columns = {"Country name":uniform_cols[1],
                             "Ladder score": uniform_cols[2],
                            'Logged GDP per capita':uniform_cols[3]})
#h_20




keep21_cols = ['Country name','Ladder score',
       'Logged GDP per capita', 'Social support', 'Healthy life expectancy',
       'Freedom to make life choices', 'Generosity',
       'Perceptions of corruption', 'Year']


h21['Year'] = 2021
h21 = h21[keep21_cols]

h_21 = h21.rename(columns = {"Country name":uniform_cols[1],
                             "Ladder score": uniform_cols[2],
                            'Logged GDP per capita':uniform_cols[3]})
#h_21


happy = pd.concat((h_15, h_16, h_17, h_18, h_19, h_20, h_21))




class data_explore:
    """Useful functions for exploring the data"""
    def __init__(self, data):
        """Input:
        a pandas data frame from world happiness report
        the year   int or float"""
    
        self.data = data
        self.uniform_cols = sorted(['Year','Country','Score','GDP','Social support','Healthy life expectancy','Freedom to make life choices','Generosity','Perceptions of corruption'])
        
        
    def column_lister(self):
        """Prints out columns"""
        a=sorted(list(self.data.columns))
        return(a)
            
    def mimmax_happy(self, country):
        min_happy = min(self.data[self.data.Country == country].Score)
        max_happy = max(self.data[self.data.Country == country].Score)
        print("lowest happiness score for " + str(country) + " is: ", min_happy)
        print("\nhighest happiness score for " + str(country) + " is: ", max_happy)
        
    def worst_year(self):
        year_mean = [(np.mean(self.data.Score[self.data.Year==i]),i) for i in sorted(list(set((self.data.Year))))]
        return(sorted(year_mean)) # returns year with lowest world happiness         

    def plot_avg_happy(self):
        year_mean = [(np.mean(self.data.Score[self.data.Year==i])) for i in sorted(list(set((self.data.Year))))]
        years = range(2015,2022)
        plt.plot(years,year_mean, 'o', markersize=12, color='orange')
        plt.title('Average World Happiness Score by Year', fontsize=18)
        plt.ylabel('Average World Happiness Score',fontsize=16)
        plt.xlabel('Year', fontsize=16)
        plt.grid()
        plt.savefig(path + 'avg_score.png')
        
        
        
import unittest
class DataTestCase(unittest.TestCase): 
    
    def test_worst_year(self):
        test1 = data_explore(happy)
        print(test1.worst_year)
        
        expected = 2017
        self.assertEqual(test1.worst_year()[0][1], expected)
        
        
    def test_is_col_corrext(self):
        test1 = data_explore(happy)
        
        expected = test1.uniform_cols
        self.assertEqual(test1.column_lister(), expected)
        
if __name__ == '__main__':
    unittest.main()   


    