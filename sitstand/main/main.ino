int trig_pin = 3;
int echo_pin = 2;

int tp_pin_a = A3;
int tp_pin_b = A4;
int test_a = A1;
int test_b = A2;

int n = 0;
int smoothed_a = 0;

void setup() {
  // put your setup code here, to run once:
  
  pinMode(trig_pin,OUTPUT);
  pinMode(echo_pin,INPUT);
  pinMode(tp_pin_a,OUTPUT);
  pinMode(tp_pin_b,OUTPUT);
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  //Serial.println("Hello");
  /*
  int val_a = analogRead(tp_pin_a);
  int val_b = analogRead(tp_pin_b);
  smoothed_a = (smoothed_a * n-1 + val_a) / n;
  Serial.print(val_a*5/1023);
  Serial.print(" ");
  Serial.print(val_b*5/1023);
  Serial.print(" ");
  Serial.print(smoothed_a);
  Serial.print(" ");
  Serial.println((val_b-val_a)*5/1023);
  delay(10);
  n = n+1;
  */
  analogWrite(tp_pin_a,0);
  analogWrite(tp_pin_b,5);
  int ta = analogRead(test_a);
  int tb = analogRead(test_b);

  Serial.print(ta);
  Serial.print(" ");
  Serial.println(tb);
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
