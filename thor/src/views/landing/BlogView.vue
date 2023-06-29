<template>
  <header>
    <Header></Header>
  </header>
  <MobileMenu></MobileMenu>
  <main>
    <Blog></Blog>
  </main>
  <footer>
      <Footer></Footer>
  </footer>
</template>

<script>
import Blog from '../../components/BlogMain.vue'
import Header from "@/components/NavHeader.vue";
import MobileMenu from "@/components/MobileMenu.vue";
import Footer from "@/components/NavFooter.vue";

export default {
  name: 'App',
  components: {
    Footer, MobileMenu,
    Header, Blog,
  }
}
</script>

<style>

</style>