<template>
    <div class="header-inner">
      <div class="container p-0">
        <div class="row col-12 align-items-center justify-content-between m-0">
          <div class="p-0 col-5 col-md-7">
            <div class="logo-et-nav-links">
              <div class="logo">
                <router-link to="/" class="traffikboss-logo"><img src="../assets/static/images/logo.png" alt="" class="traffikboss-logo" /></router-link>
              </div>
              <ul class="nav-links d-none d-lg-inline-flex gap-3">
                <li>
                  <router-link to="/prices" class="">Prices</router-link>
                </li>
                <li>
                  <router-link to="/blog" class="">Blogs</router-link>
                </li>
                <li>
                  <router-link to="/contact" class="">Contact Us</router-link>
                </li>
              </ul>
            </div>
          </div>
          <div class="p-0 col-5 col-md-5 text-end">
            <ul class="auth-link">
              <div class="auth-link-inner d-none d-lg-inline-flex">
                <li class="each-auth-link">
                  <router-link to="/login" class="login">Log In</router-link>
                </li>
                <li class="each-auth-link">
                  <router-link to="/register" class="register">register</router-link>
                </li>
              </div>
              <div class="d-lg-none">
                <button
                  type="button"
                  data-bs-toggle="offcanvas"
                  data-bs-target="#offcanvasExample"
                  aria-controls="offcanvasExample">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="32"
                    height="32"
                    preserveAspectRatio="xMidYMid meet"
                    viewBox="0 0 32 32">
                    <path
                      fill="none"
                      stroke="currentColor"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M4 8h24M4 16h24M4 24h24" />
                  </svg>
                </button>
              </div>
            </ul>
          </div>
        </div>
      </div>
    </div>
</template>
<script setup>
</script>