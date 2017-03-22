#define SLEEP 7
#define DIR 8
#define STEP 9
#define LED 13
#define STOP 12

void setup()
{
   Serial.begin(9600);
   pinMode(SLEEP, OUTPUT);
   pinMode(LED, OUTPUT);
   pinMode(DIR, OUTPUT);
   pinMode(STEP, OUTPUT);
   pinMode(STOP, OUTPUT);
   digitalWrite(SLEEP, LOW);
}
 
void loop()
{
  motorRun(1,1,200);
}
