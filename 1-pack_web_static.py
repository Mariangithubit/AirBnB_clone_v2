#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static folder """
from fabric.api import local
import time


def do_pack():
    """Generate tgz"""
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time.strftime("%Y%m%d%H%M%S")))
        return ("versions/web_static_{}.tgz".format(time.strftiem
                                                    ("%Y%m%d%H%M%S")))
    except:
        return None
