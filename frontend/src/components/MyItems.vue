<template>
  <div class="container">
    <h1 style="text-align: left">Items</h1>
    <div class="form-inline">
      <form class="form-inline" @submit.prevent="createItem">
        <div class="form-group mb-2">
          <label for="name" class="sr-only">Nombre</label>
          <input
            class="m-1 form-control"
            v-model="newItem.name"
            placeholder="Nombre"
            id="name"
            required
          />
        </div>
        <div class="form-group mx-sm-3 mb-2">
          <label for="description" class="sr-only">Descripción</label>
          <input
            class="form-control"
            v-model="newItem.description"
            placeholder="Descripción"
            id="description"
            required
          />
        </div>
        <button class="btn btn-success mb-2 mx-sm-1" type="submit">Crear</button>
      </form>
    </div>
    <div class="form-inline">
        <div class="form-group mb-2">

            <input class=" m-1 form-control mb-2"
              v-model="searchTerm"
              type="text"
              placeholder="Buscar"
              id="buscar"
              @input="searchItem"
            />
            <button @click=limpiarBusqueda() class="btn btn-info mx-sm-3 mb-2" id="btn-limpiar">Limpiar</button>
        </div>
    </div>
<div class="overTable">

    <table class="table table-dark table-striped mt-2">
      <thead class="thSticky">
        <tr>
          <th>Nombre</th>
          <th>Descripción</th>
          <th></th>
        </tr>
      </thead>
      <tbody  id="items">
        <tr v-for="item in items" :key="item.id">
          <td>{{ item.name }}</td>
          <td>{{ item.description }}</td>
          <td>
            <button class="btn btn-danger" @click="deleteItem(item.id)">
              Borrar
            </button>
          </td>
        </tr>
      </tbody>
    </table>
</div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      items: [],
      newItem: {
        name: "",
        description: "",
      },
      searchTerm: "",
    };
  },
  mounted() {
    this.searchItem();
  },
  methods: {
    loadItems() {
      axios.get("/items").then((response) => {
        this.items = response.data;
      });
    },
    createItem() {
      axios.post("/items", this.newItem).then((response) => {
        this.items.push(response.data);
        this.newItem.name = "";
        this.newItem.description = "";
      });
    },
    deleteItem(itemId) {
      axios.delete(`/items/${itemId}`).then(() => {
        this.items = this.items.filter((item) => item.id !== itemId);
      });
    },
    searchItem() {
      clearTimeout(this.timer); // Limpiar el temporizador anterior (si existe)
      this.timer = setTimeout(() => {
        axios
          .get("/items", {
            params: { search: this.searchTerm },
          })
          .then((response) => {
            this.items = response.data;
          });
      }, 300);
      
    },
    limpiarBusqueda(){
        this.searchTerm = ''
        this.searchItem()
    }
  },
};
</script>
