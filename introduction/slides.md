---
theme: seriph
background: /images/horizontal-lines.svg
class: text-center
highlighter: shiki
lineNumbers: false
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

# IoT Powerday

A buzzword with many meanings

<div class="abs-br m-6 flex gap-2">
  <button @click="$slidev.nav.openInEditor()" title="Open in Editor" class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon:edit />
  </button>
  <a href="https://github.com/renuo/iot-powerday-2023" target="_blank" alt="GitHub" title="Open in GitHub"
    class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon-logo-github />
  </a>
</div>

---
transition: fade-out
hideInToc: true
---

# Schedule

 * 09:00 - 09:45 — Introduction
 * 09:45 - 10:00 — Create Teams / Split tasks
 * 10:00 - 10:30 — Start exploring
 * Coffee Break
 * 10:45 - 12:30 — Continue Exploring
 * Lunch break
 * 13:30 - 15:30 — Wrap Things up
 * 15:30 - 16:30 — Present results
 * 16:30 - 17:00 — Discussion

---
layout: default
hideInToc: true
---

# Table of contents

<Toc maxDepth="1"></Toc>

---
transition: slide-up
---

# Overview

> The Internet of things (IoT) describes devices with sensors, processing
> ability, software and other technologies that connect and exchange data with
> other devices and systems over the Internet or other communications networks.
>
> *Source: <https://en.wikipedia.org/wiki/Internet_of_things>*

 * So connecting "stuff" via a network
 * Stuff are physical devices
 * But not necessarily connected over the Internet
 <div v-click="1">

 * For our workshop
   * Sensor devices connected via Bluetooth (BLE) or WiFi
   * "Edge" devices which collect this data
   * Dashboard which shows this data
 </div>

---

# Examples

 * Smart Home devices
 * Wearable technologies
 * Personal medical devices
 * Autonomous vehicles
 * Industrial machines
 * ...

---

# Market - Or why should I care?

 * IoT Marketvolume in Switzerland grew rapidely:
 * 6.76 bil in 2020 to 8.09 bil in 2021 (Source: https://iot-workshop.ch/)

---

# Terminology / Concepts

 * Sensors: A hardware device measuring something and broadcasting it
 * Unique identifiers: Every sensor needs a unique global identifier. We use
   the BLE device ID for that.
 * Edge devices: The device that connects the sensor to the internet. Also
   called IoT gateway. (Laptop / Raspberry Pi)


---

# Resources

 * <https://www.coursera.org/articles/internet-of-things>
 * <https://www.home-assistant.io/>

---

# Ideas to work on

 * Play around with Arduino and some Sensirion Sensors:
   * Broadcast data via BLE <https://github.com/Sensirion/arduino-ble-gadget>
   * Let MyAmbiance pick it up and display it <https://play.google.com/store/apps/details?id=com.sensirion.myam>
 * Setup <https://www.home-assistant.io/> on a Raspberry Pi
   * Can you integrate the office CO2 sensors?
   * Can you integrate other things?
 * Pick up the CO2 sensor measurement data (on your Laptop / a Raspberry Pi)
   and display it.
 * Create a Sensor Dashboard with https://grafana.com/ and let other teams push
   their data to that.
 * Integrate the CO2 sensors in the office dashboard
