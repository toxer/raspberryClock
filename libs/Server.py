import cherrypy
import simplejson


class UpdateNtp:
    exposed = True
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def POST(self):
        self.clockMaster.updateNtp();

class KillServer:
    def __init__(self,clockMaster):
        self.clockMaster=clockMaster
    exposed = True
    def GET(self):
        self.clockMaster.killServer();

class ClockServer:
    def __init__(self,port,clockMaster):
        self.clockMaster = clockMaster
        cherrypy.tree.mount(
            UpdateNtp(), '/api/clock/udpateNtp',
            {'/':
                {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
            }
        )
        cherrypy.tree.mount(
            KillServer(self.clockMaster), '/api/clock/killServer',
            {'/':
                {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
            }
        )
        cherrypy.config.update(
        {'server.socket_host': '0.0.0.0','server.socket_port':port} )

    def start(self):
        cherrypy.engine.start()
        print("Clock server started")

    def stop(self):
        cherrypy.engine.stop()
        print("Clock server stoped")

if __name__ == '__main__':
    clockServer = ClockServer(9090)
    clockServer.start()
    cherrypy.engine.block()
