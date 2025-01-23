import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './PilotLicense-card.component.html',
  styleUrls: ['./PilotLicense-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.PilotLicense-card]': 'true'
  }
})

export class PilotLicenseCardComponent {


}