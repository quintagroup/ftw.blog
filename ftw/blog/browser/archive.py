from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from collections import OrderedDict


class ArchiveView(BrowserView):

    def items(self):
        portal_catalog = getToolByName(self.context, 'portal_catalog')
        query = {
            'portal_type': 'BlogEntry',
            'sort_on': 'created',
            'sort_order': 'reverse'}
        results = OrderedDict()
        for item in portal_catalog.searchResults(query):
            year = item.created.year()
            month = item.created.Month()
            results.setdefault(year, OrderedDict()).setdefault(month, []).append(
                {'title': item.Title,
                 'date': item.created.strftime("%d/%m/%y"),
                 'url': item.getURL()})
        return results
