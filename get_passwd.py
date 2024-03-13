from subprocess import check_output, CalledProcessError
from argparse import ArgumentParser
from rich import print
from constants import constants

class GetWifiPass:
    def __init__(self) -> None:
        PARSER = ArgumentParser(description='vasco')
        PARSER.add_argument('-n', '--network', help='Enter network name')
        self.ARGS = PARSER.parse_args()
        self.commands = ['netsh', 'wlan', 'show', 'profiles', self.ARGS.network, 'key', '=', 'clear']

    def get_senhas(self):
        if (self.ARGS.network is None): return constants.MSG
        try:  
            _get_network = check_output(self.commands, encoding='cp860')
            for _net in _get_network.split('\n'):
                if 'Conteúdo da Chave' in _net:
                    passwd = _net[_net.find(':')+2:]
                    return f'Senha de {self.ARGS.network}: [green]{passwd}[/]'
        except CalledProcessError:
            return f'[red][!] A rede "{self.ARGS.network}" não existe neste computador[/]'

if __name__ == '__main__':
    _get = GetWifiPass()
    if _get.get_senhas() is not None:
        print(_get.get_senhas())