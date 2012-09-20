from tasks import celery
from tasks import add
import time

results = []

print "Submitting job 1"
results.append(add.delay(3,1))

print "Submitting job 2"
results.append(add.delay(3,2))

print "Submitting job 3"
results.append(add.delay(3,3))

for ares in results:
    print "Getting results ", ares.id
    a =  ares.get()
    print a
    
print "All Done"
