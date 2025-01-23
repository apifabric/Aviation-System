import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BaggageHomeComponent } from './home/Baggage-home.component';
import { BaggageNewComponent } from './new/Baggage-new.component';
import { BaggageDetailComponent } from './detail/Baggage-detail.component';

const routes: Routes = [
  {path: '', component: BaggageHomeComponent},
  { path: 'new', component: BaggageNewComponent },
  { path: ':id', component: BaggageDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Baggage-detail-permissions'
      }
    }
  }
];

export const BAGGAGE_MODULE_DECLARATIONS = [
    BaggageHomeComponent,
    BaggageNewComponent,
    BaggageDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class BaggageRoutingModule { }