import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import DataBindingList2 from "../views/DataBindingList2.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/databinding",
    name: "databindings",
    component: DataBindingList2
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
