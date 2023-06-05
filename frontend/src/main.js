import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios';

axios.defaults.baseURL = 'http://localhost:8000'; // Actualiza esto con la URL del backend



createApp(App).mount('#app')