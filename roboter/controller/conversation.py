from roboter.models import robot
from roboter.models import users

def talk_about_restaurant():
    restaurant_robot = robot.RestaurantRobot()
    user = users.Users()
    user.name = restaurant_robot.hello()
    restaurant_robot.ask_preferable_or_not()
    restaurant_robot.ask_preferable_restaurant(user.name)
    restaurant_robot.say_good_bye(user.name)

