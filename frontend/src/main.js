import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import components from '@/components/UI'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'

loadFonts()

const app = createApp(App)

components.forEach(component => {
    app.component(component.name, component)
})

app.use(router)
    .use(vuetify)
    .mount('#app')
