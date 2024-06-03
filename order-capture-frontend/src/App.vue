<template>
  <div id="app">
    <OrderForm />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import OrderForm from './components/OrderForm.vue'

export default defineComponent({
  components: {
    OrderForm,
  },
})
</script>

<style>
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}
</style>
