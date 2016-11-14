# Observing Events:
# one another feature added in observer pattern
# Now subscriber have freedom that they can register themselves with Publisher to :
  Do get notofied only on specific events and on that time they can do some specific activities..

class Subscriber:
    def __init__(self,name):
        self.name=name

    def eat(self,msg):
        print(self.name, ' ready to eat. :', msg)

    def notify(self,msg):
        print(self.name, 'get notifed :', msg)

    def freefood(self,msg):
        print(self.name, ' wants to eat, if food is free :',msg)

    def nutral(self,msg):
        print(self.name,' dont know what to do !!!')

class Publisher:
    def __init__(self,events):
        self.subscribers={ event : dict() for event in events }


    def register(self,event,subscriber,callbackfun=None):
        if event is None or subscriber is None:
            print('cant register')
            return -1
        if callbackfun == None:
            callbackfun=subscriber.nutral
        self.subscribers[event][subscriber]=callbackfun

    def unregister(self,event,subscriber):
        if subscriber in self.subscribers[event]:
            del self.subscribers[event][subscriber]

    def dispatchMsg(self,event,msg):
        for subscriber,callfunction in self.subscribers[event].items():
            callfunction(msg)

###########################################
# we have 3 types of events which we can publish:
pub = Publisher(['breakfast','lunch','dinner'])


# we have list of subscribers
sub1=Subscriber('sumit')
sub2=Subscriber('lammy')
sub3=Subscriber('soni')
sub4=Subscriber('jam')

#register subscribers
# for events which they wants
# for which acitivty they want to do once that event occur

pub.register('breakfast',sub1,sub1.eat)
pub.register('breakfast',sub2,sub2.eat)
pub.register('breakfast',sub3,sub3.freefood)

pub.register('lunch',sub4,sub4.notify)
pub.register('lunch',sub3,sub3.freefood)

pub.register('dinner',sub1)
pub.register('dinner',sub2,sub2.eat)


pub.dispatchMsg('lunch','Lets have LUNCH!!')
pub.dispatchMsg('breakfast','Lets have breakfast!!')
pub.dispatchMsg('dinner','Lets have dinner!!')

 
