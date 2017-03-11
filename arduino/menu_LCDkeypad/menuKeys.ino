int buttonValue()
{
  int tecla = analogRead(A0);
  lcd.setCursor(0,0);
  lcd.clear();
  lcd.print(tecla);
  delay(150);
}

int read_LCD_buttons()
{
  adc_key_in = analogRead(A0);
  if(adc_key_in > 1000) return btnNONE;
  if(adc_key_in == 410) return btnLEFT;
  if(adc_key_in == 100) return btnUP;
  if(adc_key_in == 256) return btnDOWN;
  if(adc_key_in == 0)   return btnRIGHT;
  if(adc_key_in == 640) return btnSELECT;
  return btnNONE;
}

int menuNav(int keyVal)
{
  switch(keyVal)
  {
    case 0:
      menuPos --;
      if(menuPos<0)
      {
        menuPos = menuItems;
      }
      break;
    case 3:
      menuPos ++;
      if(menuPos>menuItems)
      {
        menuPos = 0;
      }
      break;
  }
}

