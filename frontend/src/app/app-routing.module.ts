import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

const routes: Routes = [
  { path: '**',  },
];

@NgModule({
  imports: [],
  exports: [RouterModule]
})
export class AppRoutingModule { }
