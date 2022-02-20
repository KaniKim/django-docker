import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import KakaoLogin from "../views/KakaoLogin.vue";
const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/login",
    name: "login",
    compoenet: KakaoLogin
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
