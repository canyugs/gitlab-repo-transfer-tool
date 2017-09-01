import sys

from gl import Gitlab

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print 'Usage: Copy new project in Tera Group'
        print '     ' + sys.argv[0] + ' <project_name>'
        sys.exit()
    name = sys.argv[1]
 
    new_gl = Gitlab('https://code.hopebaytech.com', 'L8J74_FpxjeeVXYGynEz')
    new_gl.get_project_manager()
    # 5 = Tera
    
    data = {'name': name, 'namespace_id': 5}
    new_gl.pm.create(data)
    print 'project {} created in group {}'.format(name, 'Tera')
