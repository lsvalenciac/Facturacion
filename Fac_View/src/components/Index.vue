 <template>
    <div class="hidden">
      <link href='https://unpkg.com/boxicons@2.0.7/css/boxicons.min.css' rel='stylesheet'>
      <vs-sidebar
        background="dark"
        textWhite
        absolute
        hover-expand
        reduce
        v-model="active"
        open
        >
        <template #logo>
          <!-- ...img logo -->
        </template>
        <vs-sidebar-item id="inicio">
          <template #icon>
            <i class='bx bx-home-alt'></i>
          </template>
          Inicio
        </vs-sidebar-item>

        <vs-sidebar-group>
          <template #header>
            <vs-sidebar-item arrow>
              <template #icon>
                <i class='bx bx-group'></i>
              </template>
              Usuarios
            </vs-sidebar-item>
          </template>

          <vs-sidebar-item id="door-open">
            <template #icon>
              <i class='bx bx-door-open'></i>
            </template>
            Iniciar sesión
          </vs-sidebar-item>
          <vs-sidebar-item id="check-double">
            <template #icon>
              <i class='bx bx-check-double' ></i>
            </template>
            Crear usuario
          </vs-sidebar-item>
          <vs-sidebar-item id="x">
            <template #icon>
              <i class='bx bx-x' ></i>
            </template>
            Eliminar usuario
          </vs-sidebar-item>
          <vs-sidebar-item id="list-check">
            <template #icon>
              <i class='bx bx-list-check' ></i>
            </template>
            Listar usuarios
          </vs-sidebar-item>
        </vs-sidebar-group>
        <vs-sidebar-group>
          <template #header>
            <vs-sidebar-item arrow>
              <template #icon>
                <i class='bx bxs-id-card' ></i>
              </template>
              Clientes
            </vs-sidebar-item>
          </template>

          <vs-sidebar-item id="navegarClientes" v-on:click="navegarClientes">
            <template #icon>
              <i class='bx bx-list-check'></i>
            </template>
            <a @click="navegarClientes">Listar clientes </a>
            </vs-sidebar-item>
          <vs-sidebar-item id="search-alt">
            <template #icon>
              <i class='bx bx-search-alt'></i>
            </template>
            Buscar clientes 
          </vs-sidebar-item>
          <vs-sidebar-item id="check-double">
            <template #icon>
              <i class='bx bx-check-double'></i>
            </template>
            <a @click="navegarAgregarCliente">Crear clientes </a>
          </vs-sidebar-item>
          <vs-sidebar-item id="x">
            <template #icon>
              <i class='bx bx-x' ></i>
            </template>
            Eliminar clientes
          </vs-sidebar-item>
          <vs-sidebar-item id="paint">
            <template #icon>
              <i class='bx bxs-paint' ></i>
            </template>
            Modificar clientes
          </vs-sidebar-item>
        </vs-sidebar-group>
        <vs-sidebar-item id="paper-plane">
          <template #icon>
            <i class='bx bxs-paper-plane' ></i>
          </template>
          Proveedores
        </vs-sidebar-item>
        <vs-sidebar-item id="plus">
          <template #icon>
            <i class='bx bx-plus'></i>
          </template>
          Facturas
        </vs-sidebar-item>
        <vs-sidebar-item id="shopping">
          <template #icon>
            <i class='bx bxs-shopping-bags'></i>
          </template>
          Tiendas
        </vs-sidebar-item>
        <template #footer>
          <vs-row justify="space-between">
            
              <i class='bx bx-bell' ></i>

              <template #badge>
                28
              </template>
          
          </vs-row>
        </template>
      </vs-sidebar>
      <router-view />
    </div>
  </template>
  <script>
  export default {
    data:() => ({
      active: 'home',
    }),

  methods: {
    navegarClientes: function() {
      this.$router.push({ name: "verClientes" });
    },
    navegarAgregarCliente: function() {
      this.$router.push({ name: "agregarCliente" });
    }
  },

  }
  </script>
  
  <style>
  </style>