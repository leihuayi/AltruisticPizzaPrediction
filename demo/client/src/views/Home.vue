<template>
  <div class="home">
    <img id="raop-logo" src="../assets/raopdemo.png" alt="Random Acts of Pizza logo">
    <UploadRequest />
  </div>
</template>

<script>
// @ is an alias to /src
import UploadRequest from '@/components/UploadRequest.vue'

export default {
  name: 'Home',
  components: {
    UploadRequest
  }
}
</script>


<style scoped>
    #raop-logo {
        margin: 30px
    }

</style>