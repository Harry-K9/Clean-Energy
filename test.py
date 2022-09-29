import sys
import datetime

from Submit import output


time =datetime.datetime.now()

output="Hi %s current time is %s" %(sys.argv[1],time)

print(output)