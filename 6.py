def oper_file(file_name):
    res = {}
    with open(file_name) as f:
        for line in f:
            tmp = line.split(' ')
            ip, url = tmp[0], tmp[6]
            res[(ip, url)] = res.get((ip, url), 0) + 1
    return sorted(res.items(), key=lambda x: x[1], reverse=True)


def get_html(arr):
    tmpl = '<tr><td>No%s</td> <td>%s</td><td>%s</td><td>%s</td></tr>'
    html_str = '<h1>IP COUNT TABLE</h1>'
    html_str += '<table border="1px">'
    html_str += tmpl % (' ', 'IP', 'URL', 'COUNT')
    for index, value in enumerate(arr[:10]):
        html_str += tmpl % (index, value[0][0], value[0][1], value[1])

    html_str += '</table>'
    return html_str


def start_operate(file_name):
    res = oper_file(file_name)
    with open('res.html', 'w') as f:
        f.write(get_html(res))
    f.close()
    print(res)


start_operate('log1.log')