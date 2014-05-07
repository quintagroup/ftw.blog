from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.discussion.interfaces import IConversation
from ftw.blog.interfaces import IBlogEntryView
from ftw.tagging.interfaces.tagging import ITagRoot
from ftw.tagging.utils import getInterfaceRoot
from zope.component import getMultiAdapter
from zope.interface import implements
from Products.CMFCore.utils import getToolByName


class BlogEntryView(BrowserView):
    """ The Blog entry detail View. """

    implements(IBlogEntryView)

    template = ViewPageTemplateFile("entry.pt")

    def __init__(self, *args, **kwargs):
        super(BlogEntryView, self).__init__(*args, **kwargs)
        self.tag_root = None

    def __call__(self):
        self.tag_root = getInterfaceRoot(self.context, ITagRoot)
        return self.template()

    def show_images(self):
        return self.context.getShowImages()

    def show_lead_image(self):
        return self.context.getLeadimage() and self.context.showLeadImage()

    def comments_enabled(self):
        conversation = getMultiAdapter((self.context, self.request),
                                       name='conversation_view')
        return conversation.enabled()

    def amount_of_replies(self):
        conversation = IConversation(self.context)
        return len([thread for thread in conversation.getThreads()])

    def get_same_author_blog_entries(self):
        catalog = getToolByName(self.context, 'portal_catalog')
        query = {
            'portal_type': 'BlogEntry',
            'Creator': self.context.Creator()}
        results = catalog.searchResults(query)
        uid = self.context.UID()
        return list(item.getObject() for item in results if item.UID != uid)
