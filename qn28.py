#dumps and loads

#dumps: is used to convert python object into json format. used to serialize python object.

import json 
a = {"a":"diwas", "b":"softwarica"}
d = json.dumps(a)
print(d,type(d))


#loads: is used to convert json format back to python object. used to deseralize python object.
import json
a = '{"a":"diwas", "b":"coventry"}'
d = json.loads(a)
print(d,type(a))
