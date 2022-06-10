import ComponentModel

class TireModel(ComponentModel):
    def __init__(self, model=dict(), params=dict()):
        self.model  = model
        self.params = params

    @property
    def model(self): return self.model

    @model.setter
    def model(self, value):
        self.model = value

    @property
    def params(self): return self.params

    @params.setter
    def params(self, value):
        self.params = value

    def __dir__(self):
        raise NotImplementedError

    def __call__(self, **kwargs):
        raise NotImplementedError

Tire = TireModel()