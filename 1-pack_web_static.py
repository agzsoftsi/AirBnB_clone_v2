#!/usr/bin/python3
"""Task 1 - Deploy archive - Write a Fabric script"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """ Generate a .tgz archive from the contents of the web_static folder """
    time = datetime.now()
    name = 'web_static_' + str(time.year) + str(time.month) + str(time.day)
    name = name + str(time.hour) + str(time.minute) + str(time.second) + '.tgz'
    local('mkdir -p versions')
    archive = local('tar -cvzf versions/{} web_static'.format(name))
    if archive.failed:
        return None
    return 'versions/{}'.format(name)
