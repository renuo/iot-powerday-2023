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

## Widget

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

### Logs

```sh
❯ python main.py --port /dev/cu.usbserial-EKS261R9AF --url http://127.0.0.1/api/sensor_data
POST  {'temperature': 25.117494468604562, 'humidity': 22.557259479667355}
POST  {'temperature': 23.504615854123756, 'humidity': 21.998397802700847}
POST  {'temperature': 17.480354009308, 'humidity': 22.37033646143282}
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

---
