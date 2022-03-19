from casadi import *

dae = DaeBuilder()
# Add input expressions
g = dae.add_p('g')

a = dae.add_p('a')
b = dae.add_p('b')

u = dae.add_u('u')

h = dae.add_x('h')
v = dae.add_x('v')
m = dae.add_x('m')

# Add output expressions
hdot = v
vdot = (u-a*v**2)/m-g
mdot = -b*u**2

dae.add_ode('hdot', hdot)
dae.add_ode('vdot', vdot)
dae.add_ode('mdot', mdot)

# Specify initial conditions
dae.set_start('h', 0)
dae.set_start('v', 0)
dae.set_start('m', 1)

# Add meta information
dae.set_unit('h','m')
dae.set_unit('v','m/s')
dae.set_unit('m','kg')

dae.make_semi_explicit()

# Make DAE Struct

intProb = {'x':dae.x, 'p':dae.p, 'ode':dae.ode, 'u':dae.u}
opts = {'tf':1}
F = integrator('F', 'idas', intProb, opts)

