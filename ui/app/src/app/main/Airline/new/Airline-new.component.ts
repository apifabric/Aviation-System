import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Airline-new',
  templateUrl: './Airline-new.component.html',
  styleUrls: ['./Airline-new.component.scss']
})
export class AirlineNewComponent {
  @ViewChild("AirlineForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}