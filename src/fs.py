#Code inspired from dfiff

import os, sys, ponify, fuse, time
from fuse import Fuse

fuse.fuse_python_api = (0, 2)

source_folder = "/home/sam/Documents/nukable"

def is_ignored(path):
    ignored = None
    
    try:
        ignored = open(os.path.join(source_folder, ".ponyignore"), "r").read()
    except IOError as e:
        print "No .ponyignore, adding one"
        ignored = open(os.path.join(source_folder, ".ponyignore"), "w")
        ignored.write(".c\n.py\n.pl\n.java\n.clj\n.javac\n.exe\n")
    
    if path in ignored:
        return True
    else:
        return False

def listdir_fullpath(d):
    #http://stackoverflow.com/questions/120656/directory-listing-in-python
    return [os.path.join(d, f) for f in os.listdir(d)]

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
    """Pretty much verbatum from fdiff.py, as there is no other way to do it"""
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
        st = gen_stats_from_real_file(os.join(self.source_folder, path))
        
        print path
        
        return st
    
    def readdir(self, path, offset):
        dirents = [ '.', '..' ]
        
        dirents.extend(listdir_fullpath(os.join(self.source_folder, path)))
        
        for r in dirents:
            yield fuse.Direntry(r)
    
    def mknod(self, path, mode, dev):
        pass
    
    
def main():
    
    usage = """
Ponify files transparently.

""" + Fuse.fusage

    server = Ponifuse(version="%prog " + fuse.__version__,
                 usage=usage,
                 dash_s_do='setsingle')

    server.parser.add_option(mountopt="root", metavar="PATH", default='/',
     help="mirror filesystem from under PATH [default: %default]")
    server.parse(values=server, errex=1)

    try:
        if server.fuse_args.mount_expected():
            os.chdir(server.root)
    except OSError:
        print >> sys.stderr, "can't enter root of underlying filesystem"
        sys.exit(1)

    server.main()


if __name__ == '__main__':
    main()