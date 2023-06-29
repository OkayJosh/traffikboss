<template>
  <header>
    <Header></Header>
  </header>
  <MobileMenu></MobileMenu>
  <main>
    <PriceMain></PriceMain>
  </main>
  <footer>
      <Footer></Footer>
  </footer>
</template>

<script>
import PriceMain from '@/components/Pricing.vue'
import Header from "@/components/NavHeader.vue";
import MobileMenu from "@/components/MobileMenu.vue";
import Footer from "@/components/NavFooter.vue";

export default {
  name: 'App',
  components: {
    Footer, MobileMenu, Header,
    PriceMain,
  }
}
</script>

<style scoped>
@import "@/assets/static/css/styles/globalstyles.css";
@import "@/assets/static/css/styles/nav.css";
@import "@/assets/static/css/styles/component.css";
@import "@/assets/static/css/styles/footer.css";

.hero-section {
  --green: #eafcfc;
  background-color: var(--green);
  margin-bottom: 3rem;
}

.hero-section-inner {
  padding: 6rem 0;
  row-gap: 4rem;
}

.hero-section-inner .content {
  text-align: center;
}
</style>
