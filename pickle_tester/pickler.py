import pickle
import sys

def list_pickler(my_list,file_name):
    f = open( file_name, "wb" )
    pickle.dump( my_list, f )
    #print "imported!"
    
def unpickler(file_name):
    f = open( file_name, "rb" )
    another_list = pickle.load( f )
    open( file_name, "rb" ).close()
    #print "imported!"
    return another_list