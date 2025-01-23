import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {AIRCRAFT_MODULE_DECLARATIONS, AircraftRoutingModule} from  './Aircraft-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    AircraftRoutingModule
  ],
  declarations: AIRCRAFT_MODULE_DECLARATIONS,
  exports: AIRCRAFT_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class AircraftModule { }