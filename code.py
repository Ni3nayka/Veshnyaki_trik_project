import sys
import time
import random
import math

def get_e_angle_akselerometer():
  pi = 3.141592653589793
  RADIAN = 180/pi
  a = brick.accelerometer().read()[0]
  b = brick.accelerometer().read()[1]
  angle = 0
  if (b!=0):
    tan = a/b
    angle = math.atan(tan)*RADIAN
    if abs(angle)>45: 
      tan = b/a
      angle = -math.atan(tan)*RADIAN
  else: angle = 0
  return angle

def move(moving):
  
  def forward():
    while not brick.encoder("E3").read() > int(1150):
      e = get_e_angle_akselerometer()
      brick.motor("M3").setPower(100-e)
      brick.motor("M4").setPower(100+e)
      script.wait(1) 
    
  def left():
    brick.motor("M3").setPower(100)
    brick.motor("M4").setPower(-100)
    while not (brick.encoder("E3").read() > int(245.6)): pass
    
  def right():
    brick.motor("M3").setPower(-100)
    brick.motor("M4").setPower(100)
    while not (brick.encoder("E4").read() > int(245.6)): pass
    
  for a in moving:
    brick.encoder("E3").reset()
    brick.encoder("E4").reset()
    if a==1: forward()
    elif a==2: left()
    elif a==3: right()
    else: print("ERROR 101")
    brick.motor("M3").setPower(0)
    brick.motor("M4").setPower(0)
  
def operating(point_start,point_finish):
  dx = point_start[0] - point_finish[0]
  dy = point_start[1] - point_finish[1]
  answer = []
  if dx!=0:
    if dx>0: 
      answer.append(2)
      answer.append(2)
    for i in range(abs(dx)): answer.append(1)
    if dx>0: 
      answer.append(2)
      answer.append(2)
  if dy!=0:
    if dy>0: answer.append(3)
    else: answer.append(2)
    for i in range(abs(dy)): answer.append(1)
    if dy>0: answer.append(2)
    else: answer.append(3)
  return answer
  
def main():
  point_start = (1,5)  # <========================================================================================
  point_finish = (6,3) # <========================================================================================
  moving = operating(point_start,point_finish)
  move(moving)

if __name__ == '__main__':
  main()
