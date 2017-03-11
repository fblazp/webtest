#include <LiquidCrystal.h>

LiquidCrystal lcd(8,9,4,5,6,7);

void setup()
{
  Serial.begin(9600);
  lcd.begin(16,2);
}

void loop()
{
  int lectura = analogRead(A0);
  Serial.println(lectura);
  if(lectura == 0)
  {
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Derecha");
  }
  else if(lectura == 410)
  {
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Izquierda");
  }
  else if(lectura == 100)
  {
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Arriba");
  }
  else if(lectura == 256)
  {
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Abajo");
  }
  else if(lectura == 640)
  {
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Select");
  }
  else if(lectura <=1023 && lectura>=1020)
  {
    lcd.clear();
    lcd.setCursor(2,0);
    lcd.print("Pulsa un boton");
  }
  delay(50);
}
