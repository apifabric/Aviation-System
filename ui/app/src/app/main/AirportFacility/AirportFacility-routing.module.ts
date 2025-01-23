import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AirportFacilityHomeComponent } from './home/AirportFacility-home.component';
import { AirportFacilityNewComponent } from './new/AirportFacility-new.component';
import { AirportFacilityDetailComponent } from './detail/AirportFacility-detail.component';

const routes: Routes = [
  {path: '', component: AirportFacilityHomeComponent},
  { path: 'new', component: AirportFacilityNewComponent },
  { path: ':id', component: AirportFacilityDetailComponent,
    data: {
      oPermission: {
        permissionId: 'AirportFacility-detail-permissions'
      }
    }
  }
];

export const AIRPORTFACILITY_MODULE_DECLARATIONS = [
    AirportFacilityHomeComponent,
    AirportFacilityNewComponent,
    AirportFacilityDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AirportFacilityRoutingModule { }