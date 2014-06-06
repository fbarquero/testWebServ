# coding: utf8
# try something like
def index():
    return dict(message="hello from apiWebService.py")

def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@service.soap('myName',returns={'result':str},args={'a':str,})
def my_name_is(a):
    return "my Name is %s" % (a)
