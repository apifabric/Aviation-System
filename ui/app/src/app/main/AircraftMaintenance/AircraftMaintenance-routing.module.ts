import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AircraftMaintenanceHomeComponent } from './home/AircraftMaintenance-home.component';
import { AircraftMaintenanceNewComponent } from './new/AircraftMaintenance-new.component';
import { AircraftMaintenanceDetailComponent } from './detail/AircraftMaintenance-detail.component';

const routes: Routes = [
  {path: '', component: AircraftMaintenanceHomeComponent},
  { path: 'new', component: AircraftMaintenanceNewComponent },
  { path: ':id', component: AircraftMaintenanceDetailComponent,
    data: {
      oPermission: {
        permissionId: 'AircraftMaintenance-detail-permissions'
      }
    }
  }
];

export const AIRCRAFTMAINTENANCE_MODULE_DECLARATIONS = [
    AircraftMaintenanceHomeComponent,
    AircraftMaintenanceNewComponent,
    AircraftMaintenanceDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AircraftMaintenanceRoutingModule { }