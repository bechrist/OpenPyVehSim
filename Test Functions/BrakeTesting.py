import numpy as np
import BrakeModels as Brakes

# %% Input Data
PedalForce = np.array([[150],[200]])

PedalRatio = np.array(4.3)

BalanceBar = np.array(0.48)

BoreDiameter = np.array([0.59, 0.8125]) * 0.0254

PadArea = np.array([2.9, 1.45]) * (0.0254**2)

PadFriction = np.array([0.55, 0.55])

RotorRadius = np.array([3.3, 3.3]) * 0.0254

# %% Test Simplified Braking
LinePressure, BrakingTorque = Brakes.SimplifiedBraking(PedalForce, \
                                                       PedalRatio, BalanceBar , BoreDiameter, \
                                                       PadArea   , PadFriction, RotorRadius )