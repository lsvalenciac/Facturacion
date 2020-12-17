import VueRouter from "vue-router";
import ListarCliente from "./components/ListarCliente";
import AgregarCliente from "./components/AgregarCliente";
import App from './App';

const router = new VueRouter({
  routes: [
    { name: "verClientes", path: "/ver", component: ListarCliente},
    {
      name: "agregarCliente",
      path: "/agregar",
      component: AgregarCliente
    }
  ]
});

export default router;