import os

fl = open("/var/log/messages", "r")
fw = open("/root/spse2.txt", "w")

for line in fl.readlines():
    
    if line.find("usb") != -1:

        fw.write(line + "/n")
        print "writing message to file"

fl.close()
fw.close()


    
     

    
    
