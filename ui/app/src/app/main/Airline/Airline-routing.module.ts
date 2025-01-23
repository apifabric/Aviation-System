import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AirlineHomeComponent } from './home/Airline-home.component';
import { AirlineNewComponent } from './new/Airline-new.component';
import { AirlineDetailComponent } from './detail/Airline-detail.component';

const routes: Routes = [
  {path: '', component: AirlineHomeComponent},
  { path: 'new', component: AirlineNewComponent },
  { path: ':id', component: AirlineDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Airline-detail-permissions'
      }
    }
  }
];

export const AIRLINE_MODULE_DECLARATIONS = [
    AirlineHomeComponent,
    AirlineNewComponent,
    AirlineDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AirlineRoutingModule { }