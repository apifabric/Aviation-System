import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CrewMemberHomeComponent } from './home/CrewMember-home.component';
import { CrewMemberNewComponent } from './new/CrewMember-new.component';
import { CrewMemberDetailComponent } from './detail/CrewMember-detail.component';

const routes: Routes = [
  {path: '', component: CrewMemberHomeComponent},
  { path: 'new', component: CrewMemberNewComponent },
  { path: ':id', component: CrewMemberDetailComponent,
    data: {
      oPermission: {
        permissionId: 'CrewMember-detail-permissions'
      }
    }
  }
];

export const CREWMEMBER_MODULE_DECLARATIONS = [
    CrewMemberHomeComponent,
    CrewMemberNewComponent,
    CrewMemberDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CrewMemberRoutingModule { }