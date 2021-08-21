import re
import gen_tree as gtree
import gen_var as gvar
sv = """assign a = b[0]&~(( b[1]// 注释
                            |b[3] ) &b[4]
                            |1'b0)|chj;
            assign  s = ~a | b[3] &(_a154_[555])|k;"""
sv= sv.replace('assign','')
in_var = set()
out_var = set()
inter_var = set()
fun = {}
exps = sv.split(';')
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

for var in in_var:
    for vaar in out_var:
        if var == vaar:
            inter_var.add(var)
for var in inter_var:
    pass
    # in_var.remove(var)
    ##out_var.remove(var) ##中间变量算作输出变量可注释掉这一句

# l = [['1']]
def apart(ls):
    for i in ls:
        if type(i)==list:
            apart(i)
# apart(l)
# print(l)
for var in out_var:
    print('out is ',var)
    logic = fun[var]
    # print(logic)
    
    tree = []
    tmp = tree

    pare = 0
    index = 0
    flag = 0
    buf = ''
    tree = [logic]
    tree = gtree.apart(tree)
    print(tree)
    print(' ')
    gvar.parse(tree,in_var,inter_var)
    
    break