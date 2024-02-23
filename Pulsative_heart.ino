#include <FastLED.h>
#define NUM_LEDS 18
#define LEDPIN 4 // GPIO4 on the ESP32 C3 

CRGB leds[NUM_LEDS];

void setup() { 
  FastLED.addLeds<NEOPIXEL, LEDPIN>(leds, NUM_LEDS); 
  for (int i=0;i<NUM_LEDS; i++){
   leds[i] = CRGB (255,0,0);    
  }
}

void loop() {
  for (int i=0;i<75; i++){
    FastLED.setBrightness(i);
    FastLED.show();
    //delay(10);
  }
  for (int i=75;i>0; i--){
    FastLED.setBrightness(i);
    FastLED.show();
    //delay(10);
  }
  for (int i=0;i<75; i++){
    FastLED.setBrightness(i);
    FastLED.show();
    //delay(10);
  }
 for (int i=75;i>0; i--){
    FastLED.setBrightness(i);
    FastLED.show();
    delay(10);
  }
}
