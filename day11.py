def  log_event(event_type, *args, **kwargs):
    if not isinstance (event_type, str):
        return "Event type should be string"
    if len (args) <=0:
        return "Provide at least one message"
    if kwargs.get ('priority')== "high":
        kwargs ['alert']= True

    return {
        "type": event_type,
        "message": list (args),
        "meta": kwargs
    }

    
print (log_event (
    1,
    "name r is not defined",
    "type error cannot add str and int",
    timestamp = "2022-02-02",
    user = "root",
    priority = "low"
))

print (log_event(
    "Success",
    timestamp="2022-02-02",
    user="root",
    priority="low"
))

#RECURSION
#1.
def test ():
    print ("This is Recursion")
    test ()
test ()

#2.
def test ():
    print ("This is Recursion")
    return test ()
test ()
