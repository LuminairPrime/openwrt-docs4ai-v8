---
module: widgets
title: LuCI API - widgets
source: https://github.com/openwrt/luci/blob/master/modules/luci-base/htdocs/luci-static/resources/tools/widgets.js
generated: 2026-08-01 05:09 UTC from commit fe9d6b4
---

# LuCI API: `widgets`

> **Live docs:** https://openwrt.github.io/luci/jsapi/LuCI.widgets.html

---



## getUsers() ⇒ `Array.<string>`
Get users found in `/etc/passwd`.

**Kind**: global function  

## getGroups() ⇒ `Array.<string>`
Get users found in `/etc/group`.

**Kind**: global function  

## getDevices(network) ⇒ `Array.<string>`
Get bridge devices or Layer 3 devices of a network object.

**Kind**: global function  

| Param | Type |
| --- | --- |
| network | `object` |