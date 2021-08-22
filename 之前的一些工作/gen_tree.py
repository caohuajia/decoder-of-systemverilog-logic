import re
tree = []

# a = '(((~all)))&(bll|(cll&dll|ell)&fll&~(gll&hll))'
# a = '(((~all)))&(bll|(cll&dll|ell)&fll&~(gll&hll))'
# a = '~(b&c)|d&e'

def exist_or(_str):  ## 括号内的不算
    pare = 0
    for i in _str:
        if i == '(':
            pare += 1
            continue
        if i == ')':
            pare -= 1
            continue
        if pare:
            continue
        if i=='|':
            return True
    return False

def exist_and(_str):  ## 括号内的不算
    pare = 0
    for i in _str:
        if i == '(':
            pare += 1
            continue
        if i == ')':
            pare -= 1
            continue
        if pare:
            continue        
        if i=='&':
            return True
    return False

def can_not_split(_str):
    if exist_and(_str) or exist_or(_str):
        return False
    return True

def is_basic_var(_str):
    # print('basic',_str)
    if len(re.findall(r'[()&|]',_str)):
        return False
    return True
# print(is_basic_var('b&c'))
def is_sub_para(_str): ## 不能划分且有括号才是子式
    if can_not_split(_str):
        if _str[-1] == ')':
            return True
    return False

def remove_pare(_str):
    buf = ''
    pare = 0
    for i in _str:
        if i == '(':
            pare += 1
            if pare == 1:
                continue
        if i == ')':
            pare -= 1
        if pare >= 1:
            buf += i
    if _str[0] == '~':
        return '~',[buf]
    else:
        return '0',[buf]

def split_with_or(_str):
    buf = ''
    pare = 0
    result = ['|']
    for i in _str:
        if i == '(':  ## 主要是屏蔽括号中 |
            pare += 1
            buf += i
            # print('发现括号 buf是',buf,'pare is',pare)
            if pare == (0+1):
                continue
        if i == ')':
            pare -= 1
            buf += i
            if pare == 0:
                continue
        if i=='|' and pare==0:
            result.append([buf])
            # print('添加的buf是',buf,'tree is ',tree)
            buf = ''
        else:
            buf += i
    result.append([buf])
    return result

def split_with_and(_str):
    # print(_str)
    buf = ''
    pare = 0
    result = ['&']
    for i in _str:
        # print(i)
        if i == '(':  ## 主要是屏蔽括号中 &
            pare += 1
            # buf += i
            # print('发现括号 buf是',buf,'pare is',pare)
            # if pare >= (0+1):
            #     continue
        if i == ')':
            pare -= 1
            # buf += i
            # print('发现括号 buf是',buf,'pare is',pare)
            # if pare == 0:
            #     continue
        if i=='&' and pare==0:
            result.append([buf])
            # print('添加的buf是',buf,'tree is ',tree)
            buf = ''
            continue
        buf += i
    result.append([buf])
    # print('添加的buf是',buf,'tree is ',tree)
    return result

def foo():
    pass

def apart(_tree):
    elem = _tree[0]
    # print('')
    # print('_tree is ',_tree)
    if is_basic_var(elem):
        # print('is basic var')
        return _tree
    if is_sub_para(elem):
        # print('is sub pare')
        _a,_b = remove_pare(elem)
        _tree = [_a,_b]
        # print('去括号后', remove_pare(elem),'_tree is ',_tree)
        # return _tree
    if exist_or(elem) or exist_and(elem):
        pass
    else:
        if is_sub_para(_tree[0][0]):
            pass
        else:
            # 
            pass
    if exist_or(elem):
        # print('exist or')
        _tree = split_with_or(elem)
    elif exist_and(elem):
        # print('exist and')
        _tree = split_with_and(elem)
        # print('_tree is ',_tree)
    else:
        pass

    for i in range(len(_tree)):
        # print('i is ',_tree[i])
        if i ==0:
            continue
        _tree[i] = apart(_tree[i])
        # print('函数递归完成 _tree is ',_tree )
    # print('函数返回 ',_tree)
    return _tree

# tree = [a]
# print(tree)
# tree = apart(tree)

# print(tree)