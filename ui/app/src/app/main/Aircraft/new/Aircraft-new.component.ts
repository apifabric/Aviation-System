import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Aircraft-new',
  templateUrl: './Aircraft-new.component.html',
  styleUrls: ['./Aircraft-new.component.scss']
})
export class AircraftNewComponent {
  @ViewChild("AircraftForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}