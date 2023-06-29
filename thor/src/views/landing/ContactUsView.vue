<template>
  <header>
    <Header></Header>
  </header>
  <MobileMenu></MobileMenu>
  <main>
    <ContactUs></ContactUs>
  </main>
  <footer>
      <Footer></Footer>
  </footer>
</template>

<script>
import ContactUs from '@/components/ContactUs.vue'
import Header from "@/components/NavHeader.vue";
import MobileMenu from "@/components/MobileMenu.vue";
import Footer from "@/components/NavFooter.vue";

export default {
  name: 'App',
  components: {
    Footer, MobileMenu, Header,
    ContactUs,
  }
}
</script>

<style scoped>
@import "@/assets/static/css/styles/globalstyles.css";
@import "@/assets/static/css/styles/nav.css";
@import "@/assets/static/css/styles/component.css";
@import "@/assets/static/css/styles/footer.css";
@import "@/assets/static/css/styles/contact.css";
</style>
