#include <WiFi.h>
#include <HTTPClient.h>
#include <WiFiClientSecure.h>
#include "DHT.h"

#define DHTPIN 4
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

const char* ssid = "Carlos";
const char* password = "030117-1804";

// Configuración del servidor
const char* serverUrl = "https://quitosano-production.up.railway.app/api/ambiente/crear/";

// Configuración de certificado (necesario para HTTPS)
const char* root_ca = \
"-----BEGIN CERTIFICATE-----\n" \
"MIIDdzCCAl+gAwIBAgIEAgAAuTANBgkqhkiG9w0BAQUFADBaMQswCQYDVQQGEwJJ\n" \
"RTESMBAGA1UEChMJQmFsdGltb3JlMRMwEQYDVQQLEwpDeWJlclRydXN0MSIwIAYD\n" \
"VQQDExlCYWx0aW1vcmUgQ3liZXJUcnVzdCBSb290MB4XDTAwMDUxMjE4NDYwMFoX\n" \
"DTI1MDUxMjIzNTkwMFowWjELMAkGA1UEBhMCSUUxEjAQBgNVBAoTCUJhbHRpbW9y\n" \
"ZTETMBEGA1UECxMKQ3liZXJUcnVzdDEiMCAGA1UEAxMZQmFsdGltb3JlIEN5YmVy\n" \
"VHJ1c3QgUm9vdDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAKMEuyKr\n" \
"mD1X6CZymrV51Cni4eiVgLGw41uOKymaZN+hXe2wCQVt2yguzmKiYv60iNoS6zjr\n" \
"IZ3AQSsBUnuId9Mcj8e6uYi1agnnc+gRQKfRzMpijS3ljwumUNKoUMMo6vWrJYeK\n" \
"mpYcqWe4PwzV9/lSEy/CG9VwcPCPwBLKBsua4dnKM3p31vjsufFoREJIE9LAwqSu\n" \
"XYm8kjZoEZvU1hSwLnPs++rHz9Q5mYURCT7PhVt3k7O3jADjHfdT6gguEo5U66Bx\n" \
"/KMBq0sCfXhieIDWYQXpTl1+U2lH7SWsN+LOOHJBMisqG3mdY4I5SHDOvl1MQ8xV\n" \
"tYWH4HT0CgYEA7yWrFozTqrldJt7IZ1TQUl2jQGA2OXAmdvV0ORdF1VjhWWPqnV0\n" \
"wUcmToJIIYRZoll0EEkSpaaXZC8/PH9TGNBr8OT/8s9jf8zJP8TBeBen7AXtK4L7\n" \
"dz2B6j6ZKd8BZIRJ0M5v3Q8VvVnPx8iT5/EeB6UZCFsNtxE7VJK8GMCgYEA083Kp\n" \
"Sm2GZSiaPiPQszjqg7vf4SBwkF1tFQ3jQJMK0NMy9D4xZJ7dNbRID6jQ8oAJuvY+\n" \
"DA1sAa7jghrwRlKF1n9qTS8VROfrBxJZS3GjCXpPDVIYHiq6U9yLcmcLvNQTWk4x\n" \
"24JHjGZgBk0E5YRVMWwY9OTlECXcihX5Xe4jZekCgYEAiXH8V1L2pY4PlCyO01Jo\n" \
"U8iUwS7A1QU3I5Vl4qJ4Z6i1iKSzFcHN+5ad6F3tlEc4gBaRlOIjqC0wNkCb0FCA\n" \
"S6NfDed7hj6JXzw6Sx8CGDOqiKmBWiLwXts8B7UDDgDEHcGj2BpCTNxd4/g0VvVY\n" \
"XjPvB2Pp2BB04YBTqY5nVqsCgYEAv/q3ampqU8/c3XJf4p1ZgZZBBWXMMDO6V7bU\n" \
"0tJYDYJ/YYuG6t1Z6X5yAMjLfHA1Yh+oh7yq4sDvX7uAkxivQMf8sJ4J4tXQhEfq\n" \
"nEi39mFRRYdKQq5qD5HixXlC5VKMFcd6pFTE9sDmISL8hC7IotbAhWgT9t3x3wK8\n" \
"j5ECgYEAkE7dY9KwGzVKm5QpJtQhlj5wUvK0QZ5wBB3E4RHjlUS11y4GQ2sGyAwt\n" \
"APxHf7Hg1B2rqyKp6XgM7VYIZgQq0gD4dj1U+ACLQSkZpJ8Zz0VPdXjZrtz5BRX6\n" \
"wVwD2zqlVI7EM0xqVVK+EmewjPqlkYPqFQzUUkIpErEe6tI=\n" \
"-----END CERTIFICATE-----";

// Campos requeridos por la API
const String id_transporte = "TRANSP-001";  // Cambiar por tu ID real
const String producto = "Quitosano";        // Cambiar por tu producto

void setup() {
  Serial.begin(9600);
  dht.begin();

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi conectado");
}

void loop() {
  float t = dht.readTemperature();
  float h = dht.readHumidity();

  if (isnan(t) || isnan(h)) {
    Serial.println("Error lectura sensor!");
    delay(2000);
    return;
  }

  Serial.print("Temperatura: ");
  Serial.print(t);
  Serial.print(" °C, Humedad: ");
  Serial.print(h);
  Serial.println(" %");

  if (WiFi.status() == WL_CONNECTED) {
    WiFiClientSecure client;
    client.setCACert(root_ca);
    
    HTTPClient http;
    http.begin(client, serverUrl);
    http.addHeader("Content-Type", "application/json");

    // Crear JSON con todos los campos requeridos
    String json = "{";
    json += "\"id_transporte\": \"" + id_transporte + "\",";
    json += "\"producto\": \"" + producto + "\",";
    json += "\"temperatura_actual\": " + String(t, 1) + ",";
    json += "\"temperatura_max\": 30.0,";       // Ajustar valores según necesidades
    json += "\"temperatura_min\": 10.0,";
    json += "\"humedad_actual\": " + String(h, 1) + ",";
    json += "\"humedad_max\": 80.0,";
    json += "\"humedad_min\": 20.0";
    json += "}";

    int httpCode = http.POST(json);
    
    if (httpCode > 0) {
      Serial.printf("Código HTTP: %d\n", httpCode);
      if (httpCode == HTTP_CODE_CREATED) {
        String payload = http.getString();
        Serial.println("Respuesta del servidor:");
        Serial.println(payload);
      }
    } else {
      Serial.printf("Error en POST: %s\n", http.errorToString(httpCode).c_str());
    }

    http.end();
  } else {
    Serial.println("WiFi desconectado");
  }

  delay(10000); // Espera 10 segundos entre lecturas
}