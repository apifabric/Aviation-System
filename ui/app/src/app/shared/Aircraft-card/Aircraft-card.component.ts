import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Aircraft-card.component.html',
  styleUrls: ['./Aircraft-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Aircraft-card]': 'true'
  }
})

export class AircraftCardComponent {


}