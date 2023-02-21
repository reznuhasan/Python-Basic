def myName(**kargs):
    print(kargs)
    for k,v in kargs.items():
        print(k,v)

myName(name="Rizwan",age="24",versity="smuct")