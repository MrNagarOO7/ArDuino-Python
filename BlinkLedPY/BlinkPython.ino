#define LED 13

void setup(){
  pinMode(LED , OUTPUT);
  Serial.begin(9600);
}

void loop(){
   if(Serial.available()){
    char  sListner = Serial.read();
    if(sListner == 'L'){
      digitalWrite(LED , LOW);
    }
  
    if(sListner == 'H' ){
      digitalWrite(LED , HIGH);
    }
  }
}
