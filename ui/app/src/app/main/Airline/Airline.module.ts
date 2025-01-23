import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {AIRLINE_MODULE_DECLARATIONS, AirlineRoutingModule} from  './Airline-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    AirlineRoutingModule
  ],
  declarations: AIRLINE_MODULE_DECLARATIONS,
  exports: AIRLINE_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class AirlineModule { }