import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { AuthComponent } from './pages/auth/auth.component';
import { RegistComponent } from './pages/regist/regist.component';
import { RecoverComponent } from './pages/recover/recover.component';
import { MainComponent } from './pages/main/main.component';

const routes: Routes = [
  { path: 'auth', component: AuthComponent},
  { path: 'regist', component: RegistComponent},
  { path: 'recover', component: RecoverComponent},
  { path: '**', component: MainComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
