import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {AIRCRAFTMAINTENANCE_MODULE_DECLARATIONS, AircraftMaintenanceRoutingModule} from  './AircraftMaintenance-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    AircraftMaintenanceRoutingModule
  ],
  declarations: AIRCRAFTMAINTENANCE_MODULE_DECLARATIONS,
  exports: AIRCRAFTMAINTENANCE_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class AircraftMaintenanceModule { }