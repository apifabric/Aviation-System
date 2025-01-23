import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Baggage-card.component.html',
  styleUrls: ['./Baggage-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Baggage-card]': 'true'
  }
})

export class BaggageCardComponent {


}