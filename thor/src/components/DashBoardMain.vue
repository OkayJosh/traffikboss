<template>
<!--  <div class="col-md-3 page-content p-0"></div>-->
  <div class="page-content">
      <div class="page-content-inner">
        <!-- topper -->
        <div class="topper">
          <!-- title -->
          <div class="title">
            <div class="d-none d-md-inline-flex"><h1>Dashboard</h1></div>
            <div class="mobile-menu-toggler d-md-none">
              <button
                type="button"
                data-bs-toggle="offcanvas"
                data-bs-target="#offcanvasWithBothOptions"
                aria-controls="offcanvasWithBothOptions">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="32"
                  height="32"
                  preserveAspectRatio="xMidYMid meet"
                  viewBox="0 0 32 32">
                  <g transform="translate(32 0) scale(-1 1)">
                    <path
                      fill="none"
                      stroke="currentColor"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M4 8h24M4 16h24M4 24h24" />
                  </g>
                </svg>
              </button>
              <router-link to="/dashboard" class="mobile-logo">
                <img src="../assets/static/images/logo.png" alt="" class="img-fluid" />
              </router-link>
            </div>
          </div>
          <!-- title ends -->
          <!-- notification starts -->
          <div class="notify-user">
            <button>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="32"
                height="32"
                preserveAspectRatio="xMidYMid meet"
                viewBox="0 0 16 16">
                <g transform="translate(16 0) scale(-1 1)">
                  <path
                    fill="currentColor"
                    d="M8 16a2 2 0 0 0 2-2H6a2 2 0 0 0 2 2zM8 1.918l-.797.161A4.002 4.002 0 0 0 4 6c0 .628-.134 2.197-.459 3.742c-.16.767-.376 1.566-.663 2.258h10.244c-.287-.692-.502-1.49-.663-2.258C12.134 8.197 12 6.628 12 6a4.002 4.002 0 0 0-3.203-3.92L8 1.917zM14.22 12c.223.447.481.801.78 1H1c.299-.199.557-.553.78-1C2.68 10.2 3 6.88 3 6c0-2.42 1.72-4.44 4.005-4.901a1 1 0 1 1 1.99 0A5.002 5.002 0 0 1 13 6c0 .88.32 4.2 1.22 6z" />
                </g>
              </svg>
            </button>

            <router-link to="/notifications" class="user-icon">
              <div class="user-image">
                <img src="../assets/static/images/Avatar.png" alt="" class="img-fluid" />
              </div>
              <div class="user-detail d-none d-md-inline-flex">
                <span><b>John Snow</b></span>
                <span><small>johnsnow@gmail.com</small></span>
              </div>
            </router-link>
          </div>
          <!-- notification ends -->
        </div>
        <!-- topper ends  -->

        <!-- page content body -->
        <div class="page-content-body">
          <!-- page title for sm screen start -->
          <div class="title d-md-none">
            <h2>Dashboard</h2>
          </div>
          <!-- page title for sm screen end-->
          <div class="page-content-body-inner">
            <div class="cards-wrapper">
              <!-- each card starts -->
              <div class="each-card">
                <div class="card-icon">
                  <em style="color: #ff0000" class="bi bi-youtube"></em>
                </div>
                <div class="value">
                  <div class="amount">
                    <h3>0</h3>
                  </div>
                  <div class="total-links">
                    <span>Total Links</span>
                  </div>
                </div>
              </div>
              <!-- card card ends -->
              <!-- each card starts -->
              <div class="each-card">
                <div class="card-icon">
                  <em style="color: #1877f2" class="bi bi-facebook"></em>
                </div>
                <div class="value">
                  <div class="amount">
                    <h3>0</h3>
                  </div>
                  <div class="total-links">
                    <span>Total Links</span>
                  </div>
                </div>
              </div>
              <!-- card card ends -->
              <!-- each card starts -->
              <div class="each-card">
                <div class="card-icon">
                  <em style="color: #0a66c2" class="bi bi-linkedin"></em>
                </div>
                <div class="value">
                  <div class="amount">
                    <h3>0</h3>
                  </div>
                  <div class="total-links">
                    <span>Total Links</span>
                  </div>
                </div>
              </div>
              <!-- card card ends -->
              <!-- each card starts -->
              <div class="each-card">
                <div class="card-icon">
                  <em style="color: #55acee" class="bi bi-twitter"></em>
                </div>
                <div class="value">
                  <div class="amount">
                    <h3>0</h3>
                  </div>
                  <div class="total-links">
                    <span>Total Links</span>
                  </div>
                </div>
              </div>
              <!-- card card ends -->
              <!-- each card starts -->
              <div class="each-card">
                <div class="card-icon">
                  <span>Custom</span>
                </div>
                <div class="value">
                  <div class="amount">
                    <h3>0</h3>
                  </div>
                  <div class="total-links">
                    <span>Total Links</span>
                  </div>
                </div>
              </div>
              <!-- card card ends -->
            </div>
            <!-- traffic chart overview start-->
            <div class="traffic-overview">
              <div class="traffic-overview-inner">
                <div class="overview-header">
                  <h4 class="title">Traffic Chart</h4>
                  <div class="d-flex align-items-center justify-content-between right">
                    <div class="dropdown d-none d-md-inline-flex">
                      <button class="all-media" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                        All Media
                      </button>
                      <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="#">Youtube</a></li>
                        <li><a class="dropdown-item" href="#">Facebook</a></li>
                        <li><a class="dropdown-item" href="#">LinkedIn</a></li>
                        <li><a class="dropdown-item" href="#">Twitter</a></li>
                        <li><a class="dropdown-item" href="#">Custom</a></li>
                      </ul>
                    </div>
                    <div class="btn-group d-md-none">
                      <button
                        class="mobile-dropdown dropdown-toggle"
                        type="button"
                        data-bs-toggle="dropdown"
                        data-bs-auto-close="outside"
                        aria-expanded="false">
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          width="32"
                          height="32"
                          preserveAspectRatio="xMidYMid meet"
                          viewBox="0 0 36 36">
                          <path
                            fill="currentColor"
                            d="M12 12.37a4 4 0 0 0-3-3.89V5a1 1 0 1 0-2 0v3.48a4 4 0 0 0 0 7.78V31a1 1 0 1 0 2 0V16.26a4 4 0 0 0 3-3.89Zm-4 2a2 2 0 1 1 2-2a2 2 0 0 1-2 2.03Z"
                            class="clr-i-outline clr-i-outline-path-1" />
                          <path
                            fill="currentColor"
                            d="M32 15.83a4 4 0 0 0-3-3.89V5a1 1 0 1 0-2 0v6.94a4 4 0 0 0 0 7.78V31a1 1 0 1 0 2 0V19.72a4 4 0 0 0 3-3.89Zm-4 2a2 2 0 1 1 2-2a2 2 0 0 1-2 2.04Z"
                            class="clr-i-outline clr-i-outline-path-2" />
                          <path
                            fill="currentColor"
                            d="M22 24.5a4 4 0 0 0-3-3.89V5a1 1 0 1 0-2 0v15.61a4 4 0 0 0 0 7.78V31a1 1 0 1 0 2 0v-2.61a4 4 0 0 0 3-3.89Zm-4 2a2 2 0 1 1 2-2a2 2 0 0 1-2 2.03Z"
                            class="clr-i-outline clr-i-outline-path-3" />
                          <path fill="none" d="M0 0h36v36H0z" />
                        </svg>
                      </button>
                      <ul class="dropdown-menu mobile-dropdown-menu">
                        <button type="button" class="date-time d-flex align-items-center">
                          <small>July 12, 2022</small>
                          <input type="date" />
                        </button>
                        <button class="all-media" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                          All Media
                        </button>
                        <ul class="dropdown-menu">
                          <li><a class="dropdown-item" href="#">Youtube</a></li>
                          <li><a class="dropdown-item" href="#">Facebook</a></li>
                          <li><a class="dropdown-item" href="#">LinkedIn</a></li>
                          <li><a class="dropdown-item" href="#">Twitter</a></li>
                          <li><a class="dropdown-item" href="#">Custom</a></li>
                        </ul>
                      </ul>
                    </div>
                    <button type="button" class="pc-view date-time d-none d-md-inline-flex d-flex align-items-center">
                      <small>July 12, 2022</small>
                      <input type="date" />
                    </button>
                  </div>
                </div>
              </div>
            </div>
            <!-- traffic chart overview ends -->
          </div>
        </div>
        <!-- page content body ends -->
      </div>

      <!-- footer starts -->
      <DashBoardFooter></DashBoardFooter>
      <!-- footer ends -->
    </div>
</template>
<script>
// import '@/assets/static/js/user-control'
import DashBoardFooter from "@/components/DashBoardFooter.vue";

export default {
  name: 'App',
  components: {
    DashBoardFooter
  }
}
</script>
