#include <LiquidCrystalRus.h>
#include <Firmata.h>

LiquidCrystalRus lcd(9, 8, 5, 4, 3, 2);
int lastLine = 1;

void stringDataCallback(char *stringData){
   if ( lastLine ) {
     lastLine = 0;
     lcd.clear();
   } else {
     lastLine = 1;
     lcd.setCursor(0,1);
   }
   lcd.print(stringData);
}

void setup() {
  lcd.begin(16,2);
  Firmata.setFirmwareVersion( FIRMATA_MAJOR_VERSION, FIRMATA_MINOR_VERSION );
  Firmata.attach( STRING_DATA, stringDataCallback);
  Firmata.begin();
}

void loop() {
  while ( Firmata.available() ) {
    Firmata.processInput();
  }
}