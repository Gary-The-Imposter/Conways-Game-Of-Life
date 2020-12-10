import pygame
import random

def conwayATOM(_point,_state):
        test = False
        connectedalive = 0
        if _state[(bordercheck(_point[0]-1),bordercheck(_point[1]-1))]:
            connectedalive += 1
        if _state[(bordercheck(_point[0]-1),bordercheck(_point[1]))]:
            connectedalive += 1
        if _state[(bordercheck(_point[0]-1),bordercheck(_point[1]+1))]:
            connectedalive += 1
        if _state[(bordercheck(_point[0]),bordercheck(_point[1]-1))]:
            connectedalive += 1
        if _state[(bordercheck(_point[0]),bordercheck(_point[1]+1))]:
            connectedalive += 1
        if _state[(bordercheck(_point[0]+1),bordercheck(_point[1]-1))]:
            connectedalive += 1
        if _state[(bordercheck(_point[0]+1),bordercheck(_point[1]))]:
            connectedalive += 1
        if _state[(bordercheck(_point[0]+1),bordercheck(_point[1]+1))]:
            connectedalive += 1
        if not _state[(_point[0],_point[1])] and connectedalive < 3:
            test = False
        if _state[(_point[0],_point[1])] and connectedalive < 2:
            test = False
        if _state[(_point[0],_point[1])] and connectedalive == 2:
            test = True
        if _state[(_point[0],_point[1])] and connectedalive == 3:
            test = True
        if _state[(_point[0],_point[1])] and connectedalive > 3:
            test = False
        if not _state[(_point[0],_point[1])] and connectedalive == 3:
            test = True
        return test

def bordercheck(_point):
    if _point == 50:
        return 0
    if _point == -1:
        return 49
    else:
        return _point

def main():
  pygame.init()
  win = pygame.display.set_mode((500,500))
  pygame.display.set_caption("Conway's Game Of Life")

  grid = []
  for x in range(0,50,1):
       for y in range(0,50,1):
           grid.append((x,y))

  state_list = [True,False]

  base = []
  for item in range(2500):
          base.append(random.choice(state_list))

  conway_dict = []
  for idx,item in enumerate(grid):
      conway_dict.append(item)
      conway_dict.append(base[idx])
  it = iter(conway_dict)
  res_dct = dict(zip(it,it))

  conway_dict2 = []
  for idx,item in enumerate(grid):
      conway_dict2.append(item)
      conway_dict2.append(base[idx])
  it = iter(conway_dict2)
  res_dct2 = dict(zip(it,it))
  
  namelist = []
  for x in range(50):
       for y in range(50):
           namelist.append((x,y))

  square_dict = {}
  for num in namelist:
      square_dict[num]={'x':0,'y':0,'w':10,'h':10}
      
  x = 0
  y = 0

  for item in square_dict:
      square_dict[item]['x']=x
      square_dict[item]['y']=y
      x+=10
      if x == 500:
          x = 0
          y+=10

  while state_list[0]:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              run = False

      for item in res_dct:
          res_dct2[item] = conwayATOM(item,res_dct)

      for item in res_dct2:
          if res_dct2[item]:  
              pygame.draw.rect(win,(random.randint(240,255),random.randint(190,210),random.randint(45,65)),(square_dict[item]['x'],square_dict[item]['y'],square_dict[item]['w'],square_dict[item]['h']))
          else:   
              pygame.draw.rect(win,(255,255,255),(square_dict[item]['x'],square_dict[item]['y'],square_dict[item]['w'],square_dict[item]['h']))      
      pygame.display.update()
      pygame.time.delay(50)
      win.fill((0,0,0))

      for item in res_dct2:
          res_dct[item] = conwayATOM(item,res_dct2)
          
      for item in res_dct:
          if res_dct[item]:
              pygame.draw.rect(win,(random.randint(240,255),random.randint(190,210),random.randint(45,65)),(square_dict[item]['x'],square_dict[item]['y'],square_dict[item]['w'],square_dict[item]['h']))
          else:
              pygame.draw.rect(win,(255,255,255),(square_dict[item]['x'],square_dict[item]['y'],square_dict[item]['w'],square_dict[item]['h']))
      pygame.display.update()
      pygame.time.delay(50)
      win.fill((0,0,0))
      
if __name__=='__main__':
  main()
    

