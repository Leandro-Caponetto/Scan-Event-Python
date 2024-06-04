import win32evtlog
from tkinter import messagebox

class EventLogViewer:
    def __init__(self):
        self.events = {
            "Create Service": [7030, 7045],
            "Create User": [4720, 4722, 4724, 4728],
            "Add user to Group": [4732],
            "Clear Event Log": [1102],
            "Create RDP Certificate": [1056],
            "Insert USB": [7045, 10000, 10001, 10100, 20001, 20002, 20003, 24576, 24577, 24579],
            "Disable Firewall": [2003],
            "Applocker": [8003, 8004, 8006, 8007],
            "EMET": [2],
            "Logon Failed": [4625],
            "Service terminated unexpectedly": [7034],
            "A service was installed in the system": [4697],
            "User Account Locked Out": [4740],
            "User Account Unlocked Out": [4767],
            "File Access / Deletion": [4663, 4659, 4660],
            "Terminal service session reconnected": [4779],
            "User Initiated Logoff": [4647],
            "A directory service object was modified": [5137],
            "Permission change with ald & new attributes": [4670],
            "Service Start Type Change (disabled, monual. Automatic)": [7040],
            "Service Start / Stop": [7036]
            
        }
        self.logType = "Security"
        self.hand = None
        
        def connect_log(self):
            self.hand = win32evtlog.OpenEventLog(None, self.logType)
        
        def disconnect_log(self):
            if self.hand:
                win32evtlog.CloseEventLog(self.hand)
        
        def read_events(self): 
            while True:
                events = win32evtlog.ReadEventLog(self.hand, win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ, 0)   
                for event in events:
                    event_type = next((type for type, ids in self.events.items() if event.EventID in ids), None)
                    if event_type:
                        messagebox.showerror(f"Event ID: {event.EventID}", f"{event.TimeGenerated}: Evento sospechoso encontrado: {event_type}")
                if not events:
                    break
                
log_events = EventLogViewer()
log_events.connect_log()   
log_events.read_events()
log_events.disconnect_log()                     