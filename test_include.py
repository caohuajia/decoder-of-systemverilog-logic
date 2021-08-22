
def assign_input_var():
    return 'a = 1'

for i in range(2):
    exec(assign_input_var())
    print(a)