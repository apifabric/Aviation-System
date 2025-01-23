import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './AircraftMaintenance-card.component.html',
  styleUrls: ['./AircraftMaintenance-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.AircraftMaintenance-card]': 'true'
  }
})

export class AircraftMaintenanceCardComponent {


}