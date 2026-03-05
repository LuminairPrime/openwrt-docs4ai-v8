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