import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PilotHomeComponent } from './home/Pilot-home.component';
import { PilotNewComponent } from './new/Pilot-new.component';
import { PilotDetailComponent } from './detail/Pilot-detail.component';

const routes: Routes = [
  {path: '', component: PilotHomeComponent},
  { path: 'new', component: PilotNewComponent },
  { path: ':id', component: PilotDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Pilot-detail-permissions'
      }
    }
  },{
    path: ':pilot_id/PilotLicense', loadChildren: () => import('../PilotLicense/PilotLicense.module').then(m => m.PilotLicenseModule),
    data: {
        oPermission: {
            permissionId: 'PilotLicense-detail-permissions'
        }
    }
}
];

export const PILOT_MODULE_DECLARATIONS = [
    PilotHomeComponent,
    PilotNewComponent,
    PilotDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PilotRoutingModule { }