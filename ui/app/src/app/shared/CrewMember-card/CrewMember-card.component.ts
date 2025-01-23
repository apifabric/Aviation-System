import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './CrewMember-card.component.html',
  styleUrls: ['./CrewMember-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.CrewMember-card]': 'true'
  }
})

export class CrewMemberCardComponent {


}