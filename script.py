import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from matplotlib.patches import Rectangle
from time import sleep
import time
import serial

connected = False

ser = serial.Serial("/dev/cu.usbmodem1411", 9600)

while not connected:
  serin = ser.read()
  connected = True

# while True:
  # print ser.readline()

# take the average of the two?
# 1|2|3|4|5(tailbone)|6|7|8|9
# returns [right_leg, right_butt, tailbone, left_butt, left_leg]
def get_values(serial_inp):
  string_vals = serial_inp.split("|")
  vals = [int(numeric_string) for numeric_string in string_vals]
  # print vals
  # for s in vals:
    # if s > 1000:
      # return None
  # avg_values = [(vals[0]+vals[1])/float(2), (vals[2]+vals[3])/float(2), vals[4], (vals[5]+vals[6])/float(2), (vals[7]+vals[8])/float(2)]
  # avg_values = [(vals[0]+vals[1])/float(2), (vals[2]+vals[3])/float(2), vals[4], (vals[5]+vals[6])/float(2), vals[7]]
  avg_values = [vals[0], vals[1], vals[2], vals[3], vals[4]]
  max_val = float(1023)
  normalized_values = [num/max_val for num in avg_values]
  return normalized_values

# print get_values("1000|1023|1|500|789|900|987|1000|870")
# print get_values("1023|1023|0|0|789|900|987|1000|870")

def sample(seconds):
  calibration_period = time.time() + seconds
  num_samples = 0
  totals = [0,0,0,0,0,0,0,0]
  while True:
    if time.time() > calibration_period:
      if num_samples == 0:
        return None
      else:
        return [t/float(num_samples) for t in totals]
    else:
      sample = get_values(ser.readline())
      if sample == None:
        continue
      totals = [x + y for x, y in zip(totals, sample)]
    num_samples += 1

img = mpimg.imread('../images/gluteus-cropped.png')
imgplot = plt.imshow(img)
currentAxis = plt.gca()

red = "#ff0000"
green = "#52bb1e"

left_butt = ((105,60), 200, 315)
tail_bone = ((left_butt[0][0]+left_butt[1], left_butt[0][1]), 140, 160)
right_butt = ((tail_bone[0][0]+tail_bone[1], tail_bone[0][1]), 200, 315)
left_leg = ((left_butt[0][0], left_butt[0][1]+left_butt[2]), 200, 315)
right_leg = ((right_butt[0][0], right_butt[0][1]+right_butt[2]), 200, 315)

left_butt_rect = Rectangle(left_butt[0], left_butt[1], left_butt[2], facecolor=green, alpha=0.7)
tail_bone_rect = Rectangle(tail_bone[0], tail_bone[1], tail_bone[2], facecolor=green, alpha=0.7)
right_butt_rect = Rectangle(right_butt[0], right_butt[1], right_butt[2], facecolor=green, alpha=0.7)
left_leg_rect = Rectangle(left_leg[0], left_leg[1], left_leg[2], facecolor=green, alpha=0.7)
right_leg_rect = Rectangle(right_leg[0], right_leg[1], right_leg[2], facecolor=green, alpha=0.7)

zones = [right_leg_rect, right_butt_rect, tail_bone_rect, left_butt_rect, left_leg_rect]

for z in zones:
  currentAxis.add_patch(z)

def get_colors(s_values, n_values):
  result = [green, green, green, green, green]
  difference = [x - y for x, y in zip(n_values, s_values)]
  print difference
  for idx, d in enumerate(difference):
    if d > red_threshold:
      result[idx] = red
  return result

# print "sleeping"
# sleep(2)
# print "end sleeping"
normal_values = sample(5)
print "NORMAL VALUES"
print normal_values
print "-------------------------------------------------------------"
red_threshold = 0.03 # if values increases by more than threshold make area red
plt.ion()

while True:
  sample_values = sample(1)
  if sample_values == None:
    continue
  # print sample_values
  colors = get_colors(sample_values, normal_values)
  # print colors
  for idx, c in enumerate(colors):
    zones[idx].set_facecolor(c)

  plt.pause(0.1)
  plt.draw()

# plt.show()

# x = np.arange(0, 5, 0.1);
# y = np.sin(x)
# plt.plot(x, y)
