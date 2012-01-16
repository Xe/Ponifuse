#Code inspired from dfiff

import os, sys, ponify, fuse, time
from fuse import Fuse

def gen_stats_from_real_file(fpath):
    res = PonifuseStat()
    
    #http://stackoverflow.com/questions/237079/how-to-get-file-creation-modification-date-times-in-python
    (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(fpath)
    
    res.st_mode = mode
    res.st_ino = ino
    res.st_dev = dev
    res.st_nlink = nlink
    res.st_uid = uid
    res.st_gid = gid
    res.st_size = size
    res.st_atime = atime
    res.st_mtime = mtime
    res.st_ctime = ctime
    
    return res

class PonifuseStat(fuse.Stat):
    """Pretty much verbatum from fdiff.py"""
    def __init__(self):
        self.st_mode = 0
        self.st_ino = 0
        self.st_dev = 0
        self.st_nlink = 0
        self.st_uid = 0
        self.st_gid = 0
        self.st_size = 0
        self.st_atime = 0
        self.st_mtime = 0
        self.st_ctime = 0

class Ponifuse(Fuse):
    def __init__(self, *args, **kw):
        Fuse.__init__(self, *args, **kw)
        
        self.mount_folder = "/home/sam/Mounts/ponifuse"
        self.source_folder = "/home/sam/Documents/nukable"
        
    def getattr(self, path):
        st = PonifuseStat()
        
        print path
        
        