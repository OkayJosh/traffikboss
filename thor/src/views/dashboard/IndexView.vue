<template>
<!-- PC VIEW-->
  <div class="">
    <div class="">
      <SideBar></SideBar>
          <!-- content start -->
      <DashBoardMain></DashBoardMain>
      <!-- end content start -->
    </div>
  </div>

  <!-- END OF PC VIEW -->
    <!--      mobile-start-->
    <DashboardMobile></DashboardMobile>
    <!--      mobile-end-->
</template>
<script>
import SideBar from "@/components/SideBar.vue";
import DashBoardMain from "@/components/DashBoardMain.vue";
import DashboardMobile from "@/components/DashboardMobile.vue";
export default {
  name: 'App',
  components: {
    DashboardMobile,
    DashBoardMain,
    SideBar,
  }
}
</script>

<style scoped>
@import "@/assets/static/css/styles/globalstyles.css";
@import "@/assets/static/css/users-styles/layout.css";
@import "@/assets/static/css/users-styles/user-index.css";
/*.wrapper {*/
/*  background-color: red;*/
/*  height: 100vh !important;*/
/*}*/

/*.wrapper-inner {*/
/*	min-height: 100%;*/
/*	position: relative;*/
/*	display: flex;*/
/*	//align-items: center;*/
/*	width: 100%;*/
/*}

 .wrapper-inner {
    min-height: 100%;
    position: relative;
    width: 70%;*/
</style>