import os

config_list = [ \
    'ln -s /usr/bin/nvim /usr/bin/v', \
    'ln -s /usr/bin/proxychains4 /usr/bin/proxy', \
    'ln -s /usr/bin/pip3 /usr/bin/pip', \
    'ln -s /usr/bin/python3 /usr/bin/py', \
    'ln -s /usr/bin/python3 /usr/bin/python' \
    ]


for i in config_list:
    #print(i)
    os.system('{}'.format(i))

