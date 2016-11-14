class Subscriber:
    def __init__(self,name):
        self.name=name

    def update(self,msg):
        print(msg,'=>',self.name)

class Publisher:
    def __init__(self):
        self.subscribers=list()

    def register(self,subscriber):
        self.subscribers.append(subscriber)

    def unregiser(self,subscriber):
        self.subscribers.remove(subscriber)

    def dispatchMsg(self,msg):
        for subscriber in self.subscribers:
            subscriber.update(msg)

######################################################


pub=Publisher()
sub1=Subscriber('sumit')
sub2=Subscriber('mayur')
pub.register(sub1)
pub.register(sub2)
pub.dispatchMsg('its snacks time!')
pub.unregiser(sub2)
pub.dispatchMsg('Time over for you!')
