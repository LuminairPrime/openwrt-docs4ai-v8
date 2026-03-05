# ucode Complete Reference

> **Generated:** 2026-03-05 18:54 UTC
> **Source:** https://github.com/jow-/ucode
> **Contains:** 15 documents concatenated

---

# ucode module: `debug`

> **Source:** [`lib/debug.c`](https://github.com/jow-/ucode/blob/master/lib/debug.c)
> **Live docs:** https://ucode.mein.io/module-debug.html
> **Generated:** 2026-03-05 18:50 UTC from commit `e87be9d`

---

jsdoc-to-markdown

  Generates markdown documentation from jsdoc-annotated source code. 

Synopsis

  $ jsdoc2md <jsdoc-options> [<dmd-options>] 
  $ jsdoc2md <jsdoc-options> --jsdoc         
  $ jsdoc2md <jsdoc-options> --json          
  $ jsdoc2md <jsdoc-options> --namepaths     
  $ jsdoc2md --help                          
  $ jsdoc2md --config                        

General options

  Main options affecting mode. If none of the following are supplied, the tool  
  will generate markdown docs.                                                  

  -h, --help    Print usage information                                         
  --config      Print all options supplied (from command line, `.jsdoc2md.json` 
                or `package.json` under the `jsdoc2md` property) and exit.      
                Useful for checking the tool is receiving the correct config.   
  --json        Prints the data (jsdoc-parse output) supplied to the template   
                (dmd).                                                          
  --jsdoc       Prints the raw jsdoc data.                                      
  --version                                                                     
  --no-cache    By default, repeat invocations against the same input with the  
                same options returns from cache. This option disables that.     
  --clear       Clears the cache.                                               

jsdoc options

  Options regarding the input source code, passed directly to jsdoc. 

  -f, --files file ...   A list of jsdoc explain files (or glob expressions) to 
                         parse for documentation. Either this or --source must  
                         be supplied.                                           
  --source string        A string containing source code to parse for           
                         documentation. Either this or --files must be          
                         supplied.                                              
  -c, --configure file   Path to a jsdoc configuration file, passed directly to 
                         `jsdoc -c`.                                            
  --namepaths            Print namepaths.                                       

dmd

  These options affect how the markdown output looks. 

 -t, --template <file>              A custom handlebars template file to insert documentation into. The default template is `{{>main}}`.                                                                                                                                                                                                                                                                                                                                                                          
 --private                          Include identifiers marked @private in the output                                                                                                                                                                                                                                                                                                                                                                                                                             
 -d, --heading-depth number         Root markdown heading depth, defaults to 2 (##).                                                                                                                                                                                                                                                                                                                                                                                                                              
 --plugin module ...                Use an installed package containing helper and/or partial overrides.                                                                                                                                                                                                                                                                                                                                                                                                          
 --helper module ...                Handlebars helper modules to override or extend the default set.                                                                                                                                                                                                                                                                                                                                                                                                              
 --partial file ...                 Handlebars partial files to override or extend the default set.                                                                                                                                                                                                                                                                                                                                                                                                               
 -l, --example-lang string          Specifies the default language used in @example blocks (for syntax-highlighting purposes). In the default gfm mode, each @example is wrapped in a fenced-code block. Example usage: --example-lang js. Use the special value none for no specific language. While using this option, you can override the supplied language for any @example by specifying the @lang subtag, e.g @example @lang hbs. Specifying @example @lang off will disable code blocks for that example. 
 --name-format                      Format identifier names as code (i.e. wrap function/property/class etc names in backticks).                                                                                                                                                                                                                                                                                                                                                                                   
 --no-gfm                           By default, dmd generates github-flavoured markdown. Not all markdown parsers render gfm correctly. If your generated docs look incorrect on sites other than Github (e.g. npmjs.org) try enabling this option to disable Github-specific syntax.                                                                                                                                                                                                                             
 --separators                       Put <hr> breaks between identifiers. Improves readability on bulky docs.                                                                                                                                                                                                                                                                                                                                                                                                      
 -m, --module-index-format string   When muliple modules are found in the input source code, an index is generated. It can be styled by one of the following options: none, grouped, table or dl.                                                                                                                                                                                                                                                                                                                 
 -g, --global-index-format string   When muliple global-scope identifiers are found in the input source code, an index is generated. It can be styled by one of the following options: none, grouped, table or dl.                                                                                                                                                                                                                                                                                                
 -p, --param-list-format string     Two options to render @param lists: list or table (default). Table format works well in most cases but switch to list if things begin to look crowded.                                                                                                                                                                                                                                                                                                                        
 -r, --property-list-format string  Two options to render @property lists: list or table (default).                                                                                                                                                                                                                                                                                                                                                                                                               
 --member-index-format string       Two options to render member lists: list or grouped (default). The list view is loosely-based on the nodejs docs.                                                                                                                                                                                                                                                                                                                                                             
 --clever-links                     By default, all {@link} tags are rendered in plain text. If `--clever-links` is set, URL {@link} tags are rendered in plain text, otherwise monospace.                                                                                                                                                                                                                                                                                                                        
 --monospace-links                  By default, all {@link} tags are rendered in plain text. If `--monospace-links` is set, all links are rendered in monospace format. This setting is ignored if `--clever-links` is set.                                                                                                                                                                                                                                                                                       
 --EOL string                       Specify ether `posix` or `win32`. Forces all line endings in the dmd output to use the specified EOL character.                                                                                                                                                                                                                                                                                                                                                               

  Project repository:   https://github.com/jsdoc2md/jsdoc-to-markdown

---

# ucode module: `digest`

> **Source:** [`lib/digest.c`](https://github.com/jow-/ucode/blob/master/lib/digest.c)
> **Live docs:** https://ucode.mein.io/module-digest.html
> **Generated:** 2026-03-05 18:50 UTC from commit `e87be9d`

---

jsdoc-to-markdown

  Generates markdown documentation from jsdoc-annotated source code. 

Synopsis

  $ jsdoc2md <jsdoc-options> [<dmd-options>] 
  $ jsdoc2md <jsdoc-options> --jsdoc         
  $ jsdoc2md <jsdoc-options> --json          
  $ jsdoc2md <jsdoc-options> --namepaths     
  $ jsdoc2md --help                          
  $ jsdoc2md --config                        

General options

  Main options affecting mode. If none of the following are supplied, the tool  
  will generate markdown docs.                                                  

  -h, --help    Print usage information                                         
  --config      Print all options supplied (from command line, `.jsdoc2md.json` 
                or `package.json` under the `jsdoc2md` property) and exit.      
                Useful for checking the tool is receiving the correct config.   
  --json        Prints the data (jsdoc-parse output) supplied to the template   
                (dmd).                                                          
  --jsdoc       Prints the raw jsdoc data.                                      
  --version                                                                     
  --no-cache    By default, repeat invocations against the same input with the  
                same options returns from cache. This option disables that.     
  --clear       Clears the cache.                                               

jsdoc options

  Options regarding the input source code, passed directly to jsdoc. 

  -f, --files file ...   A list of jsdoc explain files (or glob expressions) to 
                         parse for documentation. Either this or --source must  
                         be supplied.                                           
  --source string        A string containing source code to parse for           
                         documentation. Either this or --files must be          
                         supplied.                                              
  -c, --configure file   Path to a jsdoc configuration file, passed directly to 
                         `jsdoc -c`.                                            
  --namepaths            Print namepaths.                                       

dmd

  These options affect how the markdown output looks. 

 -t, --template <file>              A custom handlebars template file to insert documentation into. The default template is `{{>main}}`.                                                                                                                                                                                                                                                                                                                                                                          
 --private                          Include identifiers marked @private in the output                                                                                                                                                                                                                                                                                                                                                                                                                             
 -d, --heading-depth number         Root markdown heading depth, defaults to 2 (##).                                                                                                                                                                                                                                                                                                                                                                                                                              
 --plugin module ...                Use an installed package containing helper and/or partial overrides.                                                                                                                                                                                                                                                                                                                                                                                                          
 --helper module ...                Handlebars helper modules to override or extend the default set.                                                                                                                                                                                                                                                                                                                                                                                                              
 --partial file ...                 Handlebars partial files to override or extend the default set.                                                                                                                                                                                                                                                                                                                                                                                                               
 -l, --example-lang string          Specifies the default language used in @example blocks (for syntax-highlighting purposes). In the default gfm mode, each @example is wrapped in a fenced-code block. Example usage: --example-lang js. Use the special value none for no specific language. While using this option, you can override the supplied language for any @example by specifying the @lang subtag, e.g @example @lang hbs. Specifying @example @lang off will disable code blocks for that example. 
 --name-format                      Format identifier names as code (i.e. wrap function/property/class etc names in backticks).                                                                                                                                                                                                                                                                                                                                                                                   
 --no-gfm                           By default, dmd generates github-flavoured markdown. Not all markdown parsers render gfm correctly. If your generated docs look incorrect on sites other than Github (e.g. npmjs.org) try enabling this option to disable Github-specific syntax.                                                                                                                                                                                                                             
 --separators                       Put <hr> breaks between identifiers. Improves readability on bulky docs.                                                                                                                                                                                                                                                                                                                                                                                                      
 -m, --module-index-format string   When muliple modules are found in the input source code, an index is generated. It can be styled by one of the following options: none, grouped, table or dl.                                                                                                                                                                                                                                                                                                                 
 -g, --global-index-format string   When muliple global-scope identifiers are found in the input source code, an index is generated. It can be styled by one of the following options: none, grouped, table or dl.                                                                                                                                                                                                                                                                                                
 -p, --param-list-format string     Two options to render @param lists: list or table (default). Table format works well in most cases but switch to list if things begin to look crowded.                                                                                                                                                                                                                                                                                                                        
 -r, --property-list-format string  Two options to render @property lists: list or table (default).                                                                                                                                                                                                                                                                                                                                                                                                               
 --member-index-format string       Two options to render member lists: list or grouped (default). The list view is loosely-based on the nodejs docs.                                                                                                                                                                                                                                                                                                                                                             
 --clever-links                     By default, all {@link} tags are rendered in plain text. If `--clever-links` is set, URL {@link} tags are rendered in plain text, otherwise monospace.                                                                                                                                                                                                                                                                                                                        
 --monospace-links                  By default, all {@link} tags are rendered in plain text. If `--monospace-links` is set, all links are rendered in monospace format. This setting is ignored if `--clever-links` is set.                                                                                                                                                                                                                                                                                       
 --EOL string                       Specify ether `posix` or `win32`. Forces all line endings in the dmd output to use the specified EOL character.                                                                                                                                                                                                                                                                                                                                                               

  Project repository:   https://github.com/jsdoc2md/jsdoc-to-markdown

---

# ucode module: `fs`

> **Source:** [`lib/fs.c`](https://github.com/jow-/ucode/blob/master/lib/fs.c)
> **Live docs:** https://ucode.mein.io/module-fs.html
> **Generated:** 2026-03-05 18:50 UTC from commit `e87be9d`

---

jsdoc-to-markdown

  Generates markdown documentation from jsdoc-annotated source code. 

Synopsis

  $ jsdoc2md <jsdoc-options> [<dmd-options>] 
  $ jsdoc2md <jsdoc-options> --jsdoc         
  $ jsdoc2md <jsdoc-options> --json          
  $ jsdoc2md <jsdoc-options> --namepaths     
  $ jsdoc2md --help                          
  $ jsdoc2md --config                        

General options

  Main options affecting mode. If none of the following are supplied, the tool  
  will generate markdown docs.                                                  

  -h, --help    Print usage information                                         
  --config      Print all options supplied (from command line, `.jsdoc2md.json` 
                or `package.json` under the `jsdoc2md` property) and exit.      
                Useful for checking the tool is receiving the correct config.   
  --json        Prints the data (jsdoc-parse output) supplied to the template   
                (dmd).                                                          
  --jsdoc       Prints the raw jsdoc data.                                      
  --version                                                                     
  --no-cache    By default, repeat invocations against the same input with the  
                same options returns from cache. This option disables that.     
  --clear       Clears the cache.                                               

jsdoc options

  Options regarding the input source code, passed directly to jsdoc. 

  -f, --files file ...   A list of jsdoc explain files (or glob expressions) to 
                         parse for documentation. Either this or --source must  
                         be supplied.                                           
  --source string        A string containing source code to parse for           
                         documentation. Either this or --files must be          
                         supplied.                                              
  -c, --configure file   Path to a jsdoc configuration file, passed directly to 
                         `jsdoc -c`.                                            
  --namepaths            Print namepaths.                                       

dmd

  These options affect how the markdown output looks. 

 -t, --template <file>              A custom handlebars template file to insert documentation into. The default template is `{{>main}}`.                                                                                                                                                                                                                                                                                                                                                                          
 --private                          Include identifiers marked @private in the output                                                                                                                                                                                                                                                                                                                                                                                                                             
 -d, --heading-depth number         Root markdown heading depth, defaults to 2 (##).                                                                                                                                                                                                                                                                                                                                                                                                                              
 --plugin module ...                Use an installed package containing helper and/or partial overrides.                                                                                                                                                                                                                                                                                                                                                                                                          
 --helper module ...                Handlebars helper modules to override or extend the default set.                                                                                                                                                                                                                                                                                                                                                                                                              
 --partial file ...                 Handlebars partial files to override or extend the default set.                                                                                                                                                                                                                                                                                                                                                                                                               
 -l, --example-lang string          Specifies the default language used in @example blocks (for syntax-highlighting purposes). In the default gfm mode, each @example is wrapped in a fenced-code block. Example usage: --example-lang js. Use the special value none for no specific language. While using this option, you can override the supplied language for any @example by specifying the @lang subtag, e.g @example @lang hbs. Specifying @example @lang off will disable code blocks for that example. 
 --name-format                      Format identifier names as code (i.e. wrap function/property/class etc names in backticks).                                                                                                                                                                                                                                                                                                                                                                                   
 --no-gfm                           By default, dmd generates github-flavoured markdown. Not all markdown parsers render gfm correctly. If your generated docs look incorrect on sites other than Github (e.g. npmjs.org) try enabling this option to disable Github-specific syntax.                                                                                                                                                                                                                             
 --separators                       Put <hr> breaks between identifiers. Improves readability on bulky docs.                                                                                                                                                                                                                                                                                                                                                                                                      
 -m, --module-index-format string   When muliple modules are found in the input source code, an index is generated. It can be styled by one of the following options: none, grouped, table or dl.                                                                                                                                                                                                                                                                                                                 
 -g, --global-index-format string   When muliple global-scope identifiers are found in the input source code, an index is generated. It can be styled by one of the following options: none, grouped, table or dl.                                                                                                                                                                                                                                                                                                
 -p, --param-list-format string     Two options to render @param lists: list or table (default). Table format works well in most cases but switch to list if things begin to look crowded.                                                                                                                                                                                                                                                                                                                        
 -r, --property-list-format string  Two options to render @property lists: list or table (default).                                                                                                                                                                                                                                                                                                                                                                                                               
 --member-index-format string       Two options to render member lists: list or grouped (default). The list view is loosely-based on the nodejs docs.                                                                                                                                                                                                                                                                                                                                                             
 --clever-links                     By default, all {@link} tags are rendered in plain text. If `--clever-links` is set, URL {@link} tags are rendered in plain text, otherwise monospace.                                                                                                                                                                                                                                                                                                                        
 --monospace-links                  By default, all {@link} tags are rendered in plain text. If `--monospace-links` is set, all links are rendered in monospace format. This setting is ignored if `--clever-links` is set.                                                                                                                                                                                                                                                                                       
 --EOL string                       Specify ether `posix` or `win32`. Forces all line endings in the dmd output to use the specified EOL character.                                                                                                                                                                                                                                                                                                                                                               

  Project repository:   https://github.com/jsdoc2md/jsdoc-to-markdown

---

# ucode module: `io`

> **Source:** [`lib/io.c`](https://github.com/jow-/ucode/blob/master/lib/io.c)
> **Live docs:** https://ucode.mein.io/module-io.html
> **Generated:** 2026-03-05 18:50 UTC from commit `e87be9d`

---

jsdoc-to-markdown

  Generates markdown documentation from jsdoc-annotated source code. 

Synopsis

  $ jsdoc2md <jsdoc-options> [<dmd-options>] 
  $ jsdoc2md <jsdoc-options> --jsdoc         
  $ jsdoc2md <jsdoc-options> --json          
  $ jsdoc2md <jsdoc-options> --namepaths     
  $ jsdoc2md --help                          
  $ jsdoc2md --config                        

General options

  Main options affecting mode. If none of the following are supplied, the tool  
  will generate markdown docs.                                                  

  -h, --help    Print usage information                                         
  --config      Print all options supplied (from command line, `.jsdoc2md.json` 
                or `package.json` under the `jsdoc2md` property) and exit.      
                Useful for checking the tool is receiving the correct config.   
  --json        Prints the data (jsdoc-parse output) supplied to the template   
                (dmd).                                                          
  --jsdoc       Prints the raw jsdoc data.                                      
  --version                                                                     
  --no-cache    By default, repeat invocations against the same input with the  
                same options returns from cache. This option disables that.     
  --clear       Clears the cache.                                               

jsdoc options

  Options regarding the input source code, passed directly to jsdoc. 

  -f, --files file ...   A list of jsdoc explain files (or glob expressions) to 
                         parse for documentation. Either this or --source must  
                         be supplied.                                           
  --source string        A string containing source code to parse for           
                         documentation. Either this or --files must be          
                         supplied.                                              
  -c, --configure file   Path to a jsdoc configuration file, passed directly to 
                         `jsdoc -c`.                                            
  --namepaths            Print namepaths.                                       

dmd

  These options affect how the markdown output looks. 

 -t, --template <file>              A custom handlebars template file to insert documentation into. The default template is `{{>main}}`.                                                                                                                                                                                                                                                                                                                                                                          
 --private                          Include identifiers marked @private in the output                                                                                                                                                                                                                                                                                                                                                                                                                             
 -d, --heading-depth number         Root markdown heading depth, defaults to 2 (##).                                                                                                                                                                                                                                                                                                                                                                                                                              
 --plugin module ...                Use an installed package containing helper and/or partial overrides.                                                                                                                                                                                                                                                                                                                                                                                                          
 --helper module ...                Handlebars helper modules to override or extend the default set.                                                                                                                                                                                                                                                                                                                                                                                                              
 --partial file ...                 Handlebars partial files to override or extend the default set.                                                                                                                                                                                                                                                                                                                                                                                                               
 -l, --example-lang string          Specifies the default language used in @example blocks (for syntax-highlighting purposes). In the default gfm mode, each @example is wrapped in a fenced-code block. Example usage: --example-lang js. Use the special value none for no specific language. While using this option, you can override the supplied language for any @example by specifying the @lang subtag, e.g @example @lang hbs. Specifying @example @lang off will disable code blocks for that example. 
 --name-format                      Format identifier names as code (i.e. wrap function/property/class etc names in backticks).                                                                                                                                                                                                                                                                                                                                                                                   
 --no-gfm                           By default, dmd generates github-flavoured markdown. Not all markdown parsers render gfm correctly. If your generated docs look incorrect on sites other than Github (e.g. npmjs.org) try enabling this option to disable Github-specific syntax.                                                                                                                                                                                                                             
 --separators                       Put <hr> breaks between identifiers. Improves readability on bulky docs.                                                                                                                                                                                                                                                                                                                                                                                                      
 -m, --module-index-format string   When muliple modules are found in the input source code, an index is generated. It can be styled by one of the following options: none, grouped, table or dl.                                                                                                                                                                                                                                                                                                                 
 -g, --global-index-format string   When muliple global-scope identifiers are found in the input source code, an index is generated. It can be styled by one of the following options: none, grouped, table or dl.                                                                                                                                                                                                                                                                                                
 -p, --param-list-format string     Two options to render @param lists: list or table (default). Table format works well in most cases but switch to list if things begin to look crowded.                                                                                                                                                                                                                                                                                                                        
 -r, --property-list-format string  Two options to render @property lists: list or table (default).                                                                                                                                                                                                                                                                                                                                                                                                               
 --member-index-format string       Two options to render member lists: list or grouped (default). The list view is loosely-based on the nodejs docs.                                                                                                                                                                                                                                                                                                                                                             
 --clever-links                     By default, all {@link} tags are rendered in plain text. If `--clever-links` is set, URL {@link} tags are rendered in plain text, otherwise monospace.                                                                                                                                                                                                                                                                                                                        
 --monospace-links                  By default, all {@link} tags are rendered in plain text. If `--monospace-links` is set, all links are rendered in monospace format. This setting is ignored if `--clever-links` is set.                                                                                                                                                                                                                                                                                       
 --EOL string                       Specify ether `posix` or `win32`. Forces all line endings in the dmd output to use the specified EOL character.                                                                                                                                                                                                                                                                                                                                                               

  Project repository:   https://github.com/jsdoc2md/jsdoc-to-markdown

---

# ucode module: `log`

> **Source:** [`lib/log.c`](https://github.com/jow-/ucode/blob/master/lib/log.c)
> **Live docs:** https://ucode.mein.io/module-log.html
> **Generated:** 2026-03-05 18:50 UTC from commit `e87be9d`

---

jsdoc-to-markdown

  Generates markdown documentation from jsdoc-annotated source code. 

Synopsis

  $ jsdoc2md <jsdoc-options> [<dmd-options>] 
  $ jsdoc2md <jsdoc-options> --jsdoc         
  $ jsdoc2md <jsdoc-options> --json          
  $ jsdoc2md <jsdoc-options> --namepaths     
  $ jsdoc2md --help                          
  $ jsdoc2md --config                        

General options

  Main options affecting mode. If none of the following are supplied, the tool  
  will generate markdown docs.                                                  

  -h, --help    Print usage information                                         
  --config      Print all options supplied (from command line, `.jsdoc2md.json` 
                or `package.json` under the `jsdoc2md` property) and exit.      
                Useful for checking the tool is receiving the correct config.   
  --json        Prints the data (jsdoc-parse output) supplied to the template   
                (dmd).                                                          
  --jsdoc       Prints the raw jsdoc data.                                      
  --version                                                                     
  --no-cache    By default, repeat invocations against the same input with the  
                same options returns from cache. This option disables that.     
  --clear       Clears the cache.                                               

jsdoc options

  Options regarding the input source code, passed directly to jsdoc. 

  -f, --files file ...   A list of jsdoc explain files (or glob expressions) to 
                         parse for documentation. Either this or --source must  
                         be supplied.                                           
  --source string        A string containing source code to parse for           
                         documentation. Either this or --files must be          
                         supplied.                                              
  -c, --configure file   Path to a jsdoc configuration file, passed directly to 
                         `jsdoc -c`.                                            
  --namepaths            Print namepaths.                                       

dmd

  These options affect how the markdown output looks. 

 -t, --template <file>              A custom handlebars template file to insert documentation into. The default template is `{{>main}}`.                                                                                                                                                                                                                                                                                                                                                                          
 --private                          Include identifiers marked @private in the output                                                                                                                                                                                                                                                                                                                                                                                                                             
 -d, --heading-depth number         Root markdown heading depth, defaults to 2 (##).                                                                                                                                                                                                                                                                                                                                                                                                                              
 --plugin module ...                Use an installed package containing helper and/or partial overrides.                                                                                                                                                                                                                                                                                                                                                                                                          
 --helper module ...                Handlebars helper modules to override or extend the default set.                                                                                                                                                                                                                                                                                                                                                                                                              
 --partial file ...                 Handlebars partial files to override or extend the default set.                                                                                                                                                                                                                                                                                                                                                                                                               
 -l, --example-lang string          Specifies the default language used in @example blocks (for syntax-highlighting purposes). In the default gfm mode, each @example is wrapped in a fenced-code block. Example usage: --example-lang js. Use the special value none for no specific language. While using this option, you can override the supplied language for any @example by specifying the @lang subtag, e.g @example @lang hbs. Specifying @example @lang off will disable code blocks for that example. 
 --name-format                      Format identifier names as code (i.e. wrap function/property/class etc names in backticks).                                                                                                                                                                                                                                                                                                                                                                                   
 --no-gfm                           By default, dmd generates github-flavoured markdown. Not all markdown parsers render gfm correctly. If your generated docs look incorrect on sites other than Github (e.g. npmjs.org) try enabling this option to disable Github-specific syntax.                                                                                                                                                                                                                             
 --separators                       Put <hr> breaks between identifiers. Improves readability on bulky docs.                                                                                                                                                                                                                                                                                                                                                                                                      
 -m, --module-index-format string   When muliple modules are found in the input source code, an index is generated. It can be styled by one of the following options: none, grouped, table or dl.                                                                                                                                                                                                                                                                                                                 
 -g, --global-index-format string   When muliple global-scope identifiers are found in the input source code, an index is generated. It can be styled by one of the following options: none, grouped, table or dl.                                                                                                                                                                                                                                                                                                
 -p, --param-list-format string     Two options to render @param lists: list or table (default). Table format works well in most cases but switch to list if things begin to look crowded.                                                                                                                                                                                                                                                                                                                        
 -r, --property-list-format string  Two options to render @property lists: list or table (default).                                                                                                                                                                                                                                                                                                                                                                                                               
 --member-index-format string       Two options to render member lists: list or grouped (default). The list view is loosely-based on the nodejs docs.                                                                                                                                                                                                                                                                                                                                                             
 --clever-links                     By default, all {@link} tags are rendered in plain text. If `--clever-links` is set, URL {@link} tags are rendered in plain text, otherwise monospace.                                                                                                                                                                                                                                                                                                                        
 --monospace-links                  By default, all {@link} tags are rendered in plain text. If `--monospace-links` is set, all links are rendered in monospace format. This setting is ignored if `--clever-links` is set.                                                                                                                                                                                                                                                                                       
 --EOL string                       Specify ether `posix` or `win32`. Forces all line endings in the dmd output to use the specified EOL character.                                                                                                                                                                                                                                                                                                                                                               

  Project repository:   https://github.com/jsdoc2md/jsdoc-to-markdown

---

# ucode module: `math`

> **Source:** [`lib/math.c`](https://github.com/jow-/ucode/blob/master/lib/math.c)
> **Live docs:** https://ucode.mein.io/module-math.html
> **Generated:** 2026-03-05 18:50 UTC from commit `e87be9d`

---

jsdoc-to-markdown

  Generates markdown documentation from jsdoc-annotated source code. 

Synopsis

  $ jsdoc2md <jsdoc-options> [<dmd-options>] 
  $ jsdoc2md <jsdoc-options> --jsdoc         
  $ jsdoc2md <jsdoc-options> --json          
  $ jsdoc2md <jsdoc-options> --namepaths     
  $ jsdoc2md --help                          
  $ jsdoc2md --config                        

General options

  Main options affecting mode. If none of the following are supplied, the tool  
  will generate markdown docs.                                                  

  -h, --help    Print usage information                                         
  --config      Print all options supplied (from command line, `.jsdoc2md.json` 
                or `package.json` under the `jsdoc2md` property) and exit.      
                Useful for checking the tool is receiving the correct config.   
  --json        Prints the data (jsdoc-parse output) supplied to the template   
                (dmd).                                                          
  --jsdoc       Prints the raw jsdoc data.                                      
  --version                                                                     
  --no-cache    By default, repeat invocations against the same input with the  
                same options returns from cache. This option disables that.     
  --clear       Clears the cache.                                               

jsdoc options

  Options regarding the input source code, passed directly to jsdoc. 

  -f, --files file ...   A list of jsdoc explain files (or glob expressions) to 
                         parse for documentation. Either this or --source must  
                         be supplied.                                           
  --source string        A string containing source code to parse for           
                         documentation. Either this or --files must be          
                         supplied.                                              
  -c, --configure file   Path to a jsdoc configuration file, passed directly to 
                         `jsdoc -c`.                                            
  --namepaths            Print namepaths.                                       

dmd

  These options affect how the markdown output looks. 

 -t, --template <file>              A custom handlebars template file to insert documentation into. The default template is `{{>main}}`.                                                                                                                                                                                                                                                                                                                                                                          
 --private                          Include identifiers marked @private in the output                                                                                                                                                                                                                                                                                                                                                                                                                             
 -d, --heading-depth number         Root markdown heading depth, defaults to 2 (##).                                                                                                                                                                                                                                                                                                                                                                                                                              
 --plugin module ...                Use an installed package containing helper and/or partial overrides.                                                                                                                                                                                                                                                                                                                                                                                                          
 --helper module ...                Handlebars helper modules to override or extend the default set.                                                                                                                                                                                                                                                                                                                                                                                                              
 --partial file ...                 Handlebars partial files to override or extend the default set.                                                                                                                                                                                                                                                                                                                                                                                                               
 -l, --example-lang string          Specifies the default language used in @example blocks (for syntax-highlighting purposes). In the default gfm mode, each @example is wrapped in a fenced-code block. Example usage: --example-lang js. Use the special value none for no specific language. While using this option, you can override the supplied language for any @example by specifying the @lang subtag, e.g @example @lang hbs. Specifying @example @lang off will disable code blocks for that example. 
 --name-format                      Format identifier names as code (i.e. wrap function/property/class etc names in backticks).                                                                                                                                                                                                                                                                                                                                                                                   
 --no-gfm                           By default, dmd generates github-flavoured markdown. Not all markdown parsers render gfm correctly. If your generated docs look incorrect on sites other than Github (e.g. npmjs.org) try enabling this option to disable Github-specific syntax.                                                                                                                                                                                                                             
 --separators                       Put <hr> breaks between identifiers. Improves readability on bulky docs.                                                                                                                                                                                                                                                                                                                                                                                                      
 -m, --module-index-format string   When muliple modules are found in the input source code, an index is generated. It can be styled by one of the following options: none, grouped, table or dl.                                                                                                                                                                                                                                                                                                                 
 -g, --global-index-format string   When muliple global-scope identifiers are found in the input source code, an index is generated. It can be styled by one of the following options: none, grouped, table or dl.                                                                                                                                                                                                                                                                                                
 -p, --param-list-format string     Two options to render @param lists: list or table (default). Table format works well in most cases but switch to list if things begin to look crowded.                                                                                                                                                                                                                                                                                                                        
 -r, --property-list-format string  Two options to render @property lists: list or table (default).                                                                                                                                                                                                                                                                                                                                                                                                               
 --member-index-format string       Two options to render member lists: list or grouped (default). The list view is loosely-based on the nodejs docs.                                                                                                                                                                                                                                                                                                                                                             
 --clever-links                     By default, all {@link} tags are rendered in plain text. If `--clever-links` is set, URL {@link} tags are rendered in plain text, otherwise monospace.                                                                                                                                                                                                                                                                                                                        
 --monospace-links                  By default, all {@link} tags are rendered in plain text. If `--monospace-links` is set, all links are rendered in monospace format. This setting is ignored if `--clever-links` is set.                                                                                                                                                                                                                                                                                       
 --EOL string                       Specify ether `posix` or `win32`. Forces all line endings in the dmd output to use the specified EOL character.                                                                                                                                                                                                                                                                                                                                                               

  Project repository:   https://github.com/jsdoc2md/jsdoc-to-markdown

---

# ucode module: `nl80211`

> **Source:** [`lib/nl80211.c`](https://github.com/jow-/ucode/blob/master/lib/nl80211.c)
> **Live docs:** https://ucode.mein.io/module-nl80211.html
> **Generated:** 2026-03-05 18:50 UTC from commit `e87be9d`

---

jsdoc-to-markdown

  Generates markdown documentation from jsdoc-annotated source code. 

Synopsis

  $ jsdoc2md <jsdoc-options> [<dmd-options>] 
  $ jsdoc2md <jsdoc-options> --jsdoc         
  $ jsdoc2md <jsdoc-options> --json          
  $ jsdoc2md <jsdoc-options> --namepaths     
  $ jsdoc2md --help                          
  $ jsdoc2md --config                        

General options

  Main options affecting mode. If none of the following are supplied, the tool  
  will generate markdown docs.                                                  

  -h, --help    Print usage information                                         
  --config      Print all options supplied (from command line, `.jsdoc2md.json` 
                or `package.json` under the `jsdoc2md` property) and exit.      
                Useful for checking the tool is receiving the correct config.   
  --json        Prints the data (jsdoc-parse output) supplied to the template   
                (dmd).                                                          
  --jsdoc       Prints the raw jsdoc data.                                      
  --version                                                                     
  --no-cache    By default, repeat invocations against the same input with the  
                same options returns from cache. This option disables that.     
  --clear       Clears the cache.                                               

jsdoc options

  Options regarding the input source code, passed directly to jsdoc. 

  -f, --files file ...   A list of jsdoc explain files (or glob expressions) to 
                         parse for documentation. Either this or --source must  
                         be supplied.                                           
  --source string        A string containing source code to parse for           
                         documentation. Either this or --files must be          
                         supplied.                                              
  -c, --configure file   Path to a jsdoc configuration file, passed directly to 
                         `jsdoc -c`.                                            
  --namepaths            Print namepaths.                                       

dmd

  These options affect how the markdown output looks. 

 -t, --template <file>              A custom handlebars template file to insert documentation into. The default template is `{{>main}}`.                                                                                                                                                                                                                                                                                                                                                                          
 --private                          Include identifiers marked @private in the output                                                                                                                                                                                                                                                                                                                                                                                                                             
 -d, --heading-depth number         Root markdown heading depth, defaults to 2 (##).                                                                                                                                                                                                                                                                                                                                                                                                                              
 --plugin module ...                Use an installed package containing helper and/or partial overrides.                                                                                                                                                                                                                                                                                                                                                                                                          
 --helper module ...                Handlebars helper modules to override or extend the default set.                                                                                                                                                                                                                                                                                                                                                                                                              
 --partial file ...                 Handlebars partial files to override or extend the default set.                                                                                                                                                                                                                                                                                                                                                                                                               
 -l, --example-lang string          Specifies the default language used in @example blocks (for syntax-highlighting purposes). In the default gfm mode, each @example is wrapped in a fenced-code block. Example usage: --example-lang js. Use the special value none for no specific language. While using this option, you can override the supplied language for any @example by specifying the @lang subtag, e.g @example @lang hbs. Specifying @example @lang off will disable code blocks for that example. 
 --name-format                      Format identifier names as code (i.e. wrap function/property/class etc names in backticks).                                                                                                                                                                                                                                                                                                                                                                                   
 --no-gfm                           By default, dmd generates github-flavoured markdown. Not all markdown parsers render gfm correctly. If your generated docs look incorrect on sites other than Github (e.g. npmjs.org) try enabling this option to disable Github-specific syntax.                                                                                                                                                                                                                             
 --separators                       Put <hr> breaks between identifiers. Improves readability on bulky docs.                                                                                                                                                                                                                                                                                                                                                                                                      
 -m, --module-index-format string   When muliple modules are found in the input source code, an index is generated. It can be styled by one of the following options: none, grouped, table or dl.                                                                                                                                                                                                                                                                                                                 
 -g, --global-index-format string   When muliple global-scope identifiers are found in the input source code, an index is generated. It can be styled by one of the following options: none, grouped, table or dl.                                                                                                                                                                                                                                                                                                
 -p, --param-list-format string     Two options to render @param lists: list or table (default). Table format works well in most cases but switch to list if things begin to look crowded.                                                                                                                                                                                                                                                                                                                        
 -r, --property-list-format string  Two options to render @property lists: list or table (default).                                                                                                                                                                                                                                                                                                                                                                                                               
 --member-index-format string       Two options to render member lists: list or grouped (default). The list view is loosely-based on the nodejs docs.                                                                                                                                                                                                                                                                                                                                                             
 --clever-links                     By default, all {@link} tags are rendered in plain text. If `--clever-links` is set, URL {@link} tags are rendered in plain text, otherwise monospace.                                                                                                                                                                                                                                                                                                                        
 --monospace-links                  By default, all {@link} tags are rendered in plain text. If `--monospace-links` is set, all links are rendered in monospace format. This setting is ignored if `--clever-links` is set.                                                                                                                                                                                                                                                                                       
 --EOL string                       Specify ether `posix` or `win32`. Forces all line endings in the dmd output to use the specified EOL character.                                                                                                                                                                                                                                                                                                                                                               

  Project repository:   https://github.com/jsdoc2md/jsdoc-to-markdown

---

# ucode module: `resolv`

> **Source:** [`lib/resolv.c`](https://github.com/jow-/ucode/blob/master/lib/resolv.c)
> **Live docs:** https://ucode.mein.io/module-resolv.html
> **Generated:** 2026-03-05 18:50 UTC from commit `e87be9d`

---

jsdoc-to-markdown

  Generates markdown documentation from jsdoc-annotated source code. 

Synopsis

  $ jsdoc2md <jsdoc-options> [<dmd-options>] 
  $ jsdoc2md <jsdoc-options> --jsdoc         
  $ jsdoc2md <jsdoc-options> --json          
  $ jsdoc2md <jsdoc-options> --namepaths     
  $ jsdoc2md --help                          
  $ jsdoc2md --config                        

General options

  Main options affecting mode. If none of the following are supplied, the tool  
  will generate markdown docs.                                                  

  -h, --help    Print usage information                                         
  --config      Print all options supplied (from command line, `.jsdoc2md.json` 
                or `package.json` under the `jsdoc2md` property) and exit.      
                Useful for checking the tool is receiving the correct config.   
  --json        Prints the data (jsdoc-parse output) supplied to the template   
                (dmd).                                                          
  --jsdoc       Prints the raw jsdoc data.                                      
  --version                                                                     
  --no-cache    By default, repeat invocations against the same input with the  
                same options returns from cache. This option disables that.     
  --clear       Clears the cache.                                               

jsdoc options

  Options regarding the input source code, passed directly to jsdoc. 

  -f, --files file ...   A list of jsdoc explain files (or glob expressions) to 
                         parse for documentation. Either this or --source must  
                         be supplied.                                           
  --source string        A string containing source code to parse for           
                         documentation. Either this or --files must be          
                         supplied.                                              
  -c, --configure file   Path to a jsdoc configuration file, passed directly to 
                         `jsdoc -c`.                                            
  --namepaths            Print namepaths.                                       

dmd

  These options affect how the markdown output looks. 

 -t, --template <file>              A custom handlebars template file to insert documentation into. The default template is `{{>main}}`.                                                                                                                                                                                                                                                                                                                                                                          
 --private                          Include identifiers marked @private in the output                                                                                                                                                                                                                                                                                                                                                                                                                             
 -d, --heading-depth number         Root markdown heading depth, defaults to 2 (##).                                                                                                                                                                                                                                                                                                                                                                                                                              
 --plugin module ...                Use an installed package containing helper and/or partial overrides.                                                                                                                                                                                                                                                                                                                                                                                                          
 --helper module ...                Handlebars helper modules to override or extend the default set.                                                                                                                                                                                                                                                                                                                                                                                                              
 --partial file ...                 Handlebars partial files to override or extend the default set.                                                                                                                                                                                                                                                                                                                                                                                                               
 -l, --example-lang string          Specifies the default language used in @example blocks (for syntax-highlighting purposes). In the default gfm mode, each @example is wrapped in a fenced-code block. Example usage: --example-lang js. Use the special value none for no specific language. While using this option, you can override the supplied language for any @example by specifying the @lang subtag, e.g @example @lang hbs. Specifying @example @lang off will disable code blocks for that example. 
 --name-format                      Format identifier names as code (i.e. wrap function/property/class etc names in backticks).                                                                                                                                                                                                                                                                                                                                                                                   
 --no-gfm                           By default, dmd generates github-flavoured markdown. Not all markdown parsers render gfm correctly. If your generated docs look incorrect on sites other than Github (e.g. npmjs.org) try enabling this option to disable Github-specific syntax.                                                                                                                                                                                                                             
 --separators                       Put <hr> breaks between identifiers. Improves readability on bulky docs.                                                                                                                                                                                                                                                                                                                                                                                                      
 -m, --module-index-format string   When muliple modules are found in the input source code, an index is generated. It can be styled by one of the following options: none, grouped, table or dl.                                                                                                                                                                                                                                                                                                                 
 -g, --global-index-format string   When muliple global-scope identifiers are found in the input source code, an index is generated. It can be styled by one of the following options: none, grouped, table or dl.                                                                                                                                                                                                                                                                                                
 -p, --param-list-format string     Two options to render @param lists: list or table (default). Table format works well in most cases but switch to list if things begin to look crowded.                                                                                                                                                                                                                                                                                                                        
 -r, --property-list-format string  Two options to render @property lists: list or table (default).                                                                                                                                                                                                                                                                                                                                                                                                               
 --member-index-format string       Two options to render member lists: list or grouped (default). The list view is loosely-based on the nodejs docs.                                                                                                                                                                                                                                                                                                                                                             
 --clever-links                     By default, all {@link} tags are rendered in plain text. If `--clever-links` is set, URL {@link} tags are rendered in plain text, otherwise monospace.                                                                                                                                                                                                                                                                                                                        
 --monospace-links                  By default, all {@link} tags are rendered in plain text. If `--monospace-links` is set, all links are rendered in monospace format. This setting is ignored if `--clever-links` is set.                                                                                                                                                                                                                                                                                       
 --EOL string                       Specify ether `posix` or `win32`. Forces all line endings in the dmd output to use the specified EOL character.                                                                                                                                                                                                                                                                                                                                                               

  Project repository:   https://github.com/jsdoc2md/jsdoc-to-markdown

---

# ucode module: `rtnl`

> **Source:** [`lib/rtnl.c`](https://github.com/jow-/ucode/blob/master/lib/rtnl.c)
> **Live docs:** https://ucode.mein.io/module-rtnl.html
> **Generated:** 2026-03-05 18:50 UTC from commit `e87be9d`

---

jsdoc-to-markdown

  Generates markdown documentation from jsdoc-annotated source code. 

Synopsis

  $ jsdoc2md <jsdoc-options> [<dmd-options>] 
  $ jsdoc2md <jsdoc-options> --jsdoc         
  $ jsdoc2md <jsdoc-options> --json          
  $ jsdoc2md <jsdoc-options> --namepaths     
  $ jsdoc2md --help                          
  $ jsdoc2md --config                        

General options

  Main options affecting mode. If none of the following are supplied, the tool  
  will generate markdown docs.                                                  

  -h, --help    Print usage information                                         
  --config      Print all options supplied (from command line, `.jsdoc2md.json` 
                or `package.json` under the `jsdoc2md` property) and exit.      
                Useful for checking the tool is receiving the correct config.   
  --json        Prints the data (jsdoc-parse output) supplied to the template   
                (dmd).                                                          
  --jsdoc       Prints the raw jsdoc data.                                      
  --version                                                                     
  --no-cache    By default, repeat invocations against the same input with the  
                same options returns from cache. This option disables that.     
  --clear       Clears the cache.                                               

jsdoc options

  Options regarding the input source code, passed directly to jsdoc. 

  -f, --files file ...   A list of jsdoc explain files (or glob expressions) to 
                         parse for documentation. Either this or --source must  
                         be supplied.                                           
  --source string        A string containing source code to parse for           
                         documentation. Either this or --files must be          
                         supplied.                                              
  -c, --configure file   Path to a jsdoc configuration file, passed directly to 
                         `jsdoc -c`.                                            
  --namepaths            Print namepaths.                                       

dmd

  These options affect how the markdown output looks. 

 -t, --template <file>              A custom handlebars template file to insert documentation into. The default template is `{{>main}}`.                                                                                                                                                                                                                                                                                                                                                                          
 --private                          Include identifiers marked @private in the output                                                                                                                                                                                                                                                                                                                                                                                                                             
 -d, --heading-depth number         Root markdown heading depth, defaults to 2 (##).                                                                                                                                                                                                                                                                                                                                                                                                                              
 --plugin module ...                Use an installed package containing helper and/or partial overrides.                                                                                                                                                                                                                                                                                                                                                                                                          
 --helper module ...                Handlebars helper modules to override or extend the default set.                                                                                                                                                                                                                                                                                                                                                                                                              
 --partial file ...                 Handlebars partial files to override or extend the default set.                                                                                                                                                                                                                                                                                                                                                                                                               
 -l, --example-lang string          Specifies the default language used in @example blocks (for syntax-highlighting purposes). In the default gfm mode, each @example is wrapped in a fenced-code block. Example usage: --example-lang js. Use the special value none for no specific language. While using this option, you can override the supplied language for any @example by specifying the @lang subtag, e.g @example @lang hbs. Specifying @example @lang off will disable code blocks for that example. 
 --name-format                      Format identifier names as code (i.e. wrap function/property/class etc names in backticks).                                                                                                                                                                                                                                                                                                                                                                                   
 --no-gfm                           By default, dmd generates github-flavoured markdown. Not all markdown parsers render gfm correctly. If your generated docs look incorrect on sites other than Github (e.g. npmjs.org) try enabling this option to disable Github-specific syntax.                                                                                                                                                                                                                             
 --separators                       Put <hr> breaks between identifiers. Improves readability on bulky docs.                                                                                                                                                                                                                                                                                                                                                                                                      
 -m, --module-index-format string   When muliple modules are found in the input source code, an index is generated. It can be styled by one of the following options: none, grouped, table or dl.                                                                                                                                                                                                                                                                                                                 
 -g, --global-index-format string   When muliple global-scope identifiers are found in the input source code, an index is generated. It can be styled by one of the following options: none, grouped, table or dl.                                                                                                                                                                                                                                                                                                
 -p, --param-list-format string     Two options to render @param lists: list or table (default). Table format works well in most cases but switch to list if things begin to look crowded.                                                                                                                                                                                                                                                                                                                        
 -r, --property-list-format string  Two options to render @property lists: list or table (default).                                                                                                                                                                                                                                                                                                                                                                                                               
 --member-index-format string       Two options to render member lists: list or grouped (default). The list view is loosely-based on the nodejs docs.                                                                                                                                                                                                                                                                                                                                                             
 --clever-links                     By default, all {@link} tags are rendered in plain text. If `--clever-links` is set, URL {@link} tags are rendered in plain text, otherwise monospace.                                                                                                                                                                                                                                                                                                                        
 --monospace-links                  By default, all {@link} tags are rendered in plain text. If `--monospace-links` is set, all links are rendered in monospace format. This setting is ignored if `--clever-links` is set.                                                                                                                                                                                                                                                                                       
 --EOL string                       Specify ether `posix` or `win32`. Forces all line endings in the dmd output to use the specified EOL character.                                                                                                                                                                                                                                                                                                                                                               

  Project repository:   https://github.com/jsdoc2md/jsdoc-to-markdown

---

# ucode module: `socket`

> **Source:** [`lib/socket.c`](https://github.com/jow-/ucode/blob/master/lib/socket.c)
> **Live docs:** https://ucode.mein.io/module-socket.html
> **Generated:** 2026-03-05 18:50 UTC from commit `e87be9d`

---

jsdoc-to-markdown

  Generates markdown documentation from jsdoc-annotated source code. 

Synopsis

  $ jsdoc2md <jsdoc-options> [<dmd-options>] 
  $ jsdoc2md <jsdoc-options> --jsdoc         
  $ jsdoc2md <jsdoc-options> --json          
  $ jsdoc2md <jsdoc-options> --namepaths     
  $ jsdoc2md --help                          
  $ jsdoc2md --config                        

General options

  Main options affecting mode. If none of the following are supplied, the tool  
  will generate markdown docs.                                                  

  -h, --help    Print usage information                                         
  --config      Print all options supplied (from command line, `.jsdoc2md.json` 
                or `package.json` under the `jsdoc2md` property) and exit.      
                Useful for checking the tool is receiving the correct config.   
  --json        Prints the data (jsdoc-parse output) supplied to the template   
                (dmd).                                                          
  --jsdoc       Prints the raw jsdoc data.                                      
  --version                                                                     
  --no-cache    By default, repeat invocations against the same input with the  
                same options returns from cache. This option disables that.     
  --clear       Clears the cache.                                               

jsdoc options

  Options regarding the input source code, passed directly to jsdoc. 

  -f, --files file ...   A list of jsdoc explain files (or glob expressions) to 
                         parse for documentation. Either this or --source must  
                         be supplied.                                           
  --source string        A string containing source code to parse for           
                         documentation. Either this or --files must be          
                         supplied.                                              
  -c, --configure file   Path to a jsdoc configuration file, passed directly to 
                         `jsdoc -c`.                                            
  --namepaths            Print namepaths.                                       

dmd

  These options affect how the markdown output looks. 

 -t, --template <file>              A custom handlebars template file to insert documentation into. The default template is `{{>main}}`.                                                                                                                                                                                                                                                                                                                                                                          
 --private                          Include identifiers marked @private in the output                                                                                                                                                                                                                                                                                                                                                                                                                             
 -d, --heading-depth number         Root markdown heading depth, defaults to 2 (##).                                                                                                                                                                                                                                                                                                                                                                                                                              
 --plugin module ...                Use an installed package containing helper and/or partial overrides.                                                                                                                                                                                                                                                                                                                                                                                                          
 --helper module ...                Handlebars helper modules to override or extend the default set.                                                                                                                                                                                                                                                                                                                                                                                                              
 --partial file ...                 Handlebars partial files to override or extend the default set.                                                                                                                                                                                                                                                                                                                                                                                                               
 -l, --example-lang string          Specifies the default language used in @example blocks (for syntax-highlighting purposes). In the default gfm mode, each @example is wrapped in a fenced-code block. Example usage: --example-lang js. Use the special value none for no specific language. While using this option, you can override the supplied language for any @example by specifying the @lang subtag, e.g @example @lang hbs. Specifying @example @lang off will disable code blocks for that example. 
 --name-format                      Format identifier names as code (i.e. wrap function/property/class etc names in backticks).                                                                                                                                                                                                                                                                                                                                                                                   
 --no-gfm                           By default, dmd generates github-flavoured markdown. Not all markdown parsers render gfm correctly. If your generated docs look incorrect on sites other than Github (e.g. npmjs.org) try enabling this option to disable Github-specific syntax.                                                                                                                                                                                                                             
 --separators                       Put <hr> breaks between identifiers. Improves readability on bulky docs.                                                                                                                                                                                                                                                                                                                                                                                                      
 -m, --module-index-format string   When muliple modules are found in the input source code, an index is generated. It can be styled by one of the following options: none, grouped, table or dl.                                                                                                                                                                                                                                                                                                                 
 -g, --global-index-format string   When muliple global-scope identifiers are found in the input source code, an index is generated. It can be styled by one of the following options: none, grouped, table or dl.                                                                                                                                                                                                                                                                                                
 -p, --param-list-format string     Two options to render @param lists: list or table (default). Table format works well in most cases but switch to list if things begin to look crowded.                                                                                                                                                                                                                                                                                                                        
 -r, --property-list-format string  Two options to render @property lists: list or table (default).                                                                                                                                                                                                                                                                                                                                                                                                               
 --member-index-format string       Two options to render member lists: list or grouped (default). The list view is loosely-based on the nodejs docs.                                                                                                                                                                                                                                                                                                                                                             
 --clever-links                     By default, all {@link} tags are rendered in plain text. If `--clever-links` is set, URL {@link} tags are rendered in plain text, otherwise monospace.                                                                                                                                                                                                                                                                                                                        
 --monospace-links                  By default, all {@link} tags are rendered in plain text. If `--monospace-links` is set, all links are rendered in monospace format. This setting is ignored if `--clever-links` is set.                                                                                                                                                                                                                                                                                       
 --EOL string                       Specify ether `posix` or `win32`. Forces all line endings in the dmd output to use the specified EOL character.                                                                                                                                                                                                                                                                                                                                                               

  Project repository:   https://github.com/jsdoc2md/jsdoc-to-markdown

---

# ucode module: `struct`

> **Source:** [`lib/struct.c`](https://github.com/jow-/ucode/blob/master/lib/struct.c)
> **Live docs:** https://ucode.mein.io/module-struct.html
> **Generated:** 2026-03-05 18:50 UTC from commit `e87be9d`

---

jsdoc-to-markdown

  Generates markdown documentation from jsdoc-annotated source code. 

Synopsis

  $ jsdoc2md <jsdoc-options> [<dmd-options>] 
  $ jsdoc2md <jsdoc-options> --jsdoc         
  $ jsdoc2md <jsdoc-options> --json          
  $ jsdoc2md <jsdoc-options> --namepaths     
  $ jsdoc2md --help                          
  $ jsdoc2md --config                        

General options

  Main options affecting mode. If none of the following are supplied, the tool  
  will generate markdown docs.                                                  

  -h, --help    Print usage information                                         
  --config      Print all options supplied (from command line, `.jsdoc2md.json` 
                or `package.json` under the `jsdoc2md` property) and exit.      
                Useful for checking the tool is receiving the correct config.   
  --json        Prints the data (jsdoc-parse output) supplied to the template   
                (dmd).                                                          
  --jsdoc       Prints the raw jsdoc data.                                      
  --version                                                                     
  --no-cache    By default, repeat invocations against the same input with the  
                same options returns from cache. This option disables that.     
  --clear       Clears the cache.                                               

jsdoc options

  Options regarding the input source code, passed directly to jsdoc. 

  -f, --files file ...   A list of jsdoc explain files (or glob expressions) to 
                         parse for documentation. Either this or --source must  
                         be supplied.                                           
  --source string        A string containing source code to parse for           
                         documentation. Either this or --files must be          
                         supplied.                                              
  -c, --configure file   Path to a jsdoc configuration file, passed directly to 
                         `jsdoc -c`.                                            
  --namepaths            Print namepaths.                                       

dmd

  These options affect how the markdown output looks. 

 -t, --template <file>              A custom handlebars template file to insert documentation into. The default template is `{{>main}}`.                                                                                                                                                                                                                                                                                                                                                                          
 --private                          Include identifiers marked @private in the output                                                                                                                                                                                                                                                                                                                                                                                                                             
 -d, --heading-depth number         Root markdown heading depth, defaults to 2 (##).                                                                                                                                                                                                                                                                                                                                                                                                                              
 --plugin module ...                Use an installed package containing helper and/or partial overrides.                                                                                                                                                                                                                                                                                                                                                                                                          
 --helper module ...                Handlebars helper modules to override or extend the default set.                                                                                                                                                                                                                                                                                                                                                                                                              
 --partial file ...                 Handlebars partial files to override or extend the default set.                                                                                                                                                                                                                                                                                                                                                                                                               
 -l, --example-lang string          Specifies the default language used in @example blocks (for syntax-highlighting purposes). In the default gfm mode, each @example is wrapped in a fenced-code block. Example usage: --example-lang js. Use the special value none for no specific language. While using this option, you can override the supplied language for any @example by specifying the @lang subtag, e.g @example @lang hbs. Specifying @example @lang off will disable code blocks for that example. 
 --name-format                      Format identifier names as code (i.e. wrap function/property/class etc names in backticks).                                                                                                                                                                                                                                                                                                                                                                                   
 --no-gfm                           By default, dmd generates github-flavoured markdown. Not all markdown parsers render gfm correctly. If your generated docs look incorrect on sites other than Github (e.g. npmjs.org) try enabling this option to disable Github-specific syntax.                                                                                                                                                                                                                             
 --separators                       Put <hr> breaks between identifiers. Improves readability on bulky docs.                                                                                                                                                                                                                                                                                                                                                                                                      
 -m, --module-index-format string   When muliple modules are found in the input source code, an index is generated. It can be styled by one of the following options: none, grouped, table or dl.                                                                                                                                                                                                                                                                                                                 
 -g, --global-index-format string   When muliple global-scope identifiers are found in the input source code, an index is generated. It can be styled by one of the following options: none, grouped, table or dl.                                                                                                                                                                                                                                                                                                
 -p, --param-list-format string     Two options to render @param lists: list or table (default). Table format works well in most cases but switch to list if things begin to look crowded.                                                                                                                                                                                                                                                                                                                        
 -r, --property-list-format string  Two options to render @property lists: list or table (default).                                                                                                                                                                                                                                                                                                                                                                                                               
 --member-index-format string       Two options to render member lists: list or grouped (default). The list view is loosely-based on the nodejs docs.                                                                                                                                                                                                                                                                                                                                                             
 --clever-links                     By default, all {@link} tags are rendered in plain text. If `--clever-links` is set, URL {@link} tags are rendered in plain text, otherwise monospace.                                                                                                                                                                                                                                                                                                                        
 --monospace-links                  By default, all {@link} tags are rendered in plain text. If `--monospace-links` is set, all links are rendered in monospace format. This setting is ignored if `--clever-links` is set.                                                                                                                                                                                                                                                                                       
 --EOL string                       Specify ether `posix` or `win32`. Forces all line endings in the dmd output to use the specified EOL character.                                                                                                                                                                                                                                                                                                                                                               

  Project repository:   https://github.com/jsdoc2md/jsdoc-to-markdown

---

# ucode module: `ubus`

> **Source:** [`lib/ubus.c`](https://github.com/jow-/ucode/blob/master/lib/ubus.c)
> **Live docs:** https://ucode.mein.io/module-ubus.html
> **Generated:** 2026-03-05 18:50 UTC from commit `e87be9d`

---

jsdoc-to-markdown

  Generates markdown documentation from jsdoc-annotated source code. 

Synopsis

  $ jsdoc2md <jsdoc-options> [<dmd-options>] 
  $ jsdoc2md <jsdoc-options> --jsdoc         
  $ jsdoc2md <jsdoc-options> --json          
  $ jsdoc2md <jsdoc-options> --namepaths     
  $ jsdoc2md --help                          
  $ jsdoc2md --config                        

General options

  Main options affecting mode. If none of the following are supplied, the tool  
  will generate markdown docs.                                                  

  -h, --help    Print usage information                                         
  --config      Print all options supplied (from command line, `.jsdoc2md.json` 
                or `package.json` under the `jsdoc2md` property) and exit.      
                Useful for checking the tool is receiving the correct config.   
  --json        Prints the data (jsdoc-parse output) supplied to the template   
                (dmd).                                                          
  --jsdoc       Prints the raw jsdoc data.                                      
  --version                                                                     
  --no-cache    By default, repeat invocations against the same input with the  
                same options returns from cache. This option disables that.     
  --clear       Clears the cache.                                               

jsdoc options

  Options regarding the input source code, passed directly to jsdoc. 

  -f, --files file ...   A list of jsdoc explain files (or glob expressions) to 
                         parse for documentation. Either this or --source must  
                         be supplied.                                           
  --source string        A string containing source code to parse for           
                         documentation. Either this or --files must be          
                         supplied.                                              
  -c, --configure file   Path to a jsdoc configuration file, passed directly to 
                         `jsdoc -c`.                                            
  --namepaths            Print namepaths.                                       

dmd

  These options affect how the markdown output looks. 

 -t, --template <file>              A custom handlebars template file to insert documentation into. The default template is `{{>main}}`.                                                                                                                                                                                                                                                                                                                                                                          
 --private                          Include identifiers marked @private in the output                                                                                                                                                                                                                                                                                                                                                                                                                             
 -d, --heading-depth number         Root markdown heading depth, defaults to 2 (##).                                                                                                                                                                                                                                                                                                                                                                                                                              
 --plugin module ...                Use an installed package containing helper and/or partial overrides.                                                                                                                                                                                                                                                                                                                                                                                                          
 --helper module ...                Handlebars helper modules to override or extend the default set.                                                                                                                                                                                                                                                                                                                                                                                                              
 --partial file ...                 Handlebars partial files to override or extend the default set.                                                                                                                                                                                                                                                                                                                                                                                                               
 -l, --example-lang string          Specifies the default language used in @example blocks (for syntax-highlighting purposes). In the default gfm mode, each @example is wrapped in a fenced-code block. Example usage: --example-lang js. Use the special value none for no specific language. While using this option, you can override the supplied language for any @example by specifying the @lang subtag, e.g @example @lang hbs. Specifying @example @lang off will disable code blocks for that example. 
 --name-format                      Format identifier names as code (i.e. wrap function/property/class etc names in backticks).                                                                                                                                                                                                                                                                                                                                                                                   
 --no-gfm                           By default, dmd generates github-flavoured markdown. Not all markdown parsers render gfm correctly. If your generated docs look incorrect on sites other than Github (e.g. npmjs.org) try enabling this option to disable Github-specific syntax.                                                                                                                                                                                                                             
 --separators                       Put <hr> breaks between identifiers. Improves readability on bulky docs.                                                                                                                                                                                                                                                                                                                                                                                                      
 -m, --module-index-format string   When muliple modules are found in the input source code, an index is generated. It can be styled by one of the following options: none, grouped, table or dl.                                                                                                                                                                                                                                                                                                                 
 -g, --global-index-format string   When muliple global-scope identifiers are found in the input source code, an index is generated. It can be styled by one of the following options: none, grouped, table or dl.                                                                                                                                                                                                                                                                                                
 -p, --param-list-format string     Two options to render @param lists: list or table (default). Table format works well in most cases but switch to list if things begin to look crowded.                                                                                                                                                                                                                                                                                                                        
 -r, --property-list-format string  Two options to render @property lists: list or table (default).                                                                                                                                                                                                                                                                                                                                                                                                               
 --member-index-format string       Two options to render member lists: list or grouped (default). The list view is loosely-based on the nodejs docs.                                                                                                                                                                                                                                                                                                                                                             
 --clever-links                     By default, all {@link} tags are rendered in plain text. If `--clever-links` is set, URL {@link} tags are rendered in plain text, otherwise monospace.                                                                                                                                                                                                                                                                                                                        
 --monospace-links                  By default, all {@link} tags are rendered in plain text. If `--monospace-links` is set, all links are rendered in monospace format. This setting is ignored if `--clever-links` is set.                                                                                                                                                                                                                                                                                       
 --EOL string                       Specify ether `posix` or `win32`. Forces all line endings in the dmd output to use the specified EOL character.                                                                                                                                                                                                                                                                                                                                                               

  Project repository:   https://github.com/jsdoc2md/jsdoc-to-markdown

---

# ucode module: `uci`

> **Source:** [`lib/uci.c`](https://github.com/jow-/ucode/blob/master/lib/uci.c)
> **Live docs:** https://ucode.mein.io/module-uci.html
> **Generated:** 2026-03-05 18:50 UTC from commit `e87be9d`

---

jsdoc-to-markdown

  Generates markdown documentation from jsdoc-annotated source code. 

Synopsis

  $ jsdoc2md <jsdoc-options> [<dmd-options>] 
  $ jsdoc2md <jsdoc-options> --jsdoc         
  $ jsdoc2md <jsdoc-options> --json          
  $ jsdoc2md <jsdoc-options> --namepaths     
  $ jsdoc2md --help                          
  $ jsdoc2md --config                        

General options

  Main options affecting mode. If none of the following are supplied, the tool  
  will generate markdown docs.                                                  

  -h, --help    Print usage information                                         
  --config      Print all options supplied (from command line, `.jsdoc2md.json` 
                or `package.json` under the `jsdoc2md` property) and exit.      
                Useful for checking the tool is receiving the correct config.   
  --json        Prints the data (jsdoc-parse output) supplied to the template   
                (dmd).                                                          
  --jsdoc       Prints the raw jsdoc data.                                      
  --version                                                                     
  --no-cache    By default, repeat invocations against the same input with the  
                same options returns from cache. This option disables that.     
  --clear       Clears the cache.                                               

jsdoc options

  Options regarding the input source code, passed directly to jsdoc. 

  -f, --files file ...   A list of jsdoc explain files (or glob expressions) to 
                         parse for documentation. Either this or --source must  
                         be supplied.                                           
  --source string        A string containing source code to parse for           
                         documentation. Either this or --files must be          
                         supplied.                                              
  -c, --configure file   Path to a jsdoc configuration file, passed directly to 
                         `jsdoc -c`.                                            
  --namepaths            Print namepaths.                                       

dmd

  These options affect how the markdown output looks. 

 -t, --template <file>              A custom handlebars template file to insert documentation into. The default template is `{{>main}}`.                                                                                                                                                                                                                                                                                                                                                                          
 --private                          Include identifiers marked @private in the output                                                                                                                                                                                                                                                                                                                                                                                                                             
 -d, --heading-depth number         Root markdown heading depth, defaults to 2 (##).                                                                                                                                                                                                                                                                                                                                                                                                                              
 --plugin module ...                Use an installed package containing helper and/or partial overrides.                                                                                                                                                                                                                                                                                                                                                                                                          
 --helper module ...                Handlebars helper modules to override or extend the default set.                                                                                                                                                                                                                                                                                                                                                                                                              
 --partial file ...                 Handlebars partial files to override or extend the default set.                                                                                                                                                                                                                                                                                                                                                                                                               
 -l, --example-lang string          Specifies the default language used in @example blocks (for syntax-highlighting purposes). In the default gfm mode, each @example is wrapped in a fenced-code block. Example usage: --example-lang js. Use the special value none for no specific language. While using this option, you can override the supplied language for any @example by specifying the @lang subtag, e.g @example @lang hbs. Specifying @example @lang off will disable code blocks for that example. 
 --name-format                      Format identifier names as code (i.e. wrap function/property/class etc names in backticks).                                                                                                                                                                                                                                                                                                                                                                                   
 --no-gfm                           By default, dmd generates github-flavoured markdown. Not all markdown parsers render gfm correctly. If your generated docs look incorrect on sites other than Github (e.g. npmjs.org) try enabling this option to disable Github-specific syntax.                                                                                                                                                                                                                             
 --separators                       Put <hr> breaks between identifiers. Improves readability on bulky docs.                                                                                                                                                                                                                                                                                                                                                                                                      
 -m, --module-index-format string   When muliple modules are found in the input source code, an index is generated. It can be styled by one of the following options: none, grouped, table or dl.                                                                                                                                                                                                                                                                                                                 
 -g, --global-index-format string   When muliple global-scope identifiers are found in the input source code, an index is generated. It can be styled by one of the following options: none, grouped, table or dl.                                                                                                                                                                                                                                                                                                
 -p, --param-list-format string     Two options to render @param lists: list or table (default). Table format works well in most cases but switch to list if things begin to look crowded.                                                                                                                                                                                                                                                                                                                        
 -r, --property-list-format string  Two options to render @property lists: list or table (default).                                                                                                                                                                                                                                                                                                                                                                                                               
 --member-index-format string       Two options to render member lists: list or grouped (default). The list view is loosely-based on the nodejs docs.                                                                                                                                                                                                                                                                                                                                                             
 --clever-links                     By default, all {@link} tags are rendered in plain text. If `--clever-links` is set, URL {@link} tags are rendered in plain text, otherwise monospace.                                                                                                                                                                                                                                                                                                                        
 --monospace-links                  By default, all {@link} tags are rendered in plain text. If `--monospace-links` is set, all links are rendered in monospace format. This setting is ignored if `--clever-links` is set.                                                                                                                                                                                                                                                                                       
 --EOL string                       Specify ether `posix` or `win32`. Forces all line endings in the dmd output to use the specified EOL character.                                                                                                                                                                                                                                                                                                                                                               

  Project repository:   https://github.com/jsdoc2md/jsdoc-to-markdown

---

# ucode module: `uloop`

> **Source:** [`lib/uloop.c`](https://github.com/jow-/ucode/blob/master/lib/uloop.c)
> **Live docs:** https://ucode.mein.io/module-uloop.html
> **Generated:** 2026-03-05 18:50 UTC from commit `e87be9d`

---

jsdoc-to-markdown

  Generates markdown documentation from jsdoc-annotated source code. 

Synopsis

  $ jsdoc2md <jsdoc-options> [<dmd-options>] 
  $ jsdoc2md <jsdoc-options> --jsdoc         
  $ jsdoc2md <jsdoc-options> --json          
  $ jsdoc2md <jsdoc-options> --namepaths     
  $ jsdoc2md --help                          
  $ jsdoc2md --config                        

General options

  Main options affecting mode. If none of the following are supplied, the tool  
  will generate markdown docs.                                                  

  -h, --help    Print usage information                                         
  --config      Print all options supplied (from command line, `.jsdoc2md.json` 
                or `package.json` under the `jsdoc2md` property) and exit.      
                Useful for checking the tool is receiving the correct config.   
  --json        Prints the data (jsdoc-parse output) supplied to the template   
                (dmd).                                                          
  --jsdoc       Prints the raw jsdoc data.                                      
  --version                                                                     
  --no-cache    By default, repeat invocations against the same input with the  
                same options returns from cache. This option disables that.     
  --clear       Clears the cache.                                               

jsdoc options

  Options regarding the input source code, passed directly to jsdoc. 

  -f, --files file ...   A list of jsdoc explain files (or glob expressions) to 
                         parse for documentation. Either this or --source must  
                         be supplied.                                           
  --source string        A string containing source code to parse for           
                         documentation. Either this or --files must be          
                         supplied.                                              
  -c, --configure file   Path to a jsdoc configuration file, passed directly to 
                         `jsdoc -c`.                                            
  --namepaths            Print namepaths.                                       

dmd

  These options affect how the markdown output looks. 

 -t, --template <file>              A custom handlebars template file to insert documentation into. The default template is `{{>main}}`.                                                                                                                                                                                                                                                                                                                                                                          
 --private                          Include identifiers marked @private in the output                                                                                                                                                                                                                                                                                                                                                                                                                             
 -d, --heading-depth number         Root markdown heading depth, defaults to 2 (##).                                                                                                                                                                                                                                                                                                                                                                                                                              
 --plugin module ...                Use an installed package containing helper and/or partial overrides.                                                                                                                                                                                                                                                                                                                                                                                                          
 --helper module ...                Handlebars helper modules to override or extend the default set.                                                                                                                                                                                                                                                                                                                                                                                                              
 --partial file ...                 Handlebars partial files to override or extend the default set.                                                                                                                                                                                                                                                                                                                                                                                                               
 -l, --example-lang string          Specifies the default language used in @example blocks (for syntax-highlighting purposes). In the default gfm mode, each @example is wrapped in a fenced-code block. Example usage: --example-lang js. Use the special value none for no specific language. While using this option, you can override the supplied language for any @example by specifying the @lang subtag, e.g @example @lang hbs. Specifying @example @lang off will disable code blocks for that example. 
 --name-format                      Format identifier names as code (i.e. wrap function/property/class etc names in backticks).                                                                                                                                                                                                                                                                                                                                                                                   
 --no-gfm                           By default, dmd generates github-flavoured markdown. Not all markdown parsers render gfm correctly. If your generated docs look incorrect on sites other than Github (e.g. npmjs.org) try enabling this option to disable Github-specific syntax.                                                                                                                                                                                                                             
 --separators                       Put <hr> breaks between identifiers. Improves readability on bulky docs.                                                                                                                                                                                                                                                                                                                                                                                                      
 -m, --module-index-format string   When muliple modules are found in the input source code, an index is generated. It can be styled by one of the following options: none, grouped, table or dl.                                                                                                                                                                                                                                                                                                                 
 -g, --global-index-format string   When muliple global-scope identifiers are found in the input source code, an index is generated. It can be styled by one of the following options: none, grouped, table or dl.                                                                                                                                                                                                                                                                                                
 -p, --param-list-format string     Two options to render @param lists: list or table (default). Table format works well in most cases but switch to list if things begin to look crowded.                                                                                                                                                                                                                                                                                                                        
 -r, --property-list-format string  Two options to render @property lists: list or table (default).                                                                                                                                                                                                                                                                                                                                                                                                               
 --member-index-format string       Two options to render member lists: list or grouped (default). The list view is loosely-based on the nodejs docs.                                                                                                                                                                                                                                                                                                                                                             
 --clever-links                     By default, all {@link} tags are rendered in plain text. If `--clever-links` is set, URL {@link} tags are rendered in plain text, otherwise monospace.                                                                                                                                                                                                                                                                                                                        
 --monospace-links                  By default, all {@link} tags are rendered in plain text. If `--monospace-links` is set, all links are rendered in monospace format. This setting is ignored if `--clever-links` is set.                                                                                                                                                                                                                                                                                       
 --EOL string                       Specify ether `posix` or `win32`. Forces all line endings in the dmd output to use the specified EOL character.                                                                                                                                                                                                                                                                                                                                                               

  Project repository:   https://github.com/jsdoc2md/jsdoc-to-markdown

---

# ucode module: `zlib`

> **Source:** [`lib/zlib.c`](https://github.com/jow-/ucode/blob/master/lib/zlib.c)
> **Live docs:** https://ucode.mein.io/module-zlib.html
> **Generated:** 2026-03-05 18:50 UTC from commit `e87be9d`

---

jsdoc-to-markdown

  Generates markdown documentation from jsdoc-annotated source code. 

Synopsis

  $ jsdoc2md <jsdoc-options> [<dmd-options>] 
  $ jsdoc2md <jsdoc-options> --jsdoc         
  $ jsdoc2md <jsdoc-options> --json          
  $ jsdoc2md <jsdoc-options> --namepaths     
  $ jsdoc2md --help                          
  $ jsdoc2md --config                        

General options

  Main options affecting mode. If none of the following are supplied, the tool  
  will generate markdown docs.                                                  

  -h, --help    Print usage information                                         
  --config      Print all options supplied (from command line, `.jsdoc2md.json` 
                or `package.json` under the `jsdoc2md` property) and exit.      
                Useful for checking the tool is receiving the correct config.   
  --json        Prints the data (jsdoc-parse output) supplied to the template   
                (dmd).                                                          
  --jsdoc       Prints the raw jsdoc data.                                      
  --version                                                                     
  --no-cache    By default, repeat invocations against the same input with the  
                same options returns from cache. This option disables that.     
  --clear       Clears the cache.                                               

jsdoc options

  Options regarding the input source code, passed directly to jsdoc. 

  -f, --files file ...   A list of jsdoc explain files (or glob expressions) to 
                         parse for documentation. Either this or --source must  
                         be supplied.                                           
  --source string        A string containing source code to parse for           
                         documentation. Either this or --files must be          
                         supplied.                                              
  -c, --configure file   Path to a jsdoc configuration file, passed directly to 
                         `jsdoc -c`.                                            
  --namepaths            Print namepaths.                                       

dmd

  These options affect how the markdown output looks. 

 -t, --template <file>              A custom handlebars template file to insert documentation into. The default template is `{{>main}}`.                                                                                                                                                                                                                                                                                                                                                                          
 --private                          Include identifiers marked @private in the output                                                                                                                                                                                                                                                                                                                                                                                                                             
 -d, --heading-depth number         Root markdown heading depth, defaults to 2 (##).                                                                                                                                                                                                                                                                                                                                                                                                                              
 --plugin module ...                Use an installed package containing helper and/or partial overrides.                                                                                                                                                                                                                                                                                                                                                                                                          
 --helper module ...                Handlebars helper modules to override or extend the default set.                                                                                                                                                                                                                                                                                                                                                                                                              
 --partial file ...                 Handlebars partial files to override or extend the default set.                                                                                                                                                                                                                                                                                                                                                                                                               
 -l, --example-lang string          Specifies the default language used in @example blocks (for syntax-highlighting purposes). In the default gfm mode, each @example is wrapped in a fenced-code block. Example usage: --example-lang js. Use the special value none for no specific language. While using this option, you can override the supplied language for any @example by specifying the @lang subtag, e.g @example @lang hbs. Specifying @example @lang off will disable code blocks for that example. 
 --name-format                      Format identifier names as code (i.e. wrap function/property/class etc names in backticks).                                                                                                                                                                                                                                                                                                                                                                                   
 --no-gfm                           By default, dmd generates github-flavoured markdown. Not all markdown parsers render gfm correctly. If your generated docs look incorrect on sites other than Github (e.g. npmjs.org) try enabling this option to disable Github-specific syntax.                                                                                                                                                                                                                             
 --separators                       Put <hr> breaks between identifiers. Improves readability on bulky docs.                                                                                                                                                                                                                                                                                                                                                                                                      
 -m, --module-index-format string   When muliple modules are found in the input source code, an index is generated. It can be styled by one of the following options: none, grouped, table or dl.                                                                                                                                                                                                                                                                                                                 
 -g, --global-index-format string   When muliple global-scope identifiers are found in the input source code, an index is generated. It can be styled by one of the following options: none, grouped, table or dl.                                                                                                                                                                                                                                                                                                
 -p, --param-list-format string     Two options to render @param lists: list or table (default). Table format works well in most cases but switch to list if things begin to look crowded.                                                                                                                                                                                                                                                                                                                        
 -r, --property-list-format string  Two options to render @property lists: list or table (default).                                                                                                                                                                                                                                                                                                                                                                                                               
 --member-index-format string       Two options to render member lists: list or grouped (default). The list view is loosely-based on the nodejs docs.                                                                                                                                                                                                                                                                                                                                                             
 --clever-links                     By default, all {@link} tags are rendered in plain text. If `--clever-links` is set, URL {@link} tags are rendered in plain text, otherwise monospace.                                                                                                                                                                                                                                                                                                                        
 --monospace-links                  By default, all {@link} tags are rendered in plain text. If `--monospace-links` is set, all links are rendered in monospace format. This setting is ignored if `--clever-links` is set.                                                                                                                                                                                                                                                                                       
 --EOL string                       Specify ether `posix` or `win32`. Forces all line endings in the dmd output to use the specified EOL character.                                                                                                                                                                                                                                                                                                                                                               

  Project repository:   https://github.com/jsdoc2md/jsdoc-to-markdown

---

