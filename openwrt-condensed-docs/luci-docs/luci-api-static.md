# LuCI API: `static`

> **Source:** [`modules/luci-base/htdocs/luci-static/resources/protocol/static.js`](https://github.com/openwrt/luci/blob/master/modules/luci-base/htdocs/luci-static/resources/protocol/static.js)
> **Live docs:** https://openwrt.github.io/luci/jsapi/LuCI.static.html
> **Generated:** 2026-03-05 19:53 UTC from commit `6959675`

---



## isCIDR(value) ⇒ `boolean`
Determine whether a provided value is a CIDR format IP string.

**Kind**: global function  

| Param | Type | Description |
| --- | --- | --- |
| value | `string` | the IP string to test. |

## calculateBroadcast(s, use_cfgvalue) ⇒ `string`
Calculate the broadcast IP for a given IP.

**Kind**: global function  

| Param | Type | Description |
| --- | --- | --- |
| s | `Node` | the ui element to test. |
| use_cfgvalue | `boolean` | whether to use the config or form value. |

## validateBroadcast(section_id, value) ⇒ `boolean`
Validate a broadcast IP for a section value.

**Kind**: global function  

| Param | Type |
| --- | --- |
| section_id | `string` | 
| value | `string` |