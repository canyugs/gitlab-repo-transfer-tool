import ConfigParser
import gitlab
import os

class Gitlab:

    def __init__(self, url=None, token=None):
        self.cfg_PATH = './auth.cfg'

        if url is None:
            if not os.path.exists(self.cfg_PATH):
                print 'Use create_config first!'
            config = ConfigParser.RawConfigParser()
            config.read(self.cfg_PATH)
            self.url = config.get('Auth', 'URL')
            self.token = config.get('Auth', 'Token')

        self.gl = self.connect(self.url, self.token)

    def connect(self, url, token):
        gl = gitlab.Gitlab(url, token)
        gl.auth()
        print
        print '========================'
        print 'Use for Auth'
        print 'URL: {}'.format(url)
        print 'Token: {}'.format(token)
        print '========================'
        print
        return gl

    def get_project_manager(self):
        self.pm = self.gl.projects
        return self.gl.projects

    def get_group_manager(self):
        self.gm = self.gl.groups
        return self.gl.groups

    def get_group_object(self, group_id):
        return self.get_group_manager().get(group_id)

    def show_all_groups(self):
        gm = self.get_group_manager()
        groups = gm.list(all=True)
        self.print_detail(groups)

    def show_group_projects(self, group_id):
        projects = self.gl.group_projects.list(group_id=group_id, all=True)
        self.print_detail(projects)

    def print_detail(self, object_list):
        print 'id-name'
        print '-----------------'
        for obj in object_list:
            print '{}-{}'.format(obj.id, obj.name)

    
