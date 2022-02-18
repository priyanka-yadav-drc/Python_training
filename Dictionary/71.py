from operator import getitem
from functools import reduce

users = {
  'Carla': {
    'name': {
      'first': 'Carla ',
      'last': 'Russell' 
    },
    'postIds': [1, 2, 3, 4, 5]
  }
}

l=['Carla','name','last']
print(reduce(getitem,l,users))