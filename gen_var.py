

def parse(tree,in_var,inter_var):
    op = tree[0]
    if op == '|':
        print(op)
    print('变量列表')
    for i,var in enumerate(in_var):
        print('{0:x{0}}{1:}'.format(i,var))
    print('')
    for i in tree[1:]:
        print('或项是',i)
        if len(i)==1:
            print('变量值')
            for var in in_var: ## 所有输入变量
                if var in i[0]:
                    print('1',end='')
                else:
                    print('-',end='')
            print('')
        else:
            continue
            print('式子')
