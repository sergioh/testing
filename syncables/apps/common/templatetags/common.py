from django import template
from django.conf import settings

import hashlib
import logging
import os

register = template.Library()

@register.simple_tag
def static_url(path):
    """Returns url {{ STATIC_URL }}path?v=####"""
    if not hasattr(settings, '_STATIC_HASHES'):
        settings._STATIC_HASHES = {}
    hashes = settings._STATIC_HASHES
    if path not in hashes:
        try:
            f = open(os.path.join(settings.STATIC_ROOT, path))
            hashes[path] = hashlib.md5(f.read()).hexdigest()
            f.close()
        except:
            logging.error("Could not open static file %r", path)
            hashes[path] = None

    url = settings.STATIC_URL + path
    if hashes.get(path):
        return url + "?v=" + hashes[path][:5]
    else:
        return url
