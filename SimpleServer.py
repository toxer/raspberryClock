
import cherrypy
import simplejson

songs = {
    '1': {
        'title': 'Lumberjack Song',
        'artist': 'Canadian Guard Choir'
    },

    '2': {
        'title': 'Always Look On the Bright Side of Life',
        'artist': 'Eric Idle'
    },

    '3': {
        'title': 'Spam Spam Spam',
        'artist': 'Monty Python'
    }
}

class Songs:
    exposed = True


    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def POST(self):
        input_json = cherrypy.request.json
        id = input_json["id"]
        if id == None:
            return('Here are all the songs we have: %s' % songs)
        elif id in songs:
            song = songs[id]
            return simplejson.dumps({'song':song['title']})
            #return('Song with the ID %s is called %s, and the artist is %s' % (id, song['title'], song['artist']))
        else:
            return('No song with the ID %s :-(' % id)

if __name__ == '__main__':

    cherrypy.tree.mount(
        Songs(), '/api/songs',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )
    cherrypy.config.update(
    {'server.socket_host': '0.0.0.0'} )
    cherrypy.engine.start()
    cherrypy.engine.block()
