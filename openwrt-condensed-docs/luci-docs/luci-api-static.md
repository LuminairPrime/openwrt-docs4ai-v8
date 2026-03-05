# LuCI API: `static`

> **Source:** [`modules/luci-base/htdocs/luci-static/resources/protocol/static.js`](https://github.com/openwrt/luci/blob/master/modules/luci-base/htdocs/luci-static/resources/protocol/static.js)
> **Live docs:** https://openwrt.github.io/luci/jsapi/LuCI.static.html
> **Generated:** 2026-03-05 18:30 UTC from commit `6959675`

---

<a name="isCIDR"></a>

## isCIDR(value) ⇒ <code>boolean</code>
Determine whether a provided value is a CIDR format IP string.

**Kind**: global function  

| Param | Type | Description |
| --- | --- | --- |
| value | <code>string</code> | the IP string to test. |

<a name="calculateBroadcast"></a>

## calculateBroadcast(s, use_cfgvalue) ⇒ <code>string</code>
Calculate the broadcast IP for a given IP.

**Kind**: global function  

| Param | Type | Description |
| --- | --- | --- |
| s | <code>Node</code> | the ui element to test. |
| use_cfgvalue | <code>boolean</code> | whether to use the config or form value. |

<a name="validateBroadcast"></a>

## validateBroadcast(section_id, value) ⇒ <code>boolean</code>
Validate a broadcast IP for a section value.

**Kind**: global function  

| Param | Type |
| --- | --- |
| section_id | <code>string</code> | 
| value | <code>string</code> |