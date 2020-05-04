import os

from termcolor import colored

from roboter.view import console
from roboter.models import ranking

class Robot(object):
    def __init__(self):
        pass

    def hello(self):
        """ Show hello template and Return user name
        :return:
            User name
        """
        contents = console.get_template('hello.txt')
        user_name = input(colored(contents.template, 'green')).capitalize()

        while True:
            if user_name:
                break
            else:
                print(colored('あなたの名前を入力してください', 'blue'))
                print(colored('Please type your name', 'blue'))
                user_name = input().capitalize()
        return user_name

    def say_good_bye(self, user_name):
        """ Show good-bye template
        :param
            user_name: user name
        """
        contents = console.get_template('good_bye.txt')
        print(colored(contents.substitute(name=user_name), 'green'))

class RestaurantRobot(Robot):
    def __init__(self):
        super().__init__()
        self.ranking_csv = ranking.RankingCsv()

    def ask_preferable_restaurant(self, user_name):
        """ Ask preferable restaurant to user
        :param
            user_name: user name
        """
        if os.path.exists(self.ranking_csv.csv_filename):
            d_restaurant = self.ranking_csv.read_csv()
            d_restaurant = sorted(d_restaurant.items(), key=lambda x: x[1], reverse=True)

            # Show the recommend restaurants
            isYes = False
            for t_restaurant in d_restaurant:
                restaurant_name, v = t_restaurant
                contents = console.get_template('my_recommend_restaurant.txt')
                yes_or_no = input(colored(contents.substitute(restaurant=restaurant_name), 'green')).capitalize()

                while True:
                    if yes_or_no == 'Yes' or yes_or_no == 'Y':
                        self.ranking_csv.add_restaurant(restaurant_name)
                        isYes = True
                        break
                    elif yes_or_no == 'No' or yes_or_no == 'N':
                        break
                    else:
                        print(colored('Yes/Noを入力してください', 'blue'))
                        print(colored('You should input Yes/No', 'blue'))
                        yes_or_no = input().capitalize()

                if isYes:
                    break

        # Show the template for asking recommend restaurant
        contents = console.get_template('which_restaurant.txt')
        restaurant_name = input(colored(contents.substitute(name=user_name), 'green'))
        while True:
            if restaurant_name:
                if ' ' in restaurant_name:
                    before_soret_list = restaurant_name.split(' ')
                    sorted_list = map(lambda s: s.capitalize(), before_soret_list)
                    restaurant_name = ' '.join(sorted_list)
                else:
                    restaurant_name = restaurant_name.capitalize()
                self.ranking_csv.add_restaurant(restaurant_name)
                break
            else:
                print(colored('\nレストラン名を入力してください', 'blue'))
                print(colored("This can't be blank.\n", 'blue'))
                restaurant_name = input().capitalize()
