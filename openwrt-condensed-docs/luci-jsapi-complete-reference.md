# LuCI JavaScript API Complete Reference

> **Generated:** 2026-03-05 18:11 UTC
> **Source:** https://github.com/openwrt/luci
> **Contains:** 10 documents concatenated

---

# LuCI API: `cbi`

> **Source:** [`modules/luci-base/htdocs/luci-static/resources/cbi.js`](https://github.com/openwrt/luci/blob/master/modules/luci-base/htdocs/luci-static/resources/cbi.js)
> **Live docs:** https://openwrt.github.io/luci/jsapi/LuCI.cbi.html
> **Generated:** 2026-03-05 18:07 UTC from commit `6959675`

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

---

# LuCI API: `firewall`

> **Source:** [`modules/luci-base/htdocs/luci-static/resources/firewall.js`](https://github.com/openwrt/luci/blob/master/modules/luci-base/htdocs/luci-static/resources/firewall.js)
> **Live docs:** https://openwrt.github.io/luci/jsapi/LuCI.firewall.html
> **Generated:** 2026-03-05 18:07 UTC from commit `6959675`

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

---

# LuCI API: `form`

> **Source:** [`modules/luci-base/htdocs/luci-static/resources/form.js`](https://github.com/openwrt/luci/blob/master/modules/luci-base/htdocs/luci-static/resources/form.js)
> **Live docs:** https://openwrt.github.io/luci/jsapi/LuCI.form.html
> **Generated:** 2026-03-05 18:07 UTC from commit `6959675`

---

<a name="isEqual"></a>

## isEqual(x, y) ⇒ <code>boolean</code>
Determines equality of two provided parameters. Can be arrays or objects.

**Kind**: global function  

| Param | Type |
| --- | --- |
| x | <code>\*</code> | 
| y | <code>\*</code> | 

<a name="isContained"></a>

## isContained(x, y) ⇒ <code>boolean</code>
Determines containment of two provided parameters. Can be arrays or objects.

**Kind**: global function  

| Param | Type |
| --- | --- |
| x | <code>\*</code> | 
| y | <code>\*</code> |

---

# LuCI API: `fs`

> **Source:** [`modules/luci-base/htdocs/luci-static/resources/fs.js`](https://github.com/openwrt/luci/blob/master/modules/luci-base/htdocs/luci-static/resources/fs.js)
> **Live docs:** https://openwrt.github.io/luci/jsapi/LuCI.fs.html
> **Generated:** 2026-03-05 18:07 UTC from commit `6959675`

---

<a name="handleRpcReply"></a>

## handleRpcReply(expect, rc) ⇒ <code>number</code>
Handle an RPC reply.

**Kind**: global function  
**Throws**:

- <code>Error</code> 


| Param | Type |
| --- | --- |
| expect | <code>object</code> | 
| rc | <code>number</code> | 

<a name="handleCgiIoReply"></a>

## handleCgiIoReply(res) ⇒ <code>string</code>
Handle a CGI-IO reply.

**Kind**: global function  
**Throws**:

- <code>Error</code> 


| Param | Type |
| --- | --- |
| res | <code>object</code> |

---

# LuCI API: `luci`

> **Source:** [`modules/luci-base/htdocs/luci-static/resources/luci.js`](https://github.com/openwrt/luci/blob/master/modules/luci-base/htdocs/luci-static/resources/luci.js)
> **Live docs:** https://openwrt.github.io/luci/jsapi/LuCI.html
> **Generated:** 2026-03-05 18:07 UTC from commit `6959675`

---

<a name="LuCI"></a>

## LuCI
**Kind**: global class  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| env | <code>object</code> | The environment settings to use for the LuCI runtime. |


* [LuCI](#LuCI)
    * [new LuCI(window, document, undefined)](#new_LuCI_new)
    * _instance_
        * [.env](#LuCI+env)
        * [.naturalCompare](#LuCI+naturalCompare) ⇒ <code>number</code>
        * ~~[.dom](#LuCI+dom)~~
        * ~~[.view](#LuCI+view)~~
        * ~~[.Poll](#LuCI+Poll)~~
        * ~~[.Request](#LuCI+Request)~~
        * ~~[.Class](#LuCI+Class)~~
        * [.raise([type], [fmt], [...args])](#LuCI+raise)
        * [.error([type], [fmt], [...args])](#LuCI+error)
        * [.bind(fn, self, [...args])](#LuCI+bind) ⇒ <code>function</code>
        * [.require(name, [from])](#LuCI+require) ⇒ [<code>Promise.&lt;baseclass&gt;</code>](#LuCI.baseclass)
        * [.hasSystemFeature(feature, [subfeature])](#LuCI+hasSystemFeature) ⇒ <code>boolean</code> \| <code>null</code>
        * [.fspath([...parts])](#LuCI+fspath) ⇒ <code>string</code>
        * [.path([prefix], [...parts])](#LuCI+path) ⇒ <code>string</code>
        * [.url([...parts])](#LuCI+url) ⇒ <code>string</code>
        * [.resource([...parts])](#LuCI+resource) ⇒ <code>string</code>
        * [.media([...parts])](#LuCI+media) ⇒ <code>string</code>
        * [.location()](#LuCI+location) ⇒ <code>string</code>
        * [.isObject([val])](#LuCI+isObject) ⇒ <code>boolean</code>
        * [.isArguments([val])](#LuCI+isArguments) ⇒ <code>boolean</code>
        * [.sortedKeys(obj, [key], [sortmode])](#LuCI+sortedKeys) ⇒ <code>Array.&lt;string&gt;</code>
        * [.sortedArray(val)](#LuCI+sortedArray) ⇒ <code>Array.&lt;\*&gt;</code>
        * [.toArray(val)](#LuCI+toArray) ⇒ <code>Array.&lt;\*&gt;</code>
        * [.resolveDefault(value, defvalue)](#LuCI+resolveDefault) ⇒ <code>Promise.&lt;\*&gt;</code>
        * ~~[.get(url, [args], cb)](#LuCI+get) ⇒ <code>Promise.&lt;null&gt;</code>~~
        * ~~[.post(url, [args], cb)](#LuCI+post) ⇒ <code>Promise.&lt;null&gt;</code>~~
        * ~~[.poll(interval, url, [args], cb, [post])](#LuCI+poll) ⇒ <code>function</code>~~
        * [.hasViewPermission()](#LuCI+hasViewPermission) ⇒ <code>boolean</code> \| <code>null</code>
        * ~~[.stop(entry)](#LuCI+stop) ⇒ <code>boolean</code>~~
        * ~~[.halt()](#LuCI+halt) ⇒ <code>boolean</code>~~
        * ~~[.run()](#LuCI+run) ⇒ <code>boolean</code>~~
    * _static_
        * [.baseclass](#LuCI.baseclass)
            * _instance_
                * [.varargs(args, offset, [...extra_args])](#LuCI.baseclass+varargs) ⇒ <code>Array.&lt;\*&gt;</code>
                * [.super(key, [callArgs])](#LuCI.baseclass+super) ⇒ <code>\*</code> \| <code>null</code>
                * [.toString()](#LuCI.baseclass+toString) ⇒ <code>string</code>
            * _static_
                * [.extend(properties)](#LuCI.baseclass.extend) ⇒ [<code>baseclass</code>](#LuCI.baseclass)
                * [.singleton(properties, ...new_args)](#LuCI.baseclass.singleton) ⇒ [<code>baseclass</code>](#LuCI.baseclass)
                * [.instantiate(args)](#LuCI.baseclass.instantiate) ⇒ [<code>baseclass</code>](#LuCI.baseclass)
                * [.isSubclass(classValue)](#LuCI.baseclass.isSubclass) ⇒ <code>boolean</code>
        * [.headers](#LuCI.headers)
            * [.has(name)](#LuCI.headers+has) ⇒ <code>boolean</code>
            * [.get(name)](#LuCI.headers+get) ⇒ <code>string</code> \| <code>null</code>
        * [.response](#LuCI.response)
            * [.ok](#LuCI.response+ok) : <code>boolean</code>
            * [.status](#LuCI.response+status) : <code>number</code>
            * [.statusText](#LuCI.response+statusText) : <code>string</code>
            * [.headers](#LuCI.response+headers) : [<code>headers</code>](#LuCI.headers)
            * [.duration](#LuCI.response+duration) : <code>number</code>
            * [.url](#LuCI.response+url) : <code>string</code>
            * [.clone([content])](#LuCI.response+clone) ⇒ [<code>response</code>](#LuCI.response)
            * [.json()](#LuCI.response+json) ⇒ <code>\*</code>
            * [.text()](#LuCI.response+text) ⇒ <code>string</code>
            * [.blob()](#LuCI.response+blob) ⇒ <code>Blob</code>
        * [.request](#LuCI.request)
            * _instance_
                * [.expandURL(url)](#LuCI.request+expandURL) ⇒ <code>string</code>
                * [.request(target, [options])](#LuCI.request+request) ⇒ [<code>Promise.&lt;response&gt;</code>](#LuCI.response)
                * [.handleReadyStateChange(resolveFn, rejectFn, [ev])](#LuCI.request+handleReadyStateChange) ⇒ <code>void</code>
                * [.get(url, [options])](#LuCI.request+get) ⇒ [<code>Promise.&lt;response&gt;</code>](#LuCI.response)
                * [.post(url, [data], [options])](#LuCI.request+post) ⇒ [<code>Promise.&lt;response&gt;</code>](#LuCI.response)
                * [.addInterceptor(interceptorFn)](#LuCI.request+addInterceptor) ⇒ [<code>interceptorFn</code>](#LuCI.request.interceptorFn)
                * [.removeInterceptor(interceptorFn)](#LuCI.request+removeInterceptor) ⇒ <code>boolean</code>
            * _static_
                * [.poll](#LuCI.request.poll)
                    * _instance_
                        * [.add(interval, url, [options], [callback])](#LuCI.request.poll+add) ⇒ <code>function</code>
                        * [.remove(entry)](#LuCI.request.poll+remove) ⇒ <code>boolean</code>
                        * [.start()](#LuCI.request.poll+start) ⇒ <code>boolean</code>
                        * [.stop()](#LuCI.request.poll+stop) ⇒ <code>boolean</code>
                        * [.active()](#LuCI.request.poll+active) ⇒ <code>boolean</code>
                    * _inner_
                        * [~callbackFn](#LuCI.request.poll..callbackFn) : <code>function</code>
                * [.RequestOptions](#LuCI.request.RequestOptions) : <code>Object</code>
                * [.interceptorFn](#LuCI.request.interceptorFn) : <code>function</code>
        * [.poll](#LuCI.poll)
            * [.add(fn, interval)](#LuCI.poll+add) ⇒ <code>boolean</code>
            * [.remove(fn)](#LuCI.poll+remove) ⇒ <code>boolean</code>
            * [.start()](#LuCI.poll+start) ⇒ <code>boolean</code>
            * [.stop()](#LuCI.poll+stop) ⇒ <code>boolean</code>
            * [.active()](#LuCI.poll+active) ⇒ <code>boolean</code>
        * [.dom](#LuCI.dom)
            * _instance_
                * [.elem(e)](#LuCI.dom+elem) ⇒ <code>boolean</code>
                * [.parse(s)](#LuCI.dom+parse) ⇒ <code>Node</code>
                * [.matches(node, [selector])](#LuCI.dom+matches) ⇒ <code>boolean</code>
                * [.parent(node, [selector])](#LuCI.dom+parent) ⇒ <code>Node</code> \| <code>null</code>
                * [.append(node, [children])](#LuCI.dom+append) ⇒ <code>Node</code> \| <code>null</code>
                * [.content(node, [children])](#LuCI.dom+content) ⇒ <code>Node</code> \| <code>null</code>
                * [.attr(node, key, [val])](#LuCI.dom+attr) ⇒ <code>null</code>
                * [.create(html, [attr], [data])](#LuCI.dom+create) ⇒ <code>Node</code>
                * [.data(node, [key], [val])](#LuCI.dom+data) ⇒ <code>\*</code>
                * [.bindClassInstance(node, inst)](#LuCI.dom+bindClassInstance) ⇒ <code>Class</code>
                * [.findClassInstance(node)](#LuCI.dom+findClassInstance) ⇒ <code>Class</code> \| <code>null</code>
                * [.callClassMethod(node, method, ...args)](#LuCI.dom+callClassMethod) ⇒ <code>\*</code> \| <code>null</code>
                * [.isEmpty(node, [ignoreFn])](#LuCI.dom+[isEmpty](/luci-docs/luci-api-uci.md)) ⇒ <code>boolean</code>
            * _inner_
                * [~ignoreCallbackFn](#LuCI.dom..ignoreCallbackFn) ⇒ <code>boolean</code>
        * [.session](#LuCI.session)
            * [.getID()](#LuCI.session+getID) ⇒ <code>string</code>
            * [.getToken()](#LuCI.session+getToken) ⇒ <code>string</code> \| <code>null</code>
            * [.getLocalData([key])](#LuCI.session+getLocalData) ⇒ <code>\*</code>
            * [.setLocalData(key, value)](#LuCI.session+setLocalData) ⇒ <code>boolean</code>
        * [.view](#LuCI.view)
            * *[.load()](#LuCI.view+load) ⇒ <code>\*</code> \| <code>Promise.&lt;\*&gt;</code>*
            * *[.render(load_results)](#LuCI.view+render) ⇒ <code>Node</code> \| <code>Promise.&lt;Node&gt;</code>*
            * [.handleSave(ev)](#LuCI.view+handleSave) ⇒ <code>\*</code> \| <code>Promise.&lt;\*&gt;</code>
            * [.handleSaveApply(ev, mode)](#LuCI.view+handleSaveApply) ⇒ <code>\*</code> \| <code>Promise.&lt;\*&gt;</code>
            * [.handleReset(ev)](#LuCI.view+handleReset) ⇒ <code>\*</code> \| <code>Promise.&lt;\*&gt;</code>
            * [.addFooter()](#LuCI.view+addFooter) ⇒ <code>DocumentFragment</code>
        * ~~[.xhr](#LuCI.xhr)~~
            * ~~[.get(url, [data], [callback], [timeout])](#LuCI.xhr+get) ⇒ <code>Promise.&lt;null&gt;</code>~~
            * ~~[.post(url, [data], [callback], [timeout])](#LuCI.xhr+post) ⇒ <code>Promise.&lt;null&gt;</code>~~
            * ~~[.cancel()](#LuCI.xhr+cancel)~~
            * ~~[.busy()](#LuCI.xhr+busy) ⇒ <code>boolean</code>~~
            * ~~[.abort()](#LuCI.xhr+abort)~~
            * ~~[.send_form()](#LuCI.xhr+send_form)~~
        * [.requestCallbackFn](#LuCI.requestCallbackFn) : <code>function</code>

<a name="new_LuCI_new"></a>

### new LuCI(window, document, undefined)
This is the LuCI base class. It is automatically instantiated and
accessible using the global `L` variable.


| Param | Type | Description |
| --- | --- | --- |
| window | <code>Window</code> | The browser global `window` object. |
| document | <code>Document</code> | The DOM `document` root for the current page. |
| undefined | <code>undefined</code> | Local `undefined` slot (prevents shadowing and ensures `undefined` is the real undefined value). |

<a name="LuCI+env"></a>

### luCI.env
The `env` object holds environment settings used by LuCI, such
as request timeouts, base URLs, etc.

**Kind**: instance property of [<code>LuCI</code>](#LuCI)  
<a name="LuCI+naturalCompare"></a>

### luCI.naturalCompare ⇒ <code>number</code>
Compares two values numerically and returns -1, 0, or 1 depending
on whether the first value is smaller, equal to, or larger than the
second one respectively.

This function is meant to be used as a comparator function for
Array.sort().

**Kind**: instance property of [<code>LuCI</code>](#LuCI)  
**Returns**: <code>number</code> - Returns -1 if the first value is smaller than the second one.
Returns 0 if both values are equal.
Returns 1 if the first value is larger than the second one.  

| Param | Type | Description |
| --- | --- | --- |
| a | <code>\*</code> | The first value |
| b | <code>\*</code> | The second value. |

<a name="LuCI+dom"></a>

### ~~luCI.dom~~
***Deprecated***

Legacy `L.dom` class alias. New view code should use `'require dom';`
to request the `LuCI.dom` class.

**Kind**: instance property of [<code>LuCI</code>](#LuCI)  
<a name="LuCI+view"></a>

### ~~luCI.view~~
***Deprecated***

Legacy `L.view` class alias. New view code should use `'require view';`
to request the `LuCI.view` class.

**Kind**: instance property of [<code>LuCI</code>](#LuCI)  
<a name="LuCI+Poll"></a>

### ~~luCI.Poll~~
***Deprecated***

Legacy `L.Poll` class alias. New view code should use `'require poll';`
to request the `LuCI.poll` class.

**Kind**: instance property of [<code>LuCI</code>](#LuCI)  
<a name="LuCI+Request"></a>

### ~~luCI.Request~~
***Deprecated***

Legacy `L.Request` class alias. New view code should use `'require request';`
to request the `LuCI.request` class.

**Kind**: instance property of [<code>LuCI</code>](#LuCI)  
<a name="LuCI+Class"></a>

### ~~luCI.Class~~
***Deprecated***

Legacy `L.Class` class alias. New view code should use `'require baseclass';`
to request the `LuCI.baseclass` class.

**Kind**: instance property of [<code>LuCI</code>](#LuCI)  
<a name="LuCI+raise"></a>

### luCI.raise([type], [fmt], [...args])
Captures the current stack trace and throws an error of the
specified type as a new exception. Also logs the exception as
an error to the debug console if it is available.

**Kind**: instance method of [<code>LuCI</code>](#LuCI)  
**Throws**:

- <code>Error</code> Throws the created error object with the captured stack trace
appended to the message and the type set to the given type
argument or copied from the given error instance.


| Param | Type | Default | Description |
| --- | --- | --- | --- |
| [type] | <code>Error</code> \| <code>string</code> | <code>Error</code> | Either a string specifying the type of the error to throw or an existing `Error` instance to copy. |
| [fmt] | <code>string</code> | <code>&quot;Unspecified error&quot;</code> | A format string which is used to form the error message, together with all subsequent optional arguments. |
| [...args] | <code>\*</code> |  | Zero or more variable arguments to the supplied format string. |

<a name="LuCI+error"></a>

### luCI.error([type], [fmt], [...args])
A wrapper around [raise()](#LuCI+raise) which also renders
the error either as modal overlay when `ui.js` is already loaded
or directly into the view body.

**Kind**: instance method of [<code>LuCI</code>](#LuCI)  
**Throws**:

- <code>Error</code> Throws the created error object with the captured stack trace
appended to the message and the type set to the given type
argument or copied from the given error instance.


| Param | Type | Default | Description |
| --- | --- | --- | --- |
| [type] | <code>Error</code> \| <code>string</code> | <code>Error</code> | Either a string specifying the type of the error to throw or an existing `Error` instance to copy. |
| [fmt] | <code>string</code> | <code>&quot;Unspecified error&quot;</code> | A format string which is used to form the error message, together with all subsequent optional arguments. |
| [...args] | <code>\*</code> |  | Zero or more variable arguments to the supplied format string. |

<a name="LuCI+bind"></a>

### luCI.bind(fn, self, [...args]) ⇒ <code>function</code>
Return a bound function using the given `self` as `this` context
and any further arguments as parameters to the bound function.

**Kind**: instance method of [<code>LuCI</code>](#LuCI)  
**Returns**: <code>function</code> - Returns the bound function.  

| Param | Type | Description |
| --- | --- | --- |
| fn | <code>function</code> | The function to bind. |
| self | <code>\*</code> | The value to bind as `this` context to the specified function. |
| [...args] | <code>\*</code> | Zero or more variable arguments which are bound to the function as parameters. |

<a name="LuCI+require"></a>

### luCI.require(name, [from]) ⇒ [<code>Promise.&lt;baseclass&gt;</code>](#LuCI.baseclass)
Load an additional LuCI JavaScript class and its dependencies,
instantiate it and return the resulting class instance. Each
class is only loaded once. Subsequent attempts to load the same
class will return the already instantiated class.

**Kind**: instance method of [<code>LuCI</code>](#LuCI)  
**Returns**: [<code>Promise.&lt;baseclass&gt;</code>](#LuCI.baseclass) - Returns the instantiated class.  
**Throws**:

- <code>DependencyError</code> Throws a `DependencyError` when the class to load includes
circular dependencies.
- <code>NetworkError</code> Throws `NetworkError` when the underlying [request](#LuCI.request)
call failed.
- <code>SyntaxError</code> Throws `SyntaxError` when the loaded class file code cannot
be interpreted by `eval`.
- <code>TypeError</code> Throws `TypeError` when the class file could be loaded and
interpreted, but when invoking its code did not yield a valid
class instance.


| Param | Type | Default | Description |
| --- | --- | --- | --- |
| name | <code>string</code> |  | The name of the class to load in dotted notation. Dots will be replaced by spaces and joined with the runtime-determined base URL of LuCI.js to form an absolute URL to load the class file from. |
| [from] | <code>Array.&lt;string&gt;</code> | <code>[]</code> | Optional dependency chain used during dependency resolution. This array contains the sequence of class names already being resolved (the caller stack). It is used to detect circular dependencies — if `name` appears in `from` a `DependencyError` is thrown. |

<a name="LuCI+hasSystemFeature"></a>

### luCI.hasSystemFeature(feature, [subfeature]) ⇒ <code>boolean</code> \| <code>null</code>
Test whether a particular system feature is available, such as
hostapd SAE support or an installed firewall. The features are
queried once at the beginning of the LuCI session and cached in
`SessionStorage` throughout the lifetime of the associated tab or
browser window.

**Kind**: instance method of [<code>LuCI</code>](#LuCI)  
**Returns**: <code>boolean</code> \| <code>null</code> - Return `true` if the queried feature (and sub-feature) is available
or `false` if the requested feature isn't present or known.
Return `null` when a sub-feature was queried for a feature which
has no sub-features.  

| Param | Type | Description |
| --- | --- | --- |
| feature | <code>string</code> | The feature to test. For a detailed list of known feature flags, see `/modules/luci-base/root/usr/share/rpcd/ucode/luci`. |
| [subfeature] | <code>string</code> | Some feature classes like `hostapd` provide sub-feature flags, such as `sae` or `11w` support. The `subfeature` argument can be used to query these. |

<a name="LuCI+fspath"></a>

### luCI.fspath([...parts]) ⇒ <code>string</code>
Construct an absolute filesystem path relative to the server
document root.

**Kind**: instance method of [<code>LuCI</code>](#LuCI)  
**Returns**: <code>string</code> - Return the joined path.  

| Param | Type | Description |
| --- | --- | --- |
| [...parts] | <code>string</code> | An array of parts to join into a path. |

<a name="LuCI+path"></a>

### luCI.path([prefix], [...parts]) ⇒ <code>string</code>
Construct a relative URL path from the given prefix and parts.
The resulting URL is guaranteed to contain only the characters
`a-z`, `A-Z`, `0-9`, `_`, `.`, `%`, `,`, `;`, and `-` as well
as `/` for the path separator. Suffixing '?x=y&foo=bar' URI
parameters also limited to the aforementioned characters is
permissible.

**Kind**: instance method of [<code>LuCI</code>](#LuCI)  
**Returns**: <code>string</code> - Return the joined URL path.  

| Param | Type | Description |
| --- | --- | --- |
| [prefix] | <code>string</code> | The prefix to join the given parts with. If the `prefix` is omitted, it defaults to an empty string. |
| [...parts] | <code>string</code> | An array of parts to join into a URL path. Parts may contain slashes and any of the other characters mentioned above. |

<a name="LuCI+url"></a>

### luCI.url([...parts]) ⇒ <code>string</code>
Construct a URL with a path relative to the script path of the server
side LuCI application (usually `/cgi-bin/luci`).

The resulting URL is guaranteed to contain only the characters
`a-z`, `A-Z`, `0-9`, `_`, `.`, `%`, `,`, `;`, and `-` as well
as `/` for the path separator. Suffixing '?x=y&foo=bar' URI
parameters also limited to the aforementioned characters is
permissible.

**Kind**: instance method of [<code>LuCI</code>](#LuCI)  
**Returns**: <code>string</code> - Returns the resulting URL path.  

| Param | Type | Description |
| --- | --- | --- |
| [...parts] | <code>string</code> | An array of parts to join into a URL path. Parts may contain slashes and any of the other characters mentioned above. |

<a name="LuCI+resource"></a>

### luCI.resource([...parts]) ⇒ <code>string</code>
Construct a URL path relative to the global static resource path
of the LuCI ui (usually `/luci-static/resources`).

The resulting URL is guaranteed to contain only the characters
`a-z`, `A-Z`, `0-9`, `_`, `.`, `%`, `,`, `;`, and `-` as well
as `/` for the path separator. Suffixing '?x=y&foo=bar' URI
parameters also limited to the aforementioned characters is
permissible.

**Kind**: instance method of [<code>LuCI</code>](#LuCI)  
**Returns**: <code>string</code> - Returns the resulting URL path.  

| Param | Type | Description |
| --- | --- | --- |
| [...parts] | <code>string</code> | An array of parts to join into a URL path. Parts may contain slashes and any of the other characters mentioned above. |

<a name="LuCI+media"></a>

### luCI.media([...parts]) ⇒ <code>string</code>
Construct a URL path relative to the media resource path of the
LuCI ui (usually `/luci-static/$theme_name`).

The resulting URL is guaranteed to contain only the characters
`a-z`, `A-Z`, `0-9`, `_`, `.`, `%`, `,`, `;`, and `-` as well
as `/` for the path separator. Suffixing '?x=y&foo=bar' URI
parameters also limited to the aforementioned characters is
permissible.

**Kind**: instance method of [<code>LuCI</code>](#LuCI)  
**Returns**: <code>string</code> - Returns the resulting URL path.  

| Param | Type | Description |
| --- | --- | --- |
| [...parts] | <code>string</code> | An array of parts to join into a URL path. Parts may contain slashes and any of the other characters mentioned above. |

<a name="LuCI+location"></a>

### luCI.location() ⇒ <code>string</code>
Return the complete URL path to the current view.

**Kind**: instance method of [<code>LuCI</code>](#LuCI)  
**Returns**: <code>string</code> - Returns the URL path to the current view.  
<a name="LuCI+isObject"></a>

### luCI.isObject([val]) ⇒ <code>boolean</code>
Tests whether the passed argument is a JavaScript object.
This function is meant to be an object counterpart to the
standard `Array.isArray()` function.

**Kind**: instance method of [<code>LuCI</code>](#LuCI)  
**Returns**: <code>boolean</code> - Returns `true` if the given value is of a type object and
not `null`, else returns `false`.  

| Param | Type | Description |
| --- | --- | --- |
| [val] | <code>\*</code> | The value to test |

<a name="LuCI+isArguments"></a>

### luCI.isArguments([val]) ⇒ <code>boolean</code>
Tests whether the passed argument is a function arguments object.

**Kind**: instance method of [<code>LuCI</code>](#LuCI)  
**Returns**: <code>boolean</code> - Returns `true` if the given value is a function arguments object,
else returns `false`.  

| Param | Type | Description |
| --- | --- | --- |
| [val] | <code>\*</code> | The value to test |

<a name="LuCI+sortedKeys"></a>

### luCI.sortedKeys(obj, [key], [sortmode]) ⇒ <code>Array.&lt;string&gt;</code>
Return an array of sorted object keys, optionally sorted by
a different key or a different sorting mode.

**Kind**: instance method of [<code>LuCI</code>](#LuCI)  
**Returns**: <code>Array.&lt;string&gt;</code> - Returns an array containing the sorted keys of the given object.  

| Param | Type | Description |
| --- | --- | --- |
| obj | <code>object</code> | The object to extract the keys from. If the given value is not an object, the function will return an empty array. |
| [key] | <code>string</code> \| <code>null</code> | Specifies the key to order by. This is mainly useful for nested objects of objects or objects of arrays when sorting shall not be performed by the primary object keys but by some other key pointing to a value within the nested values. |
| [sortmode] | <code>&quot;addr&quot;</code> \| <code>&quot;num&quot;</code> | Can be either `addr` or `num` to override the natural lexicographic sorting with a sorting suitable for IP/MAC style addresses or numeric values respectively. |

<a name="LuCI+sortedArray"></a>

### luCI.sortedArray(val) ⇒ <code>Array.&lt;\*&gt;</code>
Converts the given value to an array using toArray() if needed,
performs a numerical sort using naturalCompare() and returns the
result. If the input already is an array, no copy is being made
and the sorting is performed in-place.

**Kind**: instance method of [<code>LuCI</code>](#LuCI)  
**Returns**: <code>Array.&lt;\*&gt;</code> - Returns the resulting, numerically sorted array.  
**See**

- toArray
- naturalCompare


| Param | Type | Description |
| --- | --- | --- |
| val | <code>\*</code> | The input value to sort (and convert to an array if needed). |

<a name="LuCI+toArray"></a>

### luCI.toArray(val) ⇒ <code>Array.&lt;\*&gt;</code>
Converts the given value to an array. If the given value is of
type array, it is returned as-is, values of a type object are
returned as one-element array containing the object, empty
strings and `null` values are returned as an empty array, all other
values are converted using `String()`, trimmed, split on white
space and returned as an array.

**Kind**: instance method of [<code>LuCI</code>](#LuCI)  
**Returns**: <code>Array.&lt;\*&gt;</code> - Returns the resulting array.  

| Param | Type | Description |
| --- | --- | --- |
| val | <code>\*</code> | The value to convert into an array. |

<a name="LuCI+resolveDefault"></a>

### luCI.resolveDefault(value, defvalue) ⇒ <code>Promise.&lt;\*&gt;</code>
Returns a promise resolving with either the given value or with
the given default in case the input value is a rejecting promise.

**Kind**: instance method of [<code>LuCI</code>](#LuCI)  
**Returns**: <code>Promise.&lt;\*&gt;</code> - Returns a new promise resolving either to the given input value or
to the given default value on error.  

| Param | Type | Description |
| --- | --- | --- |
| value | <code>\*</code> | The value to resolve the promise with. |
| defvalue | <code>\*</code> | The default value to resolve the promise with in case the given input value is a rejecting promise. |

<a name="LuCI+get"></a>

### ~~luCI.get(url, [args], cb) ⇒ <code>Promise.&lt;null&gt;</code>~~
***Deprecated***

Issues a GET request to the given url and invokes the specified
callback function. The function is a wrapper around
[Request.request()](#LuCI.request+request).

**Kind**: instance method of [<code>LuCI</code>](#LuCI)  
**Returns**: <code>Promise.&lt;null&gt;</code> - Returns a promise resolving to `null` when concluded.  

| Param | Type | Description |
| --- | --- | --- |
| url | <code>string</code> | The URL to request. |
| [args] | <code>Object.&lt;string, string&gt;</code> | Additional query string arguments to append to the URL. |
| cb | [<code>requestCallbackFn</code>](#LuCI.requestCallbackFn) | The callback function to invoke when the request finishes. |

<a name="LuCI+post"></a>

### ~~luCI.post(url, [args], cb) ⇒ <code>Promise.&lt;null&gt;</code>~~
***Deprecated***

Issues a POST request to the given url and invokes the specified
callback function. The function is a wrapper around
[Request.request()](#LuCI.request+request). The request is
sent using `application/x-www-form-urlencoded` encoding and will
contain a field `token` with the current value of `LuCI.env.token`
by default.

**Kind**: instance method of [<code>LuCI</code>](#LuCI)  
**Returns**: <code>Promise.&lt;null&gt;</code> - Returns a promise resolving to `null` when concluded.  

| Param | Type | Description |
| --- | --- | --- |
| url | <code>string</code> | The URL to request. |
| [args] | <code>Object.&lt;string, string&gt;</code> | Additional post arguments to append to the request body. |
| cb | [<code>requestCallbackFn</code>](#LuCI.requestCallbackFn) | The callback function to invoke when the request finishes. |

<a name="LuCI+poll"></a>

### ~~luCI.poll(interval, url, [args], cb, [post]) ⇒ <code>function</code>~~
***Deprecated***

Register a polling HTTP request that invokes the specified
callback function. The function is a wrapper around
[Request.poll.add()](#LuCI.request.poll+add).

**Kind**: instance method of [<code>LuCI</code>](#LuCI)  
**Returns**: <code>function</code> - Returns the internally created function that has been passed to
[Request.poll.add()](#LuCI.request.poll+add). This value can
be passed to [Poll.remove()](LuCI.poll.remove) to remove the
polling request.  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| interval | <code>number</code> |  | The poll interval to use. If set to a value less than or equal to `0`, it will default to the global poll interval configured in `LuCI.env.pollinterval`. |
| url | <code>string</code> |  | The URL to request. |
| [args] | <code>Object.&lt;string, string&gt;</code> |  | Specifies additional arguments for the request. For GET requests, the arguments are appended to the URL as query string, for POST requests, they'll be added to the request body. |
| cb | [<code>requestCallbackFn</code>](#LuCI.requestCallbackFn) |  | The callback function to invoke whenever a request finishes. |
| [post] | <code>boolean</code> | <code>false</code> | When set to `false` or not specified, poll requests will be made using the GET method. When set to `true`, POST requests will be issued. In the case of POST requests, the request body will contain an argument `token` with the current value of `LuCI.env.token` by default, regardless of the parameters specified with `args`. |

<a name="LuCI+hasViewPermission"></a>

### luCI.hasViewPermission() ⇒ <code>boolean</code> \| <code>null</code>
Check whether a view has sufficient permissions.

**Kind**: instance method of [<code>LuCI</code>](#LuCI)  
**Returns**: <code>boolean</code> \| <code>null</code> - Returns `null` if the current session has no permission at all to
load resources required by the view. Returns `false` if readonly
permissions are granted or `true` if at least one required ACL
group is granted with write permissions.  
<a name="LuCI+stop"></a>

### ~~luCI.stop(entry) ⇒ <code>boolean</code>~~
***Deprecated***

Deprecated wrapper around [Poll.remove()](LuCI.poll.remove).

**Kind**: instance method of [<code>LuCI</code>](#LuCI)  
**Returns**: <code>boolean</code> - Returns `true` when the function has been removed or `false` if
it could not be found.  

| Param | Type | Description |
| --- | --- | --- |
| entry | <code>function</code> | The polling function to remove. |

<a name="LuCI+halt"></a>

### ~~luCI.halt() ⇒ <code>boolean</code>~~
***Deprecated***

Deprecated wrapper around [Poll.stop()](LuCI.poll.stop).

**Kind**: instance method of [<code>LuCI</code>](#LuCI)  
**Returns**: <code>boolean</code> - Returns `true` when the polling loop has been stopped or `false`
when it didn't run to begin with.  
<a name="LuCI+run"></a>

### ~~luCI.run() ⇒ <code>boolean</code>~~
***Deprecated***

Deprecated wrapper around [Poll.start()](LuCI.poll.start).

**Kind**: instance method of [<code>LuCI</code>](#LuCI)  
**Returns**: <code>boolean</code> - Returns `true` when the polling loop has been started or `false`
when it was already running.  
<a name="LuCI.baseclass"></a>

### LuCI.baseclass
`LuCI.baseclass` is the abstract base class all LuCI classes inherit from.

It provides a simple means to create subclasses of given classes and
implements prototypal inheritance.

**Kind**: static class of [<code>LuCI</code>](#LuCI)  

* [.baseclass](#LuCI.baseclass)
    * _instance_
        * [.varargs(args, offset, [...extra_args])](#LuCI.baseclass+varargs) ⇒ <code>Array.&lt;\*&gt;</code>
        * [.super(key, [callArgs])](#LuCI.baseclass+super) ⇒ <code>\*</code> \| <code>null</code>
        * [.toString()](#LuCI.baseclass+toString) ⇒ <code>string</code>
    * _static_
        * [.extend(properties)](#LuCI.baseclass.extend) ⇒ [<code>baseclass</code>](#LuCI.baseclass)
        * [.singleton(properties, ...new_args)](#LuCI.baseclass.singleton) ⇒ [<code>baseclass</code>](#LuCI.baseclass)
        * [.instantiate(args)](#LuCI.baseclass.instantiate) ⇒ [<code>baseclass</code>](#LuCI.baseclass)
        * [.isSubclass(classValue)](#LuCI.baseclass.isSubclass) ⇒ <code>boolean</code>

<a name="LuCI.baseclass+varargs"></a>

#### baseclass.varargs(args, offset, [...extra_args]) ⇒ <code>Array.&lt;\*&gt;</code>
Extract all values from the given argument array beginning from
`offset` and prepend any further given optional parameters to
the beginning of the resulting array copy.

**Kind**: instance method of [<code>baseclass</code>](#LuCI.baseclass)  
**Returns**: <code>Array.&lt;\*&gt;</code> - Returns a new array consisting of the optional extra arguments
and the values extracted from the `args` array beginning with
`offset`.  

| Param | Type | Description |
| --- | --- | --- |
| args | <code>Array.&lt;\*&gt;</code> | The array to extract the values from. |
| offset | <code>number</code> | The offset from which to extract the values. An offset of `0` would copy all values till the end. |
| [...extra_args] | <code>\*</code> | Extra arguments to add to prepend to the resulting array. |

<a name="LuCI.baseclass+super"></a>

#### baseclass.super(key, [callArgs]) ⇒ <code>\*</code> \| <code>null</code>
Walks up the parent class chain and looks for a class member
called `key` in any of the parent classes this class inherits
from. Returns the member value of the superclass or calls the
member as a function and returns its return value when the
optional `callArgs` array is given.

This function has two signatures and is sensitive to the
amount of arguments passed to it:
 - `super('key')` -
	Returns the value of `key` when found within one of the
	parent classes.
 - `super('key', ['arg1', 'arg2'])` -
	Calls the `key()` method with parameters `arg1` and `arg2`
	when found within one of the parent classes.

**Kind**: instance method of [<code>baseclass</code>](#LuCI.baseclass)  
**Returns**: <code>\*</code> \| <code>null</code> - Returns the value of the found member or the return value of
the call to the found method. Returns `null` when no member
was found in the parent class chain or when the call to the
superclass method returned `null`.  
**Throws**:

- <code>ReferenceError</code> Throws a `ReferenceError` when `callArgs` are specified and
the found member named by `key` is not a function value.


| Param | Type | Description |
| --- | --- | --- |
| key | <code>string</code> | The name of the superclass member to retrieve. |
| [callArgs] | <code>\*</code> \| <code>Array.&lt;\*&gt;</code> | Arguments to pass when invoking the superclass method. May be  either an argument array or variadic arguments. |

<a name="LuCI.baseclass+toString"></a>

#### baseclass.toString() ⇒ <code>string</code>
Returns a string representation of this class.

**Kind**: instance method of [<code>baseclass</code>](#LuCI.baseclass)  
**Returns**: <code>string</code> - Returns a string representation of this class containing the
constructor functions `displayName` and describing the class
members and their respective types.  
<a name="LuCI.baseclass.extend"></a>

#### baseclass.extend(properties) ⇒ [<code>baseclass</code>](#LuCI.baseclass)
Extends this base class with the properties described in
`properties` and returns a new subclassed Class instance

**Kind**: static method of [<code>baseclass</code>](#LuCI.baseclass)  
**Returns**: [<code>baseclass</code>](#LuCI.baseclass) - Returns a new LuCI.baseclass subclassed from this class, extended
by the given properties and with its prototype set to this base
class to enable inheritance. The resulting value represents a
class constructor and can be instantiated with `new`.  
**this**: <code>{LuCI.baseclass}</code>  

| Param | Type | Description |
| --- | --- | --- |
| properties | <code>Object.&lt;string, \*&gt;</code> | An object describing the properties to add to the new subclass. |

<a name="LuCI.baseclass.singleton"></a>

#### baseclass.singleton(properties, ...new_args) ⇒ [<code>baseclass</code>](#LuCI.baseclass)
Extends this base class with the properties described in
`properties`, instantiates the resulting subclass using
the given arguments passed to this function
and returns the resulting subclassed Class instance.

This function serves as a convenience shortcut for
[Class.extend()](#LuCI.baseclass.extend) and subsequent
`new`.

**Kind**: static method of [<code>baseclass</code>](#LuCI.baseclass)  
**Returns**: [<code>baseclass</code>](#LuCI.baseclass) - Returns a new LuCI.baseclass instance extended by the given
properties with its prototype set to this base class to
enable inheritance.  

| Param | Type | Description |
| --- | --- | --- |
| properties | <code>Object.&lt;string, \*&gt;</code> | An object describing the properties to add to the new subclass. |
| ...new_args | <code>\*</code> | Arguments forwarded to the constructor of the generated subclass. |

<a name="LuCI.baseclass.instantiate"></a>

#### baseclass.instantiate(args) ⇒ [<code>baseclass</code>](#LuCI.baseclass)
Calls the class constructor using `new` with the given argument
array being passed as variadic parameters to the constructor.

**Kind**: static method of [<code>baseclass</code>](#LuCI.baseclass)  
**Returns**: [<code>baseclass</code>](#LuCI.baseclass) - Returns a new LuCI.baseclass instance extended by the given
properties with its prototype set to this base class to
enable inheritance.  

| Param | Type | Description |
| --- | --- | --- |
| args | <code>Array.&lt;\*&gt;</code> | An array of arbitrary values which will be passed as arguments to the constructor function. |

<a name="LuCI.baseclass.isSubclass"></a>

#### baseclass.isSubclass(classValue) ⇒ <code>boolean</code>
Checks whether the given class value is a subclass of this class.

**Kind**: static method of [<code>baseclass</code>](#LuCI.baseclass)  
**Returns**: <code>boolean</code> - Returns `true` when the given `classValue` is a subclass of this
class or `false` if the given value is not a valid class or not
a subclass of this class.  

| Param | Type | Description |
| --- | --- | --- |
| classValue | [<code>baseclass</code>](#LuCI.baseclass) | The class object to test. |

<a name="LuCI.headers"></a>

### LuCI.headers
The `Headers` class is an internal utility class exposed in HTTP
response objects using the `response.headers` property.

**Kind**: static class of [<code>LuCI</code>](#LuCI)  

* [.headers](#LuCI.headers)
    * [.has(name)](#LuCI.headers+has) ⇒ <code>boolean</code>
    * [.get(name)](#LuCI.headers+get) ⇒ <code>string</code> \| <code>null</code>

<a name="LuCI.headers+has"></a>

#### headers.has(name) ⇒ <code>boolean</code>
Checks whether the given header name is present.
Note: Header-Names are case-insensitive.

**Kind**: instance method of [<code>headers</code>](#LuCI.headers)  
**Returns**: <code>boolean</code> - Returns `true` if the header name is present, `false` otherwise  

| Param | Type | Description |
| --- | --- | --- |
| name | <code>string</code> | The header name to check |

<a name="LuCI.headers+get"></a>

#### headers.get(name) ⇒ <code>string</code> \| <code>null</code>
Returns the value of the given header name.
Note: Header-Names are case-insensitive.

**Kind**: instance method of [<code>headers</code>](#LuCI.headers)  
**Returns**: <code>string</code> \| <code>null</code> - The value of the given header name or `null` if the header isn't present.  

| Param | Type | Description |
| --- | --- | --- |
| name | <code>string</code> | The header name to read |

<a name="LuCI.response"></a>

### LuCI.response
The `Response` class is an internal utility class representing HTTP responses.

**Kind**: static class of [<code>LuCI</code>](#LuCI)  

* [.response](#LuCI.response)
    * [.ok](#LuCI.response+ok) : <code>boolean</code>
    * [.status](#LuCI.response+status) : <code>number</code>
    * [.statusText](#LuCI.response+statusText) : <code>string</code>
    * [.headers](#LuCI.response+headers) : [<code>headers</code>](#LuCI.headers)
    * [.duration](#LuCI.response+duration) : <code>number</code>
    * [.url](#LuCI.response+url) : <code>string</code>
    * [.clone([content])](#LuCI.response+clone) ⇒ [<code>response</code>](#LuCI.response)
    * [.json()](#LuCI.response+json) ⇒ <code>\*</code>
    * [.text()](#LuCI.response+text) ⇒ <code>string</code>
    * [.blob()](#LuCI.response+blob) ⇒ <code>Blob</code>

<a name="LuCI.response+ok"></a>

#### response.ok : <code>boolean</code>
Describes whether the response is successful (status codes `200..299`) or not

**Kind**: instance property of [<code>response</code>](#LuCI.response)  
<a name="LuCI.response+status"></a>

#### response.status : <code>number</code>
The numeric HTTP status code of the response

**Kind**: instance property of [<code>response</code>](#LuCI.response)  
<a name="LuCI.response+statusText"></a>

#### response.statusText : <code>string</code>
The HTTP status description message of the response

**Kind**: instance property of [<code>response</code>](#LuCI.response)  
<a name="LuCI.response+headers"></a>

#### response.headers : [<code>headers</code>](#LuCI.headers)
The HTTP headers of the response

**Kind**: instance property of [<code>response</code>](#LuCI.response)  
<a name="LuCI.response+duration"></a>

#### response.duration : <code>number</code>
The total duration of the HTTP request in milliseconds

**Kind**: instance property of [<code>response</code>](#LuCI.response)  
<a name="LuCI.response+url"></a>

#### response.url : <code>string</code>
The final URL of the request, i.e. after following redirects.

**Kind**: instance property of [<code>response</code>](#LuCI.response)  
<a name="LuCI.response+clone"></a>

#### response.clone([content]) ⇒ [<code>response</code>](#LuCI.response)
Clones the given response object, optionally overriding the content
of the cloned instance.

**Kind**: instance method of [<code>response</code>](#LuCI.response)  
**Returns**: [<code>response</code>](#LuCI.response) - The cloned `Response` instance.  

| Param | Type | Description |
| --- | --- | --- |
| [content] | <code>\*</code> | Override the content of the cloned response. Object values will be treated as JSON response data, all other types will be converted using `String()` and treated as response text. |

<a name="LuCI.response+json"></a>

#### response.json() ⇒ <code>\*</code>
Access the response content as JSON data.

**Kind**: instance method of [<code>response</code>](#LuCI.response)  
**Returns**: <code>\*</code> - The parsed JSON data.  
**Throws**:

- <code>SyntaxError</code> Throws `SyntaxError` if the content isn't valid JSON.

<a name="LuCI.response+text"></a>

#### response.text() ⇒ <code>string</code>
Access the response content as string.

**Kind**: instance method of [<code>response</code>](#LuCI.response)  
**Returns**: <code>string</code> - The response content.  
<a name="LuCI.response+blob"></a>

#### response.blob() ⇒ <code>Blob</code>
Access the response content as blob.

**Kind**: instance method of [<code>response</code>](#LuCI.response)  
**Returns**: <code>Blob</code> - The response content as blob.  
<a name="LuCI.request"></a>

### LuCI.request
The `Request` class allows initiating HTTP requests and provides utilities
for dealing with responses.

**Kind**: static class of [<code>LuCI</code>](#LuCI)  

* [.request](#LuCI.request)
    * _instance_
        * [.expandURL(url)](#LuCI.request+expandURL) ⇒ <code>string</code>
        * [.request(target, [options])](#LuCI.request+request) ⇒ [<code>Promise.&lt;response&gt;</code>](#LuCI.response)
        * [.handleReadyStateChange(resolveFn, rejectFn, [ev])](#LuCI.request+handleReadyStateChange) ⇒ <code>void</code>
        * [.get(url, [options])](#LuCI.request+get) ⇒ [<code>Promise.&lt;response&gt;</code>](#LuCI.response)
        * [.post(url, [data], [options])](#LuCI.request+post) ⇒ [<code>Promise.&lt;response&gt;</code>](#LuCI.response)
        * [.addInterceptor(interceptorFn)](#LuCI.request+addInterceptor) ⇒ [<code>interceptorFn</code>](#LuCI.request.interceptorFn)
        * [.removeInterceptor(interceptorFn)](#LuCI.request+removeInterceptor) ⇒ <code>boolean</code>
    * _static_
        * [.poll](#LuCI.request.poll)
            * _instance_
                * [.add(interval, url, [options], [callback])](#LuCI.request.poll+add) ⇒ <code>function</code>
                * [.remove(entry)](#LuCI.request.poll+remove) ⇒ <code>boolean</code>
                * [.start()](#LuCI.request.poll+start) ⇒ <code>boolean</code>
                * [.stop()](#LuCI.request.poll+stop) ⇒ <code>boolean</code>
                * [.active()](#LuCI.request.poll+active) ⇒ <code>boolean</code>
            * _inner_
                * [~callbackFn](#LuCI.request.poll..callbackFn) : <code>function</code>
        * [.RequestOptions](#LuCI.request.RequestOptions) : <code>Object</code>
        * [.interceptorFn](#LuCI.request.interceptorFn) : <code>function</code>

<a name="LuCI.request+expandURL"></a>

#### request.expandURL(url) ⇒ <code>string</code>
Turn the given relative URL into an absolute URL if necessary.

**Kind**: instance method of [<code>request</code>](#LuCI.request)  
**Returns**: <code>string</code> - The absolute URL derived from the given one, or the original URL
if it already was absolute.  

| Param | Type | Description |
| --- | --- | --- |
| url | <code>string</code> | The URL to convert. |

<a name="LuCI.request+request"></a>

#### request.request(target, [options]) ⇒ [<code>Promise.&lt;response&gt;</code>](#LuCI.response)
Initiate an HTTP request to the given target.

**Kind**: instance method of [<code>request</code>](#LuCI.request)  
**Returns**: [<code>Promise.&lt;response&gt;</code>](#LuCI.response) - The resulting HTTP response.  

| Param | Type | Description |
| --- | --- | --- |
| target | <code>string</code> | The URL to request. |
| [options] | [<code>RequestOptions</code>](#LuCI.request.RequestOptions) | Additional options to configure the request. |

<a name="LuCI.request+handleReadyStateChange"></a>

#### request.handleReadyStateChange(resolveFn, rejectFn, [ev]) ⇒ <code>void</code>
Handle XHR readyState changes for an in-flight request and resolve or
reject the originating promise.

**Kind**: instance method of [<code>request</code>](#LuCI.request)  
**Returns**: <code>void</code> - No return value; the function resolves or rejects the supplied callbacks.  

| Param | Type | Description |
| --- | --- | --- |
| resolveFn | <code>function</code> | Callback invoked on success with the constructed [response](#LuCI.response). |
| rejectFn | <code>function</code> | Callback invoked on failure or abort with an `Error` instance. |
| [ev] | <code>Event</code> | The XHR `readystatechange` event (optional). |

<a name="LuCI.request+get"></a>

#### request.get(url, [options]) ⇒ [<code>Promise.&lt;response&gt;</code>](#LuCI.response)
Initiate an HTTP GET request to the given target.

**Kind**: instance method of [<code>request</code>](#LuCI.request)  
**Returns**: [<code>Promise.&lt;response&gt;</code>](#LuCI.response) - The resulting HTTP response.  

| Param | Type | Description |
| --- | --- | --- |
| url | <code>string</code> | The URL to request. |
| [options] | [<code>RequestOptions</code>](#LuCI.request.RequestOptions) | Additional options to configure the request. |

<a name="LuCI.request+post"></a>

#### request.post(url, [data], [options]) ⇒ [<code>Promise.&lt;response&gt;</code>](#LuCI.response)
Initiate an HTTP POST request to the given target.

**Kind**: instance method of [<code>request</code>](#LuCI.request)  
**Returns**: [<code>Promise.&lt;response&gt;</code>](#LuCI.response) - The resulting HTTP response.  

| Param | Type | Description |
| --- | --- | --- |
| url | <code>string</code> | The URL to request. |
| [data] | <code>\*</code> | The request data to send, see [RequestOptions](#LuCI.request.RequestOptions) for details. |
| [options] | [<code>RequestOptions</code>](#LuCI.request.RequestOptions) | Additional options to configure the request. |

<a name="LuCI.request+addInterceptor"></a>

#### request.addInterceptor(interceptorFn) ⇒ [<code>interceptorFn</code>](#LuCI.request.interceptorFn)
Register an HTTP response interceptor function. Interceptor
functions are useful to perform default actions on incoming HTTP
responses, such as checking for expired authentication or for
implementing request retries before returning a failure.

**Kind**: instance method of [<code>request</code>](#LuCI.request)  
**Returns**: [<code>interceptorFn</code>](#LuCI.request.interceptorFn) - The registered function.  

| Param | Type | Description |
| --- | --- | --- |
| interceptorFn | [<code>interceptorFn</code>](#LuCI.request.interceptorFn) | The interceptor function to register. |

<a name="LuCI.request+removeInterceptor"></a>

#### request.removeInterceptor(interceptorFn) ⇒ <code>boolean</code>
Remove an HTTP response interceptor function. The passed function
value must be the very same value that was used to register the
function.

**Kind**: instance method of [<code>request</code>](#LuCI.request)  
**Returns**: <code>boolean</code> - Returns `true` if any function has been removed, else `false`.  

| Param | Type | Description |
| --- | --- | --- |
| interceptorFn | [<code>interceptorFn</code>](#LuCI.request.interceptorFn) | The interceptor function to remove. |

<a name="LuCI.request.poll"></a>

#### request.poll
The `Request.poll` class provides some convenience wrappers around
[poll](#LuCI.poll) mainly to simplify registering repeating HTTP
request calls as polling functions.

**Kind**: static class of [<code>request</code>](#LuCI.request)  

* [.poll](#LuCI.request.poll)
    * _instance_
        * [.add(interval, url, [options], [callback])](#LuCI.request.poll+add) ⇒ <code>function</code>
        * [.remove(entry)](#LuCI.request.poll+remove) ⇒ <code>boolean</code>
        * [.start()](#LuCI.request.poll+start) ⇒ <code>boolean</code>
        * [.stop()](#LuCI.request.poll+stop) ⇒ <code>boolean</code>
        * [.active()](#LuCI.request.poll+active) ⇒ <code>boolean</code>
    * _inner_
        * [~callbackFn](#LuCI.request.poll..callbackFn) : <code>function</code>

<a name="LuCI.request.poll+add"></a>

##### poll.add(interval, url, [options], [callback]) ⇒ <code>function</code>
Register a repeating HTTP request with an optional callback
to invoke whenever a response for the request is received.

**Kind**: instance method of [<code>poll</code>](#LuCI.request.poll)  
**Returns**: <code>function</code> - Returns the internally created poll function.  
**Throws**:

- <code>TypeError</code> Throws `TypeError` when an invalid interval was passed.


| Param | Type | Description |
| --- | --- | --- |
| interval | <code>number</code> | The poll interval in seconds. |
| url | <code>string</code> | The URL to request on each poll. |
| [options] | [<code>RequestOptions</code>](#LuCI.request.RequestOptions) | Additional options to configure the request. |
| [callback] | <code>LuCI.request.poll.callbackFn</code> | [Callback](#LuCI.request.poll..callbackFn) function to invoke for each HTTP reply. |

<a name="LuCI.request.poll+remove"></a>

##### poll.remove(entry) ⇒ <code>boolean</code>
Remove a polling request that has been previously added using `add()`.
This function is essentially a wrapper around
[LuCI.poll.remove()](LuCI.poll.remove).

**Kind**: instance method of [<code>poll</code>](#LuCI.request.poll)  
**Returns**: <code>boolean</code> - Returns `true` if any function has been removed, else `false`.  

| Param | Type | Description |
| --- | --- | --- |
| entry | <code>function</code> | The poll function returned by [add()](#LuCI.request.poll+add). |

<a name="LuCI.request.poll+start"></a>

##### poll.start() ⇒ <code>boolean</code>
Alias for [LuCI.poll.start()](LuCI.poll.start).

**Kind**: instance method of [<code>poll</code>](#LuCI.request.poll)  
<a name="LuCI.request.poll+stop"></a>

##### poll.stop() ⇒ <code>boolean</code>
Alias for [LuCI.poll.stop()](LuCI.poll.stop).

**Kind**: instance method of [<code>poll</code>](#LuCI.request.poll)  
<a name="LuCI.request.poll+active"></a>

##### poll.active() ⇒ <code>boolean</code>
Alias for [LuCI.poll.active()](LuCI.poll.active).

**Kind**: instance method of [<code>poll</code>](#LuCI.request.poll)  
<a name="LuCI.request.poll..callbackFn"></a>

##### poll~callbackFn : <code>function</code>
The callback function is invoked whenever an HTTP reply to a
polled request is received or when the polled request timed
out.

**Kind**: inner typedef of [<code>poll</code>](#LuCI.request.poll)  

| Param | Type | Description |
| --- | --- | --- |
| res | [<code>response</code>](#LuCI.response) | The HTTP response object. |
| data | <code>\*</code> | The response JSON if the response could be parsed as such, else `null`. |
| duration | <code>number</code> | The total duration of the request in milliseconds. |

<a name="LuCI.request.RequestOptions"></a>

#### request.RequestOptions : <code>Object</code>
**Kind**: static typedef of [<code>request</code>](#LuCI.request)  
**Properties**

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| [method] | <code>string</code> | <code>&quot;GET&quot;</code> | The HTTP method to use, e.g. `GET` or `POST`. |
| [query] | <code>Object.&lt;string, (Object\|string)&gt;</code> |  | Query string data to append to the URL. Non-string values of the given object will be converted to JSON. |
| [cache] | <code>boolean</code> | <code>false</code> | Specifies whether the HTTP response may be retrieved from cache. |
| [username] | <code>string</code> |  | Provides a username for HTTP basic authentication. |
| [password] | <code>string</code> |  | Provides a password for HTTP basic authentication. |
| [timeout] | <code>number</code> |  | Specifies the request timeout in milliseconds. |
| [credentials] | <code>boolean</code> | <code>false</code> | Whether to include credentials such as cookies in the request. |
| [responseType] | <code>string</code> | <code>&quot;text&quot;</code> | Overrides the request response type. Valid values or `text` to interpret the response as UTF-8 string or `blob` to handle the response as binary `Blob` data. |
| [content] | <code>\*</code> |  | Specifies the HTTP message body to send along with the request. If the value is a function, it is invoked and the return value used as content, if it is a FormData instance, it is used as-is, if it is an object, it will be converted to JSON, in all other cases it is converted to a string. |
| [header] | <code>Object.&lt;string, string&gt;</code> |  | Specifies HTTP headers to set for the request. |
| [progress] | <code>function</code> |  | An optional request callback function which receives ProgressEvent instances as sole argument during the HTTP request transfer. |
| [responseProgress] | <code>function</code> |  | An optional request callback function which receives ProgressEvent instances as sole argument during the HTTP response transfer. |

<a name="LuCI.request.interceptorFn"></a>

#### request.interceptorFn : <code>function</code>
Interceptor functions are invoked whenever an HTTP reply is received, in the order
these functions have been registered.

**Kind**: static typedef of [<code>request</code>](#LuCI.request)  

| Param | Type | Description |
| --- | --- | --- |
| res | [<code>response</code>](#LuCI.response) | The HTTP response object |

<a name="LuCI.poll"></a>

### LuCI.poll
The `Poll` class allows registering and unregistering poll actions,
as well as starting, stopping, and querying the state of the polling
loop.

**Kind**: static class of [<code>LuCI</code>](#LuCI)  

* [.poll](#LuCI.poll)
    * [.add(fn, interval)](#LuCI.poll+add) ⇒ <code>boolean</code>
    * [.remove(fn)](#LuCI.poll+remove) ⇒ <code>boolean</code>
    * [.start()](#LuCI.poll+start) ⇒ <code>boolean</code>
    * [.stop()](#LuCI.poll+stop) ⇒ <code>boolean</code>
    * [.active()](#LuCI.poll+active) ⇒ <code>boolean</code>

<a name="LuCI.poll+add"></a>

#### poll.add(fn, interval) ⇒ <code>boolean</code>
Add a new operation to the polling loop. If the polling loop is not
already started at this point, it will be implicitly started.

**Kind**: instance method of [<code>poll</code>](#LuCI.poll)  
**Returns**: <code>boolean</code> - Returns `true` if the function has been added or `false` if it
already is registered.  
**Throws**:

- <code>TypeError</code> Throws `TypeError` when an invalid interval was passed.


| Param | Type | Description |
| --- | --- | --- |
| fn | <code>function</code> | The function to invoke on each poll interval. |
| interval | <code>number</code> | The poll interval in seconds. |

<a name="LuCI.poll+remove"></a>

#### poll.remove(fn) ⇒ <code>boolean</code>
Remove an operation from the polling loop. If no further operations
are registered, the polling loop is implicitly stopped.

**Kind**: instance method of [<code>poll</code>](#LuCI.poll)  
**Returns**: <code>boolean</code> - Returns `true` if the function has been removed or `false` if it
wasn't found.  
**Throws**:

- <code>TypeError</code> Throws `TypeError` when the given argument isn't a function.


| Param | Type | Description |
| --- | --- | --- |
| fn | <code>function</code> | The function to remove. |

<a name="LuCI.poll+start"></a>

#### poll.start() ⇒ <code>boolean</code>
(Re)start the polling loop. Dispatches a custom `poll-start` event
to the `document` object upon successful start.

**Kind**: instance method of [<code>poll</code>](#LuCI.poll)  
**Returns**: <code>boolean</code> - Returns `true` if polling has been started (or if no functions
where registered) or `false` when the polling loop already runs.  
<a name="LuCI.poll+stop"></a>

#### poll.stop() ⇒ <code>boolean</code>
Stop the polling loop. Dispatches a custom `poll-stop` event
to the `document` object upon successful stop.

**Kind**: instance method of [<code>poll</code>](#LuCI.poll)  
**Returns**: <code>boolean</code> - Returns `true` if polling has been stopped or `false` if it didn't
run to begin with.  
<a name="LuCI.poll+active"></a>

#### poll.active() ⇒ <code>boolean</code>
Test whether the polling loop is running.

**Kind**: instance method of [<code>poll</code>](#LuCI.poll)  
**Returns**: <code>boolean</code> - - Returns `true` if polling is active, else `false`.  
<a name="LuCI.dom"></a>

### LuCI.dom
The `dom` class provides a convenience method for creating and
manipulating DOM elements.

To import the class in views, use `'require dom'`, to import it in
external JavaScript, use `L.require("dom").then(...)`.

**Kind**: static class of [<code>LuCI</code>](#LuCI)  

* [.dom](#LuCI.dom)
    * _instance_
        * [.elem(e)](#LuCI.dom+elem) ⇒ <code>boolean</code>
        * [.parse(s)](#LuCI.dom+parse) ⇒ <code>Node</code>
        * [.matches(node, [selector])](#LuCI.dom+matches) ⇒ <code>boolean</code>
        * [.parent(node, [selector])](#LuCI.dom+parent) ⇒ <code>Node</code> \| <code>null</code>
        * [.append(node, [children])](#LuCI.dom+append) ⇒ <code>Node</code> \| <code>null</code>
        * [.content(node, [children])](#LuCI.dom+content) ⇒ <code>Node</code> \| <code>null</code>
        * [.attr(node, key, [val])](#LuCI.dom+attr) ⇒ <code>null</code>
        * [.create(html, [attr], [data])](#LuCI.dom+create) ⇒ <code>Node</code>
        * [.data(node, [key], [val])](#LuCI.dom+data) ⇒ <code>\*</code>
        * [.bindClassInstance(node, inst)](#LuCI.dom+bindClassInstance) ⇒ <code>Class</code>
        * [.findClassInstance(node)](#LuCI.dom+findClassInstance) ⇒ <code>Class</code> \| <code>null</code>
        * [.callClassMethod(node, method, ...args)](#LuCI.dom+callClassMethod) ⇒ <code>\*</code> \| <code>null</code>
        * [.isEmpty(node, [ignoreFn])](#LuCI.dom+[isEmpty](/luci-docs/luci-api-uci.md)) ⇒ <code>boolean</code>
    * _inner_
        * [~ignoreCallbackFn](#LuCI.dom..ignoreCallbackFn) ⇒ <code>boolean</code>

<a name="LuCI.dom+elem"></a>

#### dom.elem(e) ⇒ <code>boolean</code>
Tests whether the given argument is a valid DOM `Node`.

**Kind**: instance method of [<code>dom</code>](#LuCI.dom)  
**Returns**: <code>boolean</code> - Returns `true` if the value is a DOM `Node`, else `false`.  

| Param | Type | Description |
| --- | --- | --- |
| e | <code>\*</code> | The value to test. |

<a name="LuCI.dom+parse"></a>

#### dom.parse(s) ⇒ <code>Node</code>
Parses a given string as HTML and returns the first child node.

**Kind**: instance method of [<code>dom</code>](#LuCI.dom)  
**Returns**: <code>Node</code> - Returns the first DOM `Node` extracted from the HTML fragment or
`null` on parsing failures or if no element could be found.  

| Param | Type | Description |
| --- | --- | --- |
| s | <code>string</code> | A string containing an HTML fragment to parse. Note that only the first result of the resulting structure is returned, so an input value of `<div>foo</div> <div>bar</div>` will only return the first `div` element node. |

<a name="LuCI.dom+matches"></a>

#### dom.matches(node, [selector]) ⇒ <code>boolean</code>
Tests whether a given `Node` matches the given query selector.

This function is a convenience wrapper around the standard
`Node.matches("selector")` function with the added benefit that
the `node` argument may be a non-`Node` value, in which case
this function simply returns `false`.

**Kind**: instance method of [<code>dom</code>](#LuCI.dom)  
**Returns**: <code>boolean</code> - Returns `true` if the given node matches the specified selector
or `false` when the node argument is no valid DOM `Node` or the
selector didn't match.  

| Param | Type | Description |
| --- | --- | --- |
| node | <code>\*</code> | The `Node` argument to test the selector against. |
| [selector] | <code>string</code> | The query selector expression to test against the given node. |

<a name="LuCI.dom+parent"></a>

#### dom.parent(node, [selector]) ⇒ <code>Node</code> \| <code>null</code>
Returns the closest parent node that matches the given query
selector expression.

This function is a convenience wrapper around the standard
`Node.closest("selector")` function with the added benefit that
the `node` argument may be a non-`Node` value, in which case
this function simply returns `null`.

**Kind**: instance method of [<code>dom</code>](#LuCI.dom)  
**Returns**: <code>Node</code> \| <code>null</code> - Returns the closest parent node matching the selector or
`null` when the node argument is no valid DOM `Node` or the
selector didn't match any parent.  

| Param | Type | Description |
| --- | --- | --- |
| node | <code>\*</code> | The `Node` argument to find the closest parent for. |
| [selector] | <code>string</code> | The query selector expression to test against each parent. |

<a name="LuCI.dom+append"></a>

#### dom.append(node, [children]) ⇒ <code>Node</code> \| <code>null</code>
Appends the given children data to the given node.

**Kind**: instance method of [<code>dom</code>](#LuCI.dom)  
**Returns**: <code>Node</code> \| <code>null</code> - Returns the last children `Node` appended to the node or `null`
if either the `node` argument was no valid DOM `node` or if the
`children` was `null` or didn't result in further DOM nodes.  

| Param | Type | Description |
| --- | --- | --- |
| node | <code>\*</code> | The `Node` argument to append the children to. |
| [children] | <code>\*</code> | The children to append to the given node. When `children` is an array, then each item of the array will be either appended as a child element or text node, depending on whether the item is a DOM `Node` instance or some other non-`null` value. Non-`Node`, non-`null` values will be converted to strings first before being passed as argument to `createTextNode()`. When `children` is a function, it will be invoked with the passed `node` argument as the sole parameter and the `append` function will be invoked again, with the given `node` argument as first and the return value of the `children` function as  the second parameter. When `children` is a DOM `Node` instance, it will be appended to the given `node`. When `children` is any other non-`null` value, it will be converted to a string and appended to the `innerHTML` property of the given `node`. |

<a name="LuCI.dom+content"></a>

#### dom.content(node, [children]) ⇒ <code>Node</code> \| <code>null</code>
Replaces the content of the given node with the given children.

This function first removes any children of the given DOM
`Node` and then adds the given children following the
rules outlined below.

**Kind**: instance method of [<code>dom</code>](#LuCI.dom)  
**Returns**: <code>Node</code> \| <code>null</code> - Returns the last children `Node` appended to the node or `null`
if either the `node` argument was no valid DOM `node` or if the
`children` was `null` or didn't result in further DOM nodes.  

| Param | Type | Description |
| --- | --- | --- |
| node | <code>\*</code> | The `Node` argument to replace the children of. |
| [children] | <code>\*</code> | The children to replace into the given node. When `children` is an array, then each item of the array will be either appended as a child element or text node, depending on whether the item is a DOM `Node` instance or some other non-`null` value. Non-`Node`, non-`null` values will be converted to strings first before being passed as argument to `createTextNode()`. When `children` is a function, it will be invoked with the passed `node` argument as the sole parameter and the `append` function will be invoked again, with the given `node` argument as first and the return value of the `children` function as the second parameter. When `children` is a DOM `Node` instance, it will be appended to the given `node`. When `children` is any other non-`null` value, it will be converted to a string and appended to the `innerHTML` property of the given `node`. |

<a name="LuCI.dom+attr"></a>

#### dom.attr(node, key, [val]) ⇒ <code>null</code>
Sets attributes or registers event listeners on element nodes.

**Kind**: instance method of [<code>dom</code>](#LuCI.dom)  

| Param | Type | Description |
| --- | --- | --- |
| node | <code>\*</code> | The `Node` argument to set the attributes or add the event listeners for. When the given `node` value is not a valid DOM `Node`, the function returns and does nothing. |
| key | <code>string</code> \| <code>Object.&lt;string, \*&gt;</code> | Specifies either the attribute or event handler name to use, or an object containing multiple key, value pairs which are each added to the node as either attribute or event handler, depending on the respective value. |
| [val] | <code>\*</code> | Specifies the attribute value or event handler function to add. If the `key` parameter is an `Object`, this parameter will be ignored. When `val` is of type function, it will be registered as an event handler on the given `node` with the `key` parameter being the event name. When `val` is of type object, it will be serialized as JSON and added as an attribute to the given `node`, using the given `key` as an attribute name. When `val` is of any other type, it will be added as an attribute to the given `node` as-is, with the underlying `setAttribute()` call implicitly turning it into a string. |

<a name="LuCI.dom+create"></a>

#### dom.create(html, [attr], [data]) ⇒ <code>Node</code>
Creates a new DOM `Node` from the given `html`, `attr` and
`data` parameters.

This function has multiple signatures, it can be either invoked
in the form `create(html[, attr[, data]])` or in the form
`create(html[, data])`. The used variant is determined from the
type of the second argument.

**Kind**: instance method of [<code>dom</code>](#LuCI.dom)  
**Returns**: <code>Node</code> - Returns the newly created `Node`.  
**Throws**:

- <code>InvalidCharacterError</code> Throws an `InvalidCharacterError` when the given `html`
argument contained malformed markup (such as not escaped
`&` characters in XHTML mode) or when the given node name
in `html` contains characters which are not legal in DOM
element names, such as spaces.


| Param | Type | Description |
| --- | --- | --- |
| html | <code>string</code> | Describes the node to create. When the value of `html` is of type array, a `DocumentFragment` node is created and each item of the array is first converted to a DOM `Node` by passing it through `create()` and then added as a child to the fragment. When the value of `html` is a DOM `Node` instance, no new element will be created, but the node will be used as-is. When the value of `html` is a string starting with `<`, it will be passed to `dom.parse()` and the resulting value is used. When the value of `html` is any other string, it will be passed to `document.createElement()` for creating a new DOM `Node` of the given name. |
| [attr] | <code>Object.&lt;string, \*&gt;</code> | Specifies an Object of key, value pairs to set as attributes or event handlers on the created node. Refer to [dom.attr()](#LuCI.dom+attr) for details. |
| [data] | <code>\*</code> | Specifies children to append to the newly created element. Refer to [dom.append()](#LuCI.dom+append) for details. |

<a name="LuCI.dom+data"></a>

#### dom.data(node, [key], [val]) ⇒ <code>\*</code>
Attaches or detaches arbitrary data to and from a DOM `Node`.

This function is useful to attach non-string values or runtime
data that is not serializable to DOM nodes. To decouple data
from the DOM, values are not added directly to nodes, but
inserted into a registry instead which is then referenced by a
string key stored as `data-idref` attribute in the node.

This function has multiple signatures and is sensitive to the
number of arguments passed to it.

 - `dom.data(node)` -
	 Fetches all data associated with the given node.
 - `dom.data(node, key)` -
	 Fetches a specific key associated with the given node.
 - `dom.data(node, key, val)` -
	 Sets a specific key to the given value associated with the
	 given node.
 - `dom.data(node, null)` -
	 Clears any data associated with the node.
 - `dom.data(node, key, null)` -
	 Clears the given key associated with the node.

**Kind**: instance method of [<code>dom</code>](#LuCI.dom)  
**Returns**: <code>\*</code> - Returns the get or set value, or `null` when no value could
be found.  

| Param | Type | Description |
| --- | --- | --- |
| node | <code>Node</code> | The DOM `Node` instance to set or retrieve the data for. |
| [key] | <code>string</code> \| <code>null</code> | This is either a string specifying the key to retrieve, or `null` to unset the entire node data. |
| [val] | <code>\*</code> \| <code>null</code> | This is either a non-`null` value to set for a given key or `null` to remove the given `key` from the specified node. |

<a name="LuCI.dom+bindClassInstance"></a>

#### dom.bindClassInstance(node, inst) ⇒ <code>Class</code>
Binds the given class instance to the specified DOM `Node`.

This function uses the `dom.data()` facility to attach the
passed instance of a Class to a node. This is needed for
complex widget elements or similar where the corresponding
class instance responsible for the element must be retrieved
from DOM nodes obtained by `querySelector()` or similar means.

**Kind**: instance method of [<code>dom</code>](#LuCI.dom)  
**Returns**: <code>Class</code> - Returns the bound class instance.  
**Throws**:

- <code>TypeError</code> Throws a `TypeError` when the given instance argument isn't
a valid Class instance.


| Param | Type | Description |
| --- | --- | --- |
| node | <code>Node</code> | The DOM `Node` instance to bind the class to. |
| inst | <code>Class</code> | The Class instance to bind to the node. |

<a name="LuCI.dom+findClassInstance"></a>

#### dom.findClassInstance(node) ⇒ <code>Class</code> \| <code>null</code>
Finds a bound class instance on the given node itself or the
first bound instance on its closest parent node.

**Kind**: instance method of [<code>dom</code>](#LuCI.dom)  
**Returns**: <code>Class</code> \| <code>null</code> - Returns the founds class instance if any or `null` if no bound
class could be found on the node itself or any of its parents.  

| Param | Type | Description |
| --- | --- | --- |
| node | <code>Node</code> | The DOM `Node` instance to start from. |

<a name="LuCI.dom+callClassMethod"></a>

#### dom.callClassMethod(node, method, ...args) ⇒ <code>\*</code> \| <code>null</code>
Finds a bound class instance on the given node itself or the
first bound instance on its closest parent node and invokes
the specified method name on the found class instance.

**Kind**: instance method of [<code>dom</code>](#LuCI.dom)  
**Returns**: <code>\*</code> \| <code>null</code> - Returns the return value of the invoked method if a class
instance and method has been found. Returns `null` if either
no bound class instance could be found, or if the found
instance didn't have the requested `method`.  

| Param | Type | Description |
| --- | --- | --- |
| node | <code>Node</code> | The DOM `Node` instance to start from. |
| method | <code>string</code> | The name of the method to invoke on the found class instance. |
| ...args | <code>\*</code> | Additional arguments to pass to the invoked method as-is. |

<a name="LuCI.dom+[isEmpty](/luci-docs/luci-api-uci.md)"></a>

#### dom.isEmpty(node, [ignoreFn]) ⇒ <code>boolean</code>
Tests whether a given DOM `Node` instance is empty or appears
empty.

Any element child nodes which have the CSS class `hidden` set
or for which the optionally passed `ignoreFn` callback function
returns `false` are ignored.

**Kind**: instance method of [<code>dom</code>](#LuCI.dom)  
**Returns**: <code>boolean</code> - Returns `true` if the node does not have any children or if
any children node either has a `hidden` CSS class or a `false`
result when testing it using the given `ignoreFn`.  

| Param | Type | Description |
| --- | --- | --- |
| node | <code>Node</code> | The DOM `Node` instance to test. |
| [ignoreFn] | <code>LuCI.dom.ignoreCallbackFn</code> | Specifies an optional function which is invoked for each child node to decide whether the child node should be ignored or not. |

<a name="LuCI.dom..ignoreCallbackFn"></a>

#### dom~ignoreCallbackFn ⇒ <code>boolean</code>
The ignore callback function is invoked by `isEmpty()` for each
child node to decide whether to ignore a child node or not.

When this function returns `false`, the node passed to it is
ignored, else not.

**Kind**: inner typedef of [<code>dom</code>](#LuCI.dom)  
**Returns**: <code>boolean</code> - Boolean indicating whether to ignore the node or not.  

| Param | Type | Description |
| --- | --- | --- |
| node | <code>Node</code> | The child node to test. |

<a name="LuCI.session"></a>

### LuCI.session
The `session` class provides various session related functionality.

**Kind**: static class of [<code>LuCI</code>](#LuCI)  

* [.session](#LuCI.session)
    * [.getID()](#LuCI.session+getID) ⇒ <code>string</code>
    * [.getToken()](#LuCI.session+getToken) ⇒ <code>string</code> \| <code>null</code>
    * [.getLocalData([key])](#LuCI.session+getLocalData) ⇒ <code>\*</code>
    * [.setLocalData(key, value)](#LuCI.session+setLocalData) ⇒ <code>boolean</code>

<a name="LuCI.session+getID"></a>

#### session.getID() ⇒ <code>string</code>
Retrieve the current session ID.

**Kind**: instance method of [<code>session</code>](#LuCI.session)  
**Returns**: <code>string</code> - Returns the current session ID.  
<a name="LuCI.session+getToken"></a>

#### session.getToken() ⇒ <code>string</code> \| <code>null</code>
Retrieve the current session token.

**Kind**: instance method of [<code>session</code>](#LuCI.session)  
**Returns**: <code>string</code> \| <code>null</code> - Returns the current session token or `null` if not logged in.  
<a name="LuCI.session+getLocalData"></a>

#### session.getLocalData([key]) ⇒ <code>\*</code>
Retrieve data from the local session storage.

**Kind**: instance method of [<code>session</code>](#LuCI.session)  
**Returns**: <code>\*</code> - Returns the stored session data or `null` if the given key wasn't
found.  

| Param | Type | Description |
| --- | --- | --- |
| [key] | <code>string</code> | The key to retrieve from the session data store. If omitted, all session data will be returned. |

<a name="LuCI.session+setLocalData"></a>

#### session.setLocalData(key, value) ⇒ <code>boolean</code>
Set data in the local session storage.

**Kind**: instance method of [<code>session</code>](#LuCI.session)  
**Returns**: <code>boolean</code> - Returns `true` if the data could be stored or `false` on error.  

| Param | Type | Description |
| --- | --- | --- |
| key | <code>string</code> | The key to set in the session data store. |
| value | <code>\*</code> | The value to store. It will be internally converted to JSON before being put in the session store. |

<a name="LuCI.view"></a>

### LuCI.view
The `view` class forms the basis of views and provides a standard
set of methods to inherit from.

**Kind**: static class of [<code>LuCI</code>](#LuCI)  

* [.view](#LuCI.view)
    * *[.load()](#LuCI.view+load) ⇒ <code>\*</code> \| <code>Promise.&lt;\*&gt;</code>*
    * *[.render(load_results)](#LuCI.view+render) ⇒ <code>Node</code> \| <code>Promise.&lt;Node&gt;</code>*
    * [.handleSave(ev)](#LuCI.view+handleSave) ⇒ <code>\*</code> \| <code>Promise.&lt;\*&gt;</code>
    * [.handleSaveApply(ev, mode)](#LuCI.view+handleSaveApply) ⇒ <code>\*</code> \| <code>Promise.&lt;\*&gt;</code>
    * [.handleReset(ev)](#LuCI.view+handleReset) ⇒ <code>\*</code> \| <code>Promise.&lt;\*&gt;</code>
    * [.addFooter()](#LuCI.view+addFooter) ⇒ <code>DocumentFragment</code>

<a name="LuCI.view+load"></a>

#### *view.load() ⇒ <code>\*</code> \| <code>Promise.&lt;\*&gt;</code>*
The load function is invoked before the view is rendered.

The invocation of this function is wrapped by
`Promise.resolve()` so it may return Promises if needed.

The return value of the function (or the resolved values
of the promise returned by it) will be passed as the first
argument to `render()`.

This function is supposed to be overwritten by subclasses,
the default implementation does nothing.

**Kind**: instance abstract method of [<code>view</code>](#LuCI.view)  
**Returns**: <code>\*</code> \| <code>Promise.&lt;\*&gt;</code> - May return any value or a Promise resolving to any value.  
<a name="LuCI.view+render"></a>

#### *view.render(load_results) ⇒ <code>Node</code> \| <code>Promise.&lt;Node&gt;</code>*
The render function is invoked after the
[load()](#LuCI.view+load) function and responsible
for setting up the view contents. It must return a DOM
`Node` or `DocumentFragment` holding the contents to
insert into the view area.

The invocation of this function is wrapped by
`Promise.resolve()` so it may return Promises if needed.

The return value of the function (or the resolved values
of the promise returned by it) will be inserted into the
main content area using
[dom.append()](#LuCI.dom+append).

This function is supposed to be overwritten by subclasses,
the default implementation does nothing.

**Kind**: instance abstract method of [<code>view</code>](#LuCI.view)  
**Returns**: <code>Node</code> \| <code>Promise.&lt;Node&gt;</code> - Should return a DOM `Node` value or a `Promise` resolving
to a `Node` value.  

| Param | Type | Description |
| --- | --- | --- |
| load_results | <code>\*</code> \| <code>null</code> | This function will receive the return value of the [view.load()](#LuCI.view+load) function as first argument. |

<a name="LuCI.view+handleSave"></a>

#### view.handleSave(ev) ⇒ <code>\*</code> \| <code>Promise.&lt;\*&gt;</code>
The handleSave function is invoked when the user clicks
the `Save` button in the page action footer.

The default implementation should be sufficient for most
views using [form.Map()](form#Map) based forms - it
will iterate all forms present in the view and invoke
the [Map.save()](form#Map#save) method on each form.

Views not using `Map` instances or requiring other special
logic should overwrite `handleSave()` with a custom
implementation.

To disable the `Save` page footer button, views extending
this base class should overwrite the `handleSave` function
with `null`.

The invocation of this function is wrapped by
`Promise.resolve()` so it may return Promises if needed.

**Kind**: instance method of [<code>view</code>](#LuCI.view)  
**Returns**: <code>\*</code> \| <code>Promise.&lt;\*&gt;</code> - Any return values of this function are discarded, but
passed through `Promise.resolve()` to ensure that any
returned promise runs to completion before the button
is re-enabled.  

| Param | Type | Description |
| --- | --- | --- |
| ev | <code>Event</code> | The DOM event that triggered the function. |

<a name="LuCI.view+handleSaveApply"></a>

#### view.handleSaveApply(ev, mode) ⇒ <code>\*</code> \| <code>Promise.&lt;\*&gt;</code>
The handleSaveApply function is invoked when the user clicks
the `Save & Apply` button in the page action footer.

The default implementation should be sufficient for most
views using [form.Map()](form#Map) based forms - it
will first invoke
[view.handleSave()](LuCI.view.handleSave) and then
call [ui.changes.apply()](ui#changes#apply) to start the
modal config apply and page reload flow.

Views not using `Map` instances or requiring other special
logic should overwrite `handleSaveApply()` with a custom
implementation.

To disable the `Save & Apply` page footer button, views
extending this base class should overwrite the
`handleSaveApply` function with `null`.

The invocation of this function is wrapped by
`Promise.resolve()` so it may return Promises if needed.

**Kind**: instance method of [<code>view</code>](#LuCI.view)  
**Returns**: <code>\*</code> \| <code>Promise.&lt;\*&gt;</code> - Any return values of this function are discarded, but
passed through `Promise.resolve()` to ensure that any
returned promise runs to completion before the button
is re-enabled.  

| Param | Type | Description |
| --- | --- | --- |
| ev | <code>Event</code> | The DOM event that triggered the function. |
| mode | <code>number</code> | Whether to apply the changes checked. |

<a name="LuCI.view+handleReset"></a>

#### view.handleReset(ev) ⇒ <code>\*</code> \| <code>Promise.&lt;\*&gt;</code>
The handleReset function is invoked when the user clicks
the `Reset` button in the page action footer.

The default implementation should be sufficient for most
views using [form.Map()](form#Map) based forms - it
will iterate all forms present in the view and invoke
the [Map.reset()](form#Map#save) method on each form.

Views not using `Map` instances or requiring other special
logic should overwrite `handleReset()` with a custom
implementation.

To disable the `Reset` page footer button, views extending
this base class should overwrite the `handleReset` function
with `null`.

The invocation of this function is wrapped by
`Promise.resolve()` so it may return Promises if needed.

**Kind**: instance method of [<code>view</code>](#LuCI.view)  
**Returns**: <code>\*</code> \| <code>Promise.&lt;\*&gt;</code> - Any return values of this function are discarded, but
passed through `Promise.resolve()` to ensure that any
returned promise runs to completion before the button
is re-enabled.  

| Param | Type | Description |
| --- | --- | --- |
| ev | <code>Event</code> | The DOM event that triggered the function. |

<a name="LuCI.view+addFooter"></a>

#### view.addFooter() ⇒ <code>DocumentFragment</code>
Renders a standard page action footer if any of the
`handleSave()`, `handleSaveApply()` or `handleReset()`
functions are defined.

The default implementation should be sufficient for most
views - it will render a standard page footer with action
buttons labeled `Save`, `Save & Apply` and `Reset`
triggering the `handleSave()`, `handleSaveApply()` and
`handleReset()` functions respectively.

When any of these `handle*()` functions is overwritten
with `null` by a view extending this class, the
corresponding button will not be rendered.

**Kind**: instance method of [<code>view</code>](#LuCI.view)  
**Returns**: <code>DocumentFragment</code> - Returns a `DocumentFragment` containing the footer bar
with buttons for each corresponding `handle*()` action
or an empty `DocumentFragment` if all three `handle*()`
methods are overwritten with `null`.  
<a name="LuCI.xhr"></a>

### ~~LuCI.xhr~~
***Deprecated***

The `LuCI.xhr` class is a legacy compatibility shim for the
functionality formerly provided by `xhr.js`. It is registered as a global
`window.XHR` symbol for compatibility with legacy code.

New code should use [request](#LuCI.request) instead to implement HTTP
request handling.

**Kind**: static class of [<code>LuCI</code>](#LuCI)  

* ~~[.xhr](#LuCI.xhr)~~
    * ~~[.get(url, [data], [callback], [timeout])](#LuCI.xhr+get) ⇒ <code>Promise.&lt;null&gt;</code>~~
    * ~~[.post(url, [data], [callback], [timeout])](#LuCI.xhr+post) ⇒ <code>Promise.&lt;null&gt;</code>~~
    * ~~[.cancel()](#LuCI.xhr+cancel)~~
    * ~~[.busy()](#LuCI.xhr+busy) ⇒ <code>boolean</code>~~
    * ~~[.abort()](#LuCI.xhr+abort)~~
    * ~~[.send_form()](#LuCI.xhr+send_form)~~

<a name="LuCI.xhr+get"></a>

#### ~~xhr.get(url, [data], [callback], [timeout]) ⇒ <code>Promise.&lt;null&gt;</code>~~
***Deprecated***

This function is a legacy wrapper around
[LuCI.get()](#LuCI+get).

**Kind**: instance method of [<code>xhr</code>](#LuCI.xhr)  

| Param | Type | Description |
| --- | --- | --- |
| url | <code>string</code> | The URL to request |
| [data] | <code>Object</code> | Additional query string data |
| [callback] | [<code>requestCallbackFn</code>](#LuCI.requestCallbackFn) | Callback function to invoke on completion |
| [timeout] | <code>number</code> | Request timeout to use |

<a name="LuCI.xhr+post"></a>

#### ~~xhr.post(url, [data], [callback], [timeout]) ⇒ <code>Promise.&lt;null&gt;</code>~~
***Deprecated***

This function is a legacy wrapper around
[LuCI.post()](#LuCI+post).

**Kind**: instance method of [<code>xhr</code>](#LuCI.xhr)  

| Param | Type | Description |
| --- | --- | --- |
| url | <code>string</code> | The URL to request |
| [data] | <code>Object</code> | Additional data to append to the request body. |
| [callback] | [<code>requestCallbackFn</code>](#LuCI.requestCallbackFn) | Callback function to invoke on completion |
| [timeout] | <code>number</code> | Request timeout to use |

<a name="LuCI.xhr+cancel"></a>

#### ~~xhr.cancel()~~
***Deprecated***

Cancels a running request.

This function does not actually cancel the underlying
`XMLHTTPRequest` request but it sets a flag which prevents the
invocation of the callback function when the request eventually
finishes or timed out.

**Kind**: instance method of [<code>xhr</code>](#LuCI.xhr)  
<a name="LuCI.xhr+busy"></a>

#### ~~xhr.busy() ⇒ <code>boolean</code>~~
***Deprecated***

Checks the running state of the request.

**Kind**: instance method of [<code>xhr</code>](#LuCI.xhr)  
**Returns**: <code>boolean</code> - Returns `true` if the request is still running or `false` if it
already completed.  
<a name="LuCI.xhr+abort"></a>

#### ~~xhr.abort()~~
***Deprecated***

Ignored for backwards compatibility.

This function does nothing.

**Kind**: instance method of [<code>xhr</code>](#LuCI.xhr)  
<a name="LuCI.xhr+send_form"></a>

#### ~~xhr.send\_form()~~
***Deprecated***

Existing for backwards compatibility.

This function simply throws an `InternalError` when invoked.

**Kind**: instance method of [<code>xhr</code>](#LuCI.xhr)  
**Throws**:

- <code>InternalError</code> Throws an `InternalError` with the message `Not implemented`
when invoked.

<a name="LuCI.requestCallbackFn"></a>

### LuCI.requestCallbackFn : <code>function</code>
The request callback function is invoked whenever an HTTP
reply to a request made using the `L.get()`, `L.post()` or
`L.poll()` function is timed out or received successfully.

**Kind**: static typedef of [<code>LuCI</code>](#LuCI)  

| Param | Type | Description |
| --- | --- | --- |
| xhr | <code>XMLHTTPRequest</code> | The XMLHTTPRequest instance used to make the request. |
| data | <code>\*</code> | The response JSON if the response could be parsed as such, else `null`. |
| duration | <code>number</code> | The total duration of the request in milliseconds. |

---

# LuCI API: `prng`

> **Source:** [`modules/luci-base/htdocs/luci-static/resources/tools/prng.js`](https://github.com/openwrt/luci/blob/master/modules/luci-base/htdocs/luci-static/resources/tools/prng.js)
> **Live docs:** https://openwrt.github.io/luci/jsapi/LuCI.prng.html
> **Generated:** 2026-03-05 18:07 UTC from commit `6959675`

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

---

# LuCI API: `static`

> **Source:** [`modules/luci-base/htdocs/luci-static/resources/protocol/static.js`](https://github.com/openwrt/luci/blob/master/modules/luci-base/htdocs/luci-static/resources/protocol/static.js)
> **Live docs:** https://openwrt.github.io/luci/jsapi/LuCI.static.html
> **Generated:** 2026-03-05 18:07 UTC from commit `6959675`

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

---

# LuCI API: `uci`

> **Source:** [`modules/luci-base/htdocs/luci-static/resources/uci.js`](https://github.com/openwrt/luci/blob/master/modules/luci-base/htdocs/luci-static/resources/uci.js)
> **Live docs:** https://openwrt.github.io/luci/jsapi/LuCI.uci.html
> **Generated:** 2026-03-05 18:07 UTC from commit `6959675`

---

<a name="isEmpty"></a>

## isEmpty(object, ignore) ⇒ <code>boolean</code>
Determine whether an object is empty.

**Kind**: global function  

| Param | Type | Description |
| --- | --- | --- |
| object | <code>object</code> | object to enumerate. |
| ignore | <code>string</code> | property to ignore. |

---

# LuCI API: `ui`

> **Source:** [`modules/luci-base/htdocs/luci-static/resources/ui.js`](https://github.com/openwrt/luci/blob/master/modules/luci-base/htdocs/luci-static/resources/ui.js)
> **Live docs:** https://openwrt.github.io/luci/jsapi/LuCI.ui.html
> **Generated:** 2026-03-05 18:07 UTC from commit `6959675`

---

<a name="scrubMenu"></a>

## scrubMenu(node) ⇒ <code>Node</code>
Erase the menu node

**Kind**: global function  

| Param | Type |
| --- | --- |
| node | <code>Node</code> |

---

# LuCI API: `widgets`

> **Source:** [`modules/luci-base/htdocs/luci-static/resources/tools/widgets.js`](https://github.com/openwrt/luci/blob/master/modules/luci-base/htdocs/luci-static/resources/tools/widgets.js)
> **Live docs:** https://openwrt.github.io/luci/jsapi/LuCI.widgets.html
> **Generated:** 2026-03-05 18:07 UTC from commit `6959675`

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

---

