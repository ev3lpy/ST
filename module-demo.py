#!/usr/bin/python

import calculator



ins = calculator.Calculator(5,2)
print "%d" % ins.add()
print "%d" % ins.mul()

ins = calculator.Scientific(2,5)

print "%d" % ins.power()
 
print "QuickAdd %d:" % calculator.quickAdd(5,5)




