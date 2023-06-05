<template>
  <div>
    <MyItems></MyItems>
  </div>
</template>

<script>
import MyItems from './components/MyItems.vue'

export default {
  name: 'App',
  components: {
    MyItems
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
