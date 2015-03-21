import pyramid
from functools import lru_cache


def GlobalRootFactory(request):
    return TraversalRoot(request)


class TraversalResource(object):
    def __init__(self, root, route=()):
        self.root = root
        self.route = route

    def __getitem__(self, key):
        print('__getitem__({0})'.format(key))
        raise KeyError

    @property
    def template(self):
        return 'home'  # Temp hack, needs further consideration


class TraversalRoot(TraversalResource):
    def __init__(self, request):
        self.request = request
