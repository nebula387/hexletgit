#diff_keys({'name': 'Bob', 'age': 42}, {})
# {'kept': set(), 'added': set(), 'removed': {'name', 'age'}}
#diff_keys({}, {'name': 'Bob', 'age': 42})
# {'kept': set(), 'added': {'name', 'age'}, 'removed': set()}
#diff_keys({'a': 2}, {'a': 1})
# {'kept': {'a'}, 'added': set(), 'removed': set()}

def diff_keys(a, b):
    ak = set(a.keys())
    bk = set(b.keys())

    s = {}
    s['kept'] = bk - ak
    s['added'] = (ak ^ bk) - ak
    s['removed'] = ak - bk
    
    return s

print(diff_keys({'name': 'Bob', 'age': 42}, {'b': 5}))
