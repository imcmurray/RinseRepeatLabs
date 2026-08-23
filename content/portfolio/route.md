---
title: "Route"
tagline: "Optimized driving made easy to save you money."
description: "An iOS app that estimates what your driving costs in fuel, shows the trade-off between time and money, and stays quiet when it doesn't have anything useful to say."
platforms: ["iOS"]
tech: ["Swift", "SwiftUI", "SwiftData", "Core Location", "Swift Package Manager"]
featured: true
weight: 1
year: "2026"
timeline: "In TestFlight"
client: "Rinse Repeat Labs"
image: "/images/route.png"
gallery:
  - "/images/route/01-drives.png"
  - "/images/route/07-recording.png"
  - "/images/route/03-drive-detail.png"
  - "/images/route/04-plan.png"
  - "/images/route/05-options.png"
  - "/images/route/08-fuel-range.png"
  - "/images/route/02-month.png"
  - "/images/route/06-location-permission.png"
legal:
  - title: "Privacy Policy"
    url: "/legal/route/privacy-policy/"
  - title: "Terms of Service"
    url: "/legal/route/terms-of-service/"
---

## Overview

Route is for everyday drivers — commuters, highway users, occasional road-trippers — who spend real time behind the wheel and would like to spend less money doing it. Record a drive, and Route tells you roughly what it cost in fuel and gives you one thing worth knowing about how you drove it.

Everything Route reports about fuel is an **estimate produced by a model**. Route does not measure fuel consumption — a phone cannot. So it estimates, says plainly that it is estimating, and declines to speak when the estimate isn't good enough to be useful.

## The Challenge

The interesting question is not *"can we perfectly determine fuel consumption?"* — from a phone, we can't. It is:

> Can we give someone a recommendation accurate enough to help them make a better driving decision?

That reframing drove every design choice in the app:

- **Honesty over precision.** A confident-looking number that's wrong is worse than no number. The engine can return *nothing*, and regularly does.
- **A trade-off, not a verdict.** Nobody agrees on what an hour of their time is worth, so the app doesn't guess.
- **Location without a location trail.** A driving app needs your speed. It does not need to know where you went.
- **Not a speeding app.** The optimizer never considers a speed above the posted limit, and never suggests crawling far below the traffic around you.

## Our Solution

**The headline output is a rate, not an answer.**

> Driving 75 instead of 65 saves about 35 minutes and costs about $6.00 more in fuel — roughly $9.75 per hour of time you get back.

That works no matter what your time is worth, needs no wage estimate, and leaves the decision where it belongs — with the driver.

Under it sits a physics-derived efficiency model rather than a curve fit, calibrated conservatively from the one number a driver can actually give you: their typical highway MPG. The whole mathematical engine lives in a separate Swift package with no SwiftUI and no Core Location in it, so the maths can be tested — 273 tests, no simulator required — and so it *cannot* reach for the things it shouldn't.

### Key Features

**Post-drive insight**
Start and end a drive yourself. Route breaks it into stopped, town, highway-traffic and highway-steady time, estimates the fuel cost, scores the drive, and offers one recommendation — or none.

**Trip planner**
Enter a distance and the speed limit on your route. Route shows Economy, Balanced and Time options with the marginal cost of the time you'd buy, plus how many fuel stops each needs.

**Fuel-stop and range awareness**
Stop counts are computed at the boundary rather than approximated, and the planner flags a plan that only just makes it — where one mph faster adds an entire stop.

**Fill-up learning**
Log fill-ups and Route tunes its estimates toward how you actually drive. Speed and distance are observable from GPS; fuel is not — so the learned correction is fitted against real measurements, and how far it's trusted depends on how much evidence there is.

**Soft language throughout**
"Around 27 MPG (estimated)." "Roughly 7% less fuel." Every figure is phrased to carry its own uncertainty.

## Privacy by Construction

Route has **no backend**, no account, and no analytics. Everything stays on the phone.

Location is sampled only while a drive is recording, under When-In-Use authorization. **Where you went is never recorded** — each location update is converted to a speed and a distance and the coordinates are discarded immediately. This is enforced by the architecture rather than by policy: the type that carries driving data downstream has no field capable of holding a latitude or longitude, so no part of the app can store or export a route trace even by mistake.

The one thing that can leave the device is an optional VIN lookup against the U.S. Department of Transportation's public vPIC database — asked for explicitly, shown to you first, sent with nothing attached, and never retained.

## Status

MVP 0 (the engine and its harnesses) and MVP 1 (onboarding, recording, classification, scoring, recommendations, history and the trip planner) are complete. Route is in TestFlight ahead of its first App Store submission — Rinse Repeat Labs' first iOS release.

Ahead: automatic drive detection, OBD-II, CarPlay, live fuel prices, and full EV support.
