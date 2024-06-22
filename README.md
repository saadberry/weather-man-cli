# Weather Man 
A CLI based program that returns the weather of a said day.

## Setup

1. Clone this directory.
2. Create a virtual environment.
    - On Linux, you can do this by running the following commands:
        - `virtualenv venv`
        - `source venve/bin/activate`
3. Install the packages in `requirements.txt`:
    - `pip install -r requirements.txt` (Use 'pip3' instead of 'pip' if you are on Python3)
4. Run the program:
    - `python -m main` (Use 'python3' instead of 'python' if you are on Python3)

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
![img_1.png](screenshots/task_one.png)

### Given a date, return the **_**average**_** temperature was:
#### - The highest
#### - The lowest
#### - The most humid
![img.png](screenshots/task_two.png)

### Given a date, draw two horizontal bar charts for days with:
#### - The highest temperature ( In red )
#### - The lowest temperature ( In blue)
![img.png](screenshots/task_three.png)