import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './AirportFacility-card.component.html',
  styleUrls: ['./AirportFacility-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.AirportFacility-card]': 'true'
  }
})

export class AirportFacilityCardComponent {


}