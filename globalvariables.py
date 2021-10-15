x = "awesome"

def calllocalwithglobal():
  x = " calllocalwithglobal " 
  global y 
  y = "global" 
  print("Python is " + x + y )

def myfunc():
  print("Python is " + x + y)


def calllocal():
  x = " calllocal "  
  print("Python is " + x  + y)


calllocalwithglobal()
calllocal()
myfunc()