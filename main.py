"""
Main file to handle weather data
"""
import os
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

                # print(x[2])
        print(self.weather_data)

if __name__ == '__main__':
    weather = Weather()
    weather.read_data()