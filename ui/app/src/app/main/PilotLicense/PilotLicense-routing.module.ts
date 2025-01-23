import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PilotLicenseHomeComponent } from './home/PilotLicense-home.component';
import { PilotLicenseNewComponent } from './new/PilotLicense-new.component';
import { PilotLicenseDetailComponent } from './detail/PilotLicense-detail.component';

const routes: Routes = [
  {path: '', component: PilotLicenseHomeComponent},
  { path: 'new', component: PilotLicenseNewComponent },
  { path: ':id', component: PilotLicenseDetailComponent,
    data: {
      oPermission: {
        permissionId: 'PilotLicense-detail-permissions'
      }
    }
  }
];

export const PILOTLICENSE_MODULE_DECLARATIONS = [
    PilotLicenseHomeComponent,
    PilotLicenseNewComponent,
    PilotLicenseDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PilotLicenseRoutingModule { }