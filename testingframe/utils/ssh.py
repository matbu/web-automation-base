#!/usr/bin/python -O
# -*- coding: utf-8 -*-
"""
    Product name: tools project
    Copyright (C) mbu 2013
    Author(s): Mathieu BULTEL
    Description : Ssh module for manage remote command via ssh protocol
"""

import stat
import posixpath
import time
try:
    import paramiko
except ImportError:
    raise ImportError('Importing paramiko SSH module or its dependencies failed. ')


class SshClient():
    """ use paramiko for emulate testing sshclient """
    enable_ssh_logging = staticmethod(lambda path: paramiko.util.log_to_file(path))

    chan = None

    def __init__(self, host, port=22, debug_file='sshclient.log'):
        """ Create instance of paramiko sshclient """
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        paramiko.util.log_to_file(debug_file)
        self.host = host
        self.port = port
        self.shell = None

    def ssh_connect(self, username, password, keyfile=None, mode=None):
        """  """
        try:
            if keyfile is None:
                self.client.connect(self.host, self.port, username, password)
            else:
                self.client.connect(self.host, self.port, username, password, key_filename=keyfile)
            return self._open_shell()
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
            return self._open_shell()
        except paramiko.AuthenticationException:
            print "Connection Failed"
            raise paramiko.AuthenticationException()

    def _open_shell(self):
        """ open a shell """
        if self.chan is None:
            self.chan = self.client.invoke_shell()
            return self.read()
        else:
            self.chan.get_pty()
            self.chan.invoke_shell()
            return self.read()

    def _purge_buffer(self, cmd):
        """ send a command in order to purge the buffer """
        self.write_text(cmd)
        return self.read_all()

    def close(self):
        """ close ssh connection """
        if self.client is None:
            self.chan.close()
        if self.chan is None:
            self.client.close()

    def execute_command(self, command, ret_mode):
        """
            execute command on a new channel, close the channel after
            executing this command.
            paramiko exec_command return a tuple of return values
        """
        _, stdout, stderr = self.client.exec_command(command)
        return self._read_command_output(stdout, stderr, ret_mode)

    def read_command_output(self, stdout, stderr, ret_mode):
        """ read output of a command, use this with exec_command function """
        return self._read_command_output(stdout, stderr, ret_mode)

    def _read_command_output(self, stdout, stderr, ret_mode):
        """ let you choose the return mode test case """
        if ret_mode.lower() == 'both':
            return stdout.read(), stderr.read()
        if ret_mode.lower() == 'stderr':
            return stderr.read()
        return stdout.read()

    def write(self, text, read=True):
        """ send data into a shell and append a newline """
        if self.chan.send_ready():
            byte = self.chan.send(text+'\n')
            time.sleep(3)
            if read:
                return self.read()

    def write_interactive(self, list_value, expected_lst, rd_byte=65, sleep=3):
        """
            write interactively on the channel,
            take a dictonary for the value and the expected values
            the value is the key and the expected value is the value
        """
        if isinstance(list_value,list):
            for i in range(len(list_value)):
                prompt = False
                if self.chan.send_ready():
                    byte = self.chan.send(list_value[i]+'\n')
                    time.sleep(sleep)
                    out = self.read_expected_value(expected_lst[i], sleep)
                    if out != None:
                        prompt = True
                    else:
                        print "exepected value don't corespond to srv prompt "+out+" and expected value "+expected_lst[i]
                        break
                        return out
                else:
                    print "channel are not ready"
                    return False
            return self.read_last(rd_byte)
        else:
            if self.chan.send_ready():
                byte = self.chan.send(list_value+'\n')
                time.sleep(sleep)
                out = self.read_last(rd_byte)
                if expected_lst in out:
                    print "the prompt match with the expected value"
                    return out
                else:
                    print "value : "+list_value+", prompt : "+expected_lst+"not found on the output", out
                    return out
            else:
                return False

    def read_expected_value(self, expected, timeout=6):
        """ read until expected partern appear """
        ret = ''
        start_time = time.time()
        while time.time() < float(timeout) + start_time:
            ret += self.read_char()
            if (isinstance(expected, basestring) and expected in ret) or \
               (not isinstance(expected, basestring) and expected.search(ret)):
                return ret
        if not isinstance(expected, basestring):
            expected = expected.pattern

    def read_all(self):
        """ read all data on the current output """
        data = ''
        while self.chan.recv_ready():
            data += unicode(self.chan.recv(1000000), errors='replace')
        return data

    def read(self):
        """ read data on the socket """
        data = ''
        while self.chan.recv_ready():
            data += unicode(self.chan.recv(5), errors='replace')
        return data

    def read_char(self):
        """ read char on the current output """
        if self.chan.recv_ready():
            return unicode(self.chan.recv(1), errors='replace')
        return ''

    def read_data(self, bytes):
        """ read data on the current output """
        data = ''
        if self.chan.recv_ready():
            data = unicode(self.chan.recv(bytes), errors='replace')
        return data

    def read_last(self, bytes):
        """ read last data on the current output """
        ret_data = ''
        data = []
        try:
            while self.chan.recv_ready():
                data += unicode(self.chan.recv(1000000), errors='replace')
            t_data = len(data)
            if t_data < bytes:
                for byte in range(t_data):
                    t_data = t_data - 1
                    ret_data += data[t_data]
                ret_data = ret_data[::-1]
            else:
                for byte in range(bytes):
                    t_data = t_data - 1
                    ret_data += data[t_data]
                ret_data = ret_data[::-1]
            return ret_data
        except Exception:
            print "Execption caught in read_last function"
            return ret_data

    def wait_recv_ready(self, timeout=600):
        """ wait until recv is ready (when recv ready return True) """
        start_time = time.time()
        while time.time() < float(timeout) + start_time and not unicode(self.chan.recv_ready(), errors='replace'):
            print "waiting..."
        return self.read_last(65)



# Refactoring :
# Factoriser : moins de methode : ex : le login faire le open shell ainsi que le purge buffer, ou le login retourne le contenu du buffer (message bienvenu ssh)
# Moins de methode read
# Write interractive : la rendre plus simple, la methode étant juste de lire le buffer sur la socket
