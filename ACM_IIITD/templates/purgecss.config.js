module.exports = {
    content: ['src/*.html'],
    css: ['src/css/main.css'],
    defaultExtractor: (content) => content.match(/[\w-/:]+(?<!:)/g) || [],
    output: '/dist/tailwind.css',
};