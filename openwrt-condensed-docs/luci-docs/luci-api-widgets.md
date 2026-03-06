---
module: widgets
title: LuCI API - widgets
source: https://github.com/openwrt/luci/blob/master/modules/luci-base/htdocs/luci-static/resources/tools/widgets.js
generated: 2026-03-06 07:47 UTC from commit de553f3
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