# Create a decorator that makes sure that all function arguments where it's applied will match the regex on the regex
# exercise above.
from regex_searcher import regex_snake_case


def regex_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@regex_decorator
def regex_fun(*args):
    for arg in args:
        match = regex_snake_case(arg)
        if not match:
            print("Not all arguments matches")
            return
    print("All given arguments matches")


test_text = "asdv_123feq_vfdfwer12_3w_2_3qwe_t"
print("For '{}', '{}', '{}':".format( test_text, "344", "asd_asd34f_a"))
regex_fun(test_text, "344", "asd_asd34f_a")
print()
print("For '{}', '{}', '{}':".format( test_text, "yyy_www", "asd_asd34f_a"))
regex_fun(test_text, "yyy_www", "asd_asd34f_a")
