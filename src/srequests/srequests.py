import scratchattach as scratch3
from scratchattach import Encoding
class SRequests():
    def __init__(self,username,password,project_id):
        session = scratch3.login(username, password)
        global conn
        conn = session.connect_cloud(project_id)
    class Request():
        def IsPending():
            responded = conn.get_var("_REQ_RESPONDED")
            if responded == "1":
                return False
            elif responded == "0":
                return True
            else:
                return None
        def GetName():
            data = Encoding.decode(conn.get_var("_REQ_NAME"))
            return data
        def GetContent():
            data = Encoding.decode(conn.get_var("_REQ_CONTENT"))
            return data
        def Respond(response):
            conn.set_var("_REQ_RESPONSE", Encoding.encode(response))
            conn.set_var("_REQ_RESPONDED", "1")
        class User():
            def GetData():
                name = Encoding.decode(conn.get_var("_REQ_USER"))
                return scratch3.get_user(name)
            def GetName():
                return Encoding.decode(conn.get_var("_REQ_USER"))