<template>
  <div id="app">
    
  <div class="header">
    <h1>FactApp4</h1>
    
    <img src="./assets/logo.svg" width="110px">
  </div>
  <div class="main-component">
  <Index/>
  </div>

</div>

</template>

<script>

import Index from './components/Index';
import ListarCliente from "./components/ListarCliente";


export default {
  name: 'App',
  components: {
    Index 
  },
  data: function(){
    return {
      is_auth: localStorage.getItem('isAuth') || false
}
},
  methods: {
    navegarClientes: function() {
    this.$router.push({ name: "verClientes" });
    }
  },
  
}
</script>

<style>
  body{
    margin: 0 0 0 0;
  }
  .header{
    margin: 0;
    padding: 0;
    width: 100%;
    height: 20vh;
    min-height: 100px;
    background-color: #4d4d4d ;
    color:#ffffff ;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: -20px;
}
  .header h1{
    width: 20%;
    text-align:right;
    }
  .main-component{
    text-align:center;
    height: 130vh;
    padding: 0%;
    background: #2d2d2d ;
    color:#ffffff 
}
</style>

