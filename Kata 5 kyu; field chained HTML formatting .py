# We want to create an object with methods for various HTML elements: 
# div, p, span and h1 for the sake of this Kata.

# These methods will wrap the passed-in string in the tag associated 
# with each.

# Format.div("foo"); # returns "<div>foo</div>"
# Format.p("bar"); # returns "<p>bar</p>"
# Format.span("fiz"); # returns "<span>fiz</span>"
# Format.h1("buz"); # returns "<h1>buz</h1>"

# We also want to be able to add additional formatting by chaining our 
# methods together.

# Format.div.h1("FooBar");
# # "<div><h1>FooBar</h1><div>"

# Format.div.p.span("FizBuz");
# # "<div><p><span>FizBuz</span></p></div>"

# and so on, as deep as we care to use.

# Multiple arguments should be concatenated and wrapped in the correct 
# HTML formatting.

# Format.div.h1("Foo", "Bar");
# # "<div><h1>FooBar</h1></div>"

# We should be able to store the created methods and reuse them.

# wrapInDiv = Format.div;
# wrapInDiv("Foo");   # "<div>Foo</div>"
# wrapInDiv.p("Bar"); # "<div><p>Bar</p></div>"

# wrapInDivH1 = Format.div.h1;
# wrapInDivH1("Far"); # "<div><h1>Far</h1></div>"
# wrapInDivH1.span("Bar"); # "<div><h1><span>Bar</span></h1></div>"

# And finally, we should be able to nest Format calls.

# Format.div(
#   Format.h1("Title"), 
#   Format.p(f"Paragraph with a {Format.span('span')}.")
# )
# # returns "<div><h1>Title</h1><p>Paragraph with a <span>span</span>.
# </p></div>"

class HTMLConc:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        
    @property
    def h1(self):
        return HTMLConc('h1', self)
    
    @property
    def div(self):
        return HTMLConc('div', self)
            
    @property
    def span(self):
        return HTMLConc('span', self)
                
    @property
    def p(self):
        return HTMLConc('p', self)
    
    def __call__(self, *args):
        concHTML = "".join(args)
        if (self.parent is None):
            return concHTML
        return self.parent(f'<{self.name}>{concHTML}</{self.name}>')
    
Format = HTMLConc('', None)