// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import Vuesax from 'vuesax';
import "vuesax/dist/vuesax.css";
import router from "./router";
import VueRouter from "vue-router";
import 'boxicons';


Vue.config.productionTip = false
Vue.use(VueRouter);
Vue.use(Vuesax);
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})