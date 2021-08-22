import itertools

class SimpleAnalysis():

    # equ = '~a&~b|(c&d|e)&fff'
    # input_vals = ['a','b','c','d','e','fff']
    equ = ''
    input_vals = []
    true_result = []

    def __init__(self, _equ, _input_vals) -> None:
        self.equ = _equ
        self.input_vals = _input_vals
        self.true_result = []  ## 实列变量，否则作为类变量列表会共享
        self.gen_result()
        pass

    def assign_input_var(self, _vars, _vals):
        _result = ''
        for i in range(len(_vars)):
            if _vals[i] == '-':
                _result += '{} = \'{}\'\n'.format(_vars[i], _vals[i])
            else:
                _result += '{} = {}\n'.format(_vars[i], _vals[i])
        return _result

    # 生成 排列组合含x变量所有情况的 可执行语句
    def gen_statement(self, _a):
        
        ## 这个变量只能在全局中用，不能在函数中使用，很奇怪
        ## 能在类变量中用，类中函数也能用
        exp = 'self.result_of_statment = itertools.product('
        tmp = ''
        for i in _a:
            tmp += str(i)+','
        tmp = tmp[:-1]
        exp += tmp+')'
        return exp

    # a = [1,'-',0,1]
    ## 函数要求的输入格式 a = [1,'-',0,1]
    def gen_list_from_x(self, _ls):  
        _result = []
        for i in _ls:
            if i == '-':
                _result.append([1,0])
            else:
                _result.append([i])
        return _result

    # 输入的所有变量情况[(1, 0, 0, 0), (0, 0, 0, 0)]
    # 输入的逻辑式子
    def all_equal_to_one(self, _ls,_equ):
        for state in _ls:

            input_exp = self.assign_input_var(self.input_vals,state)
            exec(input_exp)  # 输入变量赋值
            # print(_equ)
            _result = eval(_equ)
            if _result == 0 or _result == -2 :
                return False
        return True

    # 主要是查看结果是否在正确的结果中
    def had_included(self, _testing):
        for _state in self.true_result: # 对于正确结果中的所有变量
            # print(_testing, _state)
            for i in range(len(self.input_vals)): # 对一个正确结果进行位检查
                if (_testing[i] == _state[i]) or _state[i]=='-':
                    if i == (len(self.input_vals)-1): # 最后一位 位检查通过
                        return True
                else:
                    break # 位检查失败，退出这个变量对比
        return False  # 所有变量对比结束，没有找到通过的，退出错误

    def gen_result(self):
        # 对输入变量的所有情况进行尝试
        for vars in list(itertools.product(['-',0,1],repeat=len(self.input_vals))):
            # print(list(vars))
            # vars is (1, 0, 1, 0)
            if '-' in vars:
                after_replace = self.gen_list_from_x( list(vars))
                statement = self.gen_statement(after_replace)
                exec(statement) # 执行生成 含x的输入的所有情况

                # 将含有x的变量 转换为所有有可能的情况列表
                # [(1, 0, 0, 0), (0, 0, 0, 0)]
                results_of_x = list(self.result_of_statment) ## 这个变量名不能动

                if(self.all_equal_to_one(results_of_x, self.equ)):
                    if self.had_included(vars):
                        continue
                    else:
                        self.true_result.append(vars)

            else:
                vars_into_list = []
                vars_into_list.append(vars)
                if self.all_equal_to_one(vars_into_list, self.equ):
                    if self.had_included(vars):
                        continue  # 这个变量情况已经存在了，不用进行任何操作
                    else:
                        self.true_result.append(vars)




# sa = SimpleAnalysis(0,0)

# for i in sa.true_result:
#     for j in i:
#         print(j,end = '')
#     print('')