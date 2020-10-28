<template>
  <div class="vue-wrapper">
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: "app"
};
</script>

<style lang="sass">
@import '../../static/sass/app'
body
  color: red
</style>
