import os
import time
import socks
import socket
import subprocess

class TorManager(object):
    def __init__(self):
        self.devnull = open(os.devnull, 'w')
        self.n = '\033[0m'
        self.r = '\033[31m'
        self.g = '\033[32m'
        self.y = '\033[33m'
        self.b = '\033[34m'

    def installTor(self):
        subprocess.call(['clear'])
        print('{0}[{1}-{0}]{2} Installing Tor, Please Wait {3}...{2}'.format(self.y, self.r, self.n, self.g))
        time.sleep(3)
        cmd = ['apt-get', 'install', 'tor', '-y']
        subprocess.Popen(cmd, stdout=self.devnull, stderr=self.devnull).wait()

    def restartTor(self):
        cmd = ['service', 'tor', 'restart']
        subprocess.Popen(cmd, stdout=self.devnull, stderr=self.devnull).wait()
        time.sleep(.5)

    def stopTor(self):
        cmd = ['service', 'tor', 'stop']
        subprocess.Popen(cmd, stdout=self.devnull, stderr=self.devnull).wait()

    def startTor(self):
        print('{0}[{1}-{0}]{2} Starting Tor {3}...{2}'.format(self.r, self.g, self.n, self.y))
        cmd = ['service', 'tor', 'start']
        subprocess.Popen(cmd, stdout=self.devnull, stderr=self.devnull).wait()

    def updateIp(self):
        self.restartTor()
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9050, True)
        socket.socket = socks.socksocket

    def getIp(self):
        result = subprocess.run(['curl', 'https://wtfismyip.com/text'], stdout=subprocess.PIPE)
        ip = result.stdout.decode().strip()
        print('{0}[{1}-{0}]{2} Current IP: {3}{4}{2}'.format(self.r, self.g, self.n, self.b, ip))
        return ip
