---
module: firewall
title: LuCI API - firewall
source: https://github.com/openwrt/luci/blob/master/modules/luci-base/htdocs/luci-static/resources/firewall.js
generated: 2026-03-06 08:44 UTC from commit de553f3
---

# LuCI API: `firewall`

> **Live docs:** https://openwrt.github.io/luci/jsapi/LuCI.firewall.html

---



## initFirewallState() ⇒ `Promise`
Load the firewall configuration.

**Kind**: global function  

## parseEnum(s, values) ⇒ `string`
Parse an enum value.

**Kind**: global function  

| Param | Type |
| --- | --- |
| s | `string` | 
| values | `Array.<string>` | 

## parsePolicy(s, [defaultValue]) ⇒ `string`
Parse a policy value, or defaultValue if not found.

**Kind**: global function  

| Param | Type | Default |
| --- | --- | --- |
| s | `string` |  | 
| [defaultValue] | `Array.<string>` | `['DROP', 'REJECT', 'ACCEPT']` | 

## lookupZone(name) ⇒ `Zone`
Look up a firewall zone.

**Kind**: global function  

| Param | Type |
| --- | --- |
| name | `string` | 

## getColorForName(forName) ⇒ `string`
Generate a colour for a name.

**Kind**: global function  

| Param | Type |
| --- | --- |
| forName | `string` |