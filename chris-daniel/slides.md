---
theme: seriph
background: /images/horizontal-lines.svg
class: text-center
highlighter: shiki
lineNumbers: true
info: |
  ## IoT Powerday 2023
  An introduction and workshop for IoT

  Learn more at [Sli.dev](https://sli.dev)
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

* ...

---

## Post data to Rails API

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
