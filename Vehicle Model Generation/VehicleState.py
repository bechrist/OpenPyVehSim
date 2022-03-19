# %% Vehicle State Definitions

import numpy as np

# %% Class Definition
class VehicleState():
    def __init__(self, Name, Symbol, Unit, Value=[], Size=[1,1], QSSFlag='Solve'):
        if isinstance(Name, str):
            self.Name = Name # Full State Name
        else:
            raise TypeError('Vehicle State Name Not Provided as String')

        if isinstance(Symbol, str):
            self.Symbol = Symbol # State Markup Symbol
        else:
            raise TypeError('Vehicle State Symbol Not Provided as Raw String')

        if isinstance(Unit, str):
            self.Unit = Unit # Computation Unit (m-k-s)

            self.Dims = 1 # Unit Dimensionality

            self.DispUnit = self.Dims # Display Unit(s)
        else:
            raise TypeError('Vehicle State Unit Not Provided as String')

        if isinstance(Size, list):
            self.Size = Size # State Size
        else:
            raise TypeError('Vehicle State Size Not Provided as List')

        if (not isinstance(Value, np.ndarray)) or (len(Value) == 0):
            self.Value = np.zeros(Size) # State Initialization
        else:
            self.Value = Value # State Allocation

        if isinstance(QSSFlag, str):
            self.QSSFlag = QSSFlag # Quasi-Steady State Computation Flag
        else:
            raise TypeError('Vehicle State QSSFlag Not Provided as String')

    def LinePlot(self, xState, Axes, Format):
        if Axes.get_xlabel() == '':
            Axes.plot(xState.Value, self.Value, Format, \
                label=r'{}, ${}$ [${}$]'.format(self.Name, self.Symbol, self.Unit))

            Axes.set_xlabel(r'{}, ${}$ [${}$]'.format(xState.Name, xState.Symbol, xState.Unit))
            Axes.set_ylabel(r'{}, ${}$ [${}$]'.format(self.Name  , self.Symbol  , self.Unit  ))

        elif Axes.get_xlabel() == r'{}, ${}$ [${}$]'.format(xState.Name, xState.Symbol, xState.Unit):
            Axes.plot(xState.Value, self.Value, Format, \
                label=r'{}, ${}$ [${}$]'.format(self.Name, self.Symbol, self.Unit))

            Axes.set_ylabel('State Values')
            Axes.legend()

        else:
            print('xState is Not Consistent with Chosen Axes')

    def ScatterPlot(self, xState, Axes):
        if Axes.get_xlabel() == '':
            Axes.scatter(xState.Value, self.Value, \
                label=r'{}, ${}$ [${}$]'.format(self.Name, self.Symbol, self.Unit))

            Axes.set_xlabel(r'{}, ${}$ [${}$]'.format(xState.Name, xState.Symbol, xState.Unit))
            Axes.set_ylabel(r'{}, ${}$ [${}$]'.format(self.Name  , self.Symbol  , self.Unit  ))

        elif Axes.get_xlabel() == r'{}, ${}$ [${}$]'.format(xState.Name, xState.Symbol, xState.Unit):
            Axes.scatter(xState.Value, self.Value, \
                label=r'{}, ${}$ [${}$]'.format(self.Name, self.Symbol, self.Unit))

            Axes.set_ylabel('State Values')
            Axes.legend()

        else:
            print('xState is Not Consistent with Chosen Axes')

    def HistogramPlot(self, Axes):
        if Axes.get_xlabel() == '':
            Axes.hist(self.Value, \
                label=r'{}, ${}$ [${}$]'.format(self.Name, self.Symbol, self.Unit))

            Axes.set_xlabel(r'{}, ${}$ [${}$]'.format(self.Name, self.Symbol, self.Unit))
            Axes.set_ylabel('Frequency')

        else:
            Axes.hist(self.Value, \
                label=r'{}, ${}$ [${}$]'.format(self.Name, self.Symbol, self.Unit))

            Axes.set_xlabel('State Values')
            Axes.set_ylabel('Frequency')
            Axes.legend()

    def FFTPlot(self):
        raise NotImplementedError('FFTPlot Method Not Implemented')

def InitVehicleStates():
    State = {}

    # %% Chassis States
    State['LongPos'] = VehicleState( Name    = 'Longitudinal Position', \
                                     Symbol  = r'X', \
                                     Unit    = 'm', \
                                     QSSFlag = 'Null' )
    State['LongVel'] = VehicleState( Name    = 'Longitudinal Velocity', \
                                     Symbol  = r'\dot{x}', \
                                     Unit    = 'm/s', \
                                     QSSFlag = 'Given' )
    State['LongAcc'] = VehicleState( Name    ='Longitudinal Acceleration', \
                                     Symbol  = r'\ddot{x}', \
                                     Unit    = 'm/s^2', \
                                     QSSFlag = 'Given' )

    State['LatPos'] = VehicleState( Name    = 'Lateral Position', \
                                    Symbol  = r'Y', \
                                    Unit    = 'm', \
                                    QSSFlag ='Null' )
    State['LatVel'] = VehicleState( Name    = 'Lateral Velocity', \
                                    Symbol  = r'\dot{y}', \
                                    Unit    = 'm/s' )
    State['LatAcc'] = VehicleState( Name    = 'Lateral Acceleration', \
                                    Symbol  = r'\ddot{y}', \
                                    Unit    = 'm/s^2' )

    State['RidePos'] = VehicleState( Name    = 'Ride Height', \
                                     Symbol  = r'z', \
                                     Unit    = 'm' )
    State['RideVel'] = VehicleState( Name    = 'Ride Velocity', \
                                     Symbol  = r'\dot{z}', \
                                     Unit    = 'm/s', \
                                     QSSFlag = 'Null' )
    State['RideAcc'] = VehicleState( Name    = 'Ride Acceleration', \
                                     Symbol  = r'\ddot{z}', \
                                     Unit    = 'm/s^2', \
                                     QSSFlag = 'Null' )

    State['PitchPos'] = VehicleState( Name    = 'Pitch Angle', \
                                      Symbol  = r'\theta', \
                                      Unit    = 'rad' )
    State['PitchVel'] = VehicleState( Name    = 'Pitch Rate', \
                                      Symbol  = r'\dot{\theta}', \
                                      Unit    = 'rad/s', \
                                      QSSFlag = 'Null' )
    State['PitchAcc'] = VehicleState( Name    = 'Pitch Acceleration', \
                                      Symbol  = r'\ddot{\theta}', \
                                      Unit    = 'rad/s^2', \
                                      QSSFlag = 'Null' )

    State['RollPos'] = VehicleState( Name    = 'Roll Angle', \
                                     Symbol  = r'\phi', \
                                     Unit    = 'rad' )
    State['RollVel'] = VehicleState( Name    = 'Roll Rate', \
                                     Symbol  = r'\dot{\phi}', \
                                     Unit    = 'rad/s', \
                                     QSSFlag = 'Null' )
    State['RollAcc'] = VehicleState( Name    = 'Roll Acceleration', \
                                     Symbol  = r'\ddot{\phi}', \
                                     Unit    = 'rad/s^2', \
                                     QSSFlag = 'Null' )

    State['YawPos'] = VehicleState( Name    = 'Heading Angle', \
                                    Symbol  = r'\psi', \
                                    Unit    = 'rad', \
                                    QSSFlag = 'Null' )
    State['YawVel'] = VehicleState( Name    = 'Yaw Rate', \
                                    Symbol  = r'\dot{\psi}', \
                                    Unit    = 'rad/s',
                                    QSSFlag = 'Given' )
    State['YawAcc'] = VehicleState( Name    = 'Yaw Acceleration', \
                                    Symbol  = r'\ddot{\psi}', \
                                    Unit    = 'rad/s^2' )

    State['LongAccTot'] = VehicleState( Name    = 'Total Longitudinal Acceleration', \
                                        Symbol  = r'a_{x}', \
                                        Unit    = 'm/s^2' )
    State['LatAccTot']  = VehicleState( Name    = 'Total Lateral Acceleration', \
                                        Symbol  = r'a_{y}', \
                                        Unit    = 'm/s^2' )
    State['RideAccTot'] = VehicleState( Name    = 'Total Ride Acceleration', \
                                        Symbol  = r'a_{z}', \
                                        Unit    = 'm/s^2', \
                                        QSSFlag = 'Null' )

    # %% Suspension States
    State['TireSteer']   = VehicleState( Name   = 'Tire Steer', \
                                         Symbol = r'\delta', \
                                         Unit   = 'rad', \
                                         Size   = [4,1] )
    State['Inclination'] = VehicleState( Name   = 'Inclination Angle', \
                                         Symbol = r'\gamma', \
                                         Unit   = 'rad', \
                                         Size   = [4,1] )
    State['Camber']      = VehicleState( Name   = 'Camber', \
                                         Symbol = r'\eps', \
                                         Unit   = 'rad', \
                                         Size   = [4,1] )

    State['ShockDisp'] = VehicleState( Name    = 'Shock Displacement', \
                                       Symbol  = r'd_{SP,SH}', \
                                       Unit    = 'm', \
                                       Size    = [4,1] )
    State['ShockVel']  = VehicleState( Name    = 'Shock Velocity', \
                                       Symbol  = r'\dot{d}_{SP,SH}', \
                                       Unit    = 'm/s', \
                                       Size    = [4,1], \
                                       QSSFlag = 'Null' )

    #State['JounceDisp'] = VehicleState('Jounce Displacement', r'')
    #State['JounceVel']

    #State['MemberLoads']

    # %% Tire States
    State['SlipAngle'] = VehicleState( Name   = 'Slip Angle', \
                                       Symbol = r'\alpha', \
                                       Unit   = 'rad', \
                                       Size   = [4,1] )
    State['SlipRatio'] = VehicleState( Name   = 'Slip Ratio', \
                                       Symbol = r'\kappa', \
                                       Unit   = '', \
                                       Size   = [4,1] )

    State['NormalLoad']   = VehicleState( Name    = 'Normal Load', \
                                          Symbol  = r'F_{TR,z}', \
                                          Unit    = 'N', \
                                          Size    = [4,1] )
    State['TirePressure'] = VehicleState( Name    = 'Tire Pressure', \
                                          Symbol  = r'p_{TR}', \
                                          Unit    = 'Pa', \
                                          Size    = [4,1], \
                                          QSSFlag = 'Given' )

    State['SpinRate'] = VehicleState( Name    = 'Wheel Spin Rate', \
                                      Symbol  = r'\omega_{TR}', \
                                      Unit    = 'rad/s', \
                                      Size    = [4,1] )
    State['SpinAcc']  = VehicleState( Name    = 'Wheel Spin Acceleration', \
                                      Symbol  = r'\dot{\omega}_{TR}', \
                                      Unit    = 'rad/s^2', \
                                      Size    = [4,1], \
                                      QSSFlag = 'Null' )

    State['EffRadius']  = VehicleState( Name   = 'Effective Radius', \
                                        Symbol = r'r_{TR,e}', \
                                        Unit   = 'm', \
                                        Size   = [4,1] )
    State['LoadRadius'] = VehicleState( Name   = 'Loaded Radius', \
                                        Symbol = r'r_{Tr,l}', \
                                        Unit   = 'm', \
                                        Size   = [4,1] )

    State['LongForce'] = VehicleState( Name   = 'Longitudinal Force', \
                                       Symbol = r'F_{TR,x}', \
                                       Unit   = 'N', \
                                       Size   = [4,1] )
    State['LatForce']  = VehicleState( Name   = 'Lateral Force', \
                                       Symbol = r'F_{TR,y}', \
                                       Unit   = 'N', \
                                       Size   = [4,1] )

    State['OverturningMom'] = VehicleState( Name   = 'Overturning Moment', \
                                            Symbol = r'M_{TR,x}', \
                                            Unit   = 'N-m', \
                                            Size   = [4,1] )
    State['RollingResist']  = VehicleState( Name   = 'Rolling Resistance', \
                                            Symbol = r'M_{TR,y}', \
                                            Unit   = 'N-m', \
                                            Size   = [4,1] )
    State['AligningMom']    = VehicleState( Name   = 'Aligning Moment', \
                                            Symbol = r'M_{TR,z}', \
                                            Unit   = 'N-m', \
                                            Size   = [4,1] )

    # %% Control States

    # %% Powertrain States

    # %% Aerodynamic States
    State['DragForce'] = VehicleState( Name   = 'Drag Force', \
                                       Symbol = r'F_{AR,x}', \
                                       Unit   = 'N' )
    State['SideForce'] = VehicleState( Name   = 'Side Force', \
                                       Symbol = r'F_{AR,y}', \
                                       Unit   = 'N' )
    State['Downforce'] = VehicleState( Name   = 'DownForce', \
                                       Symbol = r'F_{AR,z}', \
                                       Unit   = 'N' )

    State['AeroRollMom']  = VehicleState( Name   = 'Aero Roll Moment', \
                                          Symbol = r'M_{AR,x}', \
                                          Unit   = 'N-m' )
    State['AeroPitchMom'] = VehicleState( Name   = 'Aero Pitch Moment', \
                                          Symbol = r'M_{AR,y}', \
                                          Unit   = 'N-m' )
    State['AeroYawMom']   = VehicleState( Name   = 'Aero Yaw Moment', \
                                          Symbol = r'M_{AR,z}', \
                                          Unit   = 'N-m' )

    return State

InitVehicleStates()