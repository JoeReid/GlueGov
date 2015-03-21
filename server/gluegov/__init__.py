import re
from pyramid.config import Configurator
import pyramid.events
from pyramid.session import SignedCookieSessionFactory

from .traversal import GlobalRootFactory

from externals.lib.misc import convert_str_with_type, extract_subkeys, json_serializer
from externals.lib.pyramid_helpers.auto_format import registered_formats

import logging
log = logging.getLogger(__name__)

# Package Imports
from .templates import helpers as template_helpers


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings, root_factory=GlobalRootFactory)
    config.include('pyramid_mako')

    # Parse/Convert setting keys that have specifyed datatypes
    for key in config.registry.settings.keys():
        config.registry.settings[key] = convert_str_with_type(config.registry.settings[key])

    # Session Manager
    session_settings = extract_subkeys(config.registry.settings, 'session.')
    session_factory = SignedCookieSessionFactory(serializer=json_serializer, **session_settings)
    config.set_session_factory(session_factory)

    # Routes
    def append_format_pattern(route):
        return re.sub(r'{(.*)}', r'{\1:[^/\.]+}', route) + r'{spacer:[.]?}{format:(%s)?}' % '|'.join(registered_formats())

    config.add_static_view('static', 'static', cache_max_age=3600)

    #config.add_route('home', append_format_pattern('/'))
    config.add_view('gluegov.views.traversal.test', context='gluegov.traversal.TraversalResource')

    config.add_subscriber(add_render_globals_to_template, pyramid.events.BeforeRender)

    config.scan()
    return config.make_wsgi_app()


def add_render_globals_to_template(event):
    event['h'] = template_helpers
