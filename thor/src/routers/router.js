import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '@/views/landing/HomeView.vue';
import ContactUsView from '@/views/landing/ContactUsView.vue';
import PricesView from '@/views/landing/PricesView.vue';
import LoginView from '@/views/landing/LoginView.vue';
import RegisterView from '@/views/landing/RegisterView.vue';
import HelpCenterView from "@/views/landing/HelpCenterView.vue";
import BlogView from "@/views/landing/BlogView.vue";
import PasswordForgot from "@/views/landing/PasswordForgot.vue";
import PasswordForgotDone from "@/views/landing/PasswordForgotDone.vue";
import DashBoardIndexView from "@/views/dashboard/IndexView.vue";

const routes = [
  { path: '/', name: "home", component: HomeView },
  { path: '/support', name: "support", component: HelpCenterView },
  { path: '/prices', name: "about", component: PricesView },
  { path: '/contact', name: "contact-us", component: ContactUsView },
  { path: '/register', name: "register", component: RegisterView },
  { path: '/login', name: "login", component: LoginView },
  { path: '/blog', name: "blog", component: BlogView },
  { path: '/forgot-password', name: "forgot-password", component: PasswordForgot },
  { path: '/forgot-password-done', name: "forgot-password-done", component: PasswordForgotDone },
  { path: '/dashboard', name: "dashboard", component: DashBoardIndexView },
  { path: '/logout', name: "logout", component: DashBoardIndexView },
  { path: '/settings', name: "settings", component: DashBoardIndexView },
  { path: '/schedule', name: "schedule", component: DashBoardIndexView },
  { path: '/contents', name: "contents", component: DashBoardIndexView },
  { path: '/notifications', name: "notifications", component: DashBoardIndexView },
];

const router = createRouter({
  history: createWebHistory("/"),
  routes,
});

export default router;
