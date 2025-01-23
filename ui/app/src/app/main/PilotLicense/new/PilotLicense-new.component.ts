import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'PilotLicense-new',
  templateUrl: './PilotLicense-new.component.html',
  styleUrls: ['./PilotLicense-new.component.scss']
})
export class PilotLicenseNewComponent {
  @ViewChild("PilotLicenseForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}