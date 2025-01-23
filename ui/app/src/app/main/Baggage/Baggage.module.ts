import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {BAGGAGE_MODULE_DECLARATIONS, BaggageRoutingModule} from  './Baggage-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    BaggageRoutingModule
  ],
  declarations: BAGGAGE_MODULE_DECLARATIONS,
  exports: BAGGAGE_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class BaggageModule { }