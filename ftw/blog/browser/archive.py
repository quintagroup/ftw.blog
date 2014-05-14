from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from collections import OrderedDict
from zope.i18n import translate
from Products.CMFPlone.i18nl10n import monthname_msgid


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
            month_abbr = monthname_msgid(item.created.month())
            month = translate(month_abbr, 'plonelocales',
                              context=self.request, default=month_abbr)
            results.setdefault(year, OrderedDict()).setdefault(month, []).append(
                {'title': item.Title,
                 'date': item.created.strftime("%d/%m/%y"),
                 'url': item.getURL()})
        return results
