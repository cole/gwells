"""
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
from django.contrib import admin
from .models import ProvinceState, LandDistrict, WellYieldUnit, WellActivityType, WellClass, WellSubclass, IntendedWaterUse, DrillingCompany, Driller, GroundElevationMethod, DrillingMethod
from .models import SurficialMaterial, BedrockMaterial, BedrockMaterialDescriptor, LithologyStructure, LithologyWeathering, LithologyColour, LithologyHardness, LithologyMoisture
# Register your models here.
admin.site.register(ProvinceState)
admin.site.register(LandDistrict)
admin.site.register(WellYieldUnit)
admin.site.register(WellActivityType)
admin.site.register(WellClass)
admin.site.register(WellSubclass)
admin.site.register(IntendedWaterUse)
admin.site.register(DrillingCompany)
admin.site.register(Driller)
admin.site.register(GroundElevationMethod)
admin.site.register(DrillingMethod)
admin.site.register(SurficialMaterial)
admin.site.register(BedrockMaterial)
admin.site.register(BedrockMaterialDescriptor)
admin.site.register(LithologyStructure)
admin.site.register(LithologyWeathering)
admin.site.register(LithologyColour)
admin.site.register(LithologyHardness)
admin.site.register(LithologyMoisture)
