#!/usr/bin/python3
"""deploy """
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """generates a .tgz archive from the contents of the
    web_static folder of your AirBnB Clone repo
    """
    date_t = datetime.now().strftime("%Y%m%d%H%M%S")
    if os.path.isdir("versions") is False:
        if local("mkdir versions").failed is True:
            return None
    file_name = "versions/web_static_{}.tgz".format(date_t)
    if local("tar -cvzf {} web_static".format(file_name)).failed is True:
        return None
    return file_name
