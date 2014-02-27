from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName


class ContributorsView(BrowserView):
    """ The Blog Contributors View. """

    def getContributors(self):
        catalog = getToolByName(self.context, 'portal_catalog')
        query = {'portal_type': 'BlogEntry',
                 'path': '/'.join(self.context.getPhysicalPath())}

        return {blog_entry.Creator for blog_entry in catalog(query)}

