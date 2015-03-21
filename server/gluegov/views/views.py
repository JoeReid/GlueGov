from pyramid.view import view_config

from . import web, action_ok, action_error


@view_config(route_name='home')
@web
def my_view(request):
    return action_ok(data={'project': 'GlueGov'})
