# %% ComponentModel.py - Component Model Template Class
# This script defines a template class used for a general model component

class ComponentModel:
    def __init__(self, model=dict(), params=dict()):
        self.model  = model
        self.params = params

    @property
    def model(self): return self.model

    @model.setter
    def model(self, value):
        raise NotImplementedError

    @property
    def params(self): return self.params

    @params.setter
    def params(self, value):
        raise NotImplementedError

    def __dir__(self):
        raise NotImplementedError

    def __call__(self, **kwargs):
        raise NotImplementedError

Component = ComponentModel()
   