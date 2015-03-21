from gluegov.lib.tables import TableDownloadMixin


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


class TableNameResorce(object):
    def __init__(self, request, group, name):
        self.request = request
        self.group = group
        self.name = name
        #import pdb ; pdb.set_trace()

    @property
    def table(self):
        return TableDownloadMixin.registry[self.group][self.name]

    @property
    def template(self):
        return 'home'  # TODO: could be made to look at the Table object .. could be a param like that


class TableGroupResource(object):
    def __init__(self, request, group):
        self.request = request
        self.group = group

    def __getitem__(self, name):
        TableDownloadMixin.registry[self.group][name]  # Will raise KeyError if group not exisit
        return TableNameResorce(self.request, self.group, name)


class TraversalRoot(TraversalResource):
    def __init__(self, request):
        self.request = request

    def __getitem__(self, group):
        TableDownloadMixin.registry[group]  # Will raise KeyError if group not exisit
        return TableGroupResource(self.request, group)
