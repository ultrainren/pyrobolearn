#!/usr/bin/env python
"""Load the Nao robot.
"""

from itertools import count
from pyrobolearn.simulators import BulletSim
from pyrobolearn.worlds import BasicWorld
from pyrobolearn.robots import Nao

# Create simulator
sim = BulletSim()

# create world
world = BasicWorld(sim)

# create robot
robot = Nao(sim)

# print information about the robot
robot.print_info()

# Position control using sliders
# robot.add_joint_slider(robot.getLeftArmIds())

# run simulator
for _ in count():
    # robot.update_joint_slider()
    world.step(sleep_dt=1./240)