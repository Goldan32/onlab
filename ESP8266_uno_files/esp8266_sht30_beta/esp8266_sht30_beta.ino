/*
    This sketch sends a string to a TCP server, and prints a one-line response.
    You must run a TCP server in your local network.
    For example, on Linux you can use this command: nc -v -l 3000
*/

#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
#include <WEMOS_SHT3X.h>

#ifndef STASSID
#define STASSID "ESP32"
#define STAPSK  "123456789"
#endif

const char* ssid     = STASSID;
const char* password = STAPSK;

//temperature stuff
SHT3X sht30(0x45);

const char* host = "192.168.4.1";
const uint16_t port = 80;

ESP8266WiFiMulti WiFiMulti;

void setup() {
  Serial.begin(115200);

  // We start by connecting to a WiFi network
  WiFi.mode(WIFI_STA);
  WiFiMulti.addAP(ssid, password);

  Serial.println();
  Serial.println();
  Serial.print("Wait for WiFi... ");

  while (WiFiMulti.run() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  delay(500);
}


void loop() {
  Serial.print("connecting to ");
  Serial.print(host);
  Serial.print(':');
  Serial.println(port);

  // Use WiFiClient class to create TCP connections
  WiFiClient client;

  if (!client.connect(host, port)) {
    Serial.println("connection failed");
    Serial.println("wait 5 sec...");
    delay(5000);
    return;
  }

  //assemble temperature string
  if(sht30.get()==0){
    client.print("T ");
    client.println(sht30.cTemp);
    client.println();
  }
  else
  {
    client.println("Error!");
  }
  
  // This will send the request to the server
  //client.println("hello from ESP8266");

  //read back one line from server
  Serial.println("receiving from remote server");
  String line = client.readStringUntil('\r');
  Serial.println(line);

  Serial.println("closing connection");
  client.stop();

  Serial.println("wait 5 sec...");
  delay(1000);


  //second connection
  Serial.print("connecting to ");
  Serial.print(host);
  Serial.print(':');
  Serial.println(port);

  // Use WiFiClient class to create TCP connections
  WiFiClient client1;

  if (!client1.connect(host, port)) {
    Serial.println("connection failed");
    Serial.println("wait 1 sec...");
    delay(5000);
    return;
  }

  //assemble temperature string
  if(sht30.get()==0){
    client1.print("H ");
    client1.println(sht30.humidity);
    client1.println();
  }
  else
  {
    client1.println("Error!");
  }
  
  // This will send the request to the server
  //client.println("hello from ESP8266");

  //read back one line from server
  Serial.println("receiving from remote server");
  String line1 = client.readStringUntil('\r');
  Serial.println(line);

  Serial.println("closing connection");
  client1.stop();

  delay(5000);
}
