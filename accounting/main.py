from datetime import datetime
import emoji
from salary import calculate_salary
from people import get_employees

if __name__ == '__main__':
    get_employees()
    calculate_salary()
    print(datetime.today().date())
    print(emoji.emojize('Python is :thumbs_up:'))