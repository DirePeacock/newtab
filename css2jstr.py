import os
import pathlib
if __name__ == "__main__":
    '''use python to inject get local css into a string for js to inject it across domains into iframe
    
    editing css in a .css file is more pleasant than tryring to get a IDE to understand I'm writing CSS in this .js file.
    just run this to regen the js when I need it
    '''

    basedir = pathlib.Path(__file__).parent.absolute()
    cssfp = basedir / 'css' / 'todo-dark.css'
    jsfp = basedir / 'script' / 'todo-dark-css-str.js'

    BIGSTRING = ""

    with open(str(cssfp), 'r') as cssfile:
        for line in cssfile.readlines():
            BIGSTRING = BIGSTRING + ' ' + line.rstrip()

    jsfuncstr = """
    window.onload = function() {{
        let frameElement = document.getElementById("myiFrame");
        let doc = frameElement.contentDocument;
        doc.body.innerHTML = doc.body.innerHTML + '<style>{0}</style>';
    }}""".format(BIGSTRING)
    with open(str(jsfp), 'w') as jsfile:
        jsfile.write(jsfuncstr)
