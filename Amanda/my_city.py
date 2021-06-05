# encoding: utf-8

##################################################
# This describes a city. This sections is a group of commented lines (lines starting with
# the "#" character) that describes general features of the script such as the type of licence (defined by the
# developer), authors, credits, versions among others
##################################################
#
##################################################
# Author: Amanda Gioia
# Copyright: Copyright 2021
# Email: ama.gioia@gmail.com
# Status: development
##################################################

# End of header section


import datetime
current_date = datetime.date.today()
city_name = 'Montreal'
city_year = 1800
city_area = 200000000
city_population = 1000000
city_density = city_population/city_area
#city_age = current_year-city_year

print('City Population = ' + str(city_population))
print('City Density = ' + str(city_density))
print('Date = ' + str(current_date))
print('Date = ' + str(current_date))