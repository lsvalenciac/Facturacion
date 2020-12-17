<template>
  <div id="contendio">

    <h2 v-if="variableBooleana">Lista de sus clientes</h2>
    <table>
      <tr>
        <th>Cédula del cliente</th>
        <th>Nombre del cliente</th>
        <th>Apellido del cliente</th>
        <th>Teléfono del cliente</th>
        <th>E-mail del cliente</th>
        <th>Dirección del cliente</th>
      </tr>

      <tr v-for="cliente in lista_clientes">
        <td>{{ cliente.cedula }}</td>
        <td>{{ cliente.nombre }}</td>
        <td>{{ cliente.apellido }}</td>
        <td>{{ cliente.telefono }}</td>
        <td>{{ cliente.email }}</td>
        <td>{{ cliente.direccion }}</td>
      </tr>
    </table>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "verClientes",
  data: function() {
    return {
      variableBooleana: true,
      lista_clientes: []
    };
  },
  beforeCreate: function() {
    axios
      .get("http://127.0.0.1:8000/clientes/lista")
      .then(response => {
        this.lista_clientes = response.data;
      })
      .catch(error => {
        console.log(error);
        alert("Error del servidor");
      });
  }
};
</script>

<style scoped>

table,
th,
td {
  border: 0.2px solid rgb(96, 109, 187);
}
table {
  margin: auto;
}

  .header h2{
    width: 50%;
    text-align:right;
    position: relative;

    }
</style>