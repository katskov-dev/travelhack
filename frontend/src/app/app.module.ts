import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { CookieService } from 'ngx-cookie-service';

import { AuthComponent } from './pages/auth/auth.component';
import { NgZorroAntdModule, NZ_I18N, ru_RU } from 'ng-zorro-antd';

import { registerLocaleData } from '@angular/common';
import ru from '@angular/common/locales/ru';
import { RegistComponent } from './pages/regist/regist.component';
import { RecoverComponent } from './pages/recover/recover.component';
import { MainComponent } from './pages/main/main.component';
import { HeaderComponent } from './pages/main/header/header.component';
registerLocaleData(ru);

import { ChatComponent } from './pages/main/chat/chat.component';

import { MapComponent } from './pages/map/map.component';
import { TourComponent } from './pages/tour/tour.component';

// import { SocketIoModule, SocketIoConfig } from 'ngx-socket-io';
// const config: SocketIoConfig = { url: 'http://localhost:8988', options: {} };


@NgModule({
  declarations: [
    AppComponent,
    AuthComponent,
    RegistComponent,
    RecoverComponent,
    MainComponent,
    HeaderComponent,
    ChatComponent,
    MapComponent,
    TourComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    BrowserAnimationsModule,
    NgZorroAntdModule,
    // SocketIoModule.forRoot(config)
  ],
  providers: [
    CookieService,
    { provide: NZ_I18N, useValue: ru_RU }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
