import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { NgZorroAntdModule, NZ_I18N, ru_RU } from 'ng-zorro-antd';
import { AppComponent } from './app.component';

/** config angular i18n **/
import { registerLocaleData } from '@angular/common';
import ru from '@angular/common/locales/ru';
import { AuthComponent } from './pages/auth/auth.component';
import { RegistComponent } from './pages/regist/regist.component';

import { RecoverComponent } from './pages/recover/recover.component';
import { MainComponent } from './pages/main/main.component';
import { HeaderComponent } from './pages/main/header/header.component';
registerLocaleData(ru);

@NgModule({
  declarations: [
    AppComponent,
    AuthComponent,
    RegistComponent,
    RecoverComponent,
    MainComponent,
    HeaderComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    BrowserAnimationsModule,
    NgZorroAntdModule
  ],
  bootstrap: [ AppComponent ],
  providers   : [
    { provide: NZ_I18N, useValue: ru_RU }
  ]
})
export class AppModule { }