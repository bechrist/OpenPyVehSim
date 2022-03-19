# %% Brake Subsystem Models
# This file stores the class definition for the brake subsystem model and the

import numpy as np
import math

# %% Simplified Braking Model
def SimplifiedBraking( PedalForce, \
                       PedalRatio, BalanceBar , BoreDiameter, \
                       PadArea   , PadFriction, RotorRadius ):
    # Simplistic braking model that assumes rigid components and incompressible
    # brake fluid.
    #
    # Inputs:
    #   PedalForce   - (n,1 np.array) Pedal Force                   {F_p}   [N]
    #   PedalRatio   - (n,1 np.array) Pedal Ratio                   {eta_p} [ ]
    #   BalanceBar   - (n,1 np.array) Front Balance Bar Ratio       {%_bb}  [ ]
    #   BoreDiameter - (n,2 np.array) Master Cylinder Bore Diameter {D_c}   [m]
    #   PadArea      - (n,2 np.array) Brake Pad Area                {A_p}   [m^2]
    #   PadFriction  - (n,2 np.array) Brake Pad Friction            {mu_p}  [ ]
    #   RotorRadius  - (n,2 np.array) Brake Rotor Radius            {r_r}   [m]
    #
    # Outputs:
    #   BrakingTorque - (n,4 np.array) Braking Torque      {tau_b} [N-m]
    #   LinePressure  - (n,2 np.array) Brake Line Pressure {P_b}   [Pa]
    #
    # Notes:
    #
    # Author(s):
    #  Blake Christierson (bechristierson@sbcglobal.net)
    #
    # Last Updated: 07-Jul-2021

    # Determine Load Propagation
    CylinderForce = PedalForce * PedalRatio * np.array([BalanceBar, 1-BalanceBar])

    LinePressure = CylinderForce / (math.pi/4 * (BoreDiameter**2))

    BrakingTorque = LinePressure * PadArea * PadFriction * RotorRadius / 2

    BrakingTorque = np.concatenate( (BrakingTorque[:,0:1] * np.ones( (1,2) ), \
                                     BrakingTorque[:,1:2] * np.ones( (1,2) )), axis=1 )

    return BrakingTorque, LinePressure

# %% Compliant Braking Model
"""
def CompliantBraking( PedalForce, \
                      PedalRatio, BalanceBar , BoreDiameter, \
                      PadArea   , PadFriction, RotorRadius ):
    # Zero-order braking model that accounts for fluid & component compliance
    # which allows for pedal travel calculations and pressure drop studies.
    #
    # Inputs:
    #   PedalForce   - (n,1 np.array) Pedal Force                   {F_p}   [N]
    #   PedalRatio   - (n,1 np.array) Pedal Ratio                   {eta_p} [ ]
    #   BalanceBar   - (n,1 np.array) Front Balance Bar Ratio       {%_bb}  [ ]
    #   BoreDiameter - (n,2 np.array) Master Cylinder Bore Diameter {D_c}   [m]
    #   PadArea      - (n,2 np.array) Brake Pad Area                {A_p}   [m^2]
    #   PadFriction  - (n,2 np.array) Brake Pad Friction            {mu_p}  [ ]
    #   RotorRadius  - (n,2 np.array) Brake Rotor Radius            {r_r}   [m]
    #
    # Outputs:
    #   BrakingTorque - (n,4 np.array) Braking Torque      {tau_b} [N-m]
    #   LinePressure  - (n,2 np.array) Brake Line Pressure {P_b}   [Pa]
    #
    # Notes:
    #   - Incomplete, Do Not Use
    #
    # Author(s):
    #  Blake Christierson (bechristierson@sbcglobal.net)
    #
    # Last Updated: 07-Jul-2021

    # Determine System Compliance
    PedalPosition = 0

    # Determine Load Propagation
    CylinderForce = PedalForce * PedalRatio * np.array([BalanceBar, 1-BalanceBar])

    LinePressure = CylinderForce / (math.pi/4 * (BoreDiameter**2))

    BrakingTorque = LinePressure * PadArea * PadFriction * RotorRadius / 2

    BrakingTorque = np.concatenate( (BrakingTorque[:,0:1] * np.ones( (1,2) ), \
                                     BrakingTorque[:,1:2] * np.ones( (1,2) )), axis=1 )

    return BrakingTorque, LinePressure, PedalPosition
"""
