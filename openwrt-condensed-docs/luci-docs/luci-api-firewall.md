# LuCI API: `firewall`

> **Source:** [`modules/luci-base/htdocs/luci-static/resources/firewall.js`](https://github.com/openwrt/luci/blob/master/modules/luci-base/htdocs/luci-static/resources/firewall.js)
> **Live docs:** https://openwrt.github.io/luci/jsapi/LuCI.firewall.html
> **Generated:** 2026-03-05 18:43 UTC from commit `6959675`

---

<a name="initFirewallState"></a>

## initFirewallState() ⇒ <code>Promise</code>
Load the firewall configuration.

**Kind**: global function  
<a name="parseEnum"></a>

## parseEnum(s, values) ⇒ <code>string</code>
Parse an enum value.

**Kind**: global function  

| Param | Type |
| --- | --- |
| s | <code>string</code> | 
| values | <code>Array.&lt;string&gt;</code> | 

<a name="parsePolicy"></a>

## parsePolicy(s, [defaultValue]) ⇒ <code>string</code>
Parse a policy value, or defaultValue if not found.

**Kind**: global function  

| Param | Type | Default |
| --- | --- | --- |
| s | <code>string</code> |  | 
| [defaultValue] | <code>Array.&lt;string&gt;</code> | <code>[&#x27;DROP&#x27;, &#x27;REJECT&#x27;, &#x27;ACCEPT&#x27;]</code> | 

<a name="lookupZone"></a>

## lookupZone(name) ⇒ <code>Zone</code>
Look up a firewall zone.

**Kind**: global function  

| Param | Type |
| --- | --- |
| name | <code>string</code> | 

<a name="getColorForName"></a>

## getColorForName(forName) ⇒ <code>string</code>
Generate a colour for a name.

**Kind**: global function  

| Param | Type |
| --- | --- |
| forName | <code>string</code> |