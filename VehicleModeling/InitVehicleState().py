def InitVehicleState():
    State = {}

    # %% Chassis States
    State['LongPos'] = VehicleState(name  ='Longitudinal Position', \
                                    symbol=r'X', \
                                    unit  =r'm')
    State['LongVel'] = VehicleState(name  ='Longitudinal Velocity', \
                                    symbol=r'\dot{x}', \
                                    unit  =r'm/s')
    State['LongAcc'] = VehicleState(name  ='Longitudinal Acceleration', \
                                    symbol=r'\ddot{x}', \
                                    unit  =r'm/s^2')

    State['LatPos'] = VehicleState(name  ='Lateral Position', \
                                   symbol=r'Y', \
                                   unit  =r'm')
    State['LatVel'] = VehicleState(name  ='Lateral Velocity', \
                                   symbol=r'\dot{y}', \
                                   unit  =r'm/s')
    State['LatAcc'] = VehicleState(name  ='Lateral Acceleration', \
                                   symbol=r'\ddot{y}', \
                                   unit  =r'm/s^2')

    State['RidePos'] = VehicleState(name  ='Ride Height', \
                                    symbol=r'z', \
                                    unit  =r'm')
    State['RideVel'] = VehicleState(name  ='Ride Velocity', \
                                    symbol=r'\dot{z}', \
                                    unit  =r'm/s')
    State['RideAcc'] = VehicleState(name  ='Ride Acceleration', \
                                    symbol=r'\ddot{z}', \
                                    unit  =r'm/s^2')

    State['PitchPos'] = VehicleState(name  ='Pitch Angle', \
                                     symbol=r'\theta', \
                                     unit  =r'rad')
    State['PitchVel'] = VehicleState(name  ='Pitch Rate', \
                                     symbol=r'\dot{\theta}', \
                                     unit  =r'rad/s')
    State['PitchAcc'] = VehicleState(name  ='Pitch Acceleration', \
                                     symbol=r'\ddot{\theta}', \
                                     unit  =r'rad/s^2')

    State['RollPos'] = VehicleState(name  ='Roll Angle', \
                                    symbol=r'\phi', \
                                    unit  =r'rad')
    State['RollVel'] = VehicleState(name  ='Roll Rate', \
                                    symbol= r'\dot{\phi}', \
                                    unit  =r'rad/s')
    State['RollAcc'] = VehicleState(name  ='Roll Acceleration', \
                                    symbol=r'\ddot{\phi}', \
                                    unit  =r'rad/s^2')

    State['YawPos'] = VehicleState(name  ='Heading Angle', \
                                   symbol=r'\psi', \
                                   unit  =r'rad')
    State['YawVel'] = VehicleState(name  ='Yaw Rate', \
                                   symbol=r'\dot{\psi}', \
                                   unit  =r'rad/s')
    State['YawAcc'] = VehicleState(name  ='Yaw Acceleration', \
                                   symbol=r'\ddot{\psi}', \
                                   unit  =r'rad/s^2')

    State['LongAccTot'] = VehicleState(name='Total Longitudinal Acceleration', \
                                       symbol=r'a_{x}', \
                                       unit  =r'm/s^2')
    State['LatAccTot']  = VehicleState(name  ='Total Lateral Acceleration', \
                                       symbol=r'a_{y}', \
                                       unit  =r'm/s^2' )
    State['RideAccTot'] = VehicleState(name  ='Total Ride Acceleration', \
                                       symbol=r'a_{z}', \
                                       unit  =r'm/s^2')

    # %% Suspension States
    State['TireSteer']   = VehicleState(name  ='Tire Steer', \
                                        symbol=r'\delta', \
                                        unit  =r'rad', \
                                        size  =[4,1])
    State['Inclination'] = VehicleState(name  ='Inclination Angle', \
                                        symbol=r'\gamma', \
                                        unit  =r'rad', \
                                        size  =[4,1])
    State['Camber']      = VehicleState(name  ='Camber', \
                                        symbol=r'\eps', \
                                        unit  =r'rad', \
                                        size  =[4,1])

    #State['ShockDisp'] = VehicleState(name    ='Shock Displacement', \
    #                                  symbol  =r'd_{SP,SH}', \
    #                                  unit    =r'm', \
    #                                  size    =[4,1])
    #State['ShockVel']  = VehicleState( name    ='Shock Velocity', \
    #                                   symbol  =r'\dot{d}_{SP,SH}', \
    #                                   unit    = 'm/s', \
    #                                   size    = [4,1], \
    #                                   QSSFlag = 'Null' )

    #State['JounceDisp'] = VehicleState('Jounce Displacement', r'')
    #State['JounceVel']

    #State['MemberLoads']

    # %% Tire States
    State['SlipAngle'] = VehicleState( name   = 'Slip Angle', \
                                       symbol = r'\alpha', \
                                       unit   = 'rad', \
                                       size   = [4,1] )
    State['SlipRatio'] = VehicleState( name   = 'Slip Ratio', \
                                       symbol = r'\kappa', \
                                       unit   = '', \
                                       size   = [4,1] )

    State['NormalLoad']   = VehicleState( name    = 'Normal Load', \
                                          symbol  = r'F_{TR,z}', \
                                          unit    = 'N', \
                                          size    = [4,1] )
    State['TirePressure'] = VehicleState( name    = 'Tire Pressure', \
                                          symbol  = r'p_{TR}', \
                                          unit    = 'Pa', \
                                          size    = [4,1], \
                                          QSSFlag = 'Given' )

    State['SpinRate'] = VehicleState( name    = 'Wheel Spin Rate', \
                                      symbol  = r'\omega_{TR}', \
                                      unit    = 'rad/s', \
                                      size    = [4,1] )
    State['SpinAcc']  = VehicleState( name    = 'Wheel Spin Acceleration', \
                                      symbol  = r'\dot{\omega}_{TR}', \
                                      unit    = 'rad/s^2', \
                                      size    = [4,1], \
                                      QSSFlag = 'Null' )

    State['EffRadius']  = VehicleState( name   = 'Effective Radius', \
                                        symbol = r'r_{TR,e}', \
                                        unit   = 'm', \
                                        size   = [4,1] )
    State['LoadRadius'] = VehicleState( name   = 'Loaded Radius', \
                                        symbol = r'r_{Tr,l}', \
                                        unit   = 'm', \
                                        size   = [4,1] )

    State['LongForce'] = VehicleState( name   = 'Longitudinal Force', \
                                       symbol = r'F_{TR,x}', \
                                       unit   = 'N', \
                                       size   = [4,1] )
    State['LatForce']  = VehicleState( name   = 'Lateral Force', \
                                       symbol = r'F_{TR,y}', \
                                       unit   = 'N', \
                                       size   = [4,1] )

    State['OverturningMom'] = VehicleState( name   = 'Overturning Moment', \
                                            symbol = r'M_{TR,x}', \
                                            unit   = 'N-m', \
                                            size   = [4,1] )
    State['RollingResist']  = VehicleState( name   = 'Rolling Resistance', \
                                            symbol = r'M_{TR,y}', \
                                            unit   = 'N-m', \
                                            size   = [4,1] )
    State['AligningMom']    = VehicleState( name   = 'Aligning Moment', \
                                            symbol = r'M_{TR,z}', \
                                            unit   = 'N-m', \
                                            size   = [4,1] )

    # %% Control States

    # %% Powertrain States

    # %% Aerodynamic States
    State['DragForce'] = VehicleState( name   = 'Drag Force', \
                                       symbol = r'F_{AR,x}', \
                                       unit   = 'N' )
    State['SideForce'] = VehicleState( name   = 'Side Force', \
                                       symbol = r'F_{AR,y}', \
                                       unit   = 'N' )
    State['Downforce'] = VehicleState( name   = 'DownForce', \
                                       symbol = r'F_{AR,z}', \
                                       unit   = 'N' )

    State['AeroRollMom']  = VehicleState( name   = 'Aero Roll Moment', \
                                          symbol = r'M_{AR,x}', \
                                          unit   = 'N-m' )
    State['AeroPitchMom'] = VehicleState( name   = 'Aero Pitch Moment', \
                                          symbol = r'M_{AR,y}', \
                                          unit   = 'N-m' )
    State['AeroYawMom']   = VehicleState( name   = 'Aero Yaw Moment', \
                                          symbol = r'M_{AR,z}', \
                                          unit   = 'N-m' )

    return State