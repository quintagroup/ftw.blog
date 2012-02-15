from plone.app.upgrade.utils import loadMigrationProfile
from Products.CMFCore.utils import getToolByName
from zope.annotation.interfaces import IAnnotations

import logging
logger = logging.getLogger('ftw.blog')


def upgrade_to_v2(context):
    """Updates profile
    """
    ppcas = 'plone.portlets.contextassignments'
    catalog = getToolByName(context, 'portal_catalog')
    count = 0
    for brain in catalog(portal_type=['BlogEntry', 'BlogCategory', 'Blog']):
        obj = brain.getObject()
        annotations = IAnnotations(obj)
        if ppcas in annotations.keys():
            if 'blog.portlets' in annotations[ppcas]:
                count += 1
                if len(annotations[ppcas]) == 1:
                    del annotations[ppcas]
                else:
                    del annotations[ppcas]['blog.portlets']

    logger.info("%s %s annotations removed" % (str(count), ppcas))
    loadMigrationProfile(context, 'profile-ftw.blog:to_v2')
