#Write your functions here: they should be named parse_ints
#parse_floats, filter_title_words, arithmetic_mean, arithmetic_median

def hello_world():
    return "HelloWorld"


assert(hello_world() == "HelloWorld")
assert(tuple(parse_ints("1 2 3 4")) == (1, 2, 3, 4))
assert(tuple(parse_ints("1 5 2 57")) == (1, 5, 2, 57))
assert(tuple(parse_ints("-16 46 0 13")) == (-16, 46, 0, 13))
assert(tuple(parse_floats("1.2 3.4 5.7")) == (1.2, 3.4, 5.7))
assert(tuple(parse_floats("5.2 4.655 6.894")) == (5.2, 4.655, 6.894))
assert(tuple(parse_floats("38.0 15.96 3.005")) == (38.0, 15.96, 3.005))
assert(tuple(filter_title_words("Abigale barse Carter durry Emerson flat Grey")) == ("Abigale", "Carter", "Emerson", "Grey"))
assert(tuple(filter_title_words("Titanic Normandy steamer captain Great Eastern sea")) == ("Titanic", "Normandy", "Great", "Eastern"))
assert(tuple(filter_title_words("accordeon Paris metropolitain Rouene arc du Triumph le Tour d Eiffel")) == ("Paris", "Rouene", "Triumph", "Tour", "Eiffel"))
assert(tuple(arithmetic_mean([1.0, 3.0, 5.0])) == 3.0)
assert(tuple(arithmetic_mean([23.0, 5.0, 14.0])) == 14.0)
assert(tuple(arithmetic_mean([1.6 , 4.0 , 6.8 , 5.7])) == 4.525)
assert(tuple(arithmetic_median([1.0, 3.0, 5.0])) == 3.0)
assert(tuple(arithmetic_median([23.0, 5.0, 14.0 , 4.0 , 6.8])) == 6.8)
assert(tuple(arithmetic_median([1.6 , 4.0 , 6.8 , 5.7])) == 4.85)
