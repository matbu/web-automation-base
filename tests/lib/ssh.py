
import stat
import posixpath
import time
try:
    import paramiko
except ImportError:
    raise ImportError('Importing paramiko SSH module or its dependencies failed. ')


class WSSHClient():
    """ use paramiko for emulate testing sshclient """
    enable_ssh_logging = staticmethod(lambda path: paramiko.util.log_to_file(path))

    def __init__(self, host, port=22, debug_file='sshclient.log'):
        """ Create instance of paramiko sshclient """
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        paramiko.util.log_to_file(debug_file)
        self.host = host
        self.port = port
        self.shell = None

    def login(self, username, password):
        """ login to the remote server with sshclient"""
        try:
            self.client.connect(self.host, self.port, username, password)
        except paramiko.AuthenticationException:
            print "Connection Failed"
            raise paramiko.AuthenticationException()



