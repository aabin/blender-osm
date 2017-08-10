from . import RoofRealistic
from building.roof.hipped import RoofHipped
from .flat import RoofFlatRealistic


class RoofHippedRealistic(RoofRealistic, RoofHipped):
    
    def renderRoofTextured(self):
        if self.makeFlat:
            return RoofFlatRealistic.renderRoofTextured(self)
        else:
            super().renderRoofTextured()