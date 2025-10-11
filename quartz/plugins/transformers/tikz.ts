import { QuartzTransformerPlugin } from "../types";
import { visit } from "unist-util-visit"

export const Tikz: QuartzTransformerPlugin = () => {
    return {
        name: "Tikz",
        htmlPlugins() {
            return [() => {
                return (tree, file) => {
                    visit(tree, 'element', (node) => {
                        if (node.tagName === 'pre' &&
                            node.children?.[0]?.properties?.className?.includes('language-tikz')) {
                            node.tagName = 'div'
                            node.properties.className = ["tikzblock"]
                            node.children[0].tagName = "script"
                            node.children[0].properties.type = "text/tikz"
                            node.children[0].properties["data-width"] = 50
                            node.children[0].properties["data-height"] = 50
                        }
                    })
                }
            }]
        },
        externalResources() {
            return {
                css: [{ content: 'https://shemei666.github.io/public-notes/static/css/styles.css' }],
                js: [{
                    src: 'https://shemei666.github.io/public-notes/static/js/tikzjax.js',
                    loadTime: "beforeDOMReady",
                    contentType: "external",
                }]
            }
        }

    }
}