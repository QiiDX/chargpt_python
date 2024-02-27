import {marked} from 'marked'
import hljs from 'highlight.js'
import 'highlight.js/styles/atom-one-dark.css'

function renderMessageContent(msg: any) {
        marked.setOptions({
            renderer: new marked.Renderer(),
            highlight: function (code, _lang) {
                return hljs.highlightAuto(code).value;
            },
            langPrefix: 'hljs language-',
            pedantic: false,
            gfm: true,
            breaks: false,
            sanitize: false,
            smartypants: false,
            xhtml: false
          })
        const { content } = msg;

         let html = marked(content.text)
         return <div className="show-html" dangerouslySetInnerHTML={{ __html: html }}></div>

    }