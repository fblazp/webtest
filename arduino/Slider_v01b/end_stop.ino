bool endStop()
{
  bool stopRead = digitalRead(STOP);
  return stopRead; 
}

