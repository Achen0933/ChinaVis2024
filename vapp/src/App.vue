<template>
    <div>
      <button @click="toggleView" class="toggle-button">切换大屏</button>
      <router-view/>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      toggleView() {
        if (this.$route.name === 'view1') {
          this.$router.push({ name: 'view2' });
        } else {
          this.$router.push({ name: 'view1' });
        }
      }
    }
  }
  </script>
  
  <style scoped>
  .toggle-button {
    position: fixed;
    top: 10px;
    right: 10px;
    z-index: 1000; /* 确保按钮在最前面 */
    padding: 10px 10px;
    background-color: #516b91;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .toggle-button:hover {
    background-color: #93b7e3;
  }
  </style>
  