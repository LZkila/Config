import os

install_list = [ \
    'apt install autoconf automake libtool -y', \
    'apt install boxes -y', \
    'apt install cheat -y', \
    'apt install cmake -y', \
    'apt install cowsay -y', \
    'apt install fortunes-min fortune-mod fortunes-zh -y', \
    'apt install g++ -y', \
    'apt install moreutils -y', \
    'apt install neovim -y', \
    'apt install npm -y', \
    'apt install pick -y', \
    'apt install proxychains4 -y', \
    'apt install python3-pip -y', \
    'apt install rpm -y', \
    'apt install samba -y', \
    'apt install shadowsocks -y', \
    'apt install subversion -y', \
    'apt install unzip -y' \
    'apt install vsftpd -y' \
    'apt install w3m -y', \
    'apt install zsh -y' \
    ]

for i in install_list:
    #print(i)
    os.system('{}'.format(i))

