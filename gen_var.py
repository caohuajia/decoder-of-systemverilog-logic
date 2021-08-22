results = []
result = {}
def add_result(_result):
    results.append(_result)


def parse(tree,in_var,inter_var):
    print('解析的tree', tree)
    op = tree[0]
    if op == '|':
        for i in tree[1:]:
            # print('或项是',i)
            if len(i)==1:  ## 是个变量
                # print('变量值')
                for var in in_var: ## 所有输入变量
                    if var in i[0]:
                        if ('~' in i[0]) or ('!' in i[0]):
                            result[i[0]] = 0
                        else:
                            result[i[0]] = 1
                break
            else:
                parse(i,in_var,inter_var)
                # continue
                # print('式子')

    if op == '&':
        for i in tree[1:]:
            if len(i)==1:
                for var in in_var: ## 所有输入变量
                    if var in i[0]:
                        if ('~' in i[0]) or ('!' in i[0]):
                            print('0',end='')
                        else:
                            print('1',end='')
                    else:
                        print('-',end='')
                print('')
            else:
                continue
                print('式子')

    if op == '0':
        for i in tree[1:]:
            parse(i,in_var,inter_var)

