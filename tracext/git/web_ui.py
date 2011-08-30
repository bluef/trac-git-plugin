import json

from trac.core          import *
from trac.config        import Option
from trac.perm          import IPermissionRequestor, PermissionSystem
from trac.util.datefmt  import format_datetime, to_datetime
from trac.web.chrome    import ITemplateProvider, add_notice, \
                               add_stylesheet, add_warning
from trac.admin         import IAdminPanelProvider

class BranchAclAdminPage(Component):
    """docstring for BranchAclAdminPage"""
    
    implements(IAdminPanelProvider, ITemplateProvider, INavigationContributor)
    
    def __init__(self):
        self.git_repo = self.env.get_repository()
        pass
        
    # IAdminPanelProvider
    def get_admin_panels(self, req):
        """docstring for get_admin_panels"""
        pass
        
    def render_admin_panel(self, req, cat, page, path_info):
        """docstring for render_admin_panel"""
        if page == "acl"
            return self._do_acl(req)
            
    def _do_acl(self, req):
        acl_path = self.git_repo.gitrepo + "/acl"
        
        if req.method == "POST":
            if req.args.get("content"):
                acl_file = open(acl_path, "w")
                acl_file.write(req.args.get("content"))
            
        data['acl'] = open(acl_path).read()
        
        return 'admin_branches.html', data
        
    # ITemplateProvider methods
    def get_htdocs_dirs(self):
        """Return the absolute path of a directory containing additional
        static resources (such as images, style sheets, etc).
        """
        return [('acct_mgr', resource_filename(__name__, 'htdocs'))]

    def get_templates_dirs(self):
        """Return the absolute path of the directory containing the provided
        Genshi templates.
        """
        return [resource_filename(__name__, 'templates')]