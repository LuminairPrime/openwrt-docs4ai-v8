# LuCI API: `prng`

> **Source:** [`modules/luci-base/htdocs/luci-static/resources/tools/prng.js`](https://github.com/openwrt/luci/blob/master/modules/luci-base/htdocs/luci-static/resources/tools/prng.js)
> **Live docs:** https://openwrt.github.io/luci/jsapi/LuCI.prng.html
> **Generated:** 2026-03-05 18:43 UTC from commit `6959675`

---

<a name="mul"></a>

## mul(a, b) ⇒ <code>Array.&lt;number&gt;</code>
Multiply two 64-bit values represented as arrays of four 16-bit words.

Arrays use little-endian word order (least-significant 16-bit word first).
The result is truncated to the lower 64 bits and returned as a 4-element
array of 16-bit words.

**Kind**: global function  
**Returns**: <code>Array.&lt;number&gt;</code> - Product as 4 × 16-bit words (little-endian)  

| Param | Type | Description |
| --- | --- | --- |
| a | <code>Array.&lt;number&gt;</code> | Multiplicand (4 × 16-bit words, little-endian) |
| b | <code>Array.&lt;number&gt;</code> | Multiplier  (4 × 16-bit words, little-endian) |

<a name="add"></a>

## add(a, n) ⇒ <code>Array.&lt;number&gt;</code>
Add a small integer to a 64-bit value represented as four 16-bit words.

Treats `a` as a little-endian 64-bit value (4 × 16-bit words). Adds the
integer `n` to the least-significant word and propagates carry across
subsequent 16-bit words. The result is truncated to 64 bits and returned
as a 4-element array of 16-bit words (little-endian).

**Kind**: global function  
**Returns**: <code>Array.&lt;number&gt;</code> - Sum as 4 × 16-bit words (little-endian)  

| Param | Type | Description |
| --- | --- | --- |
| a | <code>Array.&lt;number&gt;</code> | Addend as 4 × 16-bit words (little-endian) |
| n | <code>number</code> | Value to add (integer carry) |

<a name="shr"></a>

## shr(a, n) ⇒ <code>Array.&lt;number&gt;</code>
Shift a 64-bit value (4 × 16-bit words, little-endian) right by `n` bits.

The input array is treated as little-endian 16-bit words. Bits shifted out
on the right are discarded; the returned array contains the lower 64-bit
result after the logical right shift.

**Kind**: global function  
**Returns**: <code>Array.&lt;number&gt;</code> - Shifted value as 4 × 16-bit words (little-endian)  

| Param | Type | Description |
| --- | --- | --- |
| a | <code>Array.&lt;number&gt;</code> | Source value as 4 × 16-bit words (little-endian) |
| n | <code>number</code> | Number of bits to shift right (non-negative integer) |

<a name="seed"></a>

## seed(n) ⇒ <code>void</code>
Seed the PRNG state.

The seed is treated as a 32-bit integer; the lower 16 bits are stored
in `s[0]`, the upper 16 bits in `s[1]`. `s[2]` and `s[3]` are zeroed.

**Kind**: global function  

| Param | Type | Description |
| --- | --- | --- |
| n | <code>number</code> | Seed value (32-bit integer) |

<a name="int"></a>

## int() ⇒ <code>number</code>
Produce the next PRNG 32-bit integer.

Advances the internal state and returns a 32-bit pseudo-random integer
derived from the current state.

**Kind**: global function  
**Returns**: <code>number</code> - 32-bit pseudo-random integer (JS number)  
<a name="get"></a>

## get([lower], [upper]) ⇒ <code>number</code>
Return a pseudo-random value.

Overloads:
- get() -> number in [0, 1]
- get(upper) -> integer in [1, upper]
- get(lower, upper) -> integer in [lower, upper]

**Kind**: global function  
**Returns**: <code>number</code> - Random value (float in [0,1] or integer in requested range)  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| [lower] | <code>number</code> | <code>0</code> | Lower bound (when two args supplied) |
| [upper] | <code>number</code> | <code>0</code> | Upper bound (when one or two args supplied) |

<a name="derive_color"></a>

## derive\_color(string) ⇒ <code>string</code>
Derive a deterministic hex color from an input string.

The color is produced by seeding the PRNG from a string-derived
hash and producing RGB components. Returns a `#rrggbb` hex string.

**Kind**: global function  
**Returns**: <code>string</code> - Hex color string in `#rrggbb` format  

| Param | Type | Description |
| --- | --- | --- |
| string | <code>string</code> | Input string used to derive the color |