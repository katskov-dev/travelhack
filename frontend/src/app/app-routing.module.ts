import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { AuthComponent } from './pages/auth/auth.component';
import { RegistComponent } from './pages/regist/regist.component';
import { RecoverComponent } from './pages/recover/recover.component';
import { MainComponent } from './pages/main/main.component';
import { MapComponent } from './map/map.component';
import { TourComponent } from './tour/tour.component';

const routes: Routes = [
  { path: 'auth', component: AuthComponent},
  { path: 'regist', component: RegistComponent},
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
