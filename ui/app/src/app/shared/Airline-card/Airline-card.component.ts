import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Airline-card.component.html',
  styleUrls: ['./Airline-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Airline-card]': 'true'
  }
})

export class AirlineCardComponent {


}