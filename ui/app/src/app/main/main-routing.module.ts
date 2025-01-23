import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MainComponent } from './main.component';

export const routes: Routes = [
  {
    path: '', component: MainComponent,
    children: [
        { path: '', redirectTo: 'home', pathMatch: 'full' },
        { path: 'about', loadChildren: () => import('./about/about.module').then(m => m.AboutModule) },
        { path: 'home', loadChildren: () => import('./home/home.module').then(m => m.HomeModule) },
        { path: 'settings', loadChildren: () => import('./settings/settings.module').then(m => m.SettingsModule) },
      
    
        { path: 'Aircraft', loadChildren: () => import('./Aircraft/Aircraft.module').then(m => m.AircraftModule) },
    
        { path: 'AircraftMaintenance', loadChildren: () => import('./AircraftMaintenance/AircraftMaintenance.module').then(m => m.AircraftMaintenanceModule) },
    
        { path: 'Airline', loadChildren: () => import('./Airline/Airline.module').then(m => m.AirlineModule) },
    
        { path: 'Airport', loadChildren: () => import('./Airport/Airport.module').then(m => m.AirportModule) },
    
        { path: 'AirportFacility', loadChildren: () => import('./AirportFacility/AirportFacility.module').then(m => m.AirportFacilityModule) },
    
        { path: 'Baggage', loadChildren: () => import('./Baggage/Baggage.module').then(m => m.BaggageModule) },
    
        { path: 'Booking', loadChildren: () => import('./Booking/Booking.module').then(m => m.BookingModule) },
    
        { path: 'CrewMember', loadChildren: () => import('./CrewMember/CrewMember.module').then(m => m.CrewMemberModule) },
    
        { path: 'Flight', loadChildren: () => import('./Flight/Flight.module').then(m => m.FlightModule) },
    
        { path: 'Passenger', loadChildren: () => import('./Passenger/Passenger.module').then(m => m.PassengerModule) },
    
        { path: 'Pilot', loadChildren: () => import('./Pilot/Pilot.module').then(m => m.PilotModule) },
    
        { path: 'PilotLicense', loadChildren: () => import('./PilotLicense/PilotLicense.module').then(m => m.PilotLicenseModule) },
    
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MainRoutingModule { }