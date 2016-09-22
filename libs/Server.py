import cherrypy
import simplejson


class UpdateNtp:
    exposed = True
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def POST(self):
        input_json = cherrypy.request.json
        print("REQUEST")
        print(input_json["id"])


class ClockServer:
    def __init__(self,port,clockMaster):
        self.clockMaster = clockMaster
        cherrypy.tree.mount(
            UpdateNtp(), '/api/clock/udpateNtp',
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
