import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AirportHomeComponent } from './home/Airport-home.component';
import { AirportNewComponent } from './new/Airport-new.component';
import { AirportDetailComponent } from './detail/Airport-detail.component';

const routes: Routes = [
  {path: '', component: AirportHomeComponent},
  { path: 'new', component: AirportNewComponent },
  { path: ':id', component: AirportDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Airport-detail-permissions'
      }
    }
  }
];

export const AIRPORT_MODULE_DECLARATIONS = [
    AirportHomeComponent,
    AirportNewComponent,
    AirportDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AirportRoutingModule { }