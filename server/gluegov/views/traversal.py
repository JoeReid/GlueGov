from . import web, action_ok, action_error


@web
def test(request):
    print('test')
    #import pdb ; pdb.set_trace()
    return action_ok()


@web
def group(request):
    group = request.context
    return action_ok(data={'tables': {
        name: table.fields for name, table in group.tables.items()
    }})


@web
def table(request):
    table = request.context.table
    table = table.proccesQuery(request.query_string)
    return action_ok(data={'list': table.records})
