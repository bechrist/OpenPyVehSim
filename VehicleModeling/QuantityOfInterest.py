# %% QuantityOfInterest
# Defines quantity of interest class
# 
# Blake Christierson (bechristierson@sbcgloba1.net)
# 3 June 2022

import numpy as np

#from PhysicalUnits import parseUnit

# %% Class Definition
class QoI():
    def __init__(self, name, symbol, unit, value=[], size=[1,1]):
        if isinstance(name, str):
            self.name = name          
        else:
            raise TypeError('Quantity Name Not Provided as String')

        if isinstance(symbol, str):
            self.symbol = symbol      
        else:
            raise TypeError('Quantity Symbol Not Provided as Raw String')

        if isinstance(unit, str):
            self.unit = unit
            self.dim, self.cUnit = parseUnit(unit, 'MKS')
        else:
            raise TypeError('Quantity Unit Not Provided as String')

        if isinstance(size, list):
            self.size = size
        else:
            raise TypeError('Quantity Size Not Provided as List')

        if (not isinstance(value, np.ndarray)) or (len(value) == 0):
            self.value = np.zeros(size)
        else:
            self.value = value

    # Plotting
    def LinePlot(self, xQoI, axes, style):
        axes.plot(
            xQoI.value, self.value, style, 
            label=r'{}, ${}$ [${}$]'.format(
                self.name, self.symbol, self.unit,
            ),
        )

        if axes.get_xlabel() == '':
            axes.set_xlabel(
                r'{}, ${}$ [${}$]'.format(
                    xQoI.name, xQoI.symbol, xQoI.unit,
                ),
            )
            axes.set_ylabel(
                r'{}, ${}$ [${}$]'.format( 
                    self.name, self.symbol, self.unit,
                ),
            )

        elif axes.get_xlabel() == \
                r'{}, ${}$ [${}$]'.format(xQoI.name, xQoI.symbol, xQoI.unit):

            axes.set_ylabel('')
            axes.legend()

        else:
            print('x-Quantity is Not Consistent with Chosen Axes')

    def ScatterPlot(self, xQoI, axes):
        axes.scatter(
            xQoI.value, self.value, 
            label=r'{}, ${}$ [${}$]'.format(
                self.name, self.symbol, self.unit,
            ),
        )

        if axes.get_xlabel() == '':
            axes.set_xlabel(
                r'{}, ${}$ [${}$]'.format(
                    xQoI.name, xQoI.symbol, xQoI.unit,
                ),
            )
            axes.set_ylabel(
                r'{}, ${}$ [${}$]'.format(
                    self.name, self.symbol, self.unit,
                ),
            )

        elif axes.get_xlabel() == \
                r'{}, ${}$ [${}$]'.format(xQoI.name, xQoI.symbol, xQoI.unit):

            axes.set_ylabel('')
            axes.legend()

        else:
            print('x-Quantity is Not Consistent with Chosen Axes')

    def HistogramPlot(self, axes):
        axes.hist(
            self.value, label=r'{}, ${}$ [${}$]'.format(
                self.name, self.symbol, self.unit,
            ),
        )

        if axes.get_xlabel() == '':
            axes.set_xlabel(
                r'{}, ${}$ [${}$]'.format(
                    self.name, self.symbol, self.unit,
                ),
            )
            axes.set_ylabel('Frequency')

        else:
            axes.set_xlabel('Quantity Values')
            axes.set_ylabel('Frequency')
            axes.legend()

    def FFTPlot(self):
        raise NotImplementedError('FFTPlot Method Not Implemented')