import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {CREWMEMBER_MODULE_DECLARATIONS, CrewMemberRoutingModule} from  './CrewMember-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    CrewMemberRoutingModule
  ],
  declarations: CREWMEMBER_MODULE_DECLARATIONS,
  exports: CREWMEMBER_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class CrewMemberModule { }