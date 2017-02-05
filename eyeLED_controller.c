#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
  #include <avr/power.h>
#endif

#define PIN 6

// Two pixels, hooked up to pin 6, using GRB and KHZ800
Adafruit_NeoPixel strip = Adafruit_NeoPixel(2, PIN, NEO_GRB + NEO_KHZ800);

void FlickerWhite(uint16_t times, uint32_t delayMod);

void GradientRed(uint16_t times, uint32_t delayMod);

uint8_t rightEyeRed = 0;
uint8_t rightEyeBlue = 0;
uint8_t rightEyeGreen = 0;

uint8_t leftEyeRed = 0;
uint8_t leftEyeBlue = 0;
uint8_t leftEyeGreen = 0;

uint8_t mode = 0;

uint16_t iterationTimes = 10; 
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
  //leftEyeRed = Serial.read();
  //leftEyeGreen = Serial.read();
  //leftEyeBlue = Serial.read();

  String inputData;

  while (Serial.read() != '$')
  {
    
  }


//Read Mode
  inputData = Serial.readStringUntil(':');
  mode = inputData.toInt();

//Read Red Color
 inputData = Serial.readStringUntil(',');
 leftEyeRed = inputData.toInt();
 rightEyeRed = inputData.toInt();

 //Read Green Color
 inputData = Serial.readStringUntil(',');
 leftEyeGreen = inputData.toInt();
 rightEyeGreen = inputData.toInt();

 //Read Blue Color
 inputData = Serial.readStringUntil('#');
 leftEyeBlue = inputData.toInt();
 rightEyeBlue = inputData.toInt();
 


}


void loop() 
{
  if(mode == 0)
    Static();
    
  if(mode == 1)
    Flicker();
    
  if(mode == 2)
    Gradient();
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

