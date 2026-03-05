# LuCI API: `widgets`

> **Source:** [`modules/luci-base/htdocs/luci-static/resources/tools/widgets.js`](https://github.com/openwrt/luci/blob/master/modules/luci-base/htdocs/luci-static/resources/tools/widgets.js)
> **Live docs:** https://openwrt.github.io/luci/jsapi/LuCI.widgets.html
> **Generated:** 2026-03-05 18:30 UTC from commit `6959675`

---

<a name="getUsers"></a>

## getUsers() ⇒ <code>Array.&lt;string&gt;</code>
Get users found in `/etc/passwd`.

**Kind**: global function  
<a name="getGroups"></a>

## getGroups() ⇒ <code>Array.&lt;string&gt;</code>
Get users found in `/etc/group`.

**Kind**: global function  
<a name="getDevices"></a>

## getDevices(network) ⇒ <code>Array.&lt;string&gt;</code>
Get bridge devices or Layer 3 devices of a network object.

**Kind**: global function  

| Param | Type |
| --- | --- |
| network | <code>object</code> |