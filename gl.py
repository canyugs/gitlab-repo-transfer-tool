import gitlab

class Gitlab:

    def __init__(self, url, token):
        self.url = url
        self.token = token
        self.gl = self.connect(self.url, self.token)

    def connect(self, url, token):
        gl = gitlab.Gitlab(url, token)
        gl.auth()
        return gl

    def get_project_manager(self):
        self.pm = self.gl.projects
        return self.gl.projects

    def get_group_manager(self):
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
        for obj in object_list:
            print '{}-{}'.format(obj.id, obj.name)

    
