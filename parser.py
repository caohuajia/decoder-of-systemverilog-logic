import itertools



equ = '~a&~b|(c&d|e)&fff'
input_vals = ['a','b','c','d','e','fff']
true_result = []

def assign_input_var(_vars, _vals):
    _result = ''
    for i in range(len(_vars)):
        if _vals[i] == '-':
            _result += '{} = \'{}\'\n'.format(_vars[i], _vals[i])
        else:
            _result += '{} = {}\n'.format(_vars[i], _vals[i])
    return _result

def gen_statement(_a):
    exp = 'result_of_statment = itertools.product('  ## 这个变量只能在全局中用，不能在函数中使用，很奇怪
    tmp = ''
    for i in _a:
        tmp += str(i)+','
    tmp = tmp[:-1]
    exp += tmp+')'
    return exp

# a = [1,'-',0,1]
## 函数要求的输入格式 a = [1,'-',0,1]
def gen_list_from_x(_ls):  
    _result = []
    for i in _ls:
        if i == '-':
            _result.append([1,0])
        else:
            _result.append([i])
    return _result

# 输入的所有变量情况[(1, 0, 0, 0), (0, 0, 0, 0)]
# 输入的逻辑式子
def all_equal_to_one(_ls,_equ):
    for state in _ls:

        input_exp = assign_input_var(input_vals,state)
        exec(input_exp)  # 输入变量赋值

        _result = eval(_equ)
        if _result == 0 or _result == -2 :
            return False
    return True

# 主要是查看结果是否在正确的结果中
def had_included(_testing):
    for _state in true_result: # 对于正确结果中的所有变量
        # print(_testing, _state)
        for i in range(len(input_vals)): # 对一个正确结果进行位检查
            if (_testing[i] == _state[i]) or _state[i]=='-':
                if i == (len(input_vals)-1): # 最后一位 位检查通过
                    return True
            else:
                break # 位检查失败，退出这个变量对比
    return False  # 所有变量对比结束，没有找到通过的，退出错误

for vars in list(itertools.product(['-',0,1],repeat=len(input_vals))):
    # print(list(vars))
    # vars is (1, 0, 1, 0)
    if '-' in vars:
        after_replace = gen_list_from_x( list(vars))
        # print(after_replace)
        statement = gen_statement(after_replace)
        exec(statement)

        # 将含有x的变量 转换为所有有可能的情况列表
        # [(1, 0, 0, 0), (0, 0, 0, 0)]
        results_of_x = list(result_of_statment)

        if(all_equal_to_one(results_of_x,equ)):
            if had_included(vars):
                continue
            else:
                true_result.append(vars)

    else:
        vars_into_list = []
        vars_into_list.append(vars)
        if all_equal_to_one(vars_into_list,equ):
            if had_included(vars):
                # print(vars,'已经存在')
                continue  # 这个变量情况已经存在了，不用进行任何操作
            else:
                true_result.append(vars)

for i in true_result:
    for j in i:
        print(j,end=' ')
    print(' ')
