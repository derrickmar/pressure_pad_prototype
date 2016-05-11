int in1 = A2; // A4
int in2 = A3; // A3
int in3 = A4; // A1
int in4 = A5; // A0
int in5 = A6; // A5
int in6 = A7; // skip
int in7 = A8; // A8
//int in8 = A9; // tailbone (5)
int in9 = A10; // A6


// the setup routine runs once when you press reset:
void setup() {
  pinMode(in1, INPUT);
  pinMode(in2, INPUT);
  pinMode(in3, INPUT);
  pinMode(in4, INPUT);
  pinMode(in5, INPUT);
  pinMode(in6, INPUT);
  pinMode(in7, INPUT);
  //  pinMode(in8, INPUT);
  pinMode(in9, INPUT);

  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {

  int val1 = analogRead(in1);
//  int val2 = analogRead(in2);
//  int val3 = analogRead(in3); 
  int val4 = analogRead(in4);
  int val5 = analogRead(in5);
  int val6 = analogRead(in6);
//  int val7 = analogRead(in7);
  //  int val8 = analogRead(in8);
  int val9 = analogRead(in9);


  Serial.print(analogRead(val1)); // right leg
  Serial.print("|");
//  Serial.print(analogRead(val2));
//  Serial.print("|");
//  Serial.print(analogRead(val3));
//  Serial.print("|");
  Serial.print(analogRead(val4)); // right butt
  Serial.print("|");
  Serial.print(analogRead(val5)); // tailbone
  Serial.print("|");
  Serial.print(analogRead(val6)); // left butt
  Serial.print("|");
//  Serial.print(analogRead(val7));
//  Serial.print("|");
  //  Serial.print(analogRead(val8));
  //  Serial.print("  ");
  Serial.println(analogRead(val9)); //left leg
  delay(50);
}
