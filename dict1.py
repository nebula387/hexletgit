name = 'Phil'
age = 25
def make_user(name,age):
    dict = {name:age}
    return dict

result = make_user('Vasya', 20)


def format_user(result):
    for k, v in result.items():
        return f'{k}, {v}'


form = format_user(result)

print(result,form)
    

    
