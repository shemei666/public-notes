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
                            node.tagName = 'script'
                            node.properties['type'] = "text/tikz"
                            node.children = node.children[0].children
                        }
                    })
                }
            }]
        },
        externalResources() {
            return {
                css: [{ content: 'https://tikzjax.com/v1/fonts.css' }],
                js: [{
                    src: 'https://tikzjax.com/v1/tikzjax.js',
                    loadTime: "afterDOMReady",
                    contentType: "external",
                }]
            }
        }

    }
}