import json
import time


def number_of_calls(func):
    def increase_number(*args, **kwargs):
        increase_number.count += 1
        return func(*args, **kwargs)

    increase_number.count = 0
    return increase_number


@number_of_calls
def function_test():
    print('Call function')


def cacheble(time_limit=None):
    def wrapper(func):
        def memorise(*args, **kwargs):
            key = str(list(args) + [(key, value) for key, value in kwargs.items()])
            if key in memorise.cache:
                result = memorise.cache[key]
            else:
                result = func(*args, **kwargs)
                memorise.cache[key] = result
                if time_limit:
                    memorise.expire_times[key] = time.time() + time_limit
            elements = [key for key in memorise.cache]
            oldest = elements[0]
            while True:
                if memorise.expire_times[oldest] < time.time():
                    memorise.expire_times[oldest].pop()
                    memorise.expire_times[oldest].pop()
                else:
                    break
            return result

        memorise.cache = dict()
        memorise.expire_times = dict()
        return memorise

    return wrapper


@cacheble(time_limit=10)
def function_test_2(a, b, c):
    return a + b + c

def json_to_dict(file):
    with open(file) as fp:
        dictionary = json.load(fp)
    return dictionary

def convert_dictionary(dictionary):
    for key, value in dictionary.items():
        print(str(key) + '.', end='')
        if isinstance(value, dict):
            convert_dictionary(value)
        else:
            print(str(value))

if __name__ == '__main__':
    print('Prima problema:')
    print(function_test.count)
    function_test()
    function_test()
    print(function_test.count)
    print('A doua problema:')
    function_test_2(a=1, b=2, c=3)
    function_test_2(1, c=2, b=3)
    print(function_test_2.cache)
    print(function_test_2.expire_times)
    print('A treia problema:')
    print(json_to_dict("json_test"))
    dictionary = {'a' :1, 'b': {'c': 2}, 'd': {'e' : {'f': 3}, 'g': 4}}
    convert_dictionary(dictionary)