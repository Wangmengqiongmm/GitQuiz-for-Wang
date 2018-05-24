#学长，这些是我自己捏造的.
class Screen(object):
   @property
   def width(self): 
       return self._width
    def height(self):
    	return self._width
    
    @width.setter
    def width(self.value):
    	self._width=value
    	
    @height.setter
    def height(self.value):
    	self._height=value
    	
    @resolution.setter
      self._resolution=1024*1208 
    	
def main():
	s = Screen()
	s.width=1208
	s.height=1024
	print(s.resolution)
   
