#include <LiquidCrystal.h>

LiquidCrystal lcd(8,9,4,5,6,7);

String menuOptions[3]={"Motor","Sensores","LCD Setup"};

int lcd_key = 0;
int adc_key_in = 0;

#define btnLEFT 0
#define btnUP 1
#define btnDOWN 2
#define btnRIGHT 3
#define btnSELECT 4
#define btnNONE 5

int menuPos = 0;
int submenuPos = 0;
int menuItems = 2;

void setup()
{
  Serial.begin(9600);
  lcd.begin(16,2);
}

void loop()
{
  
}
