from gluegov.lib.tables import TableDownloadMixin


def GlobalRootFactory(request):
    return TraversalRoot(request)


class TableResource(object):
    def __init__(self, request, group, name):
        self.request = request
        self.group = group
        self.name = name

    @property
    def table(self):
        return TableDownloadMixin.registry[self.group][self.name]

    @property
    def template(self):
        return 'table'  # TODO: could be made to look at the Table object .. could be a param like that


class TableGroupResource(object):
    def __init__(self, request, group):
        self.request = request
        self.group = group

    def __getitem__(self, name):
        TableDownloadMixin.registry[self.group][name]  # Will raise KeyError if group not exisit
        return TableResource(self.request, self.group, name)

    @property
    def tables(self):
        return TableDownloadMixin.registry[self.group]

    @property
    def template(self):
        return 'group'


class TraversalRoot(object):
    def __init__(self, request):
        self.request = request

    def __getitem__(self, group):
        TableDownloadMixin.registry[group]  # Will raise KeyError if group not exisit
        return TableGroupResource(self.request, group)
