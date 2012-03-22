import os
import shutil
import Image

# please set the relative path here
srcdir = '../TiebaImageStore'
dstdir = '../TiebaAnimaStore'


pathname = os.path.dirname(os.path.realpath( __file__ ))

srcdir = os.path.join(pathname, srcdir)
dstdir = os.path.join(pathname, dstdir)

srcdir = os.path.abspath(srcdir)
dstdir = os.path.abspath(dstdir)

print 'src dir: %s' % srcdir
print 'dst dir: %s' % dstdir


if (srcdir in dstdir) or (dstdir in srcdir):
    print 'The dirs should not be intersected!'
    exit(1)

if not os.path.exists(srcdir):
    print 'src dir: %s , not exit!' % srcdir
    exit(1)

     
if not os.path.exists(dstdir):
    print 'dst dir: %s , not exit,' % dstdir
    print 'create...'
    os.makedirs(dstdir)

def _check_animation(file):
    try:
        im = Image.open(file)
        im.seek(1) # skip to the second frame
    except:
        #not even a image file
        return False
    try:
        im.seek(im.tell()+1)
    except EOFError:
        return False # no 2nd sequence
    return True

count = 0
copy_list = []
for dirname, dirnames, filenames in os.walk(srcdir):
    for subdirname in dirnames:
        print os.path.join(dirname, subdirname)
    for filename in filenames:
        absfile = os.path.join(dirname, filename)     
        if _check_animation(absfile):
            shutil.copyfile(absfile, os.path.join(dstdir, filename))
            copy_list.append(filename)
            count = count+1

print('process over. %d files copied:' % count)
for i, afile in enumerate(copy_list):
  if (i % 100 < 10):
      print '[%d] %s' % (i, afile)
  elif (i % 100 == 10):
      print('......')


          
