# LuCI API: `cbi`

> **Source:** [`modules/luci-base/htdocs/luci-static/resources/cbi.js`](https://github.com/openwrt/luci/blob/master/modules/luci-base/htdocs/luci-static/resources/cbi.js)
> **Live docs:** https://openwrt.github.io/luci/jsapi/LuCI.cbi.html
> **Generated:** 2026-03-05 18:30 UTC from commit `6959675`

---

<a name="LuCI.module_cbi"></a>

## cbi
CBI (Configuration Bindings Interface) helper utilities and DOM helpers.

Provides initialization for CBI UI elements, dependency handling,
validation wiring and miscellaneous helpers used by LuCI forms. Functions
defined here are registered as global `window.*` symbols.


* [cbi](#LuCI.module_cbi)
    * [~s8(bytes, off)](#LuCI.module_cbi..s8) ⇒ <code>number</code>
    * [~u16(bytes, off)](#LuCI.module_cbi..u16) ⇒ <code>number</code>
    * [~sfh(s)](#LuCI.module_cbi..sfh) ⇒ <code>string</code> \| <code>null</code>
    * [~trimws(s)](#LuCI.module_cbi..trimws) ⇒ <code>string</code>
    * [~_(s, [c])](#LuCI.module_cbi.._) ⇒ <code>string</code>
    * [~N_(n, s, p, [c])](#LuCI.module_cbi..N_) ⇒ <code>string</code>
    * [~cbi_d_add(field, dep, index)](#LuCI.module_cbi..cbi_d_add)
    * [~cbi_d_checkvalue(target, ref)](#LuCI.module_cbi..cbi_d_checkvalue) ⇒ <code>boolean</code>
    * [~cbi_d_check(deps)](#LuCI.module_cbi..cbi_d_check) ⇒ <code>boolean</code>
    * [~cbi_d_update()](#LuCI.module_cbi..cbi_d_update)
    * [~cbi_init()](#LuCI.module_cbi..cbi_init)
    * [~cbi_validate_form(form, [errmsg])](#LuCI.module_cbi..cbi_validate_form) ⇒ <code>boolean</code>
    * [~cbi_validate_named_section_add(input)](#LuCI.module_cbi..cbi_validate_named_section_add)
    * [~cbi_validate_reset(form)](#LuCI.module_cbi..cbi_validate_reset) ⇒ <code>boolean</code>
    * [~cbi_validate_field(cbid, optional, type)](#LuCI.module_cbi..cbi_validate_field)
    * [~cbi_row_swap(elem, up, store)](#LuCI.module_cbi..cbi_row_swap) ⇒ <code>boolean</code>
    * [~cbi_tag_last(container)](#LuCI.module_cbi..cbi_tag_last)
    * [~cbi_submit(elem, [name], [value], [action])](#LuCI.module_cbi..cbi_submit) ⇒ <code>boolean</code>
    * [~isElem(e)](#LuCI.module_cbi..isElem) ⇒ <code>HTMLElement</code> \| <code>null</code>
    * [~matchesElem(node, selector)](#LuCI.module_cbi..matchesElem) ⇒ <code>boolean</code>
    * [~findParent(node, selector)](#LuCI.module_cbi..findParent) ⇒ <code>HTMLElement</code> \| <code>null</code>
    * [~E()](#LuCI.module_cbi..E) ⇒ <code>HTMLElement</code>
    * [~cbi_dropdown_init(sb)](#LuCI.module_cbi..cbi_dropdown_init) ⇒ <code>L.ui.Dropdown</code> \| <code>undefined</code>
    * [~cbi_update_table(table, ...data, [placeholder])](#LuCI.module_cbi..cbi_update_table)

<a name="LuCI.module_cbi..s8"></a>

### cbi~s8(bytes, off) ⇒ <code>number</code>
Read signed 8-bit integer from a byte array at the given offset.

**Kind**: inner method of [<code>cbi</code>](#LuCI.module_cbi)  
**Returns**: <code>number</code> - Signed 8-bit value (returned as unsigned number).  

| Param | Type | Description |
| --- | --- | --- |
| bytes | <code>Array.&lt;number&gt;</code> | Byte array. |
| off | <code>number</code> | Offset into the array. |

<a name="LuCI.module_cbi..u16"></a>

### cbi~u16(bytes, off) ⇒ <code>number</code>
Read unsigned 16-bit little-endian integer from a byte array at offset.

**Kind**: inner method of [<code>cbi</code>](#LuCI.module_cbi)  
**Returns**: <code>number</code> - Unsigned 16-bit integer.  

| Param | Type | Description |
| --- | --- | --- |
| bytes | <code>Array.&lt;number&gt;</code> | Byte array. |
| off | <code>number</code> | Offset into the array. |

<a name="LuCI.module_cbi..sfh"></a>

### cbi~sfh(s) ⇒ <code>string</code> \| <code>null</code>
Compute a stable 32-bit-ish string hash used for translation keys.
Encodes UTF-8 surrogate pairs and mixes bytes into a hex hash string.

**Kind**: inner method of [<code>cbi</code>](#LuCI.module_cbi)  
**Returns**: <code>string</code> \| <code>null</code> - Hex hash string or null for empty input.  

| Param | Type | Description |
| --- | --- | --- |
| s | <code>string</code> \| <code>null</code> | Input string. |

<a name="LuCI.module_cbi..trimws"></a>

### cbi~trimws(s) ⇒ <code>string</code>
Trim whitespace and normalise internal whitespace sequences to single spaces.

**Kind**: inner method of [<code>cbi</code>](#LuCI.module_cbi)  
**Returns**: <code>string</code> - Trimmed and normalised string.  

| Param | Type | Description |
| --- | --- | --- |
| s | <code>\*</code> | Value to convert to string and trim. |

<a name="LuCI.module_cbi.._"></a>

### cbi~\_(s, [c]) ⇒ <code>string</code>
Lookup a translated string for the given message and optional context.
Falls back to the source string when no translation found.

**Kind**: inner method of [<code>cbi</code>](#LuCI.module_cbi)  
**Returns**: <code>string</code> - Translated string or original.  

| Param | Type | Description |
| --- | --- | --- |
| s | <code>string</code> | Source string. |
| [c] | <code>string</code> | Optional translation context. |

<a name="LuCI.module_cbi..N_"></a>

### cbi~N\_(n, s, p, [c]) ⇒ <code>string</code>
Plural-aware translation lookup.

**Kind**: inner method of [<code>cbi</code>](#LuCI.module_cbi)  
**Returns**: <code>string</code> - Translated plural form or source string.  

| Param | Type | Description |
| --- | --- | --- |
| n | <code>number</code> | Quantity to evaluate plural form. |
| s | <code>string</code> | Singular string. |
| p | <code>string</code> | Plural string. |
| [c] | <code>string</code> | Optional context. |

<a name="LuCI.module_cbi..cbi_d_add"></a>

### cbi~cbi\_d\_add(field, dep, index)
Register a dependency entry for a field.

**Kind**: inner method of [<code>cbi</code>](#LuCI.module_cbi)  

| Param | Type | Description |
| --- | --- | --- |
| field | <code>HTMLElement</code> \| <code>string</code> | Field element or its id. |
| dep | <code>Object</code> | Dependency specification object. |
| index | <code>number</code> | Order index of the dependent node. |

<a name="LuCI.module_cbi..cbi_d_checkvalue"></a>

### cbi~cbi\_d\_checkvalue(target, ref) ⇒ <code>boolean</code>
Check whether an input/select identified by target matches the given reference value.

**Kind**: inner method of [<code>cbi</code>](#LuCI.module_cbi)  
**Returns**: <code>boolean</code> - True if the current value matches ref.  

| Param | Type | Description |
| --- | --- | --- |
| target | <code>string</code> | Element id or name to query. |
| ref | <code>string</code> | Reference value to compare with. |

<a name="LuCI.module_cbi..cbi_d_check"></a>

### cbi~cbi\_d\_check(deps) ⇒ <code>boolean</code>
Evaluate a list of dependency descriptors and return whether any match.

**Kind**: inner method of [<code>cbi</code>](#LuCI.module_cbi)  
**Returns**: <code>boolean</code> - True when dependencies indicate the element should be shown.  

| Param | Type | Description |
| --- | --- | --- |
| deps | <code>Array.&lt;Object&gt;</code> | Array of dependency objects to evaluate. |

<a name="LuCI.module_cbi..cbi_d_update"></a>

### cbi~cbi\_d\_update()
Update DOM nodes based on registered dependencies, showing or hiding
nodes and restoring their order when dependency state changes.

**Kind**: inner method of [<code>cbi</code>](#LuCI.module_cbi)  
<a name="LuCI.module_cbi..cbi_init"></a>

### cbi~cbi\_init()
Initialize CBI widgets and wire up dependency and validation handlers.
Walks the DOM looking for CBI-specific data attributes and replaces
placeholders with interactive widgets.

**Kind**: inner method of [<code>cbi</code>](#LuCI.module_cbi)  
<a name="LuCI.module_cbi..cbi_validate_form"></a>

### cbi~cbi\_validate\_form(form, [errmsg]) ⇒ <code>boolean</code>
Run all validators associated with a form and optionally show an error.

**Kind**: inner method of [<code>cbi</code>](#LuCI.module_cbi)  
**Returns**: <code>boolean</code> - True when form is valid.  

| Param | Type | Description |
| --- | --- | --- |
| form | <code>HTMLFormElement</code> | Form element containing validators. |
| [errmsg] | <code>string</code> | Message to show when validation fails. |

<a name="LuCI.module_cbi..cbi_validate_named_section_add"></a>

### cbi~cbi\_validate\_named\_section\_add(input)
Enable/disable a named-section add button depending on input value.

**Kind**: inner method of [<code>cbi</code>](#LuCI.module_cbi)  

| Param | Type | Description |
| --- | --- | --- |
| input | <code>HTMLInputElement</code> | Input that contains the new section name. |

<a name="LuCI.module_cbi..cbi_validate_reset"></a>

### cbi~cbi\_validate\_reset(form) ⇒ <code>boolean</code>
Trigger a delayed form validation (used to allow UI state to settle).

**Kind**: inner method of [<code>cbi</code>](#LuCI.module_cbi)  
**Returns**: <code>boolean</code> - Always returns true.  

| Param | Type | Description |
| --- | --- | --- |
| form | <code>HTMLFormElement</code> | Form to validate after a short delay. |

<a name="LuCI.module_cbi..cbi_validate_field"></a>

### cbi~cbi\_validate\_field(cbid, optional, type)
Attach a validator to a field and wire validation events.

**Kind**: inner method of [<code>cbi</code>](#LuCI.module_cbi)  

| Param | Type | Description |
| --- | --- | --- |
| cbid | <code>HTMLElement</code> \| <code>string</code> | Element or element id to validate. |
| optional | <code>boolean</code> | Whether an empty value is allowed. |
| type | <code>string</code> | Validator type expression (passed to L.validation). |

<a name="LuCI.module_cbi..cbi_row_swap"></a>

### cbi~cbi\_row\_swap(elem, up, store) ⇒ <code>boolean</code>
Move a table row up or down within a section and update the storage field.

**Kind**: inner method of [<code>cbi</code>](#LuCI.module_cbi)  
**Returns**: <code>boolean</code> - Always returns false to cancel default action.  

| Param | Type | Description |
| --- | --- | --- |
| elem | <code>HTMLElement</code> | Element inside the row that triggers the swap. |
| up | <code>boolean</code> | If true, move the row up; otherwise move down. |
| store | <code>string</code> | ID of the hidden input used to store the order. |

<a name="LuCI.module_cbi..cbi_tag_last"></a>

### cbi~cbi\_tag\_last(container)
Mark the last visible value container child with class `cbi-value-last`.

**Kind**: inner method of [<code>cbi</code>](#LuCI.module_cbi)  

| Param | Type | Description |
| --- | --- | --- |
| container | <code>HTMLElement</code> | Parent container element. |

<a name="LuCI.module_cbi..cbi_submit"></a>

### cbi~cbi\_submit(elem, [name], [value], [action]) ⇒ <code>boolean</code>
Submit a form, optionally adding a hidden input to pass a name/value pair.

**Kind**: inner method of [<code>cbi</code>](#LuCI.module_cbi)  
**Returns**: <code>boolean</code> - True on successful submit, false when no form found.  

| Param | Type | Description |
| --- | --- | --- |
| elem | <code>HTMLElement</code> | Element inside the form or an element with a form. |
| [name] | <code>string</code> | Name of hidden input to include, if any. |
| [value] | <code>string</code> | Value for the hidden input (defaults to '1'). |
| [action] | <code>string</code> | Optional form action URL override. |

<a name="LuCI.module_cbi..isElem"></a>

### cbi~isElem(e) ⇒ <code>HTMLElement</code> \| <code>null</code>
Return the element for input which may be an element or an id.

**Kind**: inner method of [<code>cbi</code>](#LuCI.module_cbi)  

| Param | Type | Description |
| --- | --- | --- |
| e | <code>Element</code> \| <code>string</code> | Element or id. |

<a name="LuCI.module_cbi..matchesElem"></a>

### cbi~matchesElem(node, selector) ⇒ <code>boolean</code>
Test whether node matches a CSS selector.

**Kind**: inner method of [<code>cbi</code>](#LuCI.module_cbi)  

| Param | Type | Description |
| --- | --- | --- |
| node | <code>Node</code> | Node to test. |
| selector | <code>string</code> | CSS selector. |

<a name="LuCI.module_cbi..findParent"></a>

### cbi~findParent(node, selector) ⇒ <code>HTMLElement</code> \| <code>null</code>
Find the parent matching selector from node upwards.

**Kind**: inner method of [<code>cbi</code>](#LuCI.module_cbi)  

| Param | Type | Description |
| --- | --- | --- |
| node | <code>Node</code> | Starting node. |
| selector | <code>string</code> | CSS selector to match ancestor. |

<a name="LuCI.module_cbi..E"></a>

### cbi~E() ⇒ <code>HTMLElement</code>
Create DOM elements using [L.dom.create](L.dom.create) helper (convenience wrapper).

**Kind**: inner method of [<code>cbi</code>](#LuCI.module_cbi)  
<a name="LuCI.module_cbi..cbi_dropdown_init"></a>

### cbi~cbi\_dropdown\_init(sb) ⇒ <code>L.ui.Dropdown</code> \| <code>undefined</code>
Initialize a dropdown element into an [L.ui.Dropdown](L.ui.Dropdown) instance and bind it.
If already bound, this is a no-op.

**Kind**: inner method of [<code>cbi</code>](#LuCI.module_cbi)  
**Returns**: <code>L.ui.Dropdown</code> \| <code>undefined</code> - Dropdown instance or undefined when already bound.  

| Param | Type | Description |
| --- | --- | --- |
| sb | <code>HTMLElement</code> | The select element to convert. |

<a name="LuCI.module_cbi..cbi_update_table"></a>

### cbi~cbi\_update\_table(table, ...data, [placeholder])
Update or initialize a table UI widget with new data.

**Kind**: inner method of [<code>cbi</code>](#LuCI.module_cbi)  

| Param | Type | Description |
| --- | --- | --- |
| table | <code>HTMLElement</code> \| <code>string</code> | Table element or selector. |
| ...data | <code>Array.&lt;Node&gt;</code> | Data to update the table with. |
| [placeholder] | <code>string</code> | Placeholder text when empty. |