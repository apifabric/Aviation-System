import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'AirportFacility-new',
  templateUrl: './AirportFacility-new.component.html',
  styleUrls: ['./AirportFacility-new.component.scss']
})
export class AirportFacilityNewComponent {
  @ViewChild("AirportFacilityForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}