import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {LUGGAGE_MODULE_DECLARATIONS, LuggageRoutingModule} from  './Luggage-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    LuggageRoutingModule
  ],
  declarations: LUGGAGE_MODULE_DECLARATIONS,
  exports: LUGGAGE_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class LuggageModule { }