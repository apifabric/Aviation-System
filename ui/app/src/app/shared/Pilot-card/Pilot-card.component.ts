import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Pilot-card.component.html',
  styleUrls: ['./Pilot-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Pilot-card]': 'true'
  }
})

export class PilotCardComponent {


}