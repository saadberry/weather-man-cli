# Weather Man 
A CLI based program that returns the weather of a said day.

### The Problem

Given a dataset of weather readings of Muree, Pakistan:

- Read the dataset & parse it.
- Store the data in an appropriate data structure
- Write a program that accepts a time, and return the corresponding weather reading.

### The Solution

We will be storing the weather readings in the following format:

```
weather = {
        'year': {
            'month': {
                'day': ['max_temp', 'mean_temp', 'min_temp']
            }
        }
    }
```


## Screenshots
### Given an year, return the days where the temperature was:
#### - The highest
#### - The lowest
#### - The most humid
![task_1_output](https://github.com/saadberry/weather-man-cli/assets/15974895/f25ef5cb-3692-438d-ba88-73b2f3b7466b)
