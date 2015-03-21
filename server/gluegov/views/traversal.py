from . import web, action_ok, action_error


@web
def test(request):
    #print('test')
    return action_ok()
