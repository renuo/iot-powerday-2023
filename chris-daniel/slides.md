---
theme: seriph
class: text-center
highlighter: shiki
lineNumbers: true
drawings:
  persist: false
transition: slide-left
title: IoT Powerday
mdc: true
hideInToc: true
---

# Temperature/Humidity in Dashboard Monitor

---

## Motivation

- It is fun

---

## Widget

Shows "realtime" temperature and humidity data in the new dashboard monitor.

<img src="/images/widget2.png" style="width: 700px;">

---

<img src="/images/widget.png" style="width: 300px;">

---


## Stack
1. Python script
2. Rails backend
3. Vuejs frontend

---

## Python script

### Dependencies
1. Requests
2. Sensirion sensor bridge

### Steps
1. Connect to sensor bridge
2. Read sensor data in a loop
3. Send sensor data to REST API

### Post data to Rails API

```sh
❯ python main.py --port /dev/cu.usbserial-EKS261R9AF --url http://127.0.0.1/api/sensor_data
POST  {'temperature': 25.117494468604562, 'humidity': 22.557259479667355}
POST  {'temperature': 23.504615854123756, 'humidity': 21.998397802700847}
POST  {'temperature': 17.480354009308, 'humidity': 22.37033646143282}
POST  {'temperature': 15.544365606164646, 'humidity': 23.16762035553521}
POST  {'temperature': 13.207827878233005, 'humidity': 28.403372243839172}
POST  {'temperature': 17.560463874265658, 'humidity': 30.53772793163958}
POST  {'temperature': 22.941176470588232, 'humidity': 36.47539482719158}
```

---

## Rails backend

### Model
- temperature: decimal
- humidity: decimal

### Routes

```ruby
scope :api do
  resources :sensor_data, only: %i[index create]
end
```

### Controller

- GET /index endpoint to show the latest data point
- POST /create endpoint to record a new data point

---

## Vuejs Frontend (The actual widget)

### State
```html
<template>
  <div class="widget bg-gray-700 p-2 w-full flex flex-col">
    <div class="flex-1">
      <b>Temperature</b>
      <br>
      <div class="text-lg">
        {{temperature}} C°
      </div>
      <b>Humidity</b>
      <br>
      <div class="text-lg">
        {{humidity}} %
      </div>
    </div>
    <div class="text-xs italic">
      {{lastUpdated}}
    </div>
  </div>
</template>
```
---

```html
<script setup lang="ts">
  import { ref } from 'vue'

  const humidity = ref(0)
  const temperature = ref(0)
  const lastUpdated = ref('loading...')

  setInterval(async () => {
    fetch('http://localhost:4200/api/sensor_data.json', {
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
      }
    }).then((response) => response.json()).then((data) => {
      temperature.value = data.temperature
      humidity.value = data.humidity
      lastUpdated.value = new Date(data.timestamp).toLocaleString()
    }).catch((error) => {
      console.error(error)
    })
  }, 1000)
</script>
```
