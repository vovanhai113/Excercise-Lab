class Greeter(object):

   # def __init__(self, name):
   #    self.name = name

   def greet(self, loud=false):

      if loud:
         print ('HELLO, %s!' % self.name.upper())
      else:
         print ('HELLO, %s' % self.name)

g = Greeter('Fred')
g.greet()
g.greet(loud=true)
