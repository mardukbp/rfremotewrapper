from os.path import realpath
from pathlib import Path
import subprocess
import time
import sys

from robot.libraries.Remote import Remote
from robot.api.logger import logging

RemoteServer_path = Path(realpath(__file__)).parent / "lib" / "jrobotremoteserver.jar"

class JavaRemote:
    ROBOT_LIBRARY_SCOPE='GLOBAL'

    def __init__(self, library_name, port="8270"):
        self.url = f"http://127.0.0.1:{port}/"

        proc = subprocess.Popen(["java", "-jar", RemoteServer_path, "-p", port, "-l", library_name], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    
        time.sleep(0.3)
        returncode = proc.poll()

        if returncode and returncode > 0:
            message, details = [line.decode('iso-8859-1').strip() for line in proc.stdout.readlines()]
            logging.error(f"{message} {details}")
            sys.exit(1)

        self.Remote = Remote(self.url)

    def get_keyword_arguments(self, name):
        return self.Remote.get_keyword_arguments(name)

    def get_keyword_names(self):
        return self.Remote.get_keyword_names()

    def get_keyword_documentation(self, name):
        return self.Remote.get_keyword_documentation(name)

    def get_keyword_types(self, name):
        return self.Remote.get_keyword_types(name)

    def run_keyword(self, name, args, kwargs):
        return self.Remote.run_keyword(name, args, kwargs)
