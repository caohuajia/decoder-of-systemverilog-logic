import re

# sv = """assign a = b[0]&~(( b[1]// 注释
#                             |b[3] ) &b[4]
#                             |1'b0)|chj;
#             assign  s = ~a | b[3] &(_a154_[555])|k;"""
sv = 'assign a = b&(c&d)&e;'

sv= sv.replace('assign','')
in_var = set()
out_var = set()
inter_var = set()
fun = {}  ## 保存输出变量对应的 运算式子

def delete_annotation(_lines):
    pass

exps = sv.split(';')

## 处理sv字符串，提取输入输出变量和逻辑式
for exp in exps[0:-1]:
    lines = exp.split('\n')
    exp = ''
    for line in lines:
        line = line.split('//')[0]
        exp += str(line)
    exp = exp.replace(' ','')

    exp = exp.split('=')
    out_var.add(exp[0])
    fun[exp[0]] = exp[1]

    for var in re.split(r'[&|~!()]',exp[1]):
        if var==None or var=='' or var=='1\'b0' or var=='1\'b1' or var=='\'b0' or var=='\'b1' or var=='1' or var=='0':
            pass
        else:
            in_var.add(var)

## 提取中间变量
for var in in_var:
    for vaar in out_var:
        if var == vaar:
            inter_var.add(var)

## 中间变量划分给输入或输出
for var in inter_var:
    pass
    # in_var.remove(var)
    ##out_var.remove(var) ##中间变量算作输出变量可注释掉这一句

in_var = sorted(in_var)
inter_var = sorted(inter_var)
out_var = sorted(out_var)
