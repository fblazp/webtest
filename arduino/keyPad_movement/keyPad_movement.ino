#include <LiquidCrystal.h>

LiquidCrystal lcd(8,9,4,5,6,7);

int posHor = 0;
int posVer = 0;

void setup()
{
  Serial.begin(9600);
  lcd.begin(16,2);
  lcd.setCursor(posHor,posVer);
  lcd.print('*');
}

void loop()
{
  lcd.setCursor(posHor,posVer);
  lcd.print('*');
  int tecla = analogRead(A0);
  if(tecla == 0)
  {
    lcd.clear();
    posHor ++;
    if(posHor>15)
    {
      posHor = 0;
    }
  }
  else if(tecla == 410)
  {
    lcd.clear();
    posHor --;
    if(posHor<0)
    {
      posHor = 15;
    }
  }
  else if(tecla == 256)
  {
    lcd.clear();
    posVer ++;
    if(posVer>1)
    {
      posVer = 0;
    }
  }
  else if(tecla == 100)
  {
    lcd.clear();
    posVer --;
    if(posVer<0)
    {
      posVer = 1;
    }
  }
  delay(125);
}
