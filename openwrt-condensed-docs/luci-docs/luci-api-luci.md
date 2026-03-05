# LuCI API: `luci`

> **Source:** [`modules/luci-base/htdocs/luci-static/resources/luci.js`](https://github.com/openwrt/luci/blob/master/modules/luci-base/htdocs/luci-static/resources/luci.js)
> **Live docs:** https://openwrt.github.io/luci/jsapi/LuCI.html
> **Generated:** 2026-03-05 15:58 UTC from commit `ec79910`

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