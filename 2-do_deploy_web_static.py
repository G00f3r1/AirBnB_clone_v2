#!/usr/bin/python3
"""deploy """
from datetime import datetime
from fabric.api import local
from fabric.api import get
from fabric.api import put
from fabric.api import env
from fabric.api import run
import os
env.hosts = ['34.148.139.135', '34.236.36.206']


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


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if os.path.exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except Exception:
        return False
