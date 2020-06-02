from appscript import *

iTunes = app('iTunes')
p = {'name':'Testing'}
playlist = iTunes.make(new=k.playlist, with_properties=p)
