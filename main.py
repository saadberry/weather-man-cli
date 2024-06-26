"""
Main file to handle weather data
"""
import os
import re
"""

We can define data structure as: 

    weather = {
        'year': {
            'month': {
                'day': ['max_temp', 'mean_temp', 'min_temp']
            }
        }
    }

e.g.

    weather = {
        
        '2001': {
            '2': {
                '1': ['20', '18', '12'],
                '2': ['20', '18', '12'],
            },
            '5': {
                '1': ['20', '18', '12'],
                '2': ['20', '18', '12'],
            },
        },

        '2002': {
            '10': {
                '1': ['20', '18', '12'],
                '2': ['20', '18', '12'],
            },
            '11': {
                '1': ['20', '18', '12'],
                '2': ['20', '18', '12'],
            },
        },

    }
"""


class Weather():
    """
    Class to parse the files & populating the readings data structure
    """

    def __init__(self):
        self.weather_data = {}

    @staticmethod
    def convert_temp_reading_to_list(temp_reading):
        """
        Method that uses converts temperature reading to a list

        Readings are stored as:
            2009-12-1,17,13,9,8,5,3,55,52,51,,,,10.0,7.0,4.0,7,2,,0.0,,,-1
        Where:
            - The first element is the date  - 2009-12-1 (YYYY-MM-DD)
            - The second element is the max temp - 17
            - The third element is the mean temp - 13
            - The fourth element is the min temp - 9

        Args:
            temp_reading (str): temperature reading

        Returns:
            temp_list (list): temperature readings split by commas
        """
        temp_list = temp_reading.split(',')
        return temp_list

    def read_data(self):
        """
        Method to read weather data
        Returns:
            weather_data (dict): weather data
        """
        files_directory = "/home/winston/documents/code/training-plan/weather-man-cli/weatherfiles/"
        files = os.listdir(files_directory)
        print(self.weather_data)
        for f in files:
            with open(f"{files_directory}/{f}", 'r') as reader:
                x = reader.readlines()
                data = x[1:]
                # Extract the year & month
                year = str(x[1])[:4]
                # print(x[1])
                month = str(x[1])[5:8]
                if month[-1] == '-':
                    month = month[:-1]
                if month[-2] == '-':
                    month = month[:-2]
                # print('month', month)
                if year not in self.weather_data:
                    self.weather_data[year] = {}
                if month not in self.weather_data[year]:
                    self.weather_data[year][month] = {}
                for d in data:
                    # print(d)
                    # print('month', month)
                    if int(month) <= 9:
                        day = str(d)[7:9]
                    else:
                        # print('yes')
                        day = str(d)[8:10]
                        # print(day)
                    # print(day)
                    # For single-digit days, remove trailing comma
                    if day[-1] == ',':
                        day = day[:-1]
                        # print('day after operation', day)
                    if day not in self.weather_data[year][month]:
                        self.weather_data[year][month][day] = []
                    if not self.weather_data[year][month][day]:
                        temp_list = self.convert_temp_reading_to_list(d)
                        # Add max temp
                        self.weather_data[year][month][day].append(temp_list[1])
                        # Add mean temp
                        self.weather_data[year][month][day].append(temp_list[2])
                        # Add min temp
                        self.weather_data[year][month][day].append(temp_list[3])

        print(self.weather_data)

if __name__ == '__main__':
    weather = Weather()
    weather.read_data()