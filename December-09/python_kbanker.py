
def one_to_one(domain, range_, func):
    domain = [int(x.strip()) for x in domain]
    range_ = [int(x.strip()) for x in range_]

    if len(domain) != len(range_): return False

    if '^' in func: func = func.replace('^', '**')
    
    for x in domain: range_.remove(eval(func.replace('x',str(x))))
    
    if len(range_) == 0: return True
    else: return False
    
set1 = input('Set 1: ').split(',')
set2 = input('Set 2: ').split(',')

fun = input('Function: ')

print(one_to_one(set1, set2, fun))
