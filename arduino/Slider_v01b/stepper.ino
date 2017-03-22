//Iniciar el motor
int motorRun(int velocity, int dir, int angle)
{
  motorDir(dir);
  for(int i=0;i<angle; i++)
  {
    digitalWrite(STEP, HIGH);
    delay(velocity);
    digitalWrite(STEP, LOW);
    delay(velocity);
  }
}
//Dirección del motor
bool motorDir(bool dirState)
{
  digitalWrite(DIR, dirState);
}

