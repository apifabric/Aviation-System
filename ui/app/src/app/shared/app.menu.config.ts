import { MenuRootItem } from 'ontimize-web-ngx';

import { AircraftCardComponent } from './Aircraft-card/Aircraft-card.component';

import { AircraftMaintenanceCardComponent } from './AircraftMaintenance-card/AircraftMaintenance-card.component';

import { AirlineCardComponent } from './Airline-card/Airline-card.component';

import { AirportCardComponent } from './Airport-card/Airport-card.component';

import { AirportFacilityCardComponent } from './AirportFacility-card/AirportFacility-card.component';

import { BaggageCardComponent } from './Baggage-card/Baggage-card.component';

import { BookingCardComponent } from './Booking-card/Booking-card.component';

import { CrewMemberCardComponent } from './CrewMember-card/CrewMember-card.component';

import { FlightCardComponent } from './Flight-card/Flight-card.component';

import { PassengerCardComponent } from './Passenger-card/Passenger-card.component';

import { PilotCardComponent } from './Pilot-card/Pilot-card.component';

import { PilotLicenseCardComponent } from './PilotLicense-card/PilotLicense-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Aircraft', name: 'AIRCRAFT', icon: 'view_list', route: '/main/Aircraft' }
    
        ,{ id: 'AircraftMaintenance', name: 'AIRCRAFTMAINTENANCE', icon: 'view_list', route: '/main/AircraftMaintenance' }
    
        ,{ id: 'Airline', name: 'AIRLINE', icon: 'view_list', route: '/main/Airline' }
    
        ,{ id: 'Airport', name: 'AIRPORT', icon: 'view_list', route: '/main/Airport' }
    
        ,{ id: 'AirportFacility', name: 'AIRPORTFACILITY', icon: 'view_list', route: '/main/AirportFacility' }
    
        ,{ id: 'Baggage', name: 'BAGGAGE', icon: 'view_list', route: '/main/Baggage' }
    
        ,{ id: 'Booking', name: 'BOOKING', icon: 'view_list', route: '/main/Booking' }
    
        ,{ id: 'CrewMember', name: 'CREWMEMBER', icon: 'view_list', route: '/main/CrewMember' }
    
        ,{ id: 'Flight', name: 'FLIGHT', icon: 'view_list', route: '/main/Flight' }
    
        ,{ id: 'Passenger', name: 'PASSENGER', icon: 'view_list', route: '/main/Passenger' }
    
        ,{ id: 'Pilot', name: 'PILOT', icon: 'view_list', route: '/main/Pilot' }
    
        ,{ id: 'PilotLicense', name: 'PILOTLICENSE', icon: 'view_list', route: '/main/PilotLicense' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    AircraftCardComponent

    ,AircraftMaintenanceCardComponent

    ,AirlineCardComponent

    ,AirportCardComponent

    ,AirportFacilityCardComponent

    ,BaggageCardComponent

    ,BookingCardComponent

    ,CrewMemberCardComponent

    ,FlightCardComponent

    ,PassengerCardComponent

    ,PilotCardComponent

    ,PilotLicenseCardComponent

];