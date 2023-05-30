name = 'Phil'
age = 25
def make_user(name,age):
    dict = {name:age}
    return dict

user = make_user('Vasya', 20)


#def format_user(result):
    #for k, v in result.items():
        #return f'{k}, {v}'

def format_user(user):
    return f'{user["name"]}, {user["age"]}'

form = format_user(user)

print(form,user)
    

    
