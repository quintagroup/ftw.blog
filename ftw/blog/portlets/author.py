# Author portlet
from zope.interface import implements
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base
from ftw.blog.interfaces import IBlogEntry
from Products.CMFCore.utils import getToolByName


class IBlogAuthorPortlet(IPortletDataProvider):
    """A portlet which can render blog author portlet.
    """


class BlogAuthorPortletAssignment(base.Assignment):
    implements(IBlogAuthorPortlet)


class BlogAuthorPortletRenderer(base.Renderer):

    render = ViewPageTemplateFile('author.pt')

    @property
    def show(self):
        if IBlogEntry.providedBy(self.context):
            return True
        return False

    def getCreator(self):
        mtool = getToolByName(self.context, 'portal_membership')
        return mtool.getMemberById(self.context.Creator())

    def getPortrait(self, member_id):
        mtool = getToolByName(self.context, 'portal_membership')
        return mtool.getPersonalPortrait(member_id)


class BlogAuthorPortletAddForm(base.NullAddForm):

    def create(self):
        return BlogAuthorPortletAssignment()
