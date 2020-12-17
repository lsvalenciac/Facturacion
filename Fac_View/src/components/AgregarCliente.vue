<template>
  <div class="center">
    <h2>Agregar cliente</h2>

    <label for="">Cédula</label>
    <vs-input
      primary
      v-model="cedula"/>
    
    <label for="">Nombre</label>
    <vs-input
    primary
    v-model="nombre"/>
    <label for="">Apellido</label>
    <vs-input
    primary
    v-model="apellido"/> 
    <label for="">Teléfono</label>
    <vs-input
    primary
    v-model="telefono"/>
    <label for="">Email</label>
    <vs-input
    primary
    v-model="email"/>
    <label for="">Dirección</label>
    <vs-input
    primary
    v-model="direccion"/>
    <vs-button v-on:click="agregarCliente">
       Agregar Cliente
       <template #animate >
       <i class='bx bx-check-double' ></i>
       </template>
     </vs-button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "AgregarCliente",
  data: function() {
    return {
      cedula: "",
      nombre: "",
      apellido:"",
      telefono:"",
      email:"",
      direccion: ""
    };
  },
  methods: {
    agregarCliente: function() {
      var datosJson = {
        cedula: this.cedula,
        nombre: this.nombre,
        apellido: this.apellido,
        telefono: this.telefono,
        email: this.email,
        direccion: this.direccion
      };
      axios
        .post("http://127.0.0.1:8000/clientes/agregar/", datosJson)
        .then(response => {
          alert(response.data.mensaje);
        })
        .catch(err => {
          console.log(err);
          alert("error en el servidor");
        });
    }
  }
};
</script>

<style>
  .vs-input{
  padding: 0 1rem;
  margin: 1rem;
  width: 200px;
  margin-left: auto;
  margin-right: auto;
}

    
  .vs-button{
  padding: 0 1rem;
  margin: 1rem;
  width: 200px;
  margin-left: auto;
  margin-right: auto;
}
</style>