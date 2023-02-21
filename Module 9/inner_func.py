def do_something(work):
    print("Inside the function do something")
    def inner_function():
        work()
        print("Inside the Inner function")
    inner_function()
def practice_coding():
    print("I am practicing python")
do_something(practice_coding)