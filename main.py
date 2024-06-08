"""
Main file to handle weather data
"""
import os
import calendar
from colorama import Fore, Style

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


class ReadWeather():
    """
    Class to parse the files & populating the readings data structure
    """

    def __init__(self):
        self.weather_data = {}
        self.weather_data_2 = {}

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
        # print(self.weather_data)
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
                        # print(temp_list)
                        # For task 1
                        # Add max temp
                        self.weather_data[year][month][day].append(temp_list[1])
                        # Add min temp
                        self.weather_data[year][month][day].append(temp_list[3])
                        # Add max humidity
                        self.weather_data[year][month][day].append(temp_list[8])
                        # TODO: For task 2
                        # Add mean humidity
                        self.weather_data[year][month][day].append(temp_list[7])
        # print(self.weather_data)


class CalculateTemp(ReadWeather):
    """
    Class that calculates the highest, lowest temperature and max humidity
    """

    def __init__(self, weather_instance):
        # weather readings will be stored as [max_temp, min_temp, max_humidity]
        self.weather_readings = weather_instance.weather_data
        self.exception_msg = "Please enter a valid integer value from 2004 - 2016"
        self.year_month_exception_msg = "Invalid date format entered! Please enter a date of format: YYYY/MM"
        # print(self.weather_readings)
        # For task 1
        self.max_temp, self.max_humidity, self.min_temp = 0, 0, 100
        # Data structure to hold data of result 1
        self.result = {
            'Highest': [], # temperature, month, day
            'Lowest': [],
            'Humidity': []
        }
        self.months = list(calendar.month_name)
        # For task 2
        self.max_avg, self.avg_humidity, self.min_avg = 0, 0, 100
        self.result_two = {
            'Highest Average': None,
            'Lowest Average': None,
            'Average Mean Humidity': None
        }
        """
        We will store result 3 as:
            result_three = {
                 '1': [max_temp_bar_chart, min_temp_bar_chart],
                  .
                  .
                  .
           }
        """
        self.result_three = {}
    def validate_year(self, year):
        """
        Method that validates that:
           - The value entered is of type int
           - It corresponds to the range of weather values ( 2004 - 2016 )

        Raises an Exception with a message if validation fails, does nothing if validation is successful
        """
        # Convert str-value of year to int
        try:
            year = int(year)
        except:
            raise Exception(self.exception_msg)
        assert 2004 <= year <= 2016, self.exception_msg

    def validate_year_and_month(self, date):
        """
        Method that validates year & month date entered.
        Args:
            date(str): "YYYY/MM", e.g. 2005/11
        """
        assert '/' in date, self.year_month_exception_msg

    def generate_bar_chart(self, temp):
        """
        Method that generates a horizontal bar chart representing the temperature
        Args:
            temp(int): temperature reading, e.g. 5
        Returns:
            bar_chart(str): horizontal bar chart, e.g. +++++
        """
        bar_chart = ""
        count = 0
        while count < int(temp):
            bar_chart += "+"
            count += 1
        return bar_chart


    def task_one(self):
        """
        Method that, given a year, computes the days of:
            - Max temperature
            - Min temperature
            - Max Humidity
        - First max, min temp & humidity values will be stored in self.weather_readings
        - Then, for subsequent iterations we will be doing a comparison. And update values accordingly
        """
        # year = input("Enter year: [e.g. 2005")
        year = str(2005)
        self.validate_year(year)
        # print(f"Year entered: {year}")
        year_data = self.weather_readings.get(year)
        # print(f"Year data: {year_data}")
        for key, value in year_data.items():
            month = int(key)
            # print(f"{key}: {value}")
            for k, v in value.items():
                day = int(k)
                # print(f"{k}: {v}")
                # Find max temp
                # If max_temp value exists
                if v[0]:
                    # print(f"in v[0]: {v[0]}")
                    if self.max_temp < int(v[0]):
                        # print("in if")
                        self.max_temp = int(v[0])
                        if self.result['Highest']:
                            self.result['Highest'][0] = self.max_temp
                            self.result['Highest'][1] = month
                            self.result['Highest'][2] = day

                        else:
                            self.result['Highest'].append(self.max_temp)
                            self.result['Highest'].append(month)
                            self.result['Highest'].append(day)
                            # print(f"in else, {self.result['Highest']}")

                if v[1]:
                    if self.min_temp > int(v[1]):
                        # print(f"in if 2, readings: {v}")
                        self.min_temp = int(v[1])
                        if self.result['Lowest']:
                            self.result['Lowest'][0] = self.min_temp
                            self.result['Lowest'][1] = month
                            self.result['Lowest'][2] = day
                        else:
                            self.result['Lowest'].append(self.min_temp)
                            self.result['Lowest'].append(month)
                            self.result['Lowest'].append(day)
                if v[2]:
                    if self.max_humidity < int(v[2]):
                        # print(f"in if 3, {self.max_humidity}, readings: {v}")
                        self.max_humidity = int(v[2])
                        if self.result['Humidity']:
                            self.result['Humidity'][0] = self.max_humidity
                            self.result['Humidity'][1] = month
                            self.result['Humidity'][2] = day
                        else:
                            self.result['Humidity'].append(self.max_humidity)
                            self.result['Humidity'].append(month)
                            self.result['Humidity'].append(day)

        # print(f"Result: {self.result}")
        for key, value in self.result.items():
            print(f"{key}: {value[0]}C on {self.months[value[1]]} {value[2]}")

    def task_two(self):
        """
        Method that, given a month, computes the days of:
            - Average highest temperature
            - Average lowest temperature
            - Average mean humidity
        """
        # month = input("Enter the month: [e.g. 2005/6]")
        month = "2005/11"
        self.validate_year_and_month(month)
        user_input = month.split('/')
        print(user_input)
        year_data = self.weather_readings.get(user_input[0])
        # print(year_data)
        for key, value in year_data.items():
            # print(f"{key}: {value}")
            if key == user_input[1]:
                # print(value)
                max_temp_count, min_temp_count, mean_humidity_count = 0, 0, 0
                max_temp_sum, min_temp_sum, mean_humidity_sum = 0, 0, 0
                for k, v in value.items():
                    print(f"{k}: {v}")
                    day = int(k)
                    # If max_temp value exists
                    if v[0]:
                        max_temp_sum += int(v[0])
                        max_temp_count += 1
                    # If max_temp value exists
                    if v[1]:
                        min_temp_sum += int(v[1])
                        min_temp_count += 1
                    # If mean_humidity value exists
                    if v[3]:
                        mean_humidity_sum += int(v[3])
                        mean_humidity_count += 1
                self.result_two['Highest Average'] = (max_temp_sum//max_temp_count)
                self.result_two['Lowest Average'] = (min_temp_sum//min_temp_count)
                self.result_two['Average Mean Humidity'] = (mean_humidity_sum//mean_humidity_count)
        for k, v in self.result_two.items():
            print(f"{k}: {v}C")

    def task_three(self):
        """
        Method that, given a month, draws two horizontal bar charts on the console for the highest and lowest temperature on each day.
        Highest in red and lowest in blue.
        """
        # month = input("Enter the month: [e.g. 2005/6]")
        month = "2005/11"
        self.validate_year_and_month(month)
        user_input = month.split('/')
        print(user_input)
        year_data = self.weather_readings.get(user_input[0])
        # print(year_data)
        for key, value in year_data.items():
            # print(f"{key}: {value}")
            # If key is our desired month
            if key == user_input[1]:
                for k, v in value.items():
                    # print(f"{k}: {v}")
                    if not self.result_three.get(k):
                        self.result_three[k] = []
                    if v[0]:
                        self.result_three[k].append(self.generate_bar_chart(v[0]))
                    if v[1]:
                        self.result_three[k].append(self.generate_bar_chart(v[1]))
        print(Fore.RED + "This text is red", Style.RESET_ALL + "123")

        # print(self.result_three)
        for key, value in self.result_three.items():
            # print(f"{key}: {value}")
            if value:
                print(Style.RESET_ALL)
                if value[0]:
                    print(f"{key}: {Fore.RED} {value[0]} {Style.RESET_ALL} {len(value[0])}C")
                if value[1]:
                    print(f"{key}: {Fore.CYAN} {value[1]} {Style.RESET_ALL} {len(value[1])}C")



if __name__ == '__main__':
    weather = ReadWeather()
    weather.read_data()
    calc_temp = CalculateTemp(weather)
    # calc_temp.task_one()
    # calc_temp.task_two()
    calc_temp.task_three()