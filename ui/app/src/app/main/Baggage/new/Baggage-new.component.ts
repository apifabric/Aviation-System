import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Baggage-new',
  templateUrl: './Baggage-new.component.html',
  styleUrls: ['./Baggage-new.component.scss']
})
export class BaggageNewComponent {
  @ViewChild("BaggageForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}