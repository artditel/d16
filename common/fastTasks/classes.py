###############################################################################
#classes. Add your classes here.

class HelloWorld:
    def __init__(self, name="Anonymous"):
        self.name = name
    def get_hello(self):
        return "Hello world from " + self.name


###############################################################################
#tests. Add your tests here.

def test_hello_world():
    hw = HelloWorld()
    assert(hw.get_hello() == "Hello world from Anonymous")

    hw = HelloWorld("Vasya")
    assert(hw.get_hello() == "Hello world from Vasya")

    print("HelloWorld class tested")

def test_counter():
    def hw():
        print "Hello World!"
    counter = Counter(hw)
    counter()
    assert(counter.get_calls_count() == 1)
    counter()
    assert(counter.get_calls_count() == 2)
    print("Counter class tested")



###############################################################################
#main. Add test calls here.

if __name__ == "__main__":
    test_hello_world()
