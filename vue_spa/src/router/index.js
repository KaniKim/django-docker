import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import NestedComponent from "../views/NestedComponent.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/nested",
    name: "nested",
    component: NestedComponent
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
