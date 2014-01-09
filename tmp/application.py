from objectpub import ObjectPublisher

class Root(object):

    # The "index" method:
    def __call__(self):
        return '''
        <form action="welcome">
        Name: <input type="text" name="name">
        <input type="submit">
        </form>
        '''

    def welcome(self, name):
        return 'Hello %s!' % name

app = ObjectPublisher(Root())

if __name__ == '__main__':
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8080')
