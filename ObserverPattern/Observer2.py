# Once Publisher changes its state,
# now in respond to that all interested Subscriber can do the activity which they want (may be common one, may be different)

class SubscriberOne:
    def __init__(self,name):
        self.name=name

    def update(self,msg):
        print(msg,'=>',self.name)

class SubscriberTwo:
    def __init__(self,name):
        self.name=name

    def recieve(self,msg):
        print(msg,'=>',self.name)


class Publisher:
    def __init__(self):
        self.subscribers=dict()

    def register(self,subscriber,callbackfun=None):
        if callbackfun == None: callbackfun=subscriber.update
        self.subscribers[subscriber]=callbackfun

    def unregister(self,subscriber):
        if subscriber in self.subscribers:
            del self.subscribers[subscriber]

    def dispatchMsg(self,msg):
        for subscriber,callfunction in self.subscribers.items():
            callfunction(msg)


################################################3

pub=Publisher()
sub1=SubscriberOne('sumit')
sub2=SubscriberTwo('mayur')
sub22=SubscriberTwo('mayur2')
sub11=SubscriberOne('vikram')
pub.register(sub1)
pub.register(sub11,sub11.update)
pub.register(sub2,sub2.recieve)
#pub.register(sub22)
pub.dispatchMsg('Its lunch time!!')

