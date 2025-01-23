import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {AIRPORTFACILITY_MODULE_DECLARATIONS, AirportFacilityRoutingModule} from  './AirportFacility-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    AirportFacilityRoutingModule
  ],
  declarations: AIRPORTFACILITY_MODULE_DECLARATIONS,
  exports: AIRPORTFACILITY_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class AirportFacilityModule { }