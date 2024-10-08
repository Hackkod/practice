module.exports = {
    root: true,
    env: {
        browser: true,
        node: true,
    },
    extends: [
        'plugin:vue/vue3-strongly-recommended',
        'eslint:recommended',
        'prettier'
    ],
    parserOptions: {
        ecmaVersion: 2020,
    },
    rules: {
        'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
        'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    },
}