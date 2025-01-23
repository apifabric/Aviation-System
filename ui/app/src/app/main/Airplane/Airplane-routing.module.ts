import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AirplaneHomeComponent } from './home/Airplane-home.component';
import { AirplaneNewComponent } from './new/Airplane-new.component';
import { AirplaneDetailComponent } from './detail/Airplane-detail.component';

const routes: Routes = [
  {path: '', component: AirplaneHomeComponent},
  { path: 'new', component: AirplaneNewComponent },
  { path: ':id', component: AirplaneDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Airplane-detail-permissions'
      }
    }
  },{
    path: ':airplane_id/Passenger', loadChildren: () => import('../Passenger/Passenger.module').then(m => m.PassengerModule),
    data: {
        oPermission: {
            permissionId: 'Passenger-detail-permissions'
        }
    }
}
];

export const AIRPLANE_MODULE_DECLARATIONS = [
    AirplaneHomeComponent,
    AirplaneNewComponent,
    AirplaneDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AirplaneRoutingModule { }