int trig_pin = 3;
int echo_pin = 2;

void setup() {
  // put your setup code here, to run once:

  pinMode(trig_pin,OUTPUT);
  pinMode(echo_pin,INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  //long duration = get_distance();
  //Serial.println(duration_to_length(duration));
  
}

long get_distance(){
  digitalWrite(trig_pin,LOW);
  delayMicroseconds(2);

  digitalWrite(trig_pin,HIGH);
  delayMicroseconds(10);
  digitalWrite(trig_pin,LOW);

  return pulseIn(echo_pin,HIGH);
}

long duration_to_length(long d){
  return d*0.034/2;
}
