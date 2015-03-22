from externals.lib.misc import decorator_combine
from externals.lib.pyramid_helpers.auto_format import auto_format_output, action_ok, action_error

__all__ = [
    'web', 'action_ok', 'action_error',
]


def allow_cors(func):
    def inner(request, **kwargs):
        request.response.headerlist.extend([('Access-Control-Allow-Origin', '*')])
        return func(request, **kwargs)
    return inner

web = decorator_combine(
    allow_cors,
    auto_format_output,
)


