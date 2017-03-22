int leerSerial()
{
  if(Serial.available())
  {
    char serialInput = Serial.read();
    return serialInput;
  }
}
