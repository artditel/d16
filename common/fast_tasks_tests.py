#Write your functions here: they should be named parse_ints,
#parse_floats, filter_title_words, arithmetic_mean, arithmetic_median,
#positive_ammount, positive_percent

def hello_world():
    return "HelloWorld"

def parse_ints(line):
	return(list(map(int , line.split())))

def parse_floats(line):
	return(list(map(float , line.split())))

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
assert((arithmetic_mean([1.0, -3.0, 5.0])) == 1.0)
assert((arithmetic_mean([23.0, 5.0, 14.0])) == 14.0)
assert((arithmetic_mean([1.6 , 4.0 , 6.8 , 5.7])) == 4.525)
assert((arithmetic_median([1.0, 3.0, -5.0])) == 1.0)
assert((arithmetic_median([23.0, 5.0, 14.0 , 4.0 , 6.8])) == 6.8)
assert((arithmetic_median([-1.6 , 4.0 , 6.8 , 5.7])) == 4.85)
assert((int(positive_ammount([-1.0, -3.0, 5.0]))) == 1)
assert((int(positive_ammount([23.0, -5.0, 14.0, -14.0]))) == 2)
assert((int(positive_ammount([1.6 , -4.0 , 6.8 , -5.7, -4.655, 6.894]))) == 3)
assert((float(positive_percent([-1.0, 5.0]))) == 50.0)
assert((float(positive_percent([23.0, -5.0, -14.0, -14.0]))) == 25.0)
assert((float(positive_percent([1.6 , 4.0 -5.7, 4.655, 6.894]))) == 80.0)

print("No errors detected, all tests finished correctly")
