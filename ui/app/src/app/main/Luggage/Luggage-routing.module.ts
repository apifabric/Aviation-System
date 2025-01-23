import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LuggageHomeComponent } from './home/Luggage-home.component';
import { LuggageNewComponent } from './new/Luggage-new.component';
import { LuggageDetailComponent } from './detail/Luggage-detail.component';

const routes: Routes = [
  {path: '', component: LuggageHomeComponent},
  { path: 'new', component: LuggageNewComponent },
  { path: ':id', component: LuggageDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Luggage-detail-permissions'
      }
    }
  }
];

export const LUGGAGE_MODULE_DECLARATIONS = [
    LuggageHomeComponent,
    LuggageNewComponent,
    LuggageDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class LuggageRoutingModule { }