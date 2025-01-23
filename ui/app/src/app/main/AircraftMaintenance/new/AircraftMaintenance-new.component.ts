import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'AircraftMaintenance-new',
  templateUrl: './AircraftMaintenance-new.component.html',
  styleUrls: ['./AircraftMaintenance-new.component.scss']
})
export class AircraftMaintenanceNewComponent {
  @ViewChild("AircraftMaintenanceForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}