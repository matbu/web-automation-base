"""
Copyright 2011 Software Freedom Conservancy.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
__docformat__ = "restructuredtext en"

import stat
import posixpath
import time
try:
    import paramiko
except ImportError:
    raise ImportError('Importing paramiko SSH module or its dependencies failed. ')


class sshclient(object):
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

    # connection functions
    def connect(self, username, password):
        """ login to the remote server with sshclient"""
        try:
            self.client.connect(self.host, self.port, username, password)
        except paramiko.AuthenticationException:
            print "Connection Failed"
            raise paramiko.AuthenticationException()


    def set_transport(self, username, password):
        """
            create an instance of transport, open session and connect
            Open a channel in session mode.
            It's better to use transport class for interactive shell
        """
        try:
            self.transport = paramiko.Transport((self.host, self.port))
            self.transport.connect(None,username, password)
            self.chan = self.transport.open_channel("session")
        except paramiko.AuthenticationException:
            print "Connection Failed"
            raise paramiko.AuthenticationException()

    def login_with_public_key(self, username, keyfile, password):
        """ log to the remote server with a pub key """
        try:
            self.client.connect(self.host, self.port, username, password,
                                key_filename=keyfile)
        except paramiko.AuthenticationException:
            raise paramiko.AuthenticationException()

    def open_shell(self):
        """ open a shell without transport, don't call set_transport before """
        if self.chan is None:
            self.chan = self.client.invoke_shell()
            return self.chan
        else:
            self.chan.get_pty()
            return self.chan.invoke_shell()
        return False
    
    # close function
    def close(self):
        """ close ssh connection """
        if self.chan is None:
            self.client.close()
        else:
            self.chan.close()

    # write functions
    def write(self, cmd, read=True):
        """ send data into a shell and append a newline """
        if self.chan.send_ready():
            byte = self.chan.send(cmd+'\n')
            time.sleep(3)
            if read:
                return self.chan.recv(byte)
        return 'toto'

    # read channel functions

