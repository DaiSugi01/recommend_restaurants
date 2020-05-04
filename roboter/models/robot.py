import os

from termcolor import colored

from roboter.view import console
from roboter.models import ranking

class Robot(object):
    def hello(self):
        """ Show hello template and Return user name

        :return:
            User name
        """
        contents = console.get_template('hello.txt')
        print(colored(contents.template, 'green'))
        show_word = 'Enter your name: '
        return self.get_user_input(show_word)

    def say_good_bye(self, user_name):
        """ Show good-bye template

        :param
            user_name: user name
        """
        contents = console.get_template('good_bye.txt')
        contents = contents.substitute(name=user_name)
        print(colored(contents, 'green'))

class RestaurantRobot(Robot):

    def get_user_input(self, show_word=''):
        """ This encourage user to input

        :return:
            User name
        """
        while True:
            input_word = input(colored(show_word, 'blue'))
            if input_word != '':
                break
            else:
                print('\n文字を入力してください')
                print("This can't be blank.\n")

        if ' ' in input_word:
            ans_words = input_word.split(' ')
            new_ans_words = map(lambda s: s.capitalize(), ans_words)
            input_word = ' '.join(new_ans_words)
        else:
            input_word = input_word.capitalize()

        return input_word

    def get_yes_no_input(self, show_word=''):
        """ This encourage user to input their answer for recommend restaurant

        :return:
            Answer (Yes or No)
        """
        while True:
            input_word = input(colored(show_word, 'blue'))
            input_word = input_word.capitalize()
            if input_word == 'Yes' or input_word == 'Y' or input_word == 'No' or input_word == 'N':
                break
            else:
                print('\n"yes"、"y"または"no"、"n"で入力してください')
                print("You should input 'yes', 'y','no','n'.\n")
        return input_word

    def ask_preferable_restaurant(self, user_name):
        """ Ask preferable restaurant to user

        :param
            user_name: user name
        """
        ranking_csv = ranking.RankingCsv()

        if os.path.exists(ranking_csv.csv_filename):
            d_restaurant = ranking_csv.read_csv()
            d_restaurant = sorted(d_restaurant.items(), key=lambda x: x[1], reverse=True)
            show_word = 'Enter your answer: '

            # Show the recommend restaurants
            for t_restaurant in d_restaurant:
                restaurant_name, v = t_restaurant
                contents = console.get_template('my_recommend_restaurant.txt')
                contents = contents.substitute(restaurant=restaurant_name)
                print(colored(contents, 'green'))
                ans = self.get_yes_no_input(show_word)
                if ans == 'Yes' or ans == 'Y':
                    ranking_csv.add_restaurant(restaurant_name)
                    break

        # Show the template for asking recommend restaurant
        contents = console.get_template('which_restaurant.txt')
        contents = contents.substitute(name=user_name)
        print(colored(contents, 'green'))

        # wait for input that user's recommended restaurant
        show_word = 'Enter your recommend restaurant: '
        restaurant_name = self.get_user_input(show_word)
        ranking_csv.add_restaurant(restaurant_name)