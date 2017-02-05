#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
  #include <avr/power.h>
#endif

#define PIN 6

// Two pixels, hooked up to pin 6, using GRB and KHZ800
Adafruit_NeoPixel strip = Adafruit_NeoPixel(2, PIN, NEO_GRB + NEO_KHZ800);

void swap(uint8_t& x, uint8_t& y);
void Static();
void Flicker();
void Gradient();
void AltFlicker();
void AltGradient();

uint8_t rightEyeRed = 0;
uint8_t rightEyeBlue = 0;
uint8_t rightEyeGreen = 0;

uint8_t leftEyeRed = 0;
uint8_t leftEyeBlue = 0;
uint8_t leftEyeGreen = 0;

uint8_t mode = 0;

int tempInt = 0;
uint32_t delayMod = 100;


void setup() {

  // This is for Trinket 5V 16MHz, you can remove these three lines if you are not using a Trinket
  #if defined (__AVR_ATtiny85__)
    if (F_CPU == 16000000) clock_prescale_set(clock_div_1);
  #endif
  // End of trinket special code

  strip.begin();
  strip.show(); // Initialize all pixels to 'off'

  Serial.begin(9600);
}

void serialEvent()
{

  String inputData;

  while (Serial.read() != '$')
  {
    
  }

  //Read Mode
  inputData = Serial.readStringUntil(',');
  mode = inputData.toInt();

  inputData = Serial.readStringUntil(':');
  delayMod = inputData.toInt();

//Read Left Red Color
 inputData = Serial.readStringUntil(',');
 tempInt = inputData.toInt();
 if(tempInt < 0)
  tempInt = 0;
 if(tempInt > 255)
  tempInt = 255;

  leftEyeRed = tempInt;

 //Read Left Green Color
 inputData = Serial.readStringUntil(',');
 tempInt = inputData.toInt();
 if(tempInt < 0)
  tempInt = 0;
 if(tempInt > 255)
  tempInt = 255;
  
 leftEyeGreen = tempInt;

 //Read Left Blue Color
 inputData = Serial.readStringUntil(';');
 tempInt = inputData.toInt();
 if(tempInt < 0)
  tempInt = 0;
 if(tempInt > 255)
  tempInt = 255;
  
 leftEyeBlue = tempInt;

 //Read Right Red Color
 inputData = Serial.readStringUntil(',');
 tempInt = inputData.toInt();
 if(tempInt < 0)
  tempInt = 0;
 if(tempInt > 255)
  tempInt = 255;
  
 rightEyeRed = tempInt;

 //Read Right Green Color
 inputData = Serial.readStringUntil(',');
 tempInt = inputData.toInt();
 if(tempInt < 0)
  tempInt = 0;
 if(tempInt > 255)
  tempInt = 255;
  
 rightEyeGreen = tempInt;

 //Read Right Blue Color
 inputData = Serial.readStringUntil('#');
 tempInt = inputData.toInt();
 if(tempInt < 0)
  tempInt = 0;
 if(tempInt > 255)
  tempInt = 255;
  
 rightEyeBlue = tempInt;


}


void loop() 
{
  if(mode == 0)
    Static();
    
  if(mode == 1)
    Flicker();
    
  if(mode == 2)
    Gradient();

  if(mode == 3)
    AltFlicker();

  if(mode == 4)
    AltGradient();
}

// Constant color and brightness
void Static()
{
  strip.setPixelColor(0, leftEyeRed, leftEyeGreen, leftEyeBlue);
  strip.setPixelColor(1, rightEyeRed, rightEyeGreen, rightEyeBlue);
  strip.show();
}

// Flicker/Strobe lighting effect
void Flicker()
{
  if(delayMod == 0)
  {
    delayMod = 1;
  }
    for(uint16_t count = 0; count < 2; ++count)
    {
      if( count%2 == 0 )
      {
        strip.setPixelColor(0, leftEyeRed, leftEyeGreen, leftEyeBlue);
        strip.setPixelColor(1, rightEyeRed, rightEyeGreen, rightEyeBlue);
      }
      else
      {
        strip.setPixelColor(0, 0, 0, 0);
        strip.setPixelColor(1, 0, 0, 0);
      }

      strip.show();
      delay(delayMod);
    }
}

// Smooth alternating light effect
void Gradient()
{

  for(uint32_t j = 0; j < 100; ++j){
      
    strip.setPixelColor(0, (leftEyeRed * j)/100, (leftEyeGreen * j)/100, (leftEyeBlue * j)/100); 
    strip.setPixelColor(1, (rightEyeRed * j)/100, (rightEyeGreen * j)/100, (rightEyeBlue * j)/100); 

    strip.show();
    delay(delayMod/10);
    }

  for(uint32_t j = 100; j > 0; --j){
      
    strip.setPixelColor(0, (leftEyeRed * j)/100, (leftEyeGreen * j)/100, (leftEyeBlue * j)/100);
    strip.setPixelColor(1, (rightEyeRed * j)/100, (rightEyeGreen * j)/100, (rightEyeBlue * j)/100); 

    strip.show();
    delay(delayMod/10);
  }
}

void AltFlicker()
{
  if(delayMod == 0)
  {
    delayMod = 1;
  }
    for(uint16_t count = 0; count < 2; ++count)
    {
      if( count%2 == 0 )
      {
        strip.setPixelColor(0, leftEyeRed, leftEyeGreen, leftEyeBlue);
        strip.setPixelColor(1, rightEyeRed, rightEyeGreen, rightEyeBlue);
      }
      else
      {
        strip.setPixelColor(0, 0, 0, 0);
        strip.setPixelColor(1, 0, 0, 0);
      }

      strip.show();
      delay(delayMod);
    }

  swap(rightEyeRed, leftEyeRed);
  swap(rightEyeBlue, leftEyeBlue);
  swap(rightEyeGreen, leftEyeGreen);
}

void AltGradient()
{

  for(uint32_t j = 0; j < 100; ++j){
      
    strip.setPixelColor(0, (leftEyeRed * j)/100, (leftEyeGreen * j)/100, (leftEyeBlue * j)/100); 
    strip.setPixelColor(1, (rightEyeRed * j)/100, (rightEyeGreen * j)/100, (rightEyeBlue * j)/100); 

    strip.show();
    delay(delayMod/10);
    }

  for(uint32_t j = 100; j > 0; --j){
      
    strip.setPixelColor(0, (leftEyeRed * j)/100, (leftEyeGreen * j)/100, (leftEyeBlue * j)/100);
    strip.setPixelColor(1, (rightEyeRed * j)/100, (rightEyeGreen * j)/100, (rightEyeBlue * j)/100); 

    strip.show();
    delay(delayMod/10);
  }

  swap(rightEyeRed, leftEyeRed);
  swap(rightEyeBlue, leftEyeBlue);
  swap(rightEyeGreen, leftEyeGreen);
}


void swap(uint8_t& x, uint8_t& y)
{
  uint8_t temp;

  temp = x;
  x = y;
  y = temp;
}

