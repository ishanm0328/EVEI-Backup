int rpm;
String analog_a;
String analog_b;
int energy;
int gyro_x;
int gyro_y;
int gyro_z;
char digital = 'D';

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  randomSeed(0);
}

String format(int rpm, double analog_a, double analog_b, char digital,int energy, int gyro_x, int gyro_y, int gyro_z) {
  //String formatted_string = "RM" + String(rpm) + "A" + String(analog_a) + "B" + String(analog_b) + String(digital) + "\nE"+ String(gyro_x) + String(gyro_y) + String(gyro_z) + "\n";
  return "RM" + String(rpm) + "A" + String(analog_a) + "B" + String(analog_b) + String(digital) + "\nE"+ String(gyro_x) + String(gyro_y) + String(gyro_z) + "\n";
}

void loop() {
  // put your main code here, to run repeatedly:
  String temp_string;

  rpm = int(random(0,300));
  analog_a = String(int(random(0,5))) + ".5";
  analog_b = String(int(random(0,5))) + ".5";
  //energy = int(random(0,9999));
  energy = 99;
  //gyro_x = int(random(-20,20));
  gyro_x = 0;
  //gyro_y = int(random(-20,20));
  gyro_y = 10;
//  gyro_z = int(random(-20,20));
  gyro_z = 0;

  temp_string = "RM" + String(rpm) + "A" + String(analog_a) + "B" + String(analog_b) + String(digital) + "\nE" + String(energy) + " +" + String(gyro_x) + " +" + String(gyro_y) + " +" + String(gyro_z) + "\n";
  char* formatted_string = (char*) malloc(sizeof(char)* (temp_string.length() + 1));
  temp_string.toCharArray(formatted_string, temp_string.length() + 1);
  Serial.write(formatted_string);
  free(formatted_string);
  delay(500);
}
