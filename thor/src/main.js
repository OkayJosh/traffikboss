import 'bootstrap-icons/font/bootstrap-icons.min.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import AOS from 'aos';
import 'aos/dist/aos.css';
import { createApp } from 'vue';
import App from './App.vue';
import router from './routers/router';

// Initialize AOS
AOS.init();

createApp(App)
    .use(router)
    .mount('#app');