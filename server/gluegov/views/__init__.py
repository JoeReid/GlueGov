from externals.lib.misc import decorator_combine

from externals.lib.pyramid_helpers.auto_format import auto_format_output, action_ok, action_error

__all__ = [
    'web', 'action_ok', 'action_error',
]

web = decorator_combine(
    auto_format_output,
)


