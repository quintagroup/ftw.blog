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


class BlogAuthorPortletAddForm(base.NullAddForm):

    def create(self):
        return BlogAuthorPortletAssignment()
