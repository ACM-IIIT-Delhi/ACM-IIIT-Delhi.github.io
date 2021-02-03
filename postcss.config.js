const tailwindcss = require('tailwindcss')
const purgecss = require('@fullhuman/postcss-purgecss')
const cssnano = require('cssnano')
const autoprefixer = require('autoprefixer')

class TailwindExtractor {
    static extract(content) {
        return content.match(/[^<>"'`\s]*[^<>"'`\s:]/g) || [];
    }
}

module.exports = {
    plugins: [
        tailwindcss('./tailwind.js'),
        cssnano({
            preset: 'default',
        }),
        purgecss({
            content: ['./src/*.html'],
            defaultExtractor: content => content.match(/[\w-:/]+(?<!:)/g) || []
        }),
        autoprefixer
    ]
}