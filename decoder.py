import re
import itertools
import argparse
import analysis

parser = argparse.ArgumentParser("用法：", description = "dddd")
parser.add_argument("-f","--file",help="input file",type=str)
args = parser.parse_args()
if not args.file:
    print('请指定输入文件')
    exit(0)

sv = ''
with open(args.file,'r') as f_r:
    sv = f_r.read()

in_var = set()
out_var = set()
inter_var = set()
fun = {}  ## 保存输出变量对应的 运算式子

def delete_annotation(_lines):
    pass

exps = sv.split(';')

## 处理sv字符串，提取输入输出变量和逻辑式
for exp in exps[0:-1]:
    if  'assign' in exp:
        exp= exp.replace('assign','')
        exp= exp.replace('[','_')
        exp= exp.replace(']','_')
        exp= exp.replace('!','~')
    else:
        continue

    lines = exp.split('\n')
    exp = ''
    for line in lines:
        line = line.split('//')[0]
        exp += str(line)
    exp = exp.replace(' ','')
    if exp == '':
        continue
    # print(exp)
    exp = exp.split('=')
    out_var.add(exp[0])
    exp[1] = exp[1].replace('1\'b','')
    exp[1] = exp[1].replace('\'b','')
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

## 打印输入输出变量名
for i,v in enumerate(itertools.chain( in_var, out_var)):
    if i < len(in_var):
        print('{1:|>{0}}'.format(i+len(v),v))
    else:
        print('{1:|>{0}}'.format(len(in_var),''), end = '')
        print('    ',end = '')
        # print(i,len(in_var))
        print('{1:|>{0}}'.format(i-len(in_var)+len(v),v))
# exit(0)
for one_of_out in out_var:
    # print('分析', fun[one_of_out])
    sa = analysis.SimpleAnalysis(fun[one_of_out], in_var)

    for i in sa.true_result:
        for j in i :
            print(j,end='')
            
        print('    ',end='')
        for i in out_var:
            if i == one_of_out:
                print(1,end='')
            else:
                print('-',end = '')
        print('')
    del sa
    # print('完成')
