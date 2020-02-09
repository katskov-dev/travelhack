import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { AuthComponent } from './pages/auth/auth.component';
import { RecoverComponent } from './pages/recover/recover.component';
import { MainComponent } from './pages/main/main.component';
import { MapComponent } from './pages/map/map.component';
import { TourComponent } from './pages/tour/tour.component';

const routes: Routes = [
  { path: 'auth', component: AuthComponent},
  { path: 'recover', component: RecoverComponent},
  { path: 'map', component: MapComponent},
  { path: 'tour', component: TourComponent},
  { path: '**', component: MainComponent },

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
