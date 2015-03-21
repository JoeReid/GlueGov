from . import web, action_ok, action_error


@web
def test(request):
    print('test')
    #import pdb ; pdb.set_trace()
    return action_ok()


@web
def group(request):
    group = request.context
    return action_ok(data={
        'group': group.group,
        'tables': {
            name: table.fields for name, table in group.tables.items()
        }
    })


@web
def table(request):
    table = request.context.table
    table = table.proccesQuery(request.query_string)

    records = table.records
    total = len(records)
    limit = int(request.params.get('limit', request.registry.settings.get('gluegov.api.default_limit')))
    offset = int(request.params.get('offset', 0))

    return action_ok(data={
        'list': records[offset:offset + limit],
        'total': total,
        'offset': offset,
        'limit': limit,
    })
