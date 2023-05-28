name = 'Phil'
age = 25
def make_user(name,age):
    dict = {name:age}
    return dict

result = make_user('vasya', 20)
print(result)

def format_user(result):
    for k, v in result.items():
        print(k, v)


form = format_user(result)
    

    
