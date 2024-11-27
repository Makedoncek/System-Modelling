import math
import random


def generate_exponential(time_mean):
    a = 0
    while a == 0:
        a = random.random()
    a = -time_mean * math.log(a)
    return a


def generate_normal(time_mean, time_std):
    a = time_mean + time_std * random.gauss()


def generate_uniform(time_min, time_max):
    a = 0
    while a == 0:
        a = random.random()
    a = time_min + a * (time_max - time_min)
    return a
