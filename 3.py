"""
队列
栈
"""

things_list = []
while True:
    action = input('input you type,add or do:')
    if action == 'add':
        t = input('input thing you want to do:')
        things_list.append(t)
    elif action == 'do':
        if len(things_list):
            to_do = things_list.pop(0)
            print(to_do)
        else:
            print('nothing')
    else:
        print('wrong action!!')
        break