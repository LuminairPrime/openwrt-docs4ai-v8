# LuCI API: `firewall`

> **Source:** [`modules/luci-base/htdocs/luci-static/resources/firewall.js`](https://github.com/openwrt/luci/blob/master/modules/luci-base/htdocs/luci-static/resources/firewall.js)
> **Live docs:** https://openwrt.github.io/luci/jsapi/LuCI.firewall.html
> **Generated:** 2026-03-06 02:55 UTC from commit `de553f3`

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
| [defaultValue] | `Array.<string>` | `[&#x27;DROP&#x27;, &#x27;REJECT&#x27;, &#x27;ACCEPT&#x27;]` | 

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