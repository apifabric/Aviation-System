import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'CrewMember-new',
  templateUrl: './CrewMember-new.component.html',
  styleUrls: ['./CrewMember-new.component.scss']
})
export class CrewMemberNewComponent {
  @ViewChild("CrewMemberForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}