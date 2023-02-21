def first_function(work):
    print("I am first factorial")
    def second_function():
        work()
        print("I am second function")
    return second_function
@first_function
def get_factorail():
    print("result of factorial")

get_factorail()