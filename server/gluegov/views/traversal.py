from . import web, action_ok, action_error


@web
def test(request):
    print('test')
    #import pdb ; pdb.set_trace()
    return action_ok()
