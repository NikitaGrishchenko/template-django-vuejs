<template>
  <div class="vue-wrapper">
    <slot></slot>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "app",
  data() {
    return {
      todos: null
    };
  },

  created() {
    axios
      .get("www/")
      .then(response => {
        this.todos = response.data;
        console.log(this.todos);
      })
      .catch(error => console.log(error));
  }
};
</script>

<style lang="sass">
@import '../../sass/app'
</style>
