# def do_something(x,y):
#     print(f"x={x} y={y}")


# do_something(x=[1,2,3,4,5,6,6],y="hello")

def do_something(work):
    print("Start the work")
    work()
    print("Doen with the work")
def practice_coding():
    print("I am practicing python")
do_something(practice_coding)