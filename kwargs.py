def func(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} : {v}")

func(firstname='Lalit',lastname='Prajapati',age=24)