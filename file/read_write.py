with open("readsrc.txt",'r+') as read_write:
    print("readbility status :",read_write.readable())
    print("readbility status :",read_write.writable())
    read_write.write("OHHHH LALALALALasdasd asdas")