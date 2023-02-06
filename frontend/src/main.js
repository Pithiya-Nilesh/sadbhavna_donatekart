import { createApp } from 'vue'
import { FrappeUI, Button } from 'frappe-ui'
import router from './router'
import App from './App.vue'
import './index.css'
import { createToast, clearToasts } from "@/utils/toasts"
import axios from 'axios';
// import "@fortawesome/fontawesome-free/css/all.min.css";
import "@/assets/Inter/styles/tailwind.css"

// import VueSession from "vue-session";


// import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap-vue/dist/bootstrap-vue.css'

// import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
// import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap-vue/dist/bootstrap-vue.css'

// import VueCardStack from "vue-card-stack";
// app.use(VueSession);

let app = createApp(App)
app.use(router)
app.use(FrappeUI)
// app.use(BootstrapVue)
// app.use(IconsPlugin)
// app.use(Vuetify)
app.component('Button', Button)
app.config.globalProperties.$toast = createToast
app.config.globalProperties.$clearToasts = clearToasts
app.mount('#app')

