//Wifi control lib
#include<WiFi.h>


//SSID and Password
const char* ssid = "ESP32";
const char* password = "123456789";

//webserver on port 80
WiFiServer server(80);

//HTTP var
String http_header;

//Data vars
double temp = 0;
double hum = 0;;
double light = 0;
bool movement = false;


void setup() {
  //setup serial monitor to pc
  Serial.begin(115200);

  //setup serial to BeagleBone on uart2
  Serial2.begin(115200,SERIAL_8N1,16,17);

  //Set up access point with credentials
  WiFi.softAP(ssid, password);
  IPAddress IP = WiFi.softAPIP();
  Serial.print("Access point IP address is: ");
  Serial.println(IP);

  server.begin();

}

void loop() {
  //Listen for incoming clients
  WiFiClient http_client = server.available();
  
  //New client connects
  if(http_client) {
    Serial.println("New client.");
    
    String curline = "";
    while(http_client.connected()) {
      if(http_client.available()) {
    
        char c = http_client.read();
  
        Serial.write(c);
        
        http_header += c;
        if(c == '\n') {
          // 2 newline characters in a row means end of http request
          if (curline.length() == 0) {
            //sending response to client
            http_client.println("HTTP/1.1 200 OK");
            http_client.println("Content-type:text/html");
            http_client.println("Connection: close");
            http_client.println();
            
  
            //Parse the data
            String content = http_header.substring(2);
            switch (http_header.charAt(0)) {
              case 'T': temp = content.toDouble(); break;
              case 'H': hum = content.toDouble(); break;
              case 'L': light = content.toDouble(); break;
            }
  
            //another blank line to end response
            http_client.println();
            
          } else {
            curline = "";
          }
        } else if (c != '\r') curline += c;
      }
    }
    //Clear header, close connection
    http_header = "";
    http_client.stop();
  }

  
  //check if BeagleBone is requesting data
  String command = "";
  if(Serial2.available()) {
    command = Serial2.readString();
    
    if (command == "get temperature") 
      Serial2.println(temp,4);
    else if (command == "get humidity")
      Serial2.println(hum,4);
    else if (command == "get luminosity")
      Serial2.println(light,4);
    else {
      Serial2.print("Error: Command not known: ");
      Serial2.println(command);
      Serial.println(command);
    }
  }
  






  

}
