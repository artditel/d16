#Write your functions here:

def hello_world():
    return "HelloWorld"


assert(hello_world() == "HelloWorld")
assert(tuple(parse_ints("1 2 3 4")) == (1,2,3,4))
assert(tuple(parse_floats("1.2 3.4 5.7")) == (1.2, 3.4, 5.7))
assert(tuple(filter_title_words("abc "))
