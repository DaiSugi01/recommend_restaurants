import os

from termcolor import colored

from roboter.view import console
from roboter.models import ranking

class Robot(object):
    def __init__(self):
        self.template_dir_path = console.get_template_dir_path()

    def hello(self):
        """ Show hello template and Return user name

        :return:
            User name
        """
        file_path = self.template_dir_path + 'hello.txt'
        console.say_hello(file_path)
        show_word = 'Enter your name: '
        return self.get_user_input(show_word)

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
            temp_file_path = self.template_dir_path + 'my_recommend_restaurant.txt'
            show_word = 'Enter your answer: '

            # Show the recommend restaurants
            for t_restaurant in d_restaurant:
                restaurant_name, v = t_restaurant
                console.show_recommend_restaurant(temp_file_path, restaurant_name)
                ans = self.get_yes_no_input(show_word)
                if ans == 'Yes' or ans == 'Y':
                    ranking_csv.add_restaurant(restaurant_name)
                    break

        # Show the template for asking recommend restaurant
        temp_file_path = self.template_dir_path + 'which_restaurant.txt'
        console.show_template(temp_file_path, user_name)
        show_word = 'Enter your recommend restaurant: '

        # wait for input that user's recommended restaurant
        restaurant_name = self.get_user_input(show_word)
        ranking_csv.add_restaurant(restaurant_name)

    def say_good_bye(self, user_name):
        """ Show good-bye template

        :param
            user_name: user name
        """
        file_path = self.template_dir_path + 'good_bye.txt'
        console.show_template(file_path, user_name)
