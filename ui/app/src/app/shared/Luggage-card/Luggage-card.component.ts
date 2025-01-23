import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Luggage-card.component.html',
  styleUrls: ['./Luggage-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Luggage-card]': 'true'
  }
})

export class LuggageCardComponent {


}